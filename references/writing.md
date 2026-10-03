# Writing Rules

These rules turn verified facts into bullets a recruiter absorbs in seconds. Recruiters spend about 7 seconds on a first pass and read the first few words of each line, so the result has to come first.

## Contents
1. Bullet shape
2. Numbers that survive questions
3. Credit and titles
4. Plain words
5. Seniority signals
6. Tone
7. Banned words
8. Sections

## 1. Bullet shape

Write each bullet as **result, then "by", then what the person built or decided.**

| Field | Task-shaped (avoid) | Impact-first |
|---|---|---|
| Design | Redesigned the pricing page | Lifted trial-to-paid conversion 18% in an A/B test by moving the plan comparison above the fold |
| Engineering | Worked on the checkout service | Cut checkout latency from 1.2s to 300ms by moving pricing to an edge cache |
| Sales | Managed mid-market accounts | Grew a $2.1M territory 38% in a year by building a partner channel with two resellers |
| Nursing | Responsible for patient education | Cut 30-day readmissions on a 28-bed ward from 14% to 9% by running discharge teach-backs |
| Teaching | Taught Year 10 maths | Lifted pass rates from 61% to 84% in two years by redesigning the curriculum around weekly retrieval quizzes |

- Put the strongest bullet first in each role, because it gets read the most.
- **When a fact has no outcome, lead with scope, not the duty.** Scope is the size of what the person carried, such as people led, beds, volume, accounts, or systems. A duty opener tells the reader nothing the title didn't.

| Duty-shaped (avoid) | Scope-first |
|---|---|
| Coordinate night shifts as nurse in charge, leading 6 nurses | Led 6 nurses as night-shift nurse in charge of a 22-bed ICU |
| Cared for critically ill and ventilated patients | Nursed [N] ventilated patients a shift in a 22-bed ICU for 4 years before promotion to charge nurse |
| Built and maintained the checkout APIs | Owned the checkout APIs behind ~$X a month in orders |
| Served on the on-call rotation | Kept checkout at [X]% uptime as one of [N] on-call engineers |

  `[Brackets]` mark numbers to ask for. Only use numbers the person gave. If even scope is missing, that's an interview gap. Ask for it, or cut the bullet. Never write a present-tense duty ("Coordinate", "Manage", "Support") or an "-ing" opener.
- Keep bullets to 1–2 lines. If a bullet runs to three, it holds two ideas.
- Use 3–5 bullets for the current role, 2–3 for recent roles, and 1 for internships or old roles.
- Avoid laundry lists inside a bullet. "Designed A, B, C and D" reads as a task list. Pick the outcome that matters and drop the inventory.

## 2. Numbers that survive questions

Every number must survive "how did you measure that?" in an interview.

- **Give the denominator.** Write "80% of donors who started checkout completed it", not "80% conversion".
- **Give the period.** Write "within 2 months", "in Q3" or "over two years".
- **Check the sample.** A rate measured over a handful of events can collapse under questioning. If something launched three weeks ago, advise holding the number back until there's a quarter of data.
- **Company-level outcomes count** if the person's work clearly drove them and they can explain the link. These are rare and strong, so lead with them.
- **No metric?** Use one of these:
  - scale: users, accounts, revenue under care, team size
  - speed: 3 days to 4 hours
  - before and after: a manual weekly report turned into a live dashboard
  - adoption: 6 teams now use it
  - counts that sound big: deals, launches, clients
- **Watch for counts that read small**, like "13 documents" or "4 templates". Ask the person whether a count impresses or diminishes.
- Use "~", "over" or ranges for estimates. False precision ("23.7%") invites doubt.

## 3. Credit and titles

- **Say what the person did.** Use "sole designer", "led a team of 4" or "with a team of 5". Reviewers check for individual contribution versus team outcome.
- **Never claim a title the person didn't hold.** The headline uses their real title plus domain and spike, for example "Data Analyst · Retail · Forecasting and Automation". Claiming "Senior" without the title is a named red flag.
- **Stack promotions under one employer.** Give each title its own dates and bullets, and ask which projects happened under which title. Showing the promotion is itself a seniority signal.
- **Compare every bullet against its source before shipping.** For example, "from scratch" is an overclaim if they extended an existing system, and "led" is wrong if they were one of several leads.

## 4. Plain words

- **Describe products by what they do**, not internal names. A stranger can't decode "Project Nimbus", but "a dashboard that tracks every shipment across 3 warehouses" lands.
- **Spell out awards and programmes in plain language.** "Winner, national digital-health innovation challenge (Ministry of Health)" beats an acronym chain. Keep one recognisable proper noun so the award can be verified.
- **Hide anything the person flags as confidential.** Clients become "a Fortune 500 retailer" or "a top-10 US bank".
- **Keep politically or religiously specific references neutral.** Write "a relief fund" instead of naming a conflict, and tell the person why. They decide.
- **Add a one-line context under any employer that isn't widely known**, such as "One of Brazil's largest logistics marketplaces."

## 5. Seniority signals

For senior targets, make sure at least one bullet per recent role shows one of these:
- scope beyond their own team, like a system, a platform or cross-team adoption
- a disagreement settled with evidence ("settled a build-vs-buy debate with the CTO by running a two-week spike on both")
- a multiplier, meaning others adopt their work, standard or tool
- ambiguity, where they framed the problem rather than receiving it

AI and tools appear as outcomes inside bullets, like "cut report prep from 3 days to 4 hours with Python scripts". A tool list proves nothing.

## 6. Tone

Ask the person which tone fits their field.

- **Builder:** won, shipped, built, cut, launched, took X from Y to Z. This tone fits startups, tech and sales.
- **Measured:** delivered, developed, improved, led, established. This tone fits academia, healthcare, government and law.

In either tone, avoid approval-seeking words like "unasked", "was allowed to", "was given the chance" and "got to". They frame initiative as permission.

## 7. Banned words

Never use these:

| Kind | Words |
|---|---|
| Duty phrases | responsible for, helped, worked on, assisted, involved in, participated in, tasked with |
| AI tells | leveraged, spearheaded, orchestrated, utilized, synergy, cutting-edge, dynamic |
| Self-praise | results-driven, passionate, team player, detail-oriented, hard-working, go-getter |
| Unproven claims | "end-to-end" (unless a number proves it), "various", "multiple" (give the count) |

`scripts/check.py` flags most of these automatically.

## 8. Sections

| Section | Rule |
|---|---|
| Header | Name, real title plus domain plus spike, then city, email, phone and links. Links can show as labels or URLs (see `layout.md`). |
| Summary | None. The headline and the first bullet carry the positioning. |
| Experience | Reverse-chronological. Awards go in a small grey line under the role that earned them. |
| Projects | Only if they show range or traction the jobs don't, for example "Independent builds". |
| Internships | Collapse them into one block once there are two or more full-time roles. Cut those with no outcome. |
| Education | School, degree, honours or a strong GPA. The graduation year is the person's choice, so ask them. |
| Skills | Grouped and concrete, and only what they could defend in an interview. No skill bars. |
| Interests | Optional, specific, and the first thing to cut for space. |
