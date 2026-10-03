# Research Guide

Run two research subagents in the background as soon as you know the person's field, level and target role. Start the interview while they work. Fill in the bracketed parts of each prompt.

## Agent 1: market

```
Research the [YEAR] job market for a [CURRENT TITLE] with ~[N] years of experience in [FIELD/DOMAIN], based in [LOCATION], targeting [TARGET ROLE(S)] in [MARKETS: local / remote-global / relocation to X].

Use web search. Report concisely, with source URLs:
1. What hiring managers screen for in [TARGET ROLE] resumes now: senior signals, common rejection reasons, skills rising in demand (including AI fluency for this field).
2. Companies and segments hiring for this profile, with typical titles.
3. Salary bands for each market, in local currency, with sources. Flag aggregator sources as directional.
4. The top 20 ATS keywords for the target role.
5. Anything specific to this field's resumes: licences, certifications, publications, portfolios, clearances.

Keep it under ~900 words. No filler.
```

## Agent 2: resume practice for this field and level

```
Research resume best practices for [TARGET ROLE] in [FIELD], [YEAR]. Prefer hiring managers, recruiters and practitioners over SEO content farms.

Cover these, with sources:
1. What separates a mid-level resume from a senior one in this field.
2. How to quantify impact in this field: the metrics reviewers trust, and before/after bullet rewrites (paraphrased).
3. Format norms: page length, sections, whether a portfolio or publications list is expected, and norms specific to [COUNTRY] (photos, date of birth, A4 or Letter).
4. Red flags reviewers cite.
5. ATS realities in [YEAR], with myths debunked.

End with a "Rules to apply" checklist. Keep it under ~1000 words.
```

If the person names a source they trust, such as a recruiter's post or a thread, add it to agent 2's prompt as required reading.

## playbook.md template

Merge both reports into the person's playbook. Keep it scannable.

```markdown
# Resume Playbook: [Name], [Target role]

## 1. Market snapshot
| Signal | Finding |
### Salary bands
### Companies hiring

## 2. Rules to apply
### Content
### Banned words
### Format
### Where sources disagree (and what we chose)

## 3. This person's decisions
- Target, market, tone, confidentiality, layout choices from the interview

## Sources
```

Update section 3 whenever the person makes a decision during iteration. That way the playbook always records how this resume was built.
