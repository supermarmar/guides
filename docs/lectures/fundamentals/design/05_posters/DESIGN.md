# Poster and one-pager tokens

A single sheet, read standing up or at a glance, with no speaker and no scroll. Two related formats: the large-format conference poster (A0, A1) and the business one-pager (A4). Both share the defining constraint, which is that the whole argument must survive being read in three seconds by someone walking past.

Inherits [the house file](../DESIGN.md) and overrides the type scale by the largest factor of any medium, because viewing distance is the governing variable.

## Overview

**Inherits unchanged:** neutral ramp, accent, semantic colours, data palette.

**Overrides:** the type scale entirely, driven by viewing distance. Elevation is flat. Spacing scales with the sheet.

**Adds:** distance-legibility tokens, the Better Poster layout, a one-pager block structure, and Isotype pictogram rules.

**Key characteristics:**
- Three reading depths designed simultaneously: 3 seconds at 2m, 30 seconds at 1m, 3 minutes at 0.5m
- The main finding is the largest thing on the sheet, stated as a sentence
- 25 to 40 per cent whitespace, deliberately reserved rather than left over
- Quantity shown by repeating a pictogram, never by scaling one
- Word count is a design token, not an outcome

## The three-depth model

A poster has three audiences who are the same person at three distances, and it must serve all of them at once.

| Depth | Distance | Time | Content | Words |
|---|---|---|---|---|
| Billboard | 2m | 3 seconds | The finding, as one sentence. Title, author | 10 to 20 |
| Summary | 1m | 30 seconds | Problem, finding, why it matters | 50 to 150 |
| Detail | 0.5m | 3 to 5 minutes | Method, results, caveats, references | 500 to 800 total |

Most posters are built for the third audience only and consequently reach none of them, because nobody stops for a poster they cannot parse from the aisle.

Mike Morrison's Better Poster template is the sharpest attack on this failure. His layout gives the centre of the sheet to a single plain-language statement of the finding, at enormous size, with supporting material relegated to sidebars. Version 2 restores more of the method detail and adds a QR code linking to the full paper, which is the honest resolution: the poster earns the conversation, the paper carries the evidence.

## Canvas

### Conference poster

| Token | A0 | A1 | A2 |
|---|---|---|---|
| `{sheet.size}` | 841 × 1189mm | 594 × 841mm | 420 × 594mm |
| `{sheet.dpi}` | 150 | 200 | 250 |
| `{sheet.bleed}` | 5mm | 3mm | 3mm |
| `{sheet.safe}` | 10mm inside trim | 8mm | 6mm |
| `{sheet.margin}` | 40mm | 30mm | 24mm |
| `{qr.size}` | 100 to 125mm | 80mm | 55mm |

Landscape is the conference default. Morrison's template is 36 × 48 inches (914 × 1219mm), close to A0 portrait, and its proportions transfer to A0 without redrawing.

Print resolution falls as the sheet grows because viewing distance grows with it. 150 DPI at A0 is not a compromise; at two metres it is more resolution than the eye resolves.

### One-pager

| Token | Value |
|---|---|
| `{sheet.size}` | A4, 210 × 297mm |
| `{sheet.margin}` | 15mm |
| `{sheet.columns}` | 2, with a 8mm gutter |
| `{sheet.dpi}` | 300 |

## Typography

### Distance legibility

The governing table. Sizes are the practitioner consensus from institutional poster guidance rather than a formula.

| Read at | Body minimum | Body comfortable | Heading | Title minimum | Title comfortable |
|---|---|---|---|---|---|
| 0.5m | 14pt | 18pt | 24pt | 36pt | 48pt |
| 1m | 18pt | 24 to 28pt | 32 to 36pt | 50pt | 72pt |
| 1.5m | 24pt | 32pt | 44pt | 60pt | 85pt |
| 2m | 28 to 32pt | 40pt | 54pt | 72pt | 96 to 120pt |

Design the body for 1m and the title for 2m. Those are the two distances that matter: one is where someone stops, the other is where they decide whether to.

### Conference poster scale

| Token | Size | Weight | Line height | Use |
|---|---|---|---|---|
| `{type.finding}` | 100 to 125pt | 600 | 1.05 | The main finding. The largest thing on the sheet |
| `{type.title}` | 72pt | 600 | 1.10 | Poster title |
| `{type.authors}` | 40pt | 400 | 1.25 | Authors and affiliation |
| `{type.h2}` | 36pt | 600 | 1.20 | Section headings |
| `{type.body}` | 24 to 28pt | 400 | 1.45 | Body text |
| `{type.caption}` | 20pt | 400 | 1.35 | Figure captions |
| `{type.reference}` | 16pt | 400 | 1.30 | References, acknowledgements |

The ratio of title to body is roughly 2.5 to 3, and between adjacent heading levels roughly 1.3 to 1.5. Wider than that and the hierarchy fragments; narrower and it disappears.

### One-pager scale

| Token | Size | Weight | Line height | Use |
|---|---|---|---|---|
| `{type.op-title}` | 24pt | 600 | 1.15 | Title |
| `{type.op-lead}` | 13pt | 400 | 1.40 | Value proposition, one sentence |
| `{type.op-h2}` | 11pt | 600 | 1.25 | Block headings |
| `{type.op-body}` | 9.5pt | 400 | 1.40 | Body |
| `{type.op-figure}` | 28pt | 600 | 1.00 | A headline number |
| `{type.op-caption}` | 7.5pt | 400 | 1.30 | Sources, footnotes |

### Word budgets

| Token | Value |
|---|---|
| `{limit.poster-total}` | 800 words, 500 preferred |
| `{limit.poster-finding}` | 20 words |
| `{limit.poster-section}` | 120 words |
| `{limit.onepager-total}` | 400 words, 300 preferred |
| `{limit.whitespace}` | 25 to 40 per cent of the sheet |

Whitespace is a budget line, not a residue. Below 25 per cent the sheet reads as cramped regardless of what is on it.

## Colors

Inherits the house palette. Two constraints specific to the medium.

Large-format printing shifts colour. A tint that reads as a subtle background on a monitor becomes a solid field at A0, and a mid-grey rule becomes heavier than intended. Proof at size, or at least print an A4 crop at 100 per cent scale, before committing.

Colour must survive ambient light. Conference halls and office corridors are lit unevenly and often badly, so the contrast floor is higher than on screen: aim for 7:1 on body text rather than 4.5:1.

| Token | Value | Use |
|---|---|---|
| `{color.sheet}` | `#FFFFFF` | Ground |
| `{color.sheet-tint}` | `#F7F6F3` | Sidebar and block backgrounds |
| `{color.text}` | `#191918` | Body and headings |
| `{color.text-secondary}` | `#5C5B57` | Captions, references |
| `{color.accent}` | `#3D2EB5` | Section markers, the finding's emphasis. Darkened from house for print |
| `{color.rule}` | `#D5D3CD` | Block separators |

## Layout

### Better Poster structure

Morrison's layout, three vertical zones across the sheet.

| Zone | Width | Content |
|---|---|---|
| Left sidebar | 25% | Introduction, method, in `{type.body}` |
| Centre | 50% | Title, then `{type.finding}` occupying most of the height, then one key graphic |
| Right sidebar | 25% | Results detail, references, QR code |

The proportions are the template's defaults rather than a universal standard, and they are worth adapting. The load-bearing idea is not the 25/50/25 split; it is that the finding gets the centre and the middle half of the sheet, and everything that would traditionally fill the poster is pushed to the edges.

The QR code sits bottom-right at 100 to 125mm square on A0, which scans reliably from about a metre. It links to the paper, the data or the repository. It is the mechanism that lets the poster stop trying to be the paper.

### Conventional academic structure

Where the venue requires the traditional layout, use three or four columns reading left to right, top to bottom, with the finding still stated as a sentence in a full-width band under the title. The band alone recovers most of the benefit.

### One-pager blocks

Vertical proportions of the A4 sheet.

| Block | Height | Content |
|---|---|---|
| Header | 8% | Title and one-sentence value proposition |
| Problem | 18% | What is wrong, with one number |
| Solution | 22% | What is proposed |
| Evidence | 32% | Data, ideally a single chart plus two or three figures |
| Ask | 12% | One call to action |
| Footer | 8% | Source, contact, date |

Evidence gets the largest block because it is the only one the reader cannot supply themselves. One ask, not three; a one-pager with three asks gets none of them.

### Grid

| Token | Poster | One-pager |
|---|---|---|
| `{grid.columns}` | 12 | 6 |
| `{grid.gutter}` | 20mm (A0), 14mm (A1) | 8mm |
| `{grid.baseline}` | 1.45 × body size | 1.40 × body size |

## Elevation and depth

Flat. `{elevation.0}` only. Blocks are separated by `{color.sheet-tint}` fills or `{color.rule}` lines, never by shadows.

## Shapes

| Token | Value |
|---|---|
| `{radius.block}` | 6mm (A0), 4mm (A1), 2mm (A4) |
| `{radius.chip}` | 3mm (A0), 1.5mm (A4) |

Radius scales with the sheet. An 8px radius at A0 is invisible; at A4 it is right.

## Components

### `finding-statement`

The centrepiece. `{type.finding}`, `{color.text}`, centred in the middle zone, maximum 20 words, written in plain language a non-specialist can parse. A complete sentence with a verb.

"Loan-level features add nothing once portfolio vintage is controlled for" is a finding. "An analysis of loan-level feature contribution" is a title pretending to be one.

### `pictogram-set`

Isotype rules, from Otto Neurath and Marie Neurath's work with Gerd Arntz. Two rules do the work.

**Repeat, never scale.** Twice the quantity is two symbols, not one symbol at double size. Doubling a symbol's linear dimensions quadruples its area, and the reader will read the area. This is the single most-violated rule in modern infographics.

**One symbol, one concept, one size.** Every instance of a symbol is identical, and each symbol means exactly one thing throughout the sheet.

| Token | A0 | A4 |
|---|---|---|
| `{pictogram.small}` | 20mm | 5mm |
| `{pictogram.standard}` | 35mm | 8mm |
| `{pictogram.large}` | 60mm | 14mm |
| `{pictogram.gap}` | 0.25 × symbol width | 0.25 × symbol width |

### `block`

Background `{color.sheet-tint}`, radius `{radius.block}`, padding equal to `{type.body}` size × 1.5. Heading in `{type.h2}`, body in `{type.body}`. Proximity does the grouping: the gap between blocks must clearly exceed the padding inside them, or the reader cannot tell where one idea ends.

### `figure-poster`

Graphic, then caption in `{type.caption}` below. Charts need heavier treatment than anywhere else in this system: line weights of 2 to 3mm at A0, direct labels never a legend, axis labels at `{type.body}` size. A chart exported at report settings and enlarged to A0 will have hairline strokes and 6pt labels, and this is the most common poster failure after word count.

### `qr-block`

QR code at `{qr.size}` (100 to 125mm at A0, 20mm at A4), with a `{type.caption}` label stating what it links to. An unlabelled QR code gets scanned by nobody.

### `metric-figure`

One-pager component. A number in `{type.op-figure}` `{color.accent}`, label beneath in `{type.op-caption}` `{color.text-secondary}`. Three at most in a row. This is the block a busy reader takes away.

## Do's and don'ts

### Do

- State the finding as a plain sentence and make it the largest element
- Design for 2m and 1m simultaneously and check both by standing back
- Budget 25 to 40 per cent whitespace before laying anything out
- Repeat pictograms to show quantity
- Label chart series directly and thicken every stroke
- Put a QR code to the full source, and label it
- Proof at print size, or at least an A4 crop at 100 per cent

### Don't

- Don't exceed 800 words on a poster, or 400 on a one-pager
- Don't scale a single pictogram to show quantity
- Don't reproduce the paper's abstract as the poster's introduction
- Don't export charts at report settings and enlarge them
- Don't use a legend
- Don't put more than one ask on a one-pager
- Don't fill the whitespace because it looks empty. It is doing work

## Responsive behaviour

Fixed sheet. What varies is the size, and the type scale must be re-derived rather than proportionally scaled, because viewing distance does not scale linearly with sheet size. A0 is read from 2m and A1 from about 1.2m, so A1 body text is not simply 71 per cent of A0 body text; it is set from the 1.5m row of the legibility table.

| Sheet | Design distance | Body | Title |
|---|---|---|---|
| A0 | 2m | 28pt | 96 to 120pt |
| A1 | 1.5m | 24pt | 72pt |
| A2 | 1m | 20pt | 54pt |
| A4 one-pager | 0.4m | 9.5pt | 24pt |

## Iteration guide

1. Write the finding sentence first. If it will not fit in twenty words, the analysis is not finished.
2. Print an A4 crop at 100 per cent and read it at the design distance, scaled. Everything else is guesswork.
3. Cut words before shrinking type. The word budget is the constraint the design serves.
4. When a block will not fit, delete it and put its content behind the QR code.

## Known gaps

- The distance-legibility table is practitioner consensus from institutional poster guidance rather than a measured standard, and two commonly quoted rules of thumb (text height in cm ≈ distance in m × 0.84, and point size ≈ distance in inches × 0.75) disagree with it and with each other. The table is the safer guide; the formulae should not be used.
- Morrison's 25/50/25 split is the template default. Whether those exact proportions are optimal has not been tested; the principle behind them has been, informally and at scale, by the number of researchers who adopted it.
- Arntz's original Isotype pictograms have no published dimensional specification; the sizes above are derived from the medium, not from the source.
- The one-pager block proportions are synthesised from business practice rather than any published standard. Treat them as a starting layout.
- No CMYK conversion guidance, no specification of paper stock or finish, both of which change perceived colour materially at large format.
- No specification for a digital poster (a poster viewed on a screen at a virtual conference), which has entirely different distance assumptions.
