# Email and newsletter tokens

The most constrained medium in this track. Email rendering engines are twenty years behind browsers, one major client renders HTML through Microsoft Word, and the reader's client may rewrite your colours without asking. Design accordingly.

Inherits [the house file](../DESIGN.md) in intent and overrides most of it in implementation, because the house tokens assume CSS that email clients do not support.

## Overview

**Inherits unchanged:** the neutral ramp's values, the semantic colours, the spacing logic, the discipline about heading space.

**Overrides:** the font stack entirely (no web fonts, no Inter). Layout is tables, not flexbox. Radius is decorative and may not render. The type scale is coarser.

**Adds:** client-constraint tokens, a bulletproof button specification, dark-mode handling, and the legal footer requirements.

**Key characteristics:**
- 600px single column, still correct after twenty years
- Arial and Helvetica, because a web font that fails in Outlook is worse than a system font everywhere
- 16px body minimum; iOS enlarges anything smaller and breaks the layout doing it
- Tables for layout, `role="presentation"` on every one
- Dark mode is partly outside your control and must be designed as a degradation, not a feature
- The best-performing newsletters look almost like plain text

## Client constraints

The three clients that matter. Figures below are Litmus market-share estimates for 2026 and move slowly.

| Client | Share | Engine | Behaviour |
|---|---|---|---|
| Apple Mail (iOS and macOS) | ~65% | WebKit | Modern CSS, respects `prefers-color-scheme`, honours web fonts |
| Gmail (web and mobile) | ~24% | Custom | Strips `<head>` styles in some contexts, ignores `prefers-color-scheme`, applies its own dark inversion |
| Outlook (Windows desktop) | ~6% | Microsoft Word | The problem. No flexbox, no grid, no `max-width`, no `border-radius`, no background images without VML, no media queries |

Microsoft has signalled the end of the Word-based desktop Outlook, currently pointed at late 2026. Until it is actually gone, and for some time after while corporate estates catch up, dual-coding is required.

### CSS support

| Property | Status |
|---|---|
| `font-family`, `font-size`, `color`, `line-height`, `text-align` | Safe everywhere |
| `padding`, `margin` on `<td>` | Safe |
| `padding` on `<a>` | Fails in Outlook. Put padding on the containing `<td>` |
| `background-color` | Safe on `<td>` and `<table>` |
| `background-image` | Needs VML for Outlook |
| `border-radius` | Ignored by Outlook. Everything else honours it |
| `max-width` | Ignored by Outlook. Use the `width` attribute as well |
| `flexbox`, `grid`, `position`, `float` | Do not use. Nothing supports them reliably |
| Media queries | Apple Mail yes, Gmail partly, Outlook desktop no |
| Web fonts | Apple Mail yes, Gmail on Chrome only, Outlook no |

Inline the styles that must render. Put media queries and dark-mode rules in a `<style>` block in the head and treat them as progressive enhancement, since some clients strip the block.

## Layout

| Token | Value | Notes |
|---|---|---|
| `{email.width}` | 600px | Set with the `width` attribute and `max-width` both |
| `{email.width-mobile}` | 320px | iPhone SE, the practical floor |
| `{email.breakpoint}` | `@media (max-width: 600px)` | The only breakpoint |
| `{email.section-padding}` | 24px 32px | Vertical, horizontal |
| `{email.section-padding-mobile}` | 20px 20px | |
| `{email.content-width}` | 536px | 600 less two 32px gutters |
| `{email.block-gap}` | 24px | Between content blocks |
| `{email.rule}` | 1px solid `#E8E6E1` | Section divider |

Single column. Two columns are possible and stack at the breakpoint, but they fail in Outlook desktop where the media query does not fire, leaving two narrow columns on a phone-sized reading pane. Unless the content genuinely needs side-by-side comparison, do not.

600px persists because it survives every reading pane without horizontal scroll. Some platforms default wider (Klaviyo 700, Constant Contact 650) and get away with it. There is no reader benefit to the extra width and there is a rendering risk, so stay at 600.

## Typography

### Stack

```css
font-family: Arial, Helvetica, sans-serif;
```

That is the recommendation, and it is deliberately boring. Arial is on every Windows machine since the early 1990s and every Apple device. Helvetica catches Apple's preference. The generic keyword catches everything else.

Web fonts are a progressive enhancement only, loaded by `@import` in the head with a full fallback in the same declaration:

```css
font-family: 'Inter', Arial, Helvetica, sans-serif;
```

The email will look correct in Apple Mail and acceptable everywhere else. That is the best available outcome, and it is why the house `{font.sans}` cannot simply be reused: an email designed around Inter's metrics and rendered in Arial will not just look different, it will reflow.

| Token | Stack |
|---|---|
| `{font.email}` | `Arial, Helvetica, sans-serif` |
| `{font.email-serif}` | `Georgia, 'Times New Roman', serif` |
| `{font.email-mono}` | `Consolas, 'Courier New', monospace` |

Georgia is the one genuinely good system serif, present on Windows and macOS, and worth using for a text-led newsletter.

### Scale

| Token | Size | Weight | Line height | Use |
|---|---|---|---|---|
| `{type.email-hero}` | 32px | bold | 1.25 | Hero headline |
| `{type.email-h1}` | 26px | bold | 1.30 | Section headline |
| `{type.email-h2}` | 20px | bold | 1.35 | Subsection |
| `{type.email-body}` | 16px | normal | 1.55 | Body. The floor |
| `{type.email-body-sm}` | 15px | normal | 1.55 | Secondary |
| `{type.email-caption}` | 13px | normal | 1.45 | Captions |
| `{type.email-footer}` | 12px | normal | 1.45 | Footer, legal |

**16px is the body floor and it is not negotiable.** iOS automatically enlarges text below 16px, which breaks the layout you designed around the smaller size. Setting 16px is easier than fighting the enlargement.

Line height is set in unitless multiples where supported and in pixels for Outlook: `line-height: 25px;` alongside `line-height: 1.55;`.

## Colors

Email colour has one extra failure mode: some clients will change it for you in dark mode, and you cannot stop them.

| Token | Value | Use |
|---|---|---|
| `{color.email-bg}` | `#F7F6F3` | Outer background, outside the 600px column |
| `{color.email-canvas}` | `#FFFFFF` | Content column |
| `{color.email-text}` | `#37352F` | Body |
| `{color.email-text-secondary}` | `#5C5B57` | Captions, secondary |
| `{color.email-text-footer}` | `#82817D` | Footer, legal text |
| `{color.email-link}` | `#4A39C7` | Links. Darker than house accent, for the 4.5:1 floor on tinted grounds |
| `{color.email-cta}` | `#5B47E0` | Button fill |
| `{color.email-cta-text}` | `#FFFFFF` | Button label |
| `{color.email-rule}` | `#E8E6E1` | Dividers |

Body text at 4.5:1 minimum, link text at 4.5:1 minimum, both against the surface they actually sit on rather than against white.

### Dark mode

Three behaviours, and you control one of them.

| Client | Behaviour | Your control |
|---|---|---|
| Apple Mail | Honours `prefers-color-scheme` and the `color-scheme` meta | Full |
| Gmail | Ignores the media query, applies partial inversion of its own | None |
| Outlook Windows desktop | No transform. Your light design renders as-is on a dark OS | None |
| New Outlook, Outlook.com | Partial inversion | Limited |

Declare intent and design a dark palette for the client that will honour it:

```html
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
```

| Token | Value |
|---|---|
| `{color.email-bg-dark}` | `#151514` |
| `{color.email-canvas-dark}` | `#1F1F1D` |
| `{color.email-text-dark}` | `#E4E3E0` |
| `{color.email-link-dark}` | `#A99BFF` |

Then design the light version so that a naive inversion does not destroy it. The practical rules: avoid pure white backgrounds behind logos (use a transparent PNG with a light stroke so it survives on either ground), avoid text baked into images, and avoid relying on a background colour to make text legible, since the inversion may change one and not the other.

## Elevation and depth

None. `box-shadow` is unsupported in Outlook and unreliable elsewhere, so `{elevation.0}` is the only level available and separation is achieved by background colour and rules.

| Token | Implementation |
|---|---|
| `{elevation.0}` | `{color.email-canvas}` column on `{color.email-bg}` ground |
| `{elevation.card}` | A nested table with `{color.email-bg}` fill and 24px padding, not a shadow |

The 600px white column sitting on the grey page ground is the only depth cue in the medium, and it is enough. Attempting more produces something that renders in Apple Mail and disappears everywhere else, which is worse than a flat design that renders identically for everyone.

## Shapes

| Token | Value | Caveat |
|---|---|---|
| `{radius.email-button}` | 4px | Outlook renders square unless VML is used |
| `{radius.email-card}` | 8px | Outlook renders square |
| `{radius.email-image}` | 0 | Rounded images fail badly; use square |

Treat radius as decoration that some readers will not see. Never let a design depend on it.

## Components

### `email-shell`

```html
<body style="margin:0;padding:0;background-color:#F7F6F3;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td align="center" style="padding:24px 0;">
    <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"
           style="width:600px;max-width:600px;background-color:#FFFFFF;">
      <!-- sections -->
    </table>
  </td></tr>
</table>
</body>
```

Every layout table carries `role="presentation"`, which tells a screen reader it is scaffolding rather than data. Omitting it makes the email read as a nested grid of cells.

### `cta-button`

The bulletproof pattern. VML for Outlook inside a conditional comment, an anchor for everything else.

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0">
 <tr><td align="center" style="padding:8px 0;">
  <!--[if mso]>
  <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml"
    href="https://example.com" arcsize="10%" fill="true" stroke="false"
    style="height:48px;v-text-anchor:middle;width:220px;">
    <v:fill type="tile" color="#5B47E0" /><w:anchorlock/>
    <center style="color:#FFFFFF;font-family:Arial,sans-serif;font-size:16px;font-weight:bold;">
      Read the note</center>
  </v:roundrect>
  <![endif]-->
  <!--[if !mso]><!-->
  <a href="https://example.com" style="display:inline-block;background-color:#5B47E0;
     color:#FFFFFF;text-decoration:none;border-radius:4px;padding:14px 28px;
     font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:bold;
     line-height:20px;text-align:center;">Read the note</a>
  <!--<![endif]-->
 </td></tr>
</table>
```

| Token | Value |
|---|---|
| `{cta.padding}` | 14px 28px |
| `{cta.min-height}` | 48px |
| `{cta.min-width}` | 44px |
| `{cta.font-size}` | 16px bold |
| `{cta.radius}` | 4px |
| `{cta.mobile-width}` | 100% at the breakpoint |

Minimum tap target 44 × 44px, per Apple's guidance; Google prefers 48. The padding above clears both. One primary call to action per email. A second one halves the first.

### `preheader`

The text after the subject line in the inbox list. Hidden in the body, visible in the preview.

```html
<div style="display:none;font-size:1px;color:#FFFFFF;line-height:1px;
     max-height:0;max-width:0;opacity:0;overflow:hidden;">
  The one-sentence version of this email.
  &#8199;&#65279;&#8199;&#65279;&#8199;&#65279;
</div>
```

| Token | Value |
|---|---|
| `{preheader.mobile}` | 40 to 50 characters visible |
| `{preheader.desktop}` | 85 to 100 characters visible |

Front-load the meaning in the first 40 characters. The trailing invisible characters stop the client pulling body text into the preview after your sentence ends.

### `image`

| Token | Display | Export |
|---|---|---|
| `{image.full}` | 600px | 1200px |
| `{image.inline}` | 536px | 1072px |
| `{image.compression}` | JPEG 60 to 70% | 100 to 150KB per image |

Always set `width` as an attribute as well as in CSS. Always set `alt`. Many clients block images by default, so alt text is what a meaningful fraction of readers actually see.

Never put essential text inside an image. It fails when images are blocked, it cannot be read by a screen reader, it cannot be translated, and it inverts unpredictably in dark mode.

### `footer`

Legally required, not optional.

| Requirement | Regime |
|---|---|
| Working unsubscribe link | CAN-SPAM, PECR |
| Physical postal address | CAN-SPAM |
| Clear sender identification | GDPR, PECR |
| Privacy policy link | GDPR |
| Opt-out honoured within 10 business days | CAN-SPAM |

`{type.email-footer}` at `{color.email-text-footer}`, centred, with the unsubscribe link visibly a link. Making unsubscribe hard is both illegal and counterproductive: readers who cannot unsubscribe report spam, which damages deliverability for everyone on the list.

### `divider`

`<td>` with `height:1px`, `background-color:#E8E6E1`, `font-size:0`, `line-height:0`. An `<hr>` renders inconsistently; a one-pixel table cell does not.

## Do's and don'ts

### Do

- Set body at 16px
- Use tables for layout, with `role="presentation"` on every layout table
- Give every image alt text and a `width` attribute
- Put padding on the `<td>`, never on the `<a>`
- Provide VML fallbacks for buttons
- Declare `color-scheme` and design a dark palette for the clients that honour it
- Front-load the preheader
- Include unsubscribe, postal address and privacy link
- Test in Apple Mail, Gmail and Outlook before sending

### Don't

- Don't use flexbox, grid, `float` or `position`
- Don't depend on `border-radius`, `max-width` or background images
- Don't put text inside images
- Don't set body text below 16px
- Don't use more than one primary call to action
- Don't assume dark mode will look like your design
- Don't build a two-column layout unless the content requires the comparison
- Don't over-design. The evidence points the other way

## Responsive behaviour

One breakpoint.

```css
@media only screen and (max-width: 600px) {
  .container { width: 100% !important; }
  .section   { padding: 20px !important; }
  .cta       { width: 100% !important; display: block !important; }
  .stack     { display: block !important; width: 100% !important; }
  .h-hero    { font-size: 26px !important; line-height: 1.25 !important; }
}
```

Outlook desktop does not fire it, which is why the desktop layout must be acceptable at any width on its own. Design mobile-tolerant rather than mobile-first: a single 600px column that simply gets narrower is the layout that works everywhere.

## The case for plain text

The strongest finding in current email practice cuts against most of the specification above: near-plain-text newsletters consistently outperform designed HTML on click-through. Reported margins vary and the figures circulating (around 20 per cent higher click-to-open) come from vendor studies rather than controlled trials, so treat the magnitude with suspicion and the direction as well supported.

The mechanism is not mysterious. A plain email reads as correspondence; a designed one reads as marketing, and readers have learned to skip marketing. Substack's default styling, Morning Brew's two-colour masthead, Dense Discovery and The Browser all sit at the plain end and all work.

Choose plain when the sender's voice is the value, the audience is already engaged, or the message is a single idea. Choose designed HTML when brand consistency is contractual, the content is genuinely visual, or the structure is complex enough that prose cannot carry it.

The best default is the hybrid: this specification's structure, one accent colour, no decorative images, a high text-to-image ratio, one call to action. It looks almost like plain text and degrades to plain text gracefully.

## Iteration guide

1. Test before iterating. Email is the one medium where a change that looks fine locally can break for two thirds of readers.
2. When adding a component, ask what it does in Outlook first. If the answer is "nothing", it is decoration.
3. Reduce before styling. The evidence favours restraint more strongly here than anywhere else in this track.
4. Check the preheader in an actual inbox list, not in a preview pane.

## Known gaps

- Client market-share figures are 2026 Litmus estimates and shift. They are directional, not precise, and skew by audience: a corporate mailing list will have far more Outlook than the global average.
- The end-of-support date for the Word-based Outlook renderer is a Microsoft signal rather than a shipped change. Do not drop the VML fallbacks on the strength of it.
- The plain-text performance figures come from vendor-published campaign analyses with no controls stated. The direction is well attested; the magnitude is not.
- No specification for accessibility beyond `role="presentation"` and alt text: reading order, `lang`, and heading semantics in email are all under-specified here and all matter.
- No AMP for Email or interactive email specification. Both exist; neither is widely enough supported to build on.
- Nothing on deliverability: authentication (SPF, DKIM, DMARC), list hygiene and sending reputation shape whether the design is seen at all, and they sit outside this file.
