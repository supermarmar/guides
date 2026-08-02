# Dashboard tokens

A screen a reader returns to, scanning for whether anything needs attention. Stephen Few's definition is the one to hold: a visual display of the information needed to achieve one or more objectives, consolidated on a single screen so it can be monitored at a glance. Every constraint below follows from "single screen" and "at a glance".

Inherits [the house file](../DESIGN.md) and overrides density, adds a full chart specification, and adds the number formatting rules that most dashboards get wrong.

## Overview

**Inherits unchanged:** neutral ramp, accent, semantic colours, radius scale, spacing scale.

**Overrides:** the type scale compresses. Dashboard body is 13px, not 16px, because density is the point and the reader is scanning rather than reading.

**Adds:** chart palettes with explicit roles, KPI tile anatomy, gridline and axis treatment, number formatting rules, IBCS scenario notation, and a dark variant.

**Key characteristics:**
- One screen. Scrolling is a design failure, not a feature
- Chart encoding chosen by perceptual accuracy, following Cleveland and McGill
- Colour reserved for meaning; the default state of a chart is grey
- Maximum six colours in use at once across the whole dashboard
- Every number carries its unit and its comparison
- Direct labelling wherever it fits; legends are the fallback, not the default

## The perceptual basis

Cleveland and McGill's 1984 experiments ranked how accurately people read quantities from different visual encodings. The ordering, most accurate first:

1. Position along a common scale
2. Position along non-aligned scales
3. Length
4. Direction, angle, slope
5. Area
6. Volume, curvature
7. Colour saturation

This single ranking decides most chart questions. A bar chart uses position on a common scale and is therefore near the top. A pie chart uses angle and area and is therefore near the bottom, which is why it fails for anything except a rough part-to-whole read with very few slices. A bubble chart uses area, so its size channel carries less precision than its position channel, and the important variable should go on position.

Read the ranking as a budget: spend the accurate channels on the quantities that matter and the inaccurate ones on context.

## Layout

| Token | Value | Use |
|---|---|---|
| `{dash.grid-columns}` | 12 | |
| `{dash.gutter}` | 16px | Between tiles |
| `{dash.margin}` | 24px | Page edge |
| `{dash.tile-radius}` | 8px | `{radius.md}` |
| `{dash.tile-padding}` | 16px | |
| `{dash.row-height}` | 8px | Grid row unit; tiles span whole multiples |
| `{dash.max-width}` | 1600px | Beyond this, tiles stretch pointlessly |
| `{dash.header-height}` | 56px | Title, filters, refresh timestamp |

The single-screen rule holds at 1440 × 900, which is the laptop most people actually use. If it needs a second screen, it needs to be two dashboards with a link between them, because a dashboard the reader has to scroll is a dashboard where the bottom half is never seen.

Reading order runs top-left. The most important measure goes there, and importance decreases along the F-shaped scan. Filters and controls go in the header, never scattered among the tiles.

## Typography

Denser than the house scale. The reader is scanning labels, not reading prose.

| Token | Size | Weight | Line height | Use |
|---|---|---|---|---|
| `{type.dash-title}` | 20px | 600 | 1.25 | Dashboard title |
| `{type.tile-title}` | 14px | 600 | 1.30 | Tile heading |
| `{type.kpi-value}` | 40px | 600 | 1.00 | The number on a KPI tile |
| `{type.kpi-value-sm}` | 28px | 600 | 1.00 | Secondary KPI |
| `{type.kpi-label}` | 11px | 600 | 1.20 | KPI label, uppercase, 0.06em tracking |
| `{type.body}` | 13px | 400 | 1.45 | Tile body, table cells |
| `{type.axis}` | 11px | 400 | 1.20 | Axis and tick labels |
| `{type.annotation}` | 11px | 500 | 1.25 | Chart annotations, direct labels |
| `{type.source}` | 10px | 400 | 1.20 | Source line, refresh timestamp |

`{font.sans}` throughout, with `font-variant-numeric: tabular-nums` on every number. Non-tabular figures in a column that updates make the digits jump on every refresh.

Eleven pixels is the floor. It is small, and it is defensible only because axis labels are read in relation to the marks beside them rather than read as text.

## Colors

### Interface

| Token | Value | Use |
|---|---|---|
| `{color.dash-bg}` | `#F7F6F3` | Page ground, so tiles read as raised |
| `{color.tile}` | `#FFFFFF` | Tile surface |
| `{color.tile-border}` | `#E8E6E1` | Tile border |
| `{color.text}` | `#191918` | KPI values, tile titles |
| `{color.text-secondary}` | `#5C5B57` | Body, labels |
| `{color.text-tertiary}` | `#82817D` | Axis labels, timestamps |
| `{color.accent}` | `#5B47E0` | Active filter, selected state, links |

### Data

Default state of every mark is grey. Colour is added only where it encodes something.

| Token | Value | Use |
|---|---|---|
| `{data.neutral}` | `#8C8B87` | The default. Any series with no special meaning |
| `{data.neutral-light}` | `#C9C7C1` | Context series, prior period, de-emphasised |
| `{data.focus}` | `#0072B2` | The series under discussion |
| `{data.good}` | `#1E9D54` | Favourable variance |
| `{data.bad}` | `#DC2855` | Adverse variance |
| `{data.target}` | `#37352F` | Target and threshold markers |

This is the discipline Few argues for and almost no dashboard follows. Most dashboards colour every series because the tool does it by default, which spends the entire colour channel before anything meaningful arrives. Grey by default, colour on purpose.

### Categorical

Where categories genuinely need distinguishing, use the house Okabe-Ito set in order.

| Token | Value |
|---|---|
| `{data.cat-1}` to `{data.cat-8}` | `#0072B2` `#D55E00` `#009E73` `#CC79A7` `#E69F00` `#56B4E9` `#F0E442` `#000000` |

Six is the working maximum on one screen, eight the absolute. Beyond that the legend exceeds working memory and the answer is small multiples.

### Sequential and diverging

| Token | Values | Use |
|---|---|---|
| `{data.seq}` | `#F7FBFF` `#DEEBF7` `#C6DBEF` `#9ECAE1` `#6BAED6` `#4292C6` `#2171B5` `#08519C` `#08306B` | Heatmaps, choropleths, magnitude |
| `{data.div}` | `#CA0020` `#F4A582` `#F7F7F7` `#92C5DE` `#0571B0` | Variance around zero |

### IBCS scenario notation

For management reporting, encode scenario by fill rather than hue, so the meaning survives greyscale and does not consume the colour channel.

| Scenario | Encoding |
|---|---|
| Actual | Solid `{data.neutral}` or `{data.focus}` |
| Plan or budget | Outline only |
| Forecast | 45-degree hatch |
| Previous year | Solid `{data.neutral-light}` |

IBCS's SUCCESS acronym governs the wider standard: Say, Unify, Condense, Check, Express, Simplify, Structure.

### Dark variant

| Token | Value |
|---|---|
| `{color.dash-bg-dark}` | `#151514` |
| `{color.tile-dark}` | `#1F1F1D` |
| `{color.tile-border-dark}` | `#33322F` |
| `{color.text-dark}` | `#E4E3E0` |
| `{color.text-secondary-dark}` | `#A8A6A1` |
| `{data.neutral-dark}` | `#7C7A75` |
| `{data.focus-dark}` | `#4DA3DB` |
| `{data.good-dark}` | `#3EBE77` |
| `{data.bad-dark}` | `#F4577E` |

Do not invert the light palette. Saturated colours read as brighter on a dark ground and need desaturating; the semantic red and green need lightening to stay legible, and lightening them naively pushes them toward pastel where they stop reading as red and green. Each value above was re-picked, not computed.

## Elevation and depth

| Level | Use |
|---|---|
| `{elevation.0}` | Tiles. Border, no shadow. The default |
| `{elevation.1}` | Tile in a hover or selected state |
| `{elevation.3}` | Filter dropdown, tooltip, modal |

No 3D charts, no gradients on bars, no glossy fills. Every one of them adds encoding the data does not use, and Cleveland and McGill's ranking explains why: a gradient introduces a saturation channel carrying no information, which the reader must actively discount.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{radius.tile}` | 8px | Tiles, chart containers, modals |
| `{radius.control}` | 6px | Filter controls, buttons, dropdowns |
| `{radius.chip}` | 4px | Active-filter chips, legend swatches |
| `{radius.bar}` | 0 | Chart bars. Rounded bar ends distort the length the bar encodes |
| `{radius.full}` | 9999px | Status dots only |

The bar radius matters more than it looks. A rounded bar end shortens the mark by the radius and softens where it terminates, which degrades the most accurate encoding available. Bars are rectangles.

## Components

### `kpi-tile`

The most-used component and the easiest to get wrong. A number without a comparison is not information; it is trivia.

```
[LABEL]                    {type.kpi-label}, {color.text-tertiary}, uppercase
1,247                      {type.kpi-value}, {color.text}
▲ 12.3% vs prior month     {type.body}, {data.good} or {data.bad}, with sign and arrow
[sparkline]                60 × 24px, 1.5px stroke, {data.neutral}
```

| Token | Value |
|---|---|
| `{kpi.width}` | 280px minimum |
| `{kpi.height}` | 140 to 160px |
| `{kpi.padding}` | 16px |
| `{kpi.internal-gap}` | 8px |
| `{kpi.sparkline}` | 60 × 24px, 1.5px stroke |

The comparison line carries both an arrow and a sign as well as colour, so the direction survives for a colour-blind reader and in greyscale.

### `chart-container`

```
[Tile title]        {type.tile-title}
[Subtitle]          {type.body}, {color.text-secondary}, optional: the unit and the period
[Chart]
[Source]            {type.source}, {color.text-tertiary}
```

### Axis and gridline treatment

| Token | Value | Use |
|---|---|---|
| `{axis.line}` | `#C9C7C1`, 1px | The value axis line, where shown |
| `{axis.tick}` | `#C9C7C1`, 1px, 4px long | Category ticks |
| `{gridline.major}` | `#EFEEEA`, 1px | Only where a value must be read off the axis |
| `{gridline.minor}` | none | Do not use |
| `{gridline.zero}` | `#A6A5A1`, 1px | Always shown where the scale crosses zero |
| `{axis.label}` | `{type.axis}`, `{color.text-tertiary}` | |

Gridlines are the largest source of unnecessary ink on a dashboard. Show them only when the reader has to read a value off the axis, which is less often than it seems: if the number matters that much, label the point directly.

The zero line is different and is always shown, because it is the only reference that means something absolutely.

**Should the axis start at zero?** For bar charts, always: the bar encodes length, and a truncated bar lies about the ratio. For line charts, not necessarily: the line encodes change, and forcing zero can flatten the signal into a straight line. State the range clearly either way.

### `legend`

The fallback. Try direct labelling first, at the end of a line or inside a bar, in `{type.annotation}`.

Where a legend is unavoidable: horizontal above the plot, left-aligned with it, `{type.axis}`, swatches 10 × 10px at `{radius.xs}`. Never at the right, which puts it furthest from where the eye reads the marks. Order the legend to match the order of the series in the chart, not alphabetically.

### `bullet-graph`

Few's replacement for the gauge, and a strictly better use of space. A horizontal bar showing the measure, over two or three greyscale qualitative bands, with a vertical marker for the target.

| Element | Spec |
|---|---|
| Bands | 2 or 3, `#EFEEEA` `#DDDBD6` `#C9C7C1`, light to dark reading as poor to good |
| Measure bar | `{data.focus}` or `{data.neutral}`, 30 per cent of band height, vertically centred |
| Target marker | `{data.target}`, 2px, full band height |
| Size | 200 × 32px typical |

It fits in a fraction of a gauge's footprint and encodes position on a common scale rather than angle, which is two ranks better on the perceptual ordering.

### `table-dash`

`{type.body}`, tabular numerals, row height 32px, header `{type.kpi-label}`. Horizontal rules only at `{color.tile-border}`. Sortable columns marked with a caret in `{color.text-tertiary}`. In-cell bars where a magnitude comparison matters, filled `{data.neutral-light}` behind right-aligned text.

### `filter-bar`

In `{dash.header-height}`, `{type.body}`. Active filters shown as removable chips in `{color.accent-soft}` with `{color.accent-deep}` text. **Always show which filters are active.** A dashboard showing a filtered subset without saying so is not a design flaw, it is a source of wrong decisions.

### `timestamp`

`{type.source}`, `{color.text-tertiary}`, top-right of the header. "Updated 14:32, 1 Aug 2026". Absolute, never "2 hours ago", because the reader needs to know whether the data covers the event they are investigating.

## Number formatting

| Type | Format | Example |
|---|---|---|
| Currency | Symbol, thousands separator, 2 decimals | £1,234.56 |
| Currency, large | Abbreviated, 1 decimal | £1.2m |
| Percentage | 1 decimal, or 0 if precision is spurious | 12.3% |
| Percentage point change | "pp", with sign | +0.4pp |
| Count | 0 decimals, thousands separator | 1,247 |
| Count, large | Abbreviated | 1.2k, 3.4m |
| Ratio | 2 decimals | 1.34x |
| Basis points | Integer, "bp" | 40bp |
| Date | Unambiguous, never numeric-only | 1 Aug 2026 |

Never `01/08/2026`, which means two different dates depending on the reader's country.

Consistency beats precision. Every instance of the same measure carries the same number of decimals across the whole dashboard, even where a particular value would look tidier with fewer.

Abbreviate only where space forces it, and never inside a table column where some values abbreviate and others do not.

## Do's and don'ts

### Do

- Fit the dashboard on one screen at 1440 × 900
- Make grey the default and add colour only where it encodes something
- Put the most important measure top-left
- Pair every number with a comparison
- Label series directly wherever it fits
- Show which filters are active
- Show an absolute refresh timestamp
- Use tabular numerals everywhere
- Use bullet graphs instead of gauges

### Don't

- Don't scroll. Split into two dashboards instead
- Don't use pie charts for anything requiring a precise read, and never above five slices
- Don't use 3D, gradients, or gloss
- Don't truncate the y-axis on a bar chart
- Don't show gridlines by default
- Don't put the legend on the right
- Don't use more than six colours at once
- Don't invert the light palette to make a dark one
- Don't show a number without its unit and its period

## Responsive behaviour

Dashboards resist responsiveness, because the single-screen constraint and the reflow are in direct conflict. Be explicit about which version the reader gets.

| Breakpoint | Behaviour |
|---|---|
| ≥ 1440px | Full layout, 12 columns, single screen |
| 1024 to 1439px | 12 columns, tiles reflow. Charts shrink but keep their encoding |
| 768 to 1023px | 6 columns. KPI tiles two-up. Charts stack full width |
| < 768px | Single column, KPI tiles only, charts collapse to sparklines with a tap to expand |

Below 768px, accept that this is a different product. A phone shows the headline measures and a link; it does not show the dashboard. Attempting the full layout on a phone produces something nobody can read and everybody has to scroll.

## Iteration guide

1. Remove before adding. Few's list of dashboard failures is mostly failures of addition.
2. Change `{data.neutral}` and see how much of the dashboard was relying on colour it should not have been.
3. Adding a chart type means deciding its encoding rank first: what channel carries the important quantity?
4. Test in greyscale. Anything that disappears was encoding by hue alone.
5. Test at 1440 × 900 before any other size.

## Known gaps

- The IBCS scenario encodings were reconstructed from published summaries and third-party implementations (Zebra BI, Inforiver) rather than from the standard, now ISO 24896, which is proprietary. Verify before relying on them where compliance matters.
- Bullet graph proportions come from Few's published specification as summarised elsewhere; the original specification document was not retrieved.
- The dark palette values were chosen rather than derived, and have not been tested on an OLED screen where near-blacks behave differently.
- No specification for interaction: tooltips, drill-down, cross-filtering behaviour and loading states are all unaddressed and all shape how a dashboard is actually used.
- No specification for alerting or conditional formatting thresholds.
- Nothing on data freshness handling: what a tile shows when the data is stale, partial or failed to load. This is where most production dashboards mislead.
- The Financial Times Visual Vocabulary (nine relationship families: deviation, correlation, ranking, distribution, change over time, magnitude, part-to-whole, spatial, flow) is the recommended chart-selection reference but is not reproduced here as tokens.
