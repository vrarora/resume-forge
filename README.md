# resume-forge

[![Claude Code skill](https://img.shields.io/badge/Claude%20Code-skill-D97757)](https://claude.com/claude-code)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Any field](https://img.shields.io/badge/works%20for-any%20field-2ea44f)](#how-it-works)

A Claude Code skill that builds your resume the way a good career coach would. It researches your market, interviews you until every claim is verified, writes impact-first bullets, checks its own drafts, and renders the files you need. It works for any field.

## What you get

| File | Use it for |
|---|---|
| `First Last Resume.pdf` | Job portals and ATS. Single column, parses cleanly |
| `First Last Resume (Designed).pdf` | Email, referrals and founders. A clean two-column layout |
| `First Last Resume.docx` | Workday portals and anyone who edits in Word |
| `linkedin.md` | Headline, About and experience copy that matches the resume |
| `playbook.md` | Market research, salary bands and the rules your resume follows |
| `facts.md` | Every claim on your resume, with its source |

Targeting more than one role? It builds a separate set for each, in its own folder.

## How it works

1. **Reads everything you have** — your old resume, LinkedIn, portfolio and case studies.
2. **Researches your field** — what hiring managers screen for, salary bands, keywords and format norms.
3. **Interviews you** — direction first, then the facts behind every number, until nothing on the page is unverified.
4. **Writes impact-first bullets.** Each bullet leads with the result, then says how you got it. For example, "Cut checkout latency from 1.2s to 300ms by moving pricing to an edge cache."
5. **Checks every draft** for banned filler words, page fit, ATS parsing and claims that don't match your answers.
6. **Iterates with you** until you're happy.

## Install

```bash
git clone https://github.com/vrarora/resume-forge.git ~/.claude/skills/resume-forge
```

Then, in Claude Code, type `/resume-forge`, or just say "help me with my resume".

### Requirements

- [Claude Code](https://claude.com/claude-code)
- Chrome, Chromium or Edge, for rendering PDFs
- Python 3
- `pip install python-docx`, for DOCX output
- Poppler (optional, for stricter checks): `brew install poppler` or `apt install poppler-utils`

## Rules it follows

- Every bullet leads with its impact
- No filler words such as "responsible for", "helped", "leveraged" or "spearheaded"
- One page for anyone with under ~10 years of experience
- No summary section, because the headline and first bullet carry it
- Awards sit under the role that earned them
- No titles you haven't held, and no numbers you can't explain in an interview
- Builder or measured tone, chosen per person

## Scripts

You can use these on their own.

```bash
python3 scripts/render.py resume.html "First Last Resume.pdf"
python3 scripts/check.py "First Last Resume.pdf" --max-pages 1 --ats
python3 scripts/to_docx.py resume.html "First Last Resume.docx"
```

## License

MIT, © Vaibhav Ratnam Arora. The bundled Geist fonts are under the SIL Open Font License (`assets/fonts/OFL.txt`).
