# Working document and note tokens

Everyday documents that are not reports: a memo, a briefing note, a meeting record, a draft circulated for comment, a personal note in Obsidian. Written quickly, read once, often on a corporate machine that has whatever fonts Microsoft installed.

Inherits [the house file](../DESIGN.md) but makes one large concession the other mediums do not: the type stack degrades to fonts that exist on a standard Windows install, because a document that reflows on the recipient's machine has failed regardless of how good it looked on yours.

## Overview

**Inherits unchanged:** neutral ramp, spacing logic, table conventions, the discipline about heading space.

**Overrides:** the font stack entirely. Point sizes rather than pixels. No accent colour in the printed variant.

**Adds:** a Word style ladder mapped to the built-in style names, a corporate-safe font stack, and a parallel Obsidian and Markdown specification for the same content in a different container.

**Key characteristics:**
- Two profiles: **Office** (Word, .docx, circulated) and **Notes** (Obsidian, Markdown, personal)
- Office profile uses Word's built-in style names, so the document remains editable by someone who has never heard of a design system
- 11pt body, 1.15 to 1.25 line spacing, 2.54cm margins
- Never direct formatting; every visual property lives in a named style
- Notes profile is 17px at 1.6 leading in a 700px column

## Font stacks

### Office profile

Microsoft replaced Calibri with **Aptos** as the Microsoft 365 default in 2024. Aptos was drawn by Steve Matteson, who also drew Segoe. It ships with Office rather than with Windows, which matters: a machine with Windows but without a current Office install may not have it.

| Token | Stack | Use |
|---|---|---|
| `{font.office-sans}` | Aptos, Segoe UI, Calibri, Carlito, Arial, sans-serif | Body and headings, digital-first documents |
| `{font.office-serif}` | Cambria, Sitka Text, Georgia, serif | Body for documents intended to be printed and read at length |
| `{font.office-mono}` | Consolas, Courier New, monospace | Code, fixed-width data |

Carlito is in the sans stack deliberately: it is metrically compatible with Calibri, so a document falling back to it does not reflow. That is worth more than an aesthetically better substitute that changes the pagination.

Butterick would object to all of these. He is right in principle and the objection is overridden here for one reason: a document that arrives at a colleague's machine with substituted fonts and broken pagination is worse than a document set in Aptos. The concession is specific to circulated Office files and does not extend to PDFs, where the report profile applies and the fonts embed.

### Notes profile

| Token | Stack |
|---|---|
| `{font.notes}` | Inter, -apple-system, Segoe UI, sans-serif |
| `{font.notes-serif}` | Source Serif 4, Charter, Georgia, serif |
| `{font.notes-mono}` | JetBrains Mono, Consolas, monospace |

## Typography

### Office style ladder

These map to Word's built-in style names. Using the built-ins rather than custom styles means the navigation pane, the table of contents, the outline view, and every accessibility checker all work without configuration.

| Word style | Size | Weight | Space before | Space after | Line spacing |
|---|---|---|---|---|---|
| Title | 22pt | 600 | 0 | 12pt | 1.0 |
| Subtitle | 13pt | 400, `{color.text-secondary}` | 0 | 18pt | 1.15 |
| Heading 1 | 16pt | 600 | 24pt | 6pt | 1.1 |
| Heading 2 | 13pt | 600 | 18pt | 6pt | 1.15 |
| Heading 3 | 11pt | 600 | 14pt | 4pt | 1.15 |
| Normal (body) | 11pt | 400 | 0 | 8pt | 1.20 |
| List Paragraph | 11pt | 400 | 0 | 4pt | 1.20 |
| Quote | 11pt | 400, `{color.text-secondary}` | 8pt | 8pt | 1.20 |
| Caption | 9pt | 400, `{color.text-secondary}` | 4pt | 8pt | 1.10 |
| Footnote Text | 9pt | 400 | 0 | 2pt | 1.05 |

Normal is the root. Every other style inherits from it, so changing the body typeface changes the whole document from one place. This is the entire point of the style system and the reason direct formatting is forbidden.

Space before a heading always exceeds space after it, by roughly three to one. Get this backwards and every heading appears to belong to the section above.

### Line spacing

Word expresses leading as a multiplier of the font's own line height, not of the point size, so Word's "1.15" is not 115 per cent of 11pt. The values above were chosen to land inside Butterick's 120 to 145 per cent band once Word has applied them. Where precision matters, set "Exactly" instead: 11pt body at exactly 14pt line spacing is 127 per cent and unambiguous.

### Paragraphs

Space after, no first-line indent. Set space-after to 8pt in the Normal style and never press Return twice. An empty paragraph is not spacing; it is an empty paragraph, and it will break pagination the moment the text above it reflows.

### Notes profile scale

| Token | Value | Line height | Use |
|---|---|---|---|
| `{type.notes-h1}` | 28px | 1.20 | Note title |
| `{type.notes-h2}` | 22px | 1.25 | Section |
| `{type.notes-h3}` | 18px | 1.30 | Subsection |
| `{type.notes-body}` | 17px | 1.60 | Body |
| `{type.notes-code}` | 15px | 1.55 | Code |
| `{type.notes-caption}` | 14px | 1.50 | Metadata, captions |

Obsidian's readable line length setting caps the column at roughly 700px, which at 17px Inter is close to 66 characters. Leave it on. Craig Mod's practical target, twelve to fifteen words per line, describes the same band from the other direction.

## Page geometry

| Token | Value | Notes |
|---|---|---|
| `{page.size}` | A4, 210 × 297mm | |
| `{page.margins}` | 25.4mm all sides | Word's default, and correct here |
| `{page.margin-bound}` | 31.7mm left | When the document will be printed and stapled |
| `{page.text-width}` | 159mm | Roughly 66 characters at 11pt Aptos |
| `{page.header}` | 12.7mm from edge | |
| `{page.footer}` | 12.7mm from edge | |

Word's default margins happen to be right for 11pt on A4. This is the one Word default worth keeping.

## Colors

The Office profile is near-monochrome, because these documents get printed on whatever is in the corridor and forwarded to people whose screens are not calibrated.

| Token | Value | Use |
|---|---|---|
| `{color.text}` | `#191918` | Body |
| `{color.text-secondary}` | `#5C5B57` | Captions, subtitles, quotes |
| `{color.heading}` | `#191918` | Headings. Not coloured |
| `{color.rule}` | `#C9C7C1` | Table rules, dividers |
| `{color.fill-tint}` | `#F2F1ED` | Table header fill, callout background |
| `{color.link}` | `#3D2EB5` | Hyperlinks only |

Headings are black, not brand-coloured. Coloured headings in a working document read as a template someone forgot to fill in, and they cost a photocopy generation of legibility for nothing.

The Notes profile may use the full house palette, including the accent, because it is read on one screen the author controls.

## Layout

| Token | Value |
|---|---|
| `{space.para}` | 8pt |
| `{space.list}` | 4pt |
| `{space.section}` | 24pt (before Heading 1) |
| `{list.indent}` | 6.35mm (0.25 inch) per level |
| `{list.max-depth}` | 2 |

Two levels of list nesting. A third level means the content wants to be a table or a set of sub-headings.

## Elevation and depth

None. `{elevation.0}` in the Office profile; the Notes profile may use `{elevation.1}` for callout blocks if the theme provides it.

## Shapes

Square in the Office profile. Word's shape defaults are unusable and the correct response is to not use shapes. The Notes profile inherits the house radius scale.

## Components

### `table-office`

- Type 10pt, headers 10pt weight 600.
- Header row: fill `{color.fill-tint}`, rule below at `1pt {color.rule}`.
- Body rows: hairline `0.5pt {color.rule}` below each, no vertical rules.
- Cell margins: 0.1cm top and bottom, 0.19cm left and right (Word's default cell margin is too tight vertically).
- Text left, numbers right, header alignment matches its column.
- Repeat the header row on every page: this is a table property, not something to fake with a second header.
- Never let a row break across pages.

### `callout-office`

A single-cell table with fill `{color.fill-tint}`, no borders except a `2pt {color.link}` left border, 0.3cm internal margins. Word has no native callout, and a one-cell table is the only construct that survives a round trip through track changes.

### `memo-header`

Four labelled lines at the top of a memo, before the Title style.

```
To:       [recipient]
From:     [author]
Date:     [absolute date, never "yesterday"]
Subject:  [a sentence, not a topic]
```

Set as a two-column borderless table so the values align. Labels in weight 600, values in 400. This is the standard memo block in both the civil service and the military briefing traditions, and its virtue is that a reader can triage the document from four lines.

### `decision-note`

A briefing note structure, one to two pages. Purpose, background, considerations, recommendation. Marked "For decision" or "For information" in the subject line, because that single phrase determines whether the reader needs to do anything.

Amazon's six-page narrative memo is the well-known long form of the same instinct: a hard page limit at 10pt, prose rather than bullets, read in silence at the start of the meeting. The constraint is the design. Whether six pages is the right number matters less than the fact that a number was fixed.

### `note-frontmatter`

Notes profile. YAML at the head of every Markdown file:

```
---
title:
created: YYYY-MM-DD
tags: []
---
```

Absolute dates, never relative. A note that says "last week" is unreadable in a year.

## Do's and don'ts

### Do

- Use Word's built-in style names, so the navigation pane and table of contents work
- Put every visual property in a style, never in direct formatting
- Keep space before a heading roughly three times the space after it
- Use `{space.para}` for paragraph separation, never a second Return
- Set absolute dates
- Repeat table headers across page breaks using the table property
- Keep the font stack to fonts the recipient will actually have

### Don't

- Don't press Return twice for spacing
- Don't press Tab or space bar to indent; use the paragraph indent
- Don't colour headings in a circulated document
- Don't nest lists more than two deep
- Don't use text boxes; they float free of the text and break in every conversion
- Don't combine first-line indent with paragraph spacing
- Don't send a .docx where a PDF was wanted, and don't send a PDF where the recipient needs to edit

## Responsive behaviour

Not applicable. Two fixed profiles.

The screen-versus-print distinction matters more here than the specification suggests. A document read on screen wants looser leading (1.25 rather than 1.15) and a slightly larger body, because the reader is further from the page. A document to be printed wants the tighter values so it fits. If a document will genuinely be both, choose the screen values: an over-spaced printed page costs a sheet of paper, whereas a cramped screen page costs the reader.

## Iteration guide

1. Change the Normal style. Everything else inherits from it, and a change anywhere else is a change in one place only.
2. If a document needs a fourth heading level, it needs restructuring rather than a fourth style.
3. Test the font fallback by opening the document on a machine without Office. If the pagination moves, the stack is wrong.
4. The Notes profile can experiment freely. The Office profile should not, because its readers did not opt in.

## Known gaps

- Word's line-spacing multiplier is relative to the font's internal line height, which varies by typeface. The 1.15 and 1.20 values above were chosen for Aptos and will land differently in Cambria. Setting "Exactly" avoids the problem and is untested here.
- No specification for tracked changes, comment formatting, or the compare view, all of which override document styling.
- Aptos ships with Microsoft 365, not with Windows. The behaviour on a machine with Windows and no current Office install is untested.
- iA Writer's numeric defaults could not be established from published sources; the philosophy is documented but the point sizes are not.
- UK civil service briefing-note formatting exists as convention rather than published specification. The structure above reflects general practice.
- No accessibility specification: heading structure, alt text and reading order in Word are all unaddressed and all matter for a document that may be read by a screen reader.
