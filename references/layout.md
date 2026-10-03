# Layout and Rendering

The resume ships in two layouts. The ATS version is built for parsers and portals, and the designed version for people reading an email or a referral. The content is verified once, and the designed version condenses it.

## ATS version (`assets/templates/ats.html`)

- One column. Dates sit right-aligned in the same row, which still extracts in reading order.
- Contact details go in the body, not in a header or footer.
- Use standard headings: Experience, Education, Skills.
- No tables, text boxes, icons, images or skill bars.
- Fonts must embed as TrueType. `check.py` fails on Type 3 fonts, which some parsers can't read.
- **Links.** Labels like "Portfolio | LinkedIn | GitHub" look clean, but a parser that strips links keeps only the word. Write URLs out ("site.com, linkedin.com/in/x") if the person mostly applies through portals. Mention the tradeoff once, then do what they choose.
- **Page size.** Use A4 for India, the UK, Europe and Australia. Use Letter for the US and Canada.

## Designed version (`assets/templates/designed.html`)

The default look follows these rules:
- Geist, at regular and medium weights only
- the name set large in regular weight, not bold
- sentence-case section labels with no rules or all-caps
- hierarchy shown through grey versus near-black text, not bold and italics
- a narrow left column holding Contact only
- everything else in the main column
- about 300 words in total, so the whitespace shows

What makes a resume look clean is mostly how few words it carries, more than the type. When the person calls a version cluttered, check these causes in this order:
1. **Word count.** Aim for about 300 words. Cut the weakest clauses, internships and duplicate context.
2. **The sidebar.** Keep it empty except for Contact. A sidebar full of skills and education reads as clutter.
3. **Small grey lines per role.** Allow one short company label beside the name. Drop locations and context sentences.
4. **Body size.** Use 10pt with a line height of about 1.45. Never go below 9pt to make text fit.

List every cut you make for the designed version, so the person can veto any of them.

## Matching a reference resume

When the person shares a resume whose look they like:
- Measure it. `pdffonts ref.pdf` gives the font. `pdftotext -bbox ref.pdf out.html` gives the word boxes, where the box height is about 1.36 times the font size for most sans fonts. Measure the column x-positions and the line spacing.
- Copy the type system and the spacing, never its text or its owner's name.
- If the font is a variable font, generate static instances (`python3 -m fontTools.varLib.instancer font.ttf wght=400 --static -o font-400.ttf`). Otherwise Chrome embeds it as Type 3.
- Note what the reference gets away with that this person can't. A shorter career means fewer words. Famous employers need no context line.

## Fitting one page

When a draft spills onto page 2, fix it in this order and stop as soon as it fits:
1. Fix orphans, meaning lines that hold only one or two words. Rephrase the bullet so it ends a few words earlier.
2. Cut the lowest-value content, in this order:
   - interests
   - internship descriptions
   - duplicate context lines
   - the weakest bullet in the oldest role
3. Merge two related bullets.
4. Shrink the margins, to no less than 11mm on the top and bottom and 14mm on the sides.
5. Only then shrink the line height. Never take the body text below 9pt.

When content gets shorter, give the space back by restoring the template's margins.

**A thin page means missing facts, not bad layout.** If more than about a quarter of the page is empty at template sizes, don't enlarge the type, widen the line spacing or stretch the margins past the template. Padding the layout reads as padding to a recruiter. Instead:
1. Go back to the interview with 3–5 targeted questions that would each add a bullet. Examples are earlier years' results, scope numbers, how a result was achieved, and certifications.
2. If no one can answer right now, ship the page as it is and list those questions at the top of your hand-off, so the person knows exactly what fills it.

## Gotchas

- **`text-wrap: pretty`** balances the last lines of a paragraph, which kills orphans in the designed version. It can also add a line to a paragraph, so leave it out of tight ATS layouts.
- **Two-column PDFs** extract the sidebar text into the middle of a bullet. That's fine for the designed version, and it's the reason the ATS version stays one column.
- **The rupee sign and other non-Latin symbols.** Check that `pdftotext` extracts them. Geist and most system sans fonts handle "₹".
- **Fonts path.** The templates load `../fonts/` from the variant folder. Copy `assets/fonts/` to `resume/fonts/` once.
