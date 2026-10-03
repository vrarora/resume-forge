---
name: resume-forge
description: Build or rewrite a resume (CV) for any profession through market research, a fact-checking interview and impact-first writing, then render an ATS-safe PDF, a designed PDF, a DOCX, role-specific variants and matching LinkedIn copy. Use this whenever someone wants to make, fix, rewrite, tailor, review or redesign a resume or CV, turn a LinkedIn profile or portfolio into a resume, target a new role or seniority level, make versions for different roles, or update LinkedIn to match their resume. Trigger even on casual asks like "help me with my resume", "my CV is weak", "I'm job hunting", or when someone shares an old resume PDF and wants it better.
---

# Resume Forge

Resume Forge builds a resume the way a good career coach does. It reads everything the person already has, researches their market, and interviews them until every claim is verified. Then it writes impact-first bullets, checks its own drafts, and renders the files they need.

The person stays in charge. Ask before assuming, show drafts early, and treat each round of feedback as the next iteration. Most of the value comes from the interview. Old resumes undersell people, and the strongest numbers usually sit in their portfolio, performance reviews or memory.

## What you produce

Work in a `resume/` folder in the current directory unless the person names another place.

```
resume/
├── facts.md                          every claim, with its source
├── playbook.md                       research findings and this person's rules
├── fonts/                            copied from assets/fonts/
├── <variant>/                        one folder per target role, e.g. senior-pm/
│   ├── resume.html                   ATS source
│   ├── resume-designed.html          designed source
│   ├── First Last Resume.pdf         ATS PDF, for job portals
│   ├── First Last Resume (Designed).pdf
│   └── First Last Resume.docx        for Workday and Word users
└── linkedin.md
```

Keep the filename the same across variants. The folder separates them, so a hiring manager never sees "founding" or "v3" in a filename.

## Workflow

Follow these steps in order. Each step names the reference file to read when you reach it, so you only load what you need.

### 1. Read everything first

Ask for whatever exists. That usually means the current resume, a LinkedIn URL, a portfolio with case studies, award posts and performance reviews. Read all of it before asking anything else, because the interview gets sharper when you already know the material.

- LinkedIn usually needs a login. If you can't see the profile, ask the person to open it in a browser you can read, or to use LinkedIn's "Save to PDF".
- Portfolios often hide text behind animations. Look for a reader mode or plain-text view, and read every case study. Case studies hold the numbers that never made the resume.
- Start `facts.md` as you read. Read `references/interview.md` for its format. Log every discrepancy between sources, such as different end dates or titles, so you can ask about each one.

### 2. Research the field

Run two research passes, one on the market and one on resume practice. Read `references/research.md` for the prompts. If your agent can run subagents or background tasks, run both in parallel while you start the interview. Otherwise, do a short pass yourself (about 6–8 searches each) before drafting. If you have no web access, ask the person for 2–3 job postings they like and use those as the research. Research every field fresh. Advice for designers does not transfer to nurses or sales leaders. Merge the findings into `playbook.md` and tell the person the few findings that change how you'll write.

### 3. Interview until you're about 98% sure

Read `references/interview.md`. Run the interview in rounds. Direction comes first, then facts for each role, then gaps for the target role. Stop when every bullet you plan to write traces back to `facts.md` and no open question would change the content.

When research already answers a question, advise instead of asking. For example, if a conversion metric rests on two weeks of data, recommend holding it back and say why.

### 4. Write the ATS version

Read `references/writing.md`, then copy `assets/templates/ats.html` into the variant folder and fill it.

These rules apply to everyone:
- Every bullet leads with its impact.
- Nothing from the banned-word list.
- One page for anyone under about 10 years of experience.
- No summary section.
- Awards sit under the role that earned them.

Tone is a per-person choice that you settle in the interview.

### 5. Self-review every draft before showing it

Run `scripts/check.py` on the rendered PDF, then walk the checklist in `references/self-review.md`. Fix what fails. If the check reports a lot of empty space, the fix is more interview questions, not bigger type (see `references/layout.md`). Tell the person what you checked in a short table, so they see the draft has been verified, not just written.

### 6. Render and show

Render with `scripts/render.py`. Share the PDF with the person (attach it, open it, or give its path), and summarise the changes in a before/after table.

### 7. Iterate

Apply exactly what the person asks. When a request conflicts with a rule, do it anyway and state the tradeoff in one line. For example, link labels look cleaner, but parsers that strip links lose the URL. Re-run the self-review after every change, and keep the page count.

### 8. Designed version

Build it once the content is locked. Read `references/layout.md`. Start from `assets/templates/designed.html`, or match a reference resume the person likes. The designed version carries less text, around 300 words, because whitespace is what makes it look clean. Condense the wording, never shrink the type. List every cut so the person can veto it.

### 9. DOCX

Run `scripts/to_docx.py` on the ATS HTML. Workday parses DOCX better than PDF, and some people edit in Word.

### 10. Role variants

When the person targets more than one role, finish the first variant completely. Then copy its folder and run a short interview round on what the new role screens for. A founding role, for example, cares about range, code and brand. Rewrite rather than tweak, because each variant needs its own lead story.

### 11. LinkedIn copy

Read `references/linkedin.md` and write `linkedin.md` to match the main variant. Never edit someone's live profile without their explicit go-ahead, because it publishes immediately.

### 12. Hand-off

Finish with a table showing which file to use for which channel. If the folder is a git repo, offer to commit.

## Requirements

- Any agent that can read files and run shell commands. Web access makes the research step much better.

- Chrome, Chromium or Edge for rendering. `scripts/render.py` finds them automatically.
- Python 3.
- `python-docx` for DOCX output (`pip install python-docx`).
- Poppler (`pdftotext`, `pdffonts`) makes `check.py` more thorough. Without it, the script falls back to basic checks.
