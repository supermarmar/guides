# Report tokens

Print-first, A4, destined for PDF and occasionally for paper. A validation report, a board paper, a technical note. The reader is senior, sceptical, short of time, and will read the executive summary and the exhibits before deciding whether to read anything else.

Inherits [the house file](../DESIGN.md) and overrides the type family (serif body), the scale (point sizes rather than pixels), and the elevation system (flat, always). Adds page geometry, a table specification, exhibit conventions, and the IBCS business notation.

## Overview

**Inherits unchanged:** neutral ramp, semantic colours, data palette and ramps, radius scale (barely used), spacing logic.

**Overrides:** body is `{font.serif}` at 11pt. Elevation is `{elevation.0}` only, because a drop shadow printed on paper is a picture of a drop shadow. The accent is used far more sparingly than on screen.

**Adds:** page geometry, vertical rhythm anchored to the baseline, table and exhibit specifications, IBCS scenario notation for business charts, and running header and footer definitions.

**Key characteristics:**
- A4 at 11pt Source Serif 4 on 15.4pt leading, giving a measure near 66 characters
- Vertical rhythm: every vertical space is a multiple of the 15.4pt baseline
- Tables have horizontal rules only, no vertical rules, no zebra striping
- Figures captioned below, tables titled above
- Every exhibit carries a source line
- IBCS scenario notation encodes actual, plan, forecast and prior year by fill, not by hue

## Page geometry

| Token | Value | Notes |
|---|---|---|
| `{page.size}` | A4, 210 × 297mm | 595 × 842 PostScript points |
| `{page.margin-top}` | 25mm | |
| `{page.margin-bottom}` | 28mm | Deeper than the top, so the block sits above optical centre |
| `{page.margin-inner}` | 25mm | 30mm when bound, to absorb the gutter |
| `{page.margin-outer}` | 25mm | |
| `{page.text-width}` | 160mm | Roughly 66 characters at 11pt |
| `{page.text-height}` | 244mm | |
| `{page.header-height}` | 12mm | Measured from the trim edge |
| `{page.footer-height}` | 15mm | |
| `{page.columns}` | 1 | Two columns only for dense appendices |

The margins are deliberately less generous than Butterick's 1.5 to 2 inches, which he pitches at 12pt on US Letter and which produces a measure around 50 characters. At 11pt on A4, 25mm gives 160mm of text, which lands at roughly 66 characters, the target every authority converges on.

Tschichold's Van de Graaf canon (inner 2, top 3, outer 4, bottom 6) is the classical alternative and produces a beautiful book page: on A4 that is 21mm inner, 31mm top, 42mm outer, 63mm bottom. It is the right choice for a bound document read cover to cover. It is the wrong choice for a report that will be read on a laptop screen, because the asymmetry only resolves across a spread. Use the symmetric geometry above unless the document is genuinely being bound.

## Typography

### Families

| Token | Stack | Use |
|---|---|---|
| `{font.body}` | Source Serif 4, Charter, Georgia, Cambria, serif | Body text, tables |
| `{font.display}` | Inter, Segoe UI, Helvetica, sans-serif | Headings, exhibit labels, running heads |
| `{font.mono}` | JetBrains Mono, Consolas, monospace | Code, formulae |

Serif body with sans headings. The pairing is conventional because it works: the serif carries long text, the sans marks structure, and the contrast between them makes the hierarchy legible at a glance.

### Scale

Baseline leading is 15.4pt (11pt × 1.4). Every heading's space-before and space-after is a multiple of it, which keeps text on facing pages aligned.

| Token | Size | Leading | Weight | Space before | Space after | Use |
|---|---|---|---|---|---|---|
| `{type.title}` | 28pt | 32pt | 600 sans | 0 | 30.8pt | Document title, cover only |
| `{type.h1}` | 18pt | 22pt | 600 sans | 30.8pt | 7.7pt | Numbered section |
| `{type.h2}` | 14pt | 18pt | 600 sans | 23.1pt | 7.7pt | Subsection |
| `{type.h3}` | 11.5pt | 15.4pt | 600 sans | 15.4pt | 3.9pt | Minor heading, run-in permitted |
| `{type.body}` | 11pt | 15.4pt | 400 serif | 0 | 7.7pt | Body text |
| `{type.body-lead}` | 12pt | 17pt | 400 serif | 0 | 7.7pt | Executive summary |
| `{type.table}` | 9.5pt | 13pt | 400 serif | 0 | 0 | Table cells |
| `{type.table-head}` | 9.5pt | 13pt | 600 sans | 0 | 0 | Table headers |
| `{type.caption}` | 9pt | 12pt | 400 sans | 7.7pt | 0 | Exhibit captions |
| `{type.source}` | 8pt | 11pt | 400 sans | 3.9pt | 0 | Source and footnote lines |
| `{type.footnote}` | 8.5pt | 11.5pt | 400 serif | 0 | 0 | Page footnotes |
| `{type.running}` | 8pt | 11pt | 400 sans | 0 | 0 | Running head and folio |

Butterick's range is 10 to 12pt for print body, and 11pt sits in the middle. Do not default to 12pt just because Word does; 11pt with correct leading fits more on the page and reads better than 12pt at Word's default spacing.

### Measure and rhythm

| Token | Value |
|---|---|
| `{measure.target}` | 66 characters |
| `{measure.range}` | 50 to 75 characters |
| `{rhythm.baseline}` | 15.4pt |

Butterick permits up to 90 characters, Bringhurst caps at 75. Where they disagree, take the narrower figure: the overlap of the two ranges, 50 to 75, is the safe band.

### Paragraphs

Space between paragraphs, no first-line indent. Space is `{space.para}` = 7.7pt, half the baseline. Never both: an indent plus a blank line signals the paragraph break twice and wastes the page.

The exception is a long continuous narrative section with no headings, where a 11pt first-line indent (1em) and zero space reads better and saves a line per paragraph. Choose per document, never per paragraph.

### Numerals

Tabular lining figures in every table and every exhibit. Proportional figures in running prose. Source Serif 4 carries both; reach the tabular set with `font-variant-numeric: tabular-nums` in CSS or the corresponding OpenType feature in the layout tool.

## Colors

Print reduces the palette. Most reports are read in greyscale at least once, so nothing may depend on hue alone.

| Token | Value | Use |
|---|---|---|
| `{color.text}` | `#191918` | Body text. Near-black, not `#000000`, which over-inks |
| `{color.text-secondary}` | `#5C5B57` | Captions, sources, footnotes |
| `{color.rule-strong}` | `#37352F` | Rule above and below a table header |
| `{color.rule}` | `#C9C7C1` | Rules between table rows |
| `{color.rule-light}` | `#E8E6E1` | Section dividers |
| `{color.accent}` | `#3D2EB5` | Section numbers, exhibit labels. `{color.accent-deep}` from house, darkened for print |
| `{color.fill-tint}` | `#F2F1ED` | Callout and highlight blocks |

### Chart colours

Charts inherit the house `{data.*}` palette. Two print-specific constraints apply.

First, verify every chart in greyscale before it ships. A chart that collapses when the colour is removed will fail for the reader who prints it, and for the roughly one man in twelve with a colour vision deficiency.

Second, prefer direct labelling to a legend. A legend forces the reader to move between the key and the marks; a label on the line does not. This is the single highest-value change to most report charts.

### IBCS scenario notation

For business and financial reporting, the International Business Communication Standards define a semantic notation so that the same visual encoding always means the same thing. Once a reader learns it in one exhibit, every subsequent exhibit is free.

| Scenario | Fill | Token |
|---|---|---|
| Actual | Solid dark | `{ibcs.actual}` = `#37352F` |
| Plan or budget | Outline only, no fill | `{ibcs.plan}` = border `#37352F`, fill none |
| Forecast | Hatched, 45 degrees | `{ibcs.forecast}` = hatch `#37352F` on white |
| Previous year | Solid light grey | `{ibcs.prior}` = `#C9C7C1` |
| Favourable variance | `#1E9D54` | `{ibcs.good}` |
| Adverse variance | `#DC2855` | `{ibcs.bad}` |

The scenarios are distinguished by fill pattern, not by hue, which is why the notation survives greyscale printing. Colour is reserved for variance, where it carries the only judgement in the chart.

IBCS's governing acronym is SUCCESS: Say (convey a message), Unify (apply the semantic notation), Condense (increase information density), Check (ensure visual integrity), Express (choose the right visualisation), Simplify (remove clutter), Structure (organise the content).

## Layout

### Vertical rhythm

Every vertical measurement is a multiple of `{rhythm.baseline}` (15.4pt). Headings, exhibit blocks, table blocks and paragraph spacing all resolve to the grid. The payoff is that body text on facing pages sits on the same lines, which the reader will not notice and would notice immediately if it were absent.

### Exhibit placement

Exhibits sit at the top or bottom of a page, never mid-column with text above and below, and never on a page before their first mention. An exhibit wider than `{page.text-width}` rotates to landscape on its own page rather than shrinking below legibility.

### Spacing

| Token | Value | Use |
|---|---|---|
| `{space.para}` | 7.7pt | Between paragraphs |
| `{space.list}` | 3.9pt | Between list items |
| `{space.exhibit}` | 15.4pt | Above and below an exhibit block |
| `{space.section}` | 30.8pt | Above a `{type.h1}` |

## Elevation and depth

`{elevation.0}` only. Flat surfaces separated by rules. No shadows, no gradients, no rounded panels floating over the page.

## Shapes

Square. `{radius.xs}` (4px, roughly 3pt) is the maximum, used only on callout blocks and code blocks. Everything else is a rectangle with rules.

## Components

### `table`

The most important component in a report, and the one most often mishandled.

- Type `{type.table}`, headers `{type.table-head}`, tabular figures throughout.
- Rule above the header (`0.75pt {color.rule-strong}`), rule below the header (`0.5pt {color.rule-strong}`), rule below the last row (`0.75pt {color.rule-strong}`), and hairlines (`0.25pt {color.rule}`) between body rows only where the table exceeds roughly eight rows.
- **No vertical rules.** Alignment does the work vertical rules were invented for, and every rule you remove is ink the reader no longer has to filter.
- **No zebra striping.** Tufte treats it as chartjunk. Where rows are long enough to lose, add a hairline or a group gap, not a fill.
- Cell padding `4pt` vertical, `8pt` horizontal.
- Text left, numbers right or decimal-aligned, dates left, headers aligned to match their column's data.
- Decimal alignment beats right alignment wherever the number of decimal places varies.
- Totals row: rule above, weight 600, no fill.

Table titles sit **above** the table. A table is read top to bottom, so its title is its first row.

### `exhibit`

A chart, diagram or image with its apparatus.

```
[Exhibit label]     Exhibit 3        <- {type.caption}, 600 weight, {color.accent}
[Title]             A full-sentence statement of what the exhibit shows
[The graphic]
[Source line]       Source: ...      <- {type.source}, {color.text-secondary}
```

The title is a sentence, not a topic label. "Exposure is concentrated in two sectors" tells the reader what to see; "Sector exposure" makes them work it out. This is the consulting deck's action title borrowed for print, and it is the highest-value habit in the whole specification.

Captions go below figures, above tables. This is convention rather than evidence, but it is near-universal and breaking it costs credibility for nothing.

### `callout`

Background `{color.fill-tint}`, no border, padding `{space.para}` × 2 all round, radius `{radius.xs}`, left rule `2pt solid {color.accent}`. For a definition, a caveat or a key finding lifted out of the flow. One per page at most.

### `running-head`

`{type.running}`, `{color.text-secondary}`. Left: document short title. Right: section title. Rule below at `0.25pt {color.rule-light}`. Suppressed on the cover and on section-opening pages.

### `folio`

`{type.running}`, `{color.text-secondary}`, centred or outer-aligned in the footer. Roman numerals for front matter, arabic from the first body page. Format "7" or "7 of 34"; never "Page 7 of 34", which spends four words on nothing.

### `footnote`

`{type.footnote}`, separated from the body by a `0.25pt` rule 40mm wide, left-aligned. Superscript markers in the text. Number continuously through the document rather than restarting per page, so a reader can refer to "footnote 14" unambiguously.

## Do's and don'ts

### Do

- Hold every vertical measurement to a multiple of `{rhythm.baseline}`
- Title every exhibit with a sentence that states the finding
- Put a source line under every exhibit and every table
- Use tabular figures in every column of numbers
- Decimal-align numbers whose precision varies
- Check every chart in greyscale before shipping
- Label chart series directly rather than in a legend
- Use IBCS scenario notation consistently once you have used it once

### Don't

- Don't use vertical rules in tables
- Don't use zebra striping
- Don't default to 12pt because the word processor did
- Don't combine first-line indents with paragraph spacing
- Don't let an exhibit appear before its first mention in the text
- Don't shrink an exhibit below legibility to make it fit; rotate the page
- Don't put a drop shadow on anything
- Don't write "Page 7 of 34"

## Responsive behaviour

Not applicable in the screen sense. The document is a fixed canvas. Three delivery contexts exist and the geometry above serves all three, with these adjustments.

| Context | Adjustment |
|---|---|
| Printed single-sided | As specified |
| Printed and bound | `{page.margin-inner}` rises to 30mm; margins become mirrored |
| Read on screen as PDF | Unchanged. The 11pt body reads acceptably at 100 per cent zoom on a laptop, which is why the measure was set at 66 rather than 50 characters |

Do not build a separate screen version. A report with two layouts has two documents to keep in sync, and they will diverge.

## Iteration guide

1. Change the baseline before changing anything else. Every vertical token derives from it.
2. If a table will not fit, reduce the columns before reducing the type. A table at 8pt is a table nobody reads.
3. Exhibit titles are the cheapest improvement available. Rewrite them as sentences before touching the visual design.
4. When adding a chart type, define its IBCS encoding at the same time or the notation drifts.

## Known gaps

- The full IBCS ruleset is proprietary, now published as ISO 24896. The scenario encodings above were reconstructed from published summaries and third-party implementations (Zebra BI, Inforiver) rather than the standard itself, and should be verified against it before being used where compliance matters.
- Source Serif 4 has not been proofed at 11pt on the intended output device. The leading may need adjusting once it has.
- No specification for the cover page, contents page or appendix numbering.
- Karen Schriver's empirical document-design findings are cited in the lecture material but no quantitative results were extracted into tokens here.
- Central bank and consulting house report styles (Bank of England, BIS, McKinsey) were observed in published PDFs rather than from style guides, which are not public. Treat the observed conventions as evidence of practice, not as specification.
- Two-column appendix layout is named but not specified.
