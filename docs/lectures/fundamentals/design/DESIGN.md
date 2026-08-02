# House design tokens

The shared foundation for every medium in this track. Blogs, reports, documents, presentations, posters, dashboards and emails each carry their own `DESIGN.md`, and each one inherits everything below unless it says otherwise. A medium file may override a value, but it must keep the token name. If a medium needs a token that does not exist here, that is a signal the house file is incomplete.

The system is deliberately small. One accent, one warm neutral ramp, three semantic colours, one data palette, one type scale, one spacing scale. Restraint is the point: Stephen Few's rule that colour must be reserved for meaning collapses the moment a palette has fifteen equally loud entries.

## Overview

Three commitments shape everything here.

**Neutrals carry the design, the accent carries the meaning.** The warm grey ramp does the structural work (surfaces, rules, text). Colour appears only where it encodes something: a link, a state, a data series. This is Tufte's data-ink argument applied to interfaces, and it is why the palette below has one accent rather than a brand spectrum.

**Interface colour and data colour are separate systems.** The accent purple never appears in a chart, and the Okabe-Ito data palette never styles a button. Mixing them means a reader cannot tell whether a colour is decoration or information. Few, Stone and Brewer all converge on this separation.

**Every value is checked against a reader, not a taste.** Measure is 45 to 75 characters because that is where reading speed peaks (Bringhurst, Rutter, GOV.UK all land in the same band). Contrast ratios are stated, not assumed. The data palette is Okabe-Ito because it survives deuteranopia, protanopia and tritanopia, which no hand-picked palette does by accident.

**Key characteristics:**
- Warm neutral ramp (twelve steps, `#FFFFFF` to `#0A0A09`) rather than pure grey
- Single indigo accent `#5B47E0` at 6.1:1 on white, safe for body-size links
- Semantic colours split into fill variants and text-safe variants, because the fill values fail AA at body size
- Okabe-Ito eight-colour categorical palette reserved exclusively for data
- Hand-tuned type scale, ratio tightening from 1.33 at display sizes to 1.12 at body sizes
- 4px base spacing with 8px primary increment
- Inter for screen, Source Serif 4 for print and long-form, JetBrains Mono for code

## Colors

All contrast ratios below are computed against `#FFFFFF` using the WCAG 2.x relative-luminance formula, stated to one decimal place. AA normal text needs 4.5:1, AA large text (18pt / 24px, or 14pt / 18.66px bold) needs 3:1, AAA normal text needs 7:1.

### Neutral ramp

The spine of the system. Warm rather than pure grey, which reads as paper rather than screen and pairs better with serif type in print mediums.

| Token | Value | Contrast on white | Use |
|---|---|---|---|
| `{color.neutral-00}` | `#FFFFFF` | n/a | Canvas, card surface |
| `{color.neutral-05}` | `#FAFAF9` | n/a | Quietest section division |
| `{color.neutral-10}` | `#F7F6F3` | n/a | Primary surface, subtle section background |
| `{color.neutral-20}` | `#EFEEEA` | n/a | Table stripe, quiet divider |
| `{color.neutral-30}` | `#E8E6E1` | n/a | Hairline rules, 1px borders |
| `{color.neutral-40}` | `#D5D3CD` | n/a | Input borders, stronger rules |
| `{color.neutral-50}` | `#A6A5A1` | 2.5:1 | Disabled text, placeholders. Never for content |
| `{color.neutral-60}` | `#82817D` | 3.9:1 | Tertiary text at large sizes only, gridlines, icons |
| `{color.neutral-70}` | `#5C5B57` | 6.8:1 | Secondary text, captions, source lines |
| `{color.neutral-80}` | `#37352F` | 12.3:1 | Body text. The default reading colour |
| `{color.neutral-90}` | `#191918` | 17.6:1 | Headings, emphasis |
| `{color.neutral-100}` | `#0A0A09` | 19.8:1 | Maximum contrast, rarely needed |

Body text is `{color.neutral-80}`, not black. Pure black on pure white overshoots comfortable contrast and produces halation on backlit screens. The same logic runs in reverse on dark surfaces: `{color.on-dark}` is `#FFFFFF` but sits on `#191918` rather than `#000000`.

### Accent

One accent. It marks links, the current item, and the single most important action on a surface. If two things on a page are accent-coloured, at least one of them is wrong.

| Token | Value | Contrast on white | Use |
|---|---|---|---|
| `{color.accent}` | `#5B47E0` | 6.1:1 | Links, primary action, active state |
| `{color.accent-pressed}` | `#4A39C7` | 7.8:1 | Pressed and visited states |
| `{color.accent-deep}` | `#3D2EB5` | 9.3:1 | Accent text needing AAA, accent on tinted surfaces |
| `{color.accent-soft}` | `#EAE6FA` | n/a | Accent chip background, highlight fill |

### Semantic

Each semantic colour has two values. The saturated one is for fills, icons and rules where 3:1 suffices. The text variant is for words, where 4.5:1 is the floor. Using the fill value for body-size text fails AA, which is why both exist.

| Token | Value | Contrast on white | Use |
|---|---|---|---|
| `{color.success}` | `#1E9D54` | 3.5:1 | Positive fills, icons, chart series |
| `{color.success-text}` | `#0F6B3A` | 6.6:1 | Positive text at body size |
| `{color.success-soft}` | `#DDF1E5` | n/a | Positive callout background |
| `{color.warning}` | `#C76B2A` | 3.8:1 | Caution fills, icons |
| `{color.warning-text}` | `#8F4A16` | 6.6:1 | Caution text at body size |
| `{color.warning-soft}` | `#FBEDE4` | n/a | Caution callout background |
| `{color.error}` | `#DC2855` | 4.7:1 | Error fills, icons, and text |
| `{color.error-text}` | `#B01340` | 7.0:1 | Error text on tinted backgrounds |
| `{color.error-soft}` | `#F8E0DE` | n/a | Error callout background |

Never encode a state by colour alone. A red figure must also carry a sign, a label or an icon, because roughly one man in twelve cannot distinguish it from the green one.

### Data palette

The Okabe-Ito eight-colour set, published as part of the Colour Universal Design work and popularised by Bang Wong in *Nature Methods* (2011). Every pair remains distinguishable under deuteranopia, protanopia and tritanopia. Use in the order given; the order is not arbitrary, it front-loads the most separable pairs.

| Token | Value | Name |
|---|---|---|
| `{data.cat-1}` | `#0072B2` | Blue |
| `{data.cat-2}` | `#D55E00` | Vermilion |
| `{data.cat-3}` | `#009E73` | Bluish green |
| `{data.cat-4}` | `#CC79A7` | Reddish purple |
| `{data.cat-5}` | `#E69F00` | Orange |
| `{data.cat-6}` | `#56B4E9` | Sky blue |
| `{data.cat-7}` | `#F0E442` | Yellow |
| `{data.cat-8}` | `#000000` | Black |

`{data.cat-7}` is a deliberately desaturated yellow. Do not substitute `#FFFF00`, which is illegible on white and breaks the set's contrast balance.

Beyond eight categories, stop using colour. Nine or more series exceeds what any reader can hold in a legend, and the answer is a small-multiples layout or direct labelling, not a ninth hue.

### Data ramps

Sequential and diverging ramps come from ColorBrewer (Cynthia Brewer, colorbrewer2.org). Five-class versions given; the medium files extend to seven where density requires it.

| Token | Values | Use |
|---|---|---|
| `{data.seq-blue}` | `#EFF3FF` `#BDD7E7` `#6BAED6` `#3182BD` `#08519C` | Ordered magnitude, low to high |
| `{data.seq-warm}` | `#FFFFCC` `#FED976` `#FD8D3C` `#F03B20` `#BD0026` | Ordered intensity, risk heatmaps |
| `{data.div-rdbu}` | `#CA0020` `#F4A582` `#F7F7F7` `#92C5DE` `#0571B0` | Deviation around a meaningful zero |
| `{data.div-brbg}` | `#A6611A` `#DFC27D` `#F5F5F5` `#80CDC1` `#018571` | Deviation where red and blue carry unwanted meaning |

Choose sequential when the data runs one way, diverging only when a midpoint means something (zero variance, a target, a neutral rating). A diverging ramp on unidirectional data invents a midpoint the reader will try to interpret.

### Dark surfaces

| Token | Value | Use |
|---|---|---|
| `{color.dark-canvas}` | `#0A0F1C` | Dark band background |
| `{color.dark-surface}` | `#1A2238` | Raised surface on dark |
| `{color.on-dark}` | `#FFFFFF` | Primary text on dark |
| `{color.on-dark-muted}` | `rgba(255,255,255,0.72)` | Secondary text on dark |

## Typography

### Families

| Token | Stack | Use |
|---|---|---|
| `{font.sans}` | `'Inter', -apple-system, system-ui, 'Segoe UI', Helvetica, sans-serif` | Screen and UI, all interface text |
| `{font.serif}` | `'Source Serif 4', Charter, Georgia, Cambria, 'Times New Roman', serif` | Print body text, long-form reading |
| `{font.mono}` | `'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace` | Code, tabular figures where the face lacks them |

All three are free and openly licensed, which matters because a house style nobody can install is a house style nobody uses. Inter is drawn for screen at small sizes and covers every weight consistently across platforms. Source Serif 4 has a high x-height and open apertures that hold up in print at 10pt. JetBrains Mono is the strongest free coding face.

Butterick's advice to avoid system defaults stands, with one exception recorded in the documents file: a Word document destined for a corporate machine must degrade to fonts that machine actually has.

### Scale

Base 16px. The ratio is not constant: it tightens from roughly 1.33 between display sizes down to 1.12 at the body end. Constant-ratio scales either crowd the headings or explode the body, and every mature system (Material, Carbon, Apple) hand-tunes for this reason.

| Token | px | rem | pt (print) | Weight | Line height | Tracking | Use |
|---|---|---|---|---|---|---|---|
| `{type.display}` | 64 | 4.0 | 48 | 600 | 1.05 | -0.025em | Hero, title slide |
| `{type.h1}` | 48 | 3.0 | 36 | 600 | 1.10 | -0.02em | Page title |
| `{type.h2}` | 36 | 2.25 | 27 | 600 | 1.15 | -0.015em | Major section |
| `{type.h3}` | 30 | 1.875 | 22 | 600 | 1.20 | -0.01em | Section |
| `{type.h4}` | 24 | 1.5 | 18 | 600 | 1.25 | 0 | Subsection |
| `{type.h5}` | 20 | 1.25 | 15 | 600 | 1.30 | 0 | Minor heading, card title |
| `{type.body-lg}` | 18 | 1.125 | 13 | 400 | 1.60 | 0 | Long-form body, lead paragraph |
| `{type.body}` | 16 | 1.0 | 12 | 400 | 1.55 | 0 | Default body text |
| `{type.body-sm}` | 14 | 0.875 | 10.5 | 400 | 1.50 | 0 | Secondary text, table cells |
| `{type.caption}` | 12 | 0.75 | 9 | 400 | 1.45 | 0 | Captions, source lines, axis labels |
| `{type.micro}` | 11 | 0.6875 | 8 | 600 | 1.40 | 0.08em | Eyebrows, uppercase labels |

The pt column converts at roughly 0.75 (the CSS convention of 96px to the inch). Print mediums should treat it as a starting point and re-tune: 12pt body is at the upper end of Butterick's 10 to 12pt range and suits a report read on screen more than a book.

### Weights

400 for body, 500 for UI labels and buttons, 600 for headings, 700 only where 600 is genuinely insufficient. Never bold and italic together. Never underline anything that is not a link.

### Measure and leading

Measure is 45 to 75 characters, targeting 66. This is the single most-agreed number in typography: Bringhurst gives 66 as ideal and 45 to 75 as the range, Butterick gives 45 to 90, Rutter gives 45 to 75, GOV.UK caps at 75. In CSS, `max-width: 66ch` on the text container.

Leading and measure move together. A longer line needs more leading so the eye finds the next line's start. Below 50 characters, 1.4 is enough; at 66, use 1.5 to 1.6; above 75, either increase leading past 1.6 or, better, narrow the column.

### Numerals

Tabular lining figures in any column of numbers: tables, financial figures, dashboards, price lists. Proportional figures in running prose. Old-style figures only in serif long-form text where they sit better against lowercase. Inter and Source Serif 4 both carry tabular sets, reachable through `font-variant-numeric: tabular-nums`.

## Layout

### Spacing scale

4px base, 8px primary increment. The 4px sub-step exists for padding inside small components; everything structural uses multiples of 8.

| Token | Value | Use |
|---|---|---|
| `{space.xxs}` | 4px | Chip padding, icon gaps |
| `{space.xs}` | 8px | Tight component padding |
| `{space.sm}` | 12px | Input padding, list gaps |
| `{space.md}` | 16px | Default component padding |
| `{space.lg}` | 24px | Card padding, paragraph spacing |
| `{space.xl}` | 32px | Component separation |
| `{space.xxl}` | 48px | Block separation |
| `{space.section}` | 64px | Section rhythm |
| `{space.section-lg}` | 96px | Major section breaks |
| `{space.hero}` | 120px | Hero bands |

### Grid

Twelve columns is the house default, because twelve divides by 2, 3, 4 and 6, which covers every layout a document needs. Narrower mediums drop to a single column rather than subdividing further.

| Token | Value |
|---|---|
| `{grid.columns}` | 12 |
| `{grid.gutter}` | 24px |
| `{grid.margin}` | 32px |
| `{grid.max-content}` | 1280px |
| `{grid.max-reading}` | 66ch (roughly 720px at 16px Inter) |

### Whitespace

Space between elements should encode their relationship, not fill the page evenly. The Gestalt principle of proximity means a reader groups what sits close together, so the gap between a heading and its own paragraph must be smaller than the gap above the heading. Get this backwards and every heading appears to belong to the section above it. This single error accounts for more amateur-looking documents than any font choice.

## Elevation and depth

Depth is used sparingly. Most surfaces in a document sit flat and are separated by a hairline rule, which is cheaper for the reader to parse than a shadow.

| Level | Value | Use |
|---|---|---|
| `{elevation.0}` | none, `1px solid {color.neutral-30}` | Default. Cards, table rows, panels |
| `{elevation.1}` | `rgba(15,15,15,0.04) 0 1px 2px 0` | Raised list item |
| `{elevation.2}` | `rgba(15,15,15,0.08) 0 4px 12px 0` | Card lifted off the page |
| `{elevation.3}` | `rgba(15,15,15,0.16) 0 16px 48px -8px` | Modal, dropdown |
| `{elevation.4}` | `rgba(15,15,15,0.20) 0 24px 48px -8px` | Hero mockup, single focal object |

Print mediums use `{elevation.0}` only. A drop shadow on paper is a picture of a drop shadow.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{radius.xs}` | 4px | Chips, tags, small swatches |
| `{radius.sm}` | 6px | Badges |
| `{radius.md}` | 8px | Buttons, inputs |
| `{radius.lg}` | 12px | Cards, panels |
| `{radius.xl}` | 16px | Large feature panels |
| `{radius.xxl}` | 20px | Showcase surfaces |
| `{radius.full}` | 9999px | Status pills only, never buttons |

Rectangular-sober geometry. Buttons are 8px rectangles, not pills. Pills read as tags, and a button that reads as a tag does not get clicked.

## Components

Shared across mediums. Each medium file adds its own and may restyle these, keeping the names.

### Buttons

**`button-primary`**: the single dominant action on a surface.
- Background `{color.accent}`, text `#FFFFFF`, `{type.body-sm}` at weight 500, padding `10px 18px`, radius `{radius.md}`.

**`button-secondary`**: everything else.
- Transparent background, text `{color.neutral-80}`, border `1px solid {color.neutral-40}`, same metrics as primary.

**`button-ghost`**: tertiary, low-commitment.
- Transparent, text `{color.neutral-70}`, no border, padding `8px 12px`, radius `{radius.sm}`.

Minimum touch target 44 by 44px, per Apple and WCAG 2.5.5. A 40px-tall button needs padding around it to reach the target.

### Surfaces

**`card`**: background `{color.neutral-00}`, border `1px solid {color.neutral-30}`, radius `{radius.lg}`, padding `{space.lg}`.

**`panel-tinted`**: background `{color.neutral-10}`, no border, radius `{radius.lg}`, padding `{space.lg}`.

**`callout`**: background one of `{color.success-soft}` / `{color.warning-soft}` / `{color.error-soft}` / `{color.accent-soft}`, radius `{radius.lg}`, padding `{space.lg}`, with a `{type.micro}` uppercase label in the matching text colour.

### Text elements

**`link`**: text `{color.accent}`, underlined. Underline offset `0.15em`, thickness `1px`. Removing the underline and relying on colour alone fails for colour-blind readers and is the most common accessibility failure in body copy.

**`code-inline`**: `{font.mono}` at 0.9em of surrounding text, background `{color.neutral-10}`, padding `2px 5px`, radius `{radius.xs}`.

**`code-block`**: `{font.mono}` at `{type.body-sm}`, background `{color.neutral-10}`, padding `{space.md}`, radius `{radius.md}`, line height 1.55.

**`blockquote`**: left border `3px solid {color.neutral-30}`, padding-left `{space.md}`, text `{color.neutral-70}`, no italic (italic at length slows reading).

### Tables

**`table`**: `{type.body-sm}`, tabular numerals throughout.
- Header row: weight 600, `{color.neutral-90}`, bottom border `1px solid {color.neutral-40}`.
- Body rows: bottom border `1px solid {color.neutral-20}`, cell padding `{space.sm} {space.md}`.
- No vertical rules. Alignment does the work vertical rules were invented for.
- Text left, numbers right, dates left, headers aligned with their column's data.
- Zebra striping only above roughly eight rows, and then `{color.neutral-05}`, not `{color.neutral-20}`.

### Figures

**`figure`**: image or chart, then `{type.caption}` caption in `{color.neutral-70}` below, then an optional source line in `{type.caption}` at `{color.neutral-60}`.

Captions go below figures and above tables. This is convention rather than evidence, but it is near-universal in published work, and violating it costs credibility for no gain.

## Do's and don'ts

### Do

- Set body text in `{color.neutral-80}`, not black
- Keep measure between 45 and 75 characters in every medium that has running text
- Reserve `{color.accent}` for one thing per surface
- Use the Okabe-Ito palette for every categorical chart, in the order given
- Pair every colour-coded state with a second cue: a label, a sign, an icon, a pattern
- Make the space above a heading larger than the space below it
- Use tabular figures in any column of numbers
- State units and provenance under every exhibit
- Check contrast before shipping, not after

### Don't

- Don't use more than eight categorical colours. Use small multiples instead
- Don't use `{color.success}`, `{color.warning}` or `{color.neutral-60}` for body-size text; they fail AA
- Don't put a diverging ramp on unidirectional data
- Don't combine bold and italic
- Don't remove link underlines
- Don't use pill-shaped buttons
- Don't put drop shadows on anything destined for print
- Don't let a brand colour into a chart, or a data colour onto a button
- Don't justify text without hyphenation; the rivers are worse than a ragged edge

## Responsive behaviour

Screen mediums (blogs, dashboards, emails) inherit these breakpoints. Print mediums (reports, posters, documents) and fixed-canvas mediums (presentations) override them entirely.

| Name | Width | Behaviour |
|---|---|---|
| Small | < 480px | Single column. Body 16px. Margins 16px |
| Medium | 480 to 767px | Single column, wider margins. Body 16px |
| Tablet | 768 to 1023px | Two-column grids permitted. Body 17px |
| Desktop | 1024 to 1279px | Full grid. Body 18px for long-form |
| Wide | ≥ 1280px | Content capped at `{grid.max-content}`; reading column stays at `{grid.max-reading}` |

Type scales down at the display end and holds steady at the body end. A 64px hero becomes 36px on a phone; 16px body text stays 16px, because it was already at the accessible floor.

Fluid sizing between breakpoints uses `clamp()`:

```
font-size: clamp(MIN, MIN + (MAX - MIN) * ((100vw - MIN_VW) / (MAX_VW - MIN_VW)), MAX)
```

For example, a hero running 36px at 480px viewport to 64px at 1280px:

```
font-size: clamp(2.25rem, 1.4rem + 2.8vw, 4rem);
```

## Iteration guide

1. Change the house file only when a value is wrong for every medium. A value wrong for one medium belongs in that medium's override.
2. Keep token names stable. A medium file that renames a token has forked the system.
3. When adding a colour, state its contrast against white and against `{color.neutral-10}`. A colour without a contrast figure is not a token, it is a preference.
4. Default to `{type.body}` and `{color.neutral-80}`. Deviating should require a reason you can state.
5. Prefer removing a token to adding one. The system's value is in what it refuses.

## Known gaps

- Contrast ratios were computed directly from the WCAG 2.x relative-luminance formula against `#FFFFFF`, not read from an audited checker. The arithmetic is standard and the pass or fail judgements are not marginal, but confirm with a tool before relying on the palette where compliance is a requirement. Ratios against `{color.neutral-10}` rather than pure white are not stated and will be slightly lower.
- APCA, the perceptual contrast algorithm that is a candidate for WCAG 3, would likely give different guidance at the light end of the neutral ramp. WCAG 3 has no finalised contrast method as of 2026, so the WCAG 2 figures stand for now.
- No dark-mode ramp is defined beyond the four dark-surface tokens. A full dark palette is not a lightness inversion and needs its own construction.
- Animation and transition timings are absent. 150 to 200ms ease-out is the working default until something needs otherwise.
- The type scale's pt column is a mechanical conversion. Each print medium should re-tune rather than trust it.
- Source Serif 4 has not been tested in print at 10pt on this system's target output. Butterick would prefer a paid face here; the free choice is a deliberate trade.
