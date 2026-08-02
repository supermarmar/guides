# Presentation tokens

A fixed 16:9 canvas, projected or shared on a call, with a speaker attached. The slide is not the document. Every specification below follows from that one distinction, which is also the distinction most decks get wrong.

Inherits [the house file](../DESIGN.md) and overrides the type scale upward by a large factor, because the reader is metres away rather than centimetres.

## Overview

**Inherits unchanged:** neutral ramp, accent, semantic colours, data palette, radius scale.

**Overrides:** the entire type scale. Body text on a slide starts at 24pt where the house body is the equivalent of 12pt. Spacing scales with it.

**Adds:** canvas geometry, a layout master set, the action-title convention, and the empirical constraints from multimedia learning research.

**Key characteristics:**
- 13.333 × 7.5 inches, 1920 × 1080px at 2x, 16:9
- 24pt body minimum, 18pt absolute floor, and the floor is for a source line, not for content
- Action titles: a full sentence stating the takeaway, not a topic label
- 75 words per slide maximum
- Two type families, four colours, no more
- Redundancy is the enemy: on-screen text that duplicates the narration measurably harms recall

## The empirical basis

Most slide advice is taste. Some of it is not, and the exceptions are worth knowing because they override taste.

Richard Mayer's multimedia learning research gives effect sizes for design decisions, which almost nothing else in this track can. The three largest are directly actionable. **Coherence** (d ≈ 0.86): removing extraneous material, however attractive, improves learning. **Redundancy** (d ≈ 0.87): presenting the same words as both on-screen text and narration is worse than either alone. **Modality** (d ≈ 0.76): spoken words beat printed words when a graphic is also present.

Together these say something uncomfortable. A slide full of the sentences you are about to speak is not neutral, it is actively harmful, because the audience cannot read and listen at once and will do neither well.

Duarte's three-second glance test operationalises this: if the audience cannot grasp the slide's point in three seconds, they will spend the next thirty decoding it rather than listening. Her upper bound is 75 words per slide, beyond which the artefact is a document.

Tufte's critique in *The Cognitive Style of PowerPoint* goes further and argues the medium itself is the problem: bullet hierarchies fragment argument, resolution is too low for real evidence, and formatting conceals uncertainty. His Columbia example is the strongest case ever made, and the Columbia Accident Investigation Board itself criticised the use of briefing slides in place of technical papers. His prescription is a written technical report, not a better deck.

Take the point without taking the conclusion. When the analysis is the deliverable, write the report. When a room needs to reach a decision together, build the deck and accept its constraints.

## Canvas

| Token | Value |
|---|---|
| `{canvas.ratio}` | 16:9 |
| `{canvas.inches}` | 13.333 × 7.5 in |
| `{canvas.px}` | 1920 × 1080 (design at 1x = 1280 × 720, export at 2x) |
| `{canvas.margin}` | 0.6in (57.6px at 1x) |
| `{canvas.margin-top}` | 0.5in |
| `{canvas.title-zone}` | Top 1.4in, full width less margins |
| `{canvas.content-zone}` | 1.9in to 6.7in vertical |
| `{canvas.footer-zone}` | Bottom 0.55in |
| `{canvas.grid}` | 12 columns, 0.25in gutter |

Nothing crosses `{canvas.margin}` except a deliberate full-bleed image. The margin is not decoration; projectors crop and video calls letterbox.

## Typography

### Families

Two, and only two. `{font.sans}` (Inter) for everything, `{font.mono}` (JetBrains Mono) for code and fixed-width figures. No serif on slides: serifs at projection distance under compression lose their detail and gain nothing.

### Scale

Two columns, because the correct minimum depends on the room. "Projected" means a conference room or auditorium where the back row is several metres away. "Shared" means a screen-share on a call, where everyone is at laptop distance.

| Token | Projected | Shared | Weight | Line height | Use |
|---|---|---|---|---|---|
| `{type.slide-title}` | 54pt | 44pt | 600 | 1.10 | Title slide, section dividers |
| `{type.action-title}` | 32pt | 28pt | 600 | 1.15 | The headline on every content slide |
| `{type.h2}` | 28pt | 24pt | 600 | 1.20 | Column headings, chart titles |
| `{type.body}` | 24pt | 20pt | 400 | 1.35 | Body text, bullet content |
| `{type.body-sm}` | 20pt | 18pt | 400 | 1.35 | Dense tables, secondary labels |
| `{type.label}` | 18pt | 16pt | 500 | 1.25 | Axis labels, callout tags |
| `{type.source}` | 14pt | 12pt | 400 | 1.20 | Source line, footnote |
| `{type.kpi}` | 72pt | 60pt | 600 | 1.00 | A single dominant number |

**24pt is the body floor for a projected deck.** Below it the back of the room is guessing. 18pt is the absolute floor for anything at all, and it is reserved for source lines that only matter to someone who walks up afterwards.

Guy Kawasaki's 10-20-30 rule (ten slides, twenty minutes, thirty-point minimum font) is the best-known version of this constraint and is frequently misattributed to Garr Reynolds. It is Kawasaki's. His 30pt floor is stricter than the 24pt above and is a defensible choice for a pitch, where the room is large and the content is thin.

### Text volume

| Token | Value |
|---|---|
| `{limit.words-per-slide}` | 75 |
| `{limit.action-title-words}` | 15 |
| `{limit.action-title-lines}` | 2 |
| `{limit.bullets}` | 5 |
| `{limit.bullet-lines}` | 2 |
| `{limit.glance-seconds}` | 3 |
| `{limit.explain-seconds}` | 60 |

A slide that takes longer than sixty seconds to explain is two slides.

## Colors

Four colours in a deck. The house neutrals plus one accent, plus the semantic pair for variance.

| Token | Value | Use |
|---|---|---|
| `{color.slide-bg}` | `#FFFFFF` | Default background |
| `{color.slide-bg-alt}` | `#F7F6F3` | Alternate background for contrast slides |
| `{color.slide-bg-dark}` | `#0A0F1C` | Section dividers, full-bleed statement slides |
| `{color.text}` | `#191918` | Titles and body. Not black at projection: `#191918` |
| `{color.text-secondary}` | `#5C5B57` | Labels, source lines |
| `{color.text-on-dark}` | `#FFFFFF` | Text on `{color.slide-bg-dark}` |
| `{color.accent}` | `#5B47E0` | Emphasis, the one thing on the slide that matters |
| `{color.good}` | `#1E9D54` | Favourable variance |
| `{color.bad}` | `#DC2855` | Adverse variance |
| `{color.muted-fill}` | `#D5D3CD` | De-emphasised chart series |

Projection lightens and washes out. A palette that looks correct on a laptop will look pale on a projector, so test on the actual hardware where you can. Contrast that is merely adequate on a monitor is inadequate in a lit room.

The de-emphasis technique is the most useful one in the set: grey every series except the one under discussion using `{color.muted-fill}`, and colour only that one. It directs attention more reliably than an arrow and survives being photographed.

## Layout

### Master set

Seven layouts. A deck that needs an eighth usually needs an editor.

| Layout | Structure |
|---|---|
| `title` | Deck title `{type.slide-title}`, subtitle, presenter, date. Centred or lower-left |
| `section` | Full-bleed `{color.slide-bg-dark}`, section name in `{type.slide-title}` reversed. Nothing else |
| `content` | Action title, then a single content region. The workhorse |
| `two-column` | Action title, two equal columns with a 0.5in gutter. For comparison only, never for two unrelated points |
| `chart` | Action title, chart occupying the content zone, source line in the footer |
| `full-bleed` | Image edge to edge, text overlaid in `{color.text-on-dark}` on a scrim |
| `closing` | The ask or the next step, in `{type.h2}`. One sentence |

### Slide anatomy

Every content slide has the same four zones, top to bottom.

```
Action title      A full sentence stating the takeaway
Content           Chart, table, diagram or (rarely) text
Callout           Optional: one annotation pointing at the evidence
Source            Provenance, in {type.source}
```

The **action title** is the single most valuable convention in the consulting tradition, and it comes out of Barbara Minto's Pyramid Principle work at McKinsey in the 1960s. "Default rates rose 40 basis points in the second half" is an action title. "Default rate trends" is a topic label. Read only the titles of a well-built deck, in order, and you have the argument. This is the "ghost deck" test, and a deck that fails it has no argument, only slides.

### Spacing

| Token | Value (at 1x, 1280 × 720) |
|---|---|
| `{space.slide-xs}` | 8px |
| `{space.slide-sm}` | 16px |
| `{space.slide-md}` | 24px |
| `{space.slide-lg}` | 40px |
| `{space.slide-xl}` | 64px |
| `{space.column-gutter}` | 48px |

Alignment is not optional. Every element sits on the 12-column grid. Misalignment of a few pixels reads as carelessness, and an audience that notices carelessness in the layout starts wondering about the analysis.

## Elevation and depth

`{elevation.0}` and `{elevation.2}` only, and `{elevation.2}` only on a card that genuinely floats above a background. No 3D, no bevels, no gradients on charts. Tufte's objection to decoration applies with more force here than anywhere, because projection compresses and the decoration survives while the data does not.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{radius.slide-card}` | 8px at 1x | Content cards, callout boxes |
| `{radius.slide-chip}` | 4px at 1x | Labels, tags |
| `{radius.full}` | n/a | Status dots only |

## Components

### `action-title`

`{type.action-title}`, `{color.text}`, left-aligned, top-left of `{canvas.title-zone}`, maximum two lines. A complete sentence. Never ends in a colon.

### `callout`

An annotation pointing at the evidence. `{type.label}` in `{color.accent}`, on `{color.slide-bg}` with a `1px {color.accent}` border, radius `{radius.slide-card}`, with a leader line to the referenced point. One per slide. Two callouts means the audience has to choose, and they will choose wrong.

### `kpi-block`

A single number given the whole slide. Value in `{type.kpi}` `{color.text}`, label above in `{type.label}` `{color.text-secondary}`, comparison below in `{type.body-sm}` `{color.good}` or `{color.bad}` with a sign. Reserved for the one number the meeting is about.

### `chart-on-slide`

Charts inherit the house data palette but need heavier treatment than a report chart.

- Axis and tick labels at `{type.label}` minimum, which is 18pt. A default chart export will be around 10pt and unreadable.
- Line weight 3px at 1x, up from the 1.5px that suits a report.
- **No legend.** Label series directly at the end of the line or inside the bar. A legend at projection distance forces the audience to look away from the data.
- Gridlines only where the reader must read a value off the axis. Usually they must not.
- De-emphasise every series except the subject, using `{color.muted-fill}`.

Gene Zelazny's framework in *Say It With Charts* maps message to chart type and is the fastest way to choose: component (part of a whole), item (comparison across categories), time series (change), frequency (distribution), correlation (relationship). Decide the message first, and the chart type follows.

### `source-line`

`{type.source}`, `{color.text-secondary}`, bottom-left of `{canvas.footer-zone}`. Present on every slide that shows data. Format: "Source: [origin], [date]." Add "Note:" on a second line for method caveats.

### `table-on-slide`

Maximum five columns and eight rows. Type at `{type.body-sm}`, headers at `{type.label}` weight 600. Horizontal rules only. Highlight the cells that matter with `{color.accent-soft}` fill; a table where everything is equally prominent communicates nothing. A table that will not fit these limits belongs in an appendix or a handout.

### `appendix-marker`

Slides after the closing carry a muted `{type.label}` marker top-right. The appendix is where the detail Tufte wants goes, and having one is what makes the front of the deck able to stay clean.

## Do's and don'ts

### Do

- Write every content-slide title as a full sentence stating the takeaway
- Read the titles alone, in order, and check they form the argument
- Keep body text at 24pt or above for a projected deck
- Label chart series directly
- Grey out everything except the point under discussion
- Put a source line on every data slide
- Build an appendix, so the front of the deck can stay clean
- Test on the actual projector when the stakes justify it

### Don't

- Don't put the sentences you are about to speak on the slide. Duplicating narration in text measurably harms recall
- Don't exceed 75 words on a slide
- Don't use more than two type families or four colours
- Don't use a legend where direct labels will fit
- Don't shrink type to make content fit; split the slide
- Don't animate for decoration. Build steps are legitimate; flying text is not
- Don't use a topic label as a title
- Don't hand out the deck as the document. Write the document

## Responsive behaviour

Not responsive. Fixed canvas. Three delivery contexts change the choices though, and the "projected" versus "shared" split in the type scale is the main lever.

| Context | Type column | Notes |
|---|---|---|
| Auditorium or large room | Projected, or Kawasaki's 30pt floor | Fewer words, larger charts, higher contrast |
| Meeting room | Projected | The default assumption throughout |
| Screen share on a call | Shared | Denser slides survive; a table can carry more rows |
| Sent as a PDF, unpresented | Neither | This is a report. Build a report |

That last row is the important one. A deck designed to be read without a speaker has to carry the narration in text, which breaks every constraint above. The honest answer is that it is a different artefact.

## Iteration guide

1. Write the action titles first, as a list, before opening the deck tool. If the list is not an argument, the deck will not be either.
2. Cut before you design. Coherence has the largest effect size in the whole literature and it is achieved by deleting.
3. Change the type scale only in the two-column pair. Changing one column and not the other means one delivery context silently breaks.
4. When adding a layout, delete one.

## Known gaps

- Mayer's effect sizes are quoted from the multimedia learning literature at the level of the summary; five of the twelve principles (spatial contiguity, temporal contiguity, personalisation, voice, image) have empirical support but no effect size was traced.
- Duarte's 75-word limit is verifiable in her published material; the specific title and body point-size pairs above are this system's choices, informed by her general guidance rather than quoted from it.
- No animation or transition specification beyond the prohibition on decorative motion.
- Nothing on speaker notes, handouts, or the relationship between the three artefacts (slides, notes, handout) that Reynolds argues should be separate documents.
- Projector contrast behaviour is asserted from practice, not measured. The recommendation to test on the hardware stands precisely because the specification cannot substitute for it.
- No dark-deck variant. `{color.slide-bg-dark}` exists for section dividers only, and a fully dark deck would need its own palette and chart colours.
