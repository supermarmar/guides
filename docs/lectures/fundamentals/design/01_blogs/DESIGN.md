# Blog and long-form web tokens

Screen-first, single-column, built for a reader who arrived from a link and will leave at the first friction. Inherits everything in [the house file](../DESIGN.md) and overrides the type scale at the body end, adds a dark palette, and fixes the reading column.

The governing claim comes from Oliver Reichenstein: the web is overwhelmingly written language, so web design is mostly typography. His "95 per cent" figure is rhetoric rather than measurement, but the conclusion holds. On a text page there is almost nothing to design except the text.

## Overview

**Inherits unchanged:** neutral ramp, accent, semantic colours, spacing scale, radius scale, `{font.sans}`, `{font.mono}`.

**Overrides:** body size rises to 18px and its leading to 1.65, because screen reading happens at a greater distance than print and Butterick's screen range runs 15 to 25px. Elevation drops to `{elevation.0}` and `{elevation.1}` only.

**Adds:** a reading-column token, a dark palette, scanning-aware heading rules, and footnote/aside components.

**Key characteristics:**
- Reading column fixed at 66ch, roughly 720px at 18px Inter
- Body 18px at 1.65 leading, which is looser than the house default and deliberately so
- Dark mode is a designed palette, not an inversion: `#E4E3E0` on `#151514`, never white on black
- Headings carry the scanning load, because eye-tracking shows readers scan in F, layer-cake and spotted patterns before they read anything
- Serif optional for the body; the house sans is the default

## Colors

### Light

| Token | Value | Change from house |
|---|---|---|
| `{color.canvas}` | `#FFFFFF` | = `{color.neutral-00}` |
| `{color.text}` | `#37352F` | = `{color.neutral-80}` |
| `{color.text-secondary}` | `#5C5B57` | = `{color.neutral-70}` |
| `{color.text-tertiary}` | `#82817D` | = `{color.neutral-60}`, captions and metadata only |
| `{color.rule}` | `#E8E6E1` | = `{color.neutral-30}` |
| `{color.accent}` | `#5B47E0` | unchanged |

### Dark

A dark theme is a separate palette, not a lightness inversion. Pure white on pure black produces halation, the smearing effect where light glyphs bleed into a dark ground, and it measurably slows reading. Both ends are pulled off their extremes.

| Token | Value | Contrast |
|---|---|---|
| `{color.canvas-dark}` | `#151514` | n/a |
| `{color.surface-dark}` | `#1F1F1D` | n/a |
| `{color.text-dark}` | `#E4E3E0` | 14.2:1 on canvas |
| `{color.text-secondary-dark}` | `#A8A6A1` | 7.5:1 |
| `{color.text-tertiary-dark}` | `#7C7A75` | 4.3:1 |
| `{color.rule-dark}` | `#33322F` | n/a |
| `{color.accent-dark}` | `#A99BFF` | 7.7:1, lightened because `#5B47E0` fails on dark |

The accent must be re-picked for dark, not reused. A colour that passes 6.1:1 on white will typically fail on a near-black ground.

## Typography

### Scale

Overrides the house scale below `{type.h4}`. Everything above is inherited.

| Token | Size | Weight | Line height | Use |
|---|---|---|---|---|
| `{type.h1}` | clamp(2.25rem, 1.4rem + 2.4vw, 3rem) | 600 | 1.10 | Post title |
| `{type.h2}` | 1.875rem (30px) | 600 | 1.20 | Major section |
| `{type.h3}` | 1.375rem (22px) | 600 | 1.30 | Subsection |
| `{type.lead}` | 1.375rem (22px) | 400 | 1.55 | Standfirst, first paragraph |
| `{type.body}` | 1.125rem (18px) | 400 | **1.65** | Body. Overrides house 16px / 1.55 |
| `{type.body-sm}` | 1rem (16px) | 400 | 1.60 | Asides, sidenotes |
| `{type.caption}` | 0.875rem (14px) | 400 | 1.50 | Figure captions, metadata |
| `{type.code}` | 0.9375rem (15px) | 400 | 1.55 | Code blocks |

Body drops to 17px below the tablet breakpoint and never below 16px. Sixteen pixels is the accessible floor, not a target.

### Measure

| Token | Value |
|---|---|
| `{measure.reading}` | 66ch |
| `{measure.min}` | 45ch |
| `{measure.max}` | 75ch |
| `{measure.wide}` | 100ch, for code blocks and tables that break the column |

Measure and leading move together. If a design widens past 75ch, leading must rise above 1.65 or the eye loses the line return. Narrowing the column is the better fix.

### Heading spacing

The single rule that most improves an amateur page: space above a heading exceeds space below it.

| Element | Margin top | Margin bottom |
|---|---|---|
| `{type.h2}` | 3rem (48px) | 0.75rem (12px) |
| `{type.h3}` | 2rem (32px) | 0.5rem (8px) |
| Paragraph | 0 | 1.375rem (22px) |

Paragraphs are separated by space, not first-line indent. Indents assume a continuous page; the web has none.

## Layout

| Token | Value | Use |
|---|---|---|
| `{layout.column}` | 66ch | Text container |
| `{layout.bleed}` | 100ch | Figures, code and tables that exceed the column |
| `{layout.full}` | 100vw | Hero images only |
| `{layout.gutter-sm}` | 16px | Page margin below 480px |
| `{layout.gutter}` | 24px | Page margin, 480 to 1023px |
| `{layout.gutter-lg}` | 32px | Page margin, 1024px and above |
| `{layout.sidenote}` | 18ch | Margin note column, desktop only |

Three widths, not more. Text sits at `{layout.column}`, anything wider than the text sits at `{layout.bleed}`, and only a hero goes full width. Gwern's page is the reference implementation of this discipline: a strict grayscale palette and a layered hierarchy running abstract, then margin notes, then body, then footnotes, then collapsed sections, so a reader chooses their own depth.

## Elevation and depth

`{elevation.0}` for everything. `{elevation.1}` for a hovering card in an index listing. Nothing deeper. A blog post is a sheet of text and shadows on it are decoration.

## Shapes

Inherited. In practice only `{radius.xs}` for inline code, `{radius.md}` for code blocks and images, and `{radius.full}` for tag pills.

## Components

### `prose-link`

Text `{color.accent}`, underline `1px` at `0.15em` offset, `text-decoration-skip-ink: auto`. Visited `{color.accent-pressed}`.

Never remove the underline. Colour alone as a link signal fails for colour-blind readers and is the most common accessibility defect in body copy. In a paragraph dense with links, reduce the underline to `{color.neutral-40}` rather than deleting it.

### `figure`

Image at `{layout.bleed}`, radius `{radius.md}`, then caption in `{type.caption}` at `{color.text-secondary}`, left-aligned with the text column rather than centred. Centred captions read as decoration.

### `code-block`

`{font.mono}` at `{type.code}`, background `{color.neutral-10}` (light) or `{color.surface-dark}` (dark), padding `{space.md}`, radius `{radius.md}`, `overflow-x: auto`, width `{layout.bleed}`. Never wrap code; scroll it.

### `code-inline`

`{font.mono}` at `0.9em` of the surrounding text, background `{color.neutral-10}`, padding `2px 5px`, radius `{radius.xs}`. The `0.9em` matters: monospace faces run optically larger than the sans at the same nominal size.

### `blockquote`

Left rule `3px solid {color.neutral-30}`, padding-left `{space.md}`, text `{color.text-secondary}`, size unchanged from body. No italics. Italic at paragraph length slows reading, and the rule already marks the quotation.

### `sidenote`

Desktop only, at `{layout.sidenote}` in the right margin, `{type.body-sm}`, `{color.text-secondary}`. Below 1280px it collapses inline as a footnote. Sidenotes beat footnotes when they fit, because the reader never leaves their place.

### `table-responsive`

House `table` component, wrapped in a `overflow-x: auto` container at `{layout.bleed}`. Below 768px the container scrolls rather than the columns stacking, because a stacked financial table loses the comparison the columns existed to make.

### `tag-pill`

`{type.caption}`, background `{color.neutral-10}`, text `{color.text-secondary}`, padding `4px 10px`, radius `{radius.full}`.

## Do's and don'ts

### Do

- Hold the reading column at 66ch at every breakpoint above mobile
- Set body at 18px and leading at 1.65
- Design the dark palette; do not invert the light one
- Write headings that carry meaning on their own, because most readers scan them before reading anything
- Give code blocks and tables the wider `{layout.bleed}` and let them scroll
- Left-align captions with the text column

### Don't

- Don't set body text below 16px at any breakpoint
- Don't use `#000000` on `#FFFFFF`, or `#FFFFFF` on `#000000`
- Don't remove link underlines
- Don't justify. Browsers hyphenate poorly and the rivers are worse than a ragged right edge
- Don't centre body text or captions
- Don't let the page body scroll horizontally; only designated containers do

## Responsive behaviour

| Breakpoint | Body | Column | Gutter | Notes |
|---|---|---|---|---|
| < 480px | 17px | 100% − gutter | 16px | Sidenotes inline. h1 at 36px |
| 480 to 767px | 17px | 100% − gutter | 24px | |
| 768 to 1023px | 18px | 66ch | 24px | |
| 1024 to 1279px | 18px | 66ch | 32px | |
| ≥ 1280px | 18px | 66ch | auto | Sidenotes appear in the right margin |

Fluid headings use `clamp()`; body does not. Body is already at a floor and scaling it fluidly produces sizes nobody chose.

```
h1 { font-size: clamp(2.25rem, 1.4rem + 2.4vw, 3rem); }
```

## Iteration guide

1. Change measure last. Almost every readability complaint that looks like a font problem is a measure problem.
2. When adding a component, decide first which of the three widths it occupies.
3. Test dark mode by reading a full post in it, not by looking at a screenshot. Halation only shows up over time.
4. If a page needs a fourth width, the design has probably acquired a sidebar it does not need.

## Known gaps

- The dark-palette contrast figures were computed rather than measured, and dark-mode contrast is exactly where the WCAG 2 formula is weakest. APCA would likely disagree at the light end.
- The claim that high-contrast dark mode slows reading by around 20 per cent circulates widely in design writing but the underlying study was not traced. The direction of the effect is well attested; the magnitude is not.
- No specification for print stylesheets. A long post printed from the browser currently inherits screen values, which are wrong on paper.
- Web font loading strategy is unaddressed: no decision on `font-display`, subsetting, or self-hosting versus a CDN.
- Reichenstein's 95 per cent is a framing device, not a measurement, and is quoted here as such.
