# START HERE: YouTube Transcript Archive

The first thing in this repository is now the transcript archive:

- **[TRANSCRIPTS.md](TRANSCRIPTS.md)** — full index, method, and missing/unavailable audit.
- **[transcripts/START_HERE.md](transcripts/START_HERE.md)** — same index inside the transcript folder.
- **`transcripts/exurb1a/`** — Exurb1a VTT captions and readable text copies.
- **`transcripts/sxrawn/`** — sxrawn transcript destination folders.
- **[transcripts/SXRAWN_WORKAROUND.md](transcripts/SXRAWN_WORKAROUND.md)** — direct no-key fallback transcript links and the command to fetch the other channel when direct YouTube caption extraction is blocked.

Raw `.vtt` files are preserved as the preferred source of truth so the transcript archive does not lose words during cleanup. `.txt` files are generated only for easier browsing/search. For networks where YouTube blocks `yt-dlp`, the script can fall back to Markdown transcripts from `youtube-transcript.ai`.

---

Original research report: [report.md](report.md)
