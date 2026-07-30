# sxrawn Transcript Workaround

The sandbox terminal cannot currently reach YouTube caption endpoints or the no-key transcript fallback over HTTPS, but the repository now includes a fallback path that works from a normal non-blocked network:

```bash
python scripts/fetch_youtube_transcripts.py --transcript-ai-only
```

That command skips direct `yt-dlp` caption extraction and uses this no-key GET pattern instead:

```text
https://youtube-transcript.ai/transcript/VIDEO_ID.txt?lang=en
```

The links below are the direct transcript endpoints for the enumerated `@sxrawn` videos. They are included so the remaining channel can be filled without guessing or fabricating text.

| Video | YouTube | no-key transcript fallback |
| --- | --- | --- |
| There is Nobody Inside Your Head. | https://www.youtube.com/watch?v=LnGa65Xe-nE | https://youtube-transcript.ai/transcript/LnGa65Xe-nE.txt?lang=en |
| the mola mola or sunfish is a disappointment..... | https://www.youtube.com/watch?v=4vA2IulZ0Nw | https://youtube-transcript.ai/transcript/4vA2IulZ0Nw.txt?lang=en |
| Which Animal Should You Reincarnate As? | https://www.youtube.com/watch?v=audBYfnjxxo | https://youtube-transcript.ai/transcript/audBYfnjxxo.txt?lang=en |
| If Everybody Shot a Bullet... | https://www.youtube.com/watch?v=UzO60u2BHEY | https://youtube-transcript.ai/transcript/UzO60u2BHEY.txt?lang=en |
| The Chair Hypothesis | https://www.youtube.com/watch?v=SkcWeflr7mc | https://youtube-transcript.ai/transcript/SkcWeflr7mc.txt?lang=en |
| at the end of evolution | https://www.youtube.com/watch?v=wKiT-kvNn0M | https://youtube-transcript.ai/transcript/wKiT-kvNn0M.txt?lang=en |
| The Inconvenient Charity Awards Show | https://www.youtube.com/watch?v=M4rpGxmXgew | https://youtube-transcript.ai/transcript/M4rpGxmXgew.txt?lang=en |
| the timeline of the universe explained in increasing complexity ep 1 | https://www.youtube.com/watch?v=n4C5W0hLhtc | https://youtube-transcript.ai/transcript/n4C5W0hLhtc.txt?lang=en |
| How Peanut Butter helped us beat the Neanderthals. | https://www.youtube.com/watch?v=h8DZcb5suFM | https://youtube-transcript.ai/transcript/h8DZcb5suFM.txt?lang=en |
| Wasting Your Life: A 427-Second Guide | https://www.youtube.com/watch?v=U3I7xVQovis | https://youtube-transcript.ai/transcript/U3I7xVQovis.txt?lang=en |
| why is life shit now? | https://www.youtube.com/watch?v=aDP3tTY7ERk | https://youtube-transcript.ai/transcript/aDP3tTY7ERk.txt?lang=en |
| humans beat death in a fist fight | https://www.youtube.com/watch?v=BZx2SmHveOE | https://youtube-transcript.ai/transcript/BZx2SmHveOE.txt?lang=en |
| light is a wave and a particle. How? | https://www.youtube.com/watch?v=kkWwK5h3_PY | https://youtube-transcript.ai/transcript/kkWwK5h3_PY.txt?lang=en |
| How to Live Forever | https://www.youtube.com/watch?v=251tqtR4nUA | https://youtube-transcript.ai/transcript/251tqtR4nUA.txt?lang=en |
| The Last Man Standing in the Universe | https://www.youtube.com/watch?v=LHY6QUw8Ofw | https://youtube-transcript.ai/transcript/LHY6QUw8Ofw.txt?lang=en |
| who are You? | https://www.youtube.com/watch?v=ZHE7iaLOMd0 | https://youtube-transcript.ai/transcript/ZHE7iaLOMd0.txt?lang=en |
| humans are all that matter in the universe (no really) | https://www.youtube.com/watch?v=-ecp_4pKVrA | https://youtube-transcript.ai/transcript/-ecp_4pKVrA.txt?lang=en |
| how to be religious | https://www.youtube.com/watch?v=6cTAfthUFv4 | https://youtube-transcript.ai/transcript/6cTAfthUFv4.txt?lang=en |
| will AI ever be conscious? | https://www.youtube.com/watch?v=ILDBj4aOQ1w | https://youtube-transcript.ai/transcript/ILDBj4aOQ1w.txt?lang=en |

## Notes

- This fallback returns Markdown/text, not raw VTT. The script saves it under `transcripts/<channel>/transcript_ai/markdown/` and a text-only copy under `transcripts/<channel>/transcript_ai/text/`.
- Raw VTT from `yt-dlp` remains preferred when available.
- Do not use private cookies or credentials; this is only for public captions.
