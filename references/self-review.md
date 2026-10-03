# Self-Review

Run this before showing any draft. Reviewing it yourself catches the mistakes a person would otherwise spend a round pointing out.

## 1. Run the script

```bash
python3 scripts/check.py "resume/<variant>/First Last Resume.pdf" --max-pages 1
```

The script reports:
- page count
- word count
- banned words
- fonts that aren't embedded as TrueType
- link targets
- probable orphan lines
- the first lines of extracted text, so you can confirm reading order

Fix every failure before going on.

## 2. Walk the checklist

| Check | Pass when |
|---|---|
| Impact first | Every bullet opens with a result, or with scope when no result exists. Never a duty, a present-tense verb, or an "-ing" verb |
| Traceable | Every number and claim is in `facts.md` with a source |
| Defined numbers | Each metric has its denominator and period, or doesn't need them |
| Honest credit | Team outcomes say what the person did |
| Honest title | The headline and titles match titles actually held |
| No overclaims | Words like "from scratch", "sole", "first" and "single-handedly" match the source exactly |
| Plain words | No internal product names, no unexplained acronyms, nothing confidential |
| No laundry lists | No bullet is an inventory of items |
| Tone | Matches the tone chosen in the interview, with no approval-seeking words |
| Seniority | For senior targets, each recent role shows scope, a multiplier, or evidence-settled judgment |
| Fit | One page, no orphans, type at template sizes. If more than a quarter of the page is empty, run more interview questions rather than enlarging the layout |
| Dates | Match the dates confirmed in the interview |

## 3. Report it

Open with the draft. Follow it with a short table of what changed, then one line on what the review fixed, for example "Review fixed 2 orphans and 1 'helped'." Then list any claims the person should double-check. Keep this list to two or three items, and phrase each one as a question they can answer in a word.
