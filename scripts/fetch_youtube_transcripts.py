#!/usr/bin/env python3
"""Fetch and index public YouTube transcripts for @Exurb1a and @sxrawn.

Design goals:
- Preserve raw caption files (.vtt) so no words are lost by cleanup.
- Generate readable .txt copies for GitHub browsing/search.
- Use yt-dlp for public YouTube captions only; do not use cookies or private credentials.
- Seed Exurb1a's older caption archive from HACKER097/exurbia-video-finder because it is
  a known public VTT corpus and reduces YouTube rate/bot pressure.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPTS = ROOT / "transcripts"
LOGS = TRANSCRIPTS / "_logs"

ARCHIVE_REPO = "https://github.com/HACKER097/exurbia-video-finder.git"

CHANNELS = {
    "exurb1a": {
        "handle": "@Exurb1a",
        "channel_id": "UCimiUgDLbi6P17BdaCZpVbg",
        "urls": [
            "https://www.youtube.com/@Exurb1a/videos",
            "https://www.youtube.com/@Exurb1a/shorts",
            "https://www.youtube.com/playlist?list=UUimiUgDLbi6P17BdaCZpVbg",
        ],
        # Fallback from YouTube RSS current as of 2026-07-30 plus known unlisted/private originals.
        "fallback_videos": [
            ("y894m7joEBc", "maybe I'm the alien"),
            ("BUtzl6b0uKU", "a pointless ad for my pointless new book"),
            ("Ctwc8t5CsQs", "Chess is When You Microdose Infinity"),
            ("0y6wiBzPMSI", "everybody is a total mess (and you should be one too)"),
            ("o1OsDWT_DUc", "Then Next Comes"),
            ("8HzIlKe--NU", "How Long is Now? | Introduction to Metaphysics"),
            ("VQjPKqE39No", "How Will We Know When AI is Conscious?"),
            ("sKouPOhh_9I", "Big Oxygen"),
            ("O0EKaSmtpA0", "Ether/Or — The story of black holes"),
            ("Jv79l1b-eoI", "Absurdism | How to Party at the End of Meaning"),
            ("VztEcSYXQr0", "the existence forecast"),
            ("Fzhkwyoe5vI", "Don't Hex the Water"),
            ("P9Q3crLWQY8", "How the Frogs Cooked Dinner"),
            ("3IT_rnV1LBw", "Red Dead No Redemption"),
            ("9uhURpEbK40", "exam for humans"),
            # Known removed/unlisted originals/reuploads referenced in community sources.
            ("K3W61Ae0M9g", "Dear Nia (known unlisted/removed original link)"),
            ("om6uhLs75Bk", "Losing You (original; may be private)"),
            ("_lY32QRHMjk", "Losing You (community reupload; fallback only)"),
        ],
    },
    "sxrawn": {
        "handle": "@sxrawn",
        "channel_id": "UC55eqa7u-UnEqKMAAQZsfjg",
        "urls": [
            "https://www.youtube.com/@sxrawn/videos",
            "https://www.youtube.com/@sxrawn/shorts",
            "https://www.youtube.com/playlist?list=UU55eqa7u-UnEqKMAAQZsfjg",
            "https://www.youtube.com/playlist?list=PLDGmN6K_AY6_Zrrjt-JK-LX3DooNGpn9_",
        ],
        # Fallback from channel RSS/about/playlist current as of 2026-07-30.
        "fallback_videos": [
            ("LnGa65Xe-nE", "There is Nobody Inside Your Head."),
            ("4vA2IulZ0Nw", "the mola mola or sunfish is a disappointment....."),
            ("audBYfnjxxo", "Which Animal Should You Reincarnate As?"),
            ("UzO60u2BHEY", "If Everybody Shot a Bullet..."),
            ("SkcWeflr7mc", "The Chair Hypothesis"),
            ("wKiT-kvNn0M", "at the end of evolution"),
            ("M4rpGxmXgew", "The Inconvenient Charity Awards Show"),
            ("n4C5W0hLhtc", "the timeline of the universe explained in increasing complexity ep 1"),
            ("h8DZcb5suFM", "How Peanut Butter helped us beat the Neanderthals."),
            ("U3I7xVQovis", "Wasting Your Life: A 427-Second Guide"),
            ("aDP3tTY7ERk", "why is life shit now?"),
            ("BZx2SmHveOE", "humans beat death in a fist fight"),
            ("kkWwK5h3_PY", "light is a wave and a particle. How?"),
            ("251tqtR4nUA", "How to Live Forever"),
            ("LHY6QUw8Ofw", "The Last Man Standing in the Universe"),
            ("ZHE7iaLOMd0", "who are You?"),
            ("-ecp_4pKVrA", "humans are all that matter in the universe (no really)"),
            ("6cTAfthUFv4", "how to be religious"),
            ("ILDBj4aOQ1w", "will AI ever be conscious?"),
        ],
    },
}

VIDEO_ID_RE = re.compile(r"(?<![A-Za-z0-9_-])([A-Za-z0-9_-]{11})(?![A-Za-z0-9_-])")
TIMESTAMP_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}\.\d{3}")
HTML_TAG_RE = re.compile(r"<[^>]+>")
BAD_FILENAME_RE = re.compile(r"[\\/:*?\"<>|]+")


@dataclass
class Video:
    channel: str
    id: str
    title: str = ""
    url: str = ""
    source: str = ""


@dataclass
class TranscriptRecord:
    channel: str
    video_id: str
    title: str
    url: str
    source: str
    vtt_path: str
    txt_path: str
    bytes: int
    status: str


def run(cmd: list[str], *, cwd: Path | None = None, check: bool = False, capture: bool = True) -> subprocess.CompletedProcess:
    kwargs = {
        "cwd": str(cwd) if cwd else None,
        "text": True,
        "check": check,
    }
    if capture:
        kwargs.update(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return subprocess.run(cmd, **kwargs)


def which(name: str) -> str | None:
    return shutil.which(name)


def safe_name(value: str, max_len: int = 180) -> str:
    value = html.unescape(value or "untitled")
    value = value.replace("\n", " ").strip()
    value = BAD_FILENAME_RE.sub("_", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    if not value:
        value = "untitled"
    return value[:max_len].rstrip(" .")


def video_id_from_name(path: Path) -> str | None:
    # Prefer the final -VIDEOID before .en.vtt, but accept any 11-char id.
    stem = path.name
    m = re.search(r"-([A-Za-z0-9_-]{11})(?:\.[A-Za-z-]+)?\.vtt$", stem)
    if m:
        return m.group(1)
    ids = VIDEO_ID_RE.findall(stem)
    return ids[-1] if ids else None


def title_from_archive_name(path: Path) -> str:
    name = path.name
    vid = video_id_from_name(path)
    if vid:
        name = name.split("-" + vid)[0]
    name = re.sub(r"\.en\.vtt$", "", name)
    return html.unescape(name).strip() or "untitled"


def vtt_to_text(vtt_path: Path) -> str:
    lines: list[str] = []
    last = None
    for raw in vtt_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip().lstrip("\ufeff")
        if not line:
            continue
        if line in {"WEBVTT", "Kind: captions", "Language: en"}:
            continue
        if line.startswith(("NOTE", "STYLE", "REGION")):
            continue
        if TIMESTAMP_RE.match(line):
            continue
        if re.fullmatch(r"\d+", line):
            continue
        line = HTML_TAG_RE.sub("", line)
        line = html.unescape(line)
        line = re.sub(r"\s+", " ", line).strip()
        if not line:
            continue
        # Keep non-consecutive repeats; remove only exact adjacent duplicates.
        if line == last:
            continue
        lines.append(line)
        last = line
    return "\n".join(lines).strip() + ("\n" if lines else "")


def write_text_copy(vtt_path: Path, txt_root: Path) -> Path:
    txt_root.mkdir(parents=True, exist_ok=True)
    txt_path = txt_root / (vtt_path.stem + ".txt")
    txt_path.write_text(vtt_to_text(vtt_path), encoding="utf-8")
    return txt_path


def copy_exurb1a_archive() -> list[TranscriptRecord]:
    records: list[TranscriptRecord] = []
    dest_vtt = TRANSCRIPTS / "exurb1a" / "archive_hacker097" / "vtt"
    dest_txt = TRANSCRIPTS / "exurb1a" / "archive_hacker097" / "text"
    dest_vtt.mkdir(parents=True, exist_ok=True)
    dest_txt.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="exurbia-video-finder-") as tmp:
        tmp_path = Path(tmp) / "repo"
        cp = run(["git", "clone", "--depth", "1", ARCHIVE_REPO, str(tmp_path)], capture=True)
        (LOGS / "archive_clone.log").write_text((cp.stdout or "") + (cp.stderr or ""), encoding="utf-8")
        if cp.returncode != 0:
            print(f"WARN: could not clone {ARCHIVE_REPO}", file=sys.stderr)
            return records
        for src in sorted(tmp_path.glob("*.vtt")):
            vid = video_id_from_name(src) or "unknown"
            title = title_from_archive_name(src)
            target = dest_vtt / src.name
            shutil.copy2(src, target)
            txt = write_text_copy(target, dest_txt)
            records.append(TranscriptRecord(
                channel="exurb1a",
                video_id=vid,
                title=title,
                url=f"https://www.youtube.com/watch?v={vid}" if vid != "unknown" else "",
                source="HACKER097/exurbia-video-finder public VTT archive",
                vtt_path=str(target.relative_to(ROOT)),
                txt_path=str(txt.relative_to(ROOT)),
                bytes=target.stat().st_size,
                status="archived",
            ))
    return records


def enumerate_with_ytdlp(channel: str, url: str) -> list[Video]:
    if not which("yt-dlp"):
        return []
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-single-json",
        "--ignore-no-formats-error",
        "--no-warnings",
        url,
    ]
    cp = run(cmd, capture=True)
    log_name = safe_name(f"enumerate_{channel}_{url}", 120) + ".log"
    (LOGS / log_name).write_text((cp.stdout or "") + "\nSTDERR:\n" + (cp.stderr or ""), encoding="utf-8")
    if cp.returncode != 0 or not cp.stdout.strip():
        return []
    try:
        data = json.loads(cp.stdout)
    except json.JSONDecodeError:
        return []
    videos: list[Video] = []
    for e in data.get("entries") or []:
        if not isinstance(e, dict):
            continue
        vid = e.get("id") or e.get("url") or ""
        m = VIDEO_ID_RE.search(str(vid))
        if not m:
            continue
        vid = m.group(1)
        title = e.get("title") or ""
        videos.append(Video(channel=channel, id=vid, title=title, url=f"https://www.youtube.com/watch?v={vid}", source=f"yt-dlp enumeration: {url}"))
    return videos


def enumerate_videos() -> list[Video]:
    by_id: dict[tuple[str, str], Video] = {}
    for channel, cfg in CHANNELS.items():
        for url in cfg["urls"]:
            for v in enumerate_with_ytdlp(channel, url):
                by_id[(channel, v.id)] = v
        # Always add fallbacks/known extras; enumerated titles win if already present.
        for vid, title in cfg["fallback_videos"]:
            by_id.setdefault((channel, vid), Video(channel=channel, id=vid, title=title, url=f"https://www.youtube.com/watch?v={vid}", source="curated fallback manifest"))
    return sorted(by_id.values(), key=lambda v: (v.channel, v.title.lower(), v.id))


def existing_ids(records: Iterable[TranscriptRecord]) -> set[tuple[str, str]]:
    return {(r.channel, r.video_id) for r in records if r.video_id and r.video_id != "unknown"}


def download_caption(video: Video) -> tuple[list[TranscriptRecord], str | None]:
    if not which("yt-dlp"):
        return [], "yt-dlp not installed"
    channel_dir = TRANSCRIPTS / video.channel / "ytdlp"
    vtt_dir = channel_dir / "vtt"
    txt_dir = channel_dir / "text"
    vtt_dir.mkdir(parents=True, exist_ok=True)
    txt_dir.mkdir(parents=True, exist_ok=True)
    title_part = safe_name(video.title or video.id, 140)
    outtmpl = str(vtt_dir / f"{title_part}-{video.id}.%(ext)s")
    url = video.url or f"https://www.youtube.com/watch?v={video.id}"
    before = set(vtt_dir.glob(f"*{video.id}*.vtt"))
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", "en,en.*,en-US,en-GB",
        "--sub-format", "vtt/best",
        "--convert-subs", "vtt",
        "--ignore-errors",
        "--no-abort-on-error",
        "--retries", "5",
        "--fragment-retries", "5",
        "--sleep-requests", "1",
        "--sleep-subtitles", "1",
        "-o", outtmpl,
        url,
    ]
    cp = run(cmd, capture=True)
    log_file = LOGS / f"download_{video.channel}_{video.id}.log"
    log_file.write_text("$ " + " ".join(cmd) + "\n\nSTDOUT:\n" + (cp.stdout or "") + "\nSTDERR:\n" + (cp.stderr or ""), encoding="utf-8")
    after = set(vtt_dir.glob(f"*{video.id}*.vtt"))
    new_files = sorted(after - before) or sorted(after)
    records: list[TranscriptRecord] = []
    for vtt in new_files:
        if vtt.stat().st_size == 0:
            continue
        txt = write_text_copy(vtt, txt_dir)
        records.append(TranscriptRecord(
            channel=video.channel,
            video_id=video.id,
            title=video.title or vtt.stem,
            url=url,
            source=video.source,
            vtt_path=str(vtt.relative_to(ROOT)),
            txt_path=str(txt.relative_to(ROOT)),
            bytes=vtt.stat().st_size,
            status="downloaded",
        ))
    if records:
        return records, None
    reason = "no English caption file produced"
    log_text = (cp.stdout or "") + "\n" + (cp.stderr or "")
    for marker in ["Sign in to confirm", "No subtitles", "no subtitles", "Private video", "Video unavailable", "This video is unavailable", "HTTP Error 429"]:
        if marker in log_text:
            reason = marker
            break
    return [], reason


def write_csv(records: list[TranscriptRecord], missing: list[dict]) -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    with (TRANSCRIPTS / "manifest.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(records[0]).keys()) if records else [
            "channel", "video_id", "title", "url", "source", "vtt_path", "txt_path", "bytes", "status"
        ])
        writer.writeheader()
        for r in records:
            writer.writerow(asdict(r))
    with (TRANSCRIPTS / "missing.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["channel", "video_id", "title", "url", "reason", "source"])
        writer.writeheader()
        for m in missing:
            writer.writerow(m)


def write_markdown(records: list[TranscriptRecord], missing: list[dict], videos: list[Video]) -> None:
    now = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    total_by_channel: dict[str, int] = {}
    for r in records:
        total_by_channel[r.channel] = total_by_channel.get(r.channel, 0) + 1
    missing_by_channel: dict[str, int] = {}
    for m in missing:
        missing_by_channel[m["channel"]] = missing_by_channel.get(m["channel"], 0) + 1

    lines = [
        "# START HERE — YouTube Transcripts",
        "",
        f"Last generated: `{now}`.",
        "",
        "This directory is the transcript archive for **@Exurb1a** and **@sxrawn**.",
        "The raw `.vtt` caption files are preserved first; cleaned `.txt` copies are provided only for easier reading/searching.",
        "",
        "## Summary",
        "",
        "| Channel | Transcript files present | Videos still missing / unavailable |",
        "| --- | ---: | ---: |",
    ]
    for channel in sorted(CHANNELS):
        lines.append(f"| `{channel}` | {total_by_channel.get(channel, 0)} | {missing_by_channel.get(channel, 0)} |")
    lines += [
        "",
        "## Method",
        "",
        "1. Enumerate each channel's public uploads/shorts with `yt-dlp --flat-playlist` against the handle pages and uploads playlists.",
        "2. Download **only** public English captions/subtitles with `yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs en,en.*`.",
        "3. Preserve raw `.vtt` files exactly as obtained, then generate `.txt` copies from those files.",
        "4. Seed older Exurb1a captions from the public `HACKER097/exurbia-video-finder` VTT archive to avoid losing older community-preserved captions.",
        "5. Do not use private cookies, private YouTube sessions, or bypassed credentials.",
        "",
        "## Files",
        "",
        "- `manifest.csv` — every transcript file currently present.",
        "- `missing.csv` — videos that were enumerated or known but did not produce an English caption file.",
        "- `exurb1a/archive_hacker097/vtt/` — public archived Exurb1a VTT files.",
        "- `exurb1a/ytdlp/vtt/` — freshly downloaded Exurb1a VTT files.",
        "- `sxrawn/ytdlp/vtt/` — freshly downloaded sxrawn VTT files.",
        "- `*/text/` — readable text conversions generated from VTT.",
        "",
        "## Transcript Index",
        "",
        "| Channel | Video | Transcript | Text | Source |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in sorted(records, key=lambda r: (r.channel, r.title.lower(), r.video_id, r.vtt_path)):
        title = r.title.replace("|", "\\|")
        lines.append(f"| `{r.channel}` | [{title}]({r.url}) | [`vtt`]({r.vtt_path}) | [`txt`]({r.txt_path}) | {r.source.replace('|', '/')} |")
    if missing:
        lines += ["", "## Missing / Unavailable", "", "| Channel | Video | Reason | Source |", "| --- | --- | --- | --- |"]
        for m in sorted(missing, key=lambda m: (m["channel"], m["title"].lower(), m["video_id"])):
            title = (m["title"] or m["video_id"]).replace("|", "\\|")
            lines.append(f"| `{m['channel']}` | [{title}]({m['url']}) | {m['reason'].replace('|', '/')} | {m['source'].replace('|', '/')} |")
    lines += ["", "## Enumerated Video Inputs", "", "| Channel | Video | Source |", "| --- | --- | --- |"]
    for v in sorted(videos, key=lambda v: (v.channel, v.title.lower(), v.id)):
        title = (v.title or v.id).replace("|", "\\|")
        lines.append(f"| `{v.channel}` | [{title}]({v.url}) | {v.source.replace('|', '/')} |")
    text = "\n".join(lines) + "\n"
    (TRANSCRIPTS / "START_HERE.md").write_text(text, encoding="utf-8")
    (ROOT / "TRANSCRIPTS.md").write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-ytdlp", action="store_true", help="Only copy/archive existing public transcript sources; do not call YouTube.")
    parser.add_argument("--refresh-archive-ids", action="store_true", help="Also yt-dlp-download videos already covered by the Exurb1a archive.")
    args = parser.parse_args()

    LOGS.mkdir(parents=True, exist_ok=True)
    all_records: list[TranscriptRecord] = []
    missing: list[dict] = []

    print("Copying public Exurb1a VTT archive...")
    archive_records = copy_exurb1a_archive()
    all_records.extend(archive_records)
    covered = existing_ids(archive_records)

    print("Enumerating videos...")
    videos = enumerate_videos()
    (TRANSCRIPTS / "enumerated_videos.json").write_text(json.dumps([asdict(v) for v in videos], indent=2, ensure_ascii=False), encoding="utf-8")

    if not args.skip_ytdlp:
        for v in videos:
            if (v.channel, v.id) in covered and not args.refresh_archive_ids:
                continue
            print(f"Fetching captions: {v.channel} {v.id} {v.title}")
            records, reason = download_caption(v)
            if records:
                all_records.extend(records)
                for r in records:
                    covered.add((r.channel, r.video_id))
            else:
                missing.append({
                    "channel": v.channel,
                    "video_id": v.id,
                    "title": v.title,
                    "url": v.url or f"https://www.youtube.com/watch?v={v.id}",
                    "reason": reason or "unknown",
                    "source": v.source,
                })
    else:
        for v in videos:
            if (v.channel, v.id) not in covered:
                missing.append({
                    "channel": v.channel,
                    "video_id": v.id,
                    "title": v.title,
                    "url": v.url or f"https://www.youtube.com/watch?v={v.id}",
                    "reason": "yt-dlp skipped in this run",
                    "source": v.source,
                })

    # De-dupe exact same VTT path and sort.
    dedup: dict[str, TranscriptRecord] = {r.vtt_path: r for r in all_records}
    all_records = sorted(dedup.values(), key=lambda r: (r.channel, r.title.lower(), r.video_id, r.vtt_path))
    write_csv(all_records, missing)
    write_markdown(all_records, missing, videos)
    print(f"Done. Transcript files: {len(all_records)}. Missing/unavailable: {len(missing)}")
    return 0 if all_records else 1


if __name__ == "__main__":
    raise SystemExit(main())
