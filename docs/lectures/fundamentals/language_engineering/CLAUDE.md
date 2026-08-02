# CLAUDE.md — language engineering track

This file governs the eighteen lectures in `docs/lectures/fundamentals/language_engineering/`. It supplements the root `CLAUDE.md` and `docs/CLAUDE.md`, which carry the repository-wide markdown style guide, the writing rules and the confidentiality rules; read those first. What follows is specific to this track, and it was derived by measuring the built lectures rather than by stating intentions, so where a convention is only partly observed this file says so explicitly.

---

## 1. What the track is, and what it is not

Eighteen lectures on building working systems out of language models, adapted from Alammar and Grootendorst, *Hands-On Large Language Models* (O'Reilly, 2024). Five parts: foundations (1 to 4), using pretrained models (5 to 8), systems (9 to 12), multimodal (13), training your own (14 to 18).

Three neighbouring tracks touch the same subject and the boundaries are load-bearing. `machine_learning/11_large_language_models/` answers **why it works**: scaling laws, emergent capability, in-context learning theory, governance. This track answers **how to build with it**. `claude_engineering/` answers a third question, how to direct a coding agent somebody else built. When a lecture here needs attention, transformers, UMAP, HDBSCAN, precision and recall, or word2vec, it **links to the machine learning track and does not re-derive**. That restraint is the main thing keeping the track from doubling in length, so preserve it.

The extraction the lectures were written from lives outside the repository, in OneDrive under `4. Career/9. Professional Material/Hands-On Large Language Models - Extracted/`, as fourteen markdown files plus 288 figures. It is the source of record for numbers and worked examples.

---

## 2. Structure that holds across all eighteen

Verified present in every lecture. Do not break these.

| Element | Rule |
|---|---|
| Sections | Exactly five, using `<div class="banner"><span class="step">Step N</span><h2>…</h2></div>` |
| Step titles | The 30-second version · Why this matters · The mental model · The detail · Synthesis and what's next |
| Opening | Exactly one `<p class="lede">` as the first paragraph of step 1 |
| Feynman test | Exactly one `<div class="callout feynman">` closing step 1 |
| Step 2 | Three or four reasons, opened as "The first reason is…", "The second reason is…", and so on |
| Step 3 | A short framing sentence, then the figure. No `<h3>` |
| Step 4 | `<h3>` subheadings only here |
| Step 5 | A synthesis paragraph, then `<div class="recall">` with an `<ol>`, then `<div class="connections">` |
| Header meta | Three spans: `Lecture N of 18` · `Reading time, 40 minutes` · `Part <roman>: <lower-case title>` |
| Breadcrumb | `<a href="../../index.html">Lectures</a> / <a href="index.html">Language engineering</a>` |
| Footer | Course link, all-lectures link, and `Lecture N of 18` |

The `<head>` and the three closing `<script>` tags are byte-identical across all eighteen. Copy them from any existing lecture rather than retyping; the stylesheet path is `../../assets/lecture.css` and KaTeX is loaded whether or not the lecture uses maths.

---

## 3. Conventions for new work

Lectures 9 to 18 established a tighter house style than lectures 1 to 8. **Follow the 9-to-18 convention.** The most recent lectures are the reference; the best single model is `13-multimodal_models.html` or `17-supervised_fine_tuning_with_qlora.html`.

**Length.** Roughly 2,850 to 3,800 words of rendered text. Lectures 1 to 8 run 3,765 to 4,710 and are the outliers, not the target.

**Figures.** One `<figure class="wide">` holding one inline SVG, in step 3. Not two.

**Arithmetic in `.worked` blocks.** This is the distinguishing feature of the later style and the highest-value thing to copy. Three to five `<div class="worked">` blocks per lecture, each a plain-text panel of derivations, comparisons and parameter tables in a fixed-width layout. Numbers are quoted to the precision the source gives them (0.8094, not "about 0.81"), ratios are computed and shown, and the reader can check every step. Prefer a `.worked` block to an HTML `<table>`; lectures 9 to 18 contain no `<table>` elements at all.

**Recall lists.** Fifteen to twenty-one items, several prefixed `<strong>Do the arithmetic.</strong>` where the answer is a calculation the lecture supports. Lectures 1 to 8 use seven to nine items with no arithmetic prompts, which is too few.

**Callouts.** One `feynman` (mandatory), zero to two `insight`, zero to one `warn`. Do **not** write "Vignette from the field" narratives; lectures 1 to 8 use them and lectures 9 to 18 dropped them in favour of quantified argument.

**Citations.** Author and year in prose, as "Reimers and Gurevych, 2019" or "Li and colleagues, 2023". No footnotes, no bibliography, no bare URLs in body text.

**Definition cards.** `<div class="defcard">` is available and lightly used. Fine for two or three genuine definitions; not a substitute for prose.

---

## 4. The SVG contract

One inline SVG per lecture, in step 3, inside `<figure class="wide">`.

```
<figure class="wide">
  <svg viewBox="0 0 880 400" xmlns="http://www.w3.org/2000/svg" role="img"
       aria-label="A sentence describing what the diagram shows, for screen readers.">
    <rect x="0" y="0" width="880" height="400" fill="#FFFFFF"/>
    <text x="440" y="20" text-anchor="middle" font-family="Inter" font-size="13"
          font-weight="600" fill="#18181b">The claim the figure makes</text>
    …
  </svg>
  <figcaption>What to look at and why it matters. Two or three sentences.</figcaption>
</figure>
```

Rules. Width is always 880, without exception across all eighteen; height runs 340 to 440 in lectures 9 to 18 and is the range to work in. A white background rect is the first child (present in lectures 12 to 18, absent in 9 to 11; include it). `role="img"` and a descriptive `aria-label` are required, and both are present on all twenty-six existing figures. A title `<text>` near the top, at y between 18 and 24, states the figure's claim. A `<figcaption>` is required and should interpret rather than restate. Fonts are `Inter` for labels and `JetBrains Mono` for anything representing code, numbers or tokens.

**Arrows.** Lectures 9 to 18 draw arrowheads as an inline `<line>` plus `<polygon>` rather than declaring `<defs><marker>`. Prefer that: it avoids `id` collisions if two figures ever appear on one page.

**Entities.** Use numeric character references (`&#8594;`, `&#215;`, `&#8722;`) rather than named ones. Named HTML entities such as `&minus;` and `&middot;` do render correctly, because inline SVG in an HTML document is parsed by the HTML parser, but they break any XML-based validation of the markup and have already caused false alarms.

**Palette.** Lectures 12 to 18 use the repository's design tokens from `assets/lecture.css`. Lectures 1 to 8 use a different, Tailwind-derived set (`#7c3aed`, `#0d9488`, `#2A3A78`) that appears nowhere in the later lectures. Use the token palette below.

| Family | Stroke / fill | Tint | Dark text | Typical use |
|---|---|---|---|---|
| Purple (primary) | `#5B47E0` | `#EDE9FE` | `#4C1D95` | The emphasised path, the thing being trained |
| Green | `#3E7A45` | `#DCFCE7` | `#14532D` | Good outcomes, frozen-and-fine, the recommended option |
| Blue | `#0F62FE` | `#DEEAFB` | `#0B4BBD` | Alternatives, secondary structures |
| Pink / red | `#DC2855`, `#BE185D` | `#FFE4E6` | `#831843`, `#9F1239` | Costs, failures, generative models |
| Amber (optional) | `#A16207` | `#FBF1D4` | `#713F12` | A fifth family when four is not enough |
| Neutral | `#71717A` | `#F4F4F5`, `#E4E4E7` | `#18181B`, `#3F3F46` | Frames, inactive bars, body labels |

---

## 5. Code policy

Code appears as `<pre><code>…</code></pre>`, as in the software and data engineering tracks. Note that `assets/lecture.css` has **no `pre` rule**, so a code block inherits the inline `code` styling and renders slightly boxed. That is how every code-bearing track in this repository looks. Do not add a `pre` rule to the shared stylesheet to fix it here; that asset is used by more than five hundred lectures and restyling it is a separate concern requiring its own review.

Snippets are illustrative, not runnable end to end. Show the shape of the idea and name the library. Where the source material's interface has since been deprecated, teach the durable pattern and say so in a `callout warn` rather than reproducing dead code, and point to the book's own repository for anything that must actually run. Escape `<`, `>` and `&` inside code blocks; a scan for raw tags is part of the verification below.

---

## 6. Prose

The repository writing rules apply in full: British English, no em or en dashes as punctuation, contractions where natural, lead with the conclusion, prose over bullets, and never open a paragraph with "However", "Moreover", "Furthermore", "Overall" or "Additionally".

Three additions specific to this track. **Quantify.** The later lectures earn their brevity by replacing adjectives with figures, so prefer "768-fold" to "dramatically smaller". **Be honest about the source.** Where the book contains an arithmetic slip or an internal contradiction, correct it and say what you did; two such cases are already flagged in lectures 16 and 17. **Name contamination.** Several benchmark figures quoted in the source are measured on models that had already seen the test data. Lectures 5, 15 and 18 flag this; any new number from a public benchmark deserves the same scrutiny.

---

## 7. Attribution

The landing page carries the source-material statement and it should not be weakened. Prose, structure, worked examples and figures are written fresh and do not reproduce the book's text or its illustrations. **Never copy the extracted PNGs into the repository**: they are O'Reilly's copyright, and the repository is a public one. Redraw as inline SVG, which is also what every other lecture in the repository does.

---

## 8. Verification

Run this from the track directory after any change. It checks link resolution, SVG structure, tag balance and code-block escaping in one pass.

```
PYTHONIOENCODING=utf-8 python - <<'PY'
import os, re, glob, html
from xml.etree import ElementTree as ET
ALLOWED = {"code","/code","strong","/strong","em","/em","h4","/h4","br","tspan","/tspan"}
base, broken = os.getcwd(), []
for f in sorted(glob.glob("*.html")):
    s = open(f, encoding="utf-8").read()
    for h in re.findall(r'href="([^"]+)"', s):
        if not h.startswith(("http", "#", "mailto")) and not os.path.exists(
                os.path.normpath(os.path.join(base, h))):
            broken.append((f, h))
    for svg in re.findall(r'<svg.*?</svg>', s, re.S):
        resolved = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#)([a-zA-Z][a-zA-Z0-9]*);',
                          lambda m: html.unescape(m.group(0)), svg)
        try: ET.fromstring(resolved)
        except ET.ParseError as e: print("SVG", f, e)
    for tag in ("section","figure","div","table","pre","ol","li","tr","td","th"):
        o, c = len(re.findall(rf'<{tag}[\s>]', s)), len(re.findall(rf'</{tag}>', s))
        if o != c: print(f"IMBALANCE {f} <{tag}> {o}/{c}")
    for block in re.findall(r'<pre>(.*?)</pre>', s, re.S):
        for t in re.findall(r'<(/?[A-Za-z|][^>\s]*)', block):
            if t.lower() not in ALLOWED: print(f"RAW TAG {f}: <{t}>")
    print(f"{f:44s} {len(re.findall(r'\w+', re.sub('<[^>]+>',' ',s))):5d} words")
print("BROKEN:", broken or "none")
PY
```

Then check the three index pages by hand: this track's `index.html` status badges, the `LE` row in `docs/lectures/index.html`, and the cross-links in `machine_learning/index.html`, `machine_learning/11_large_language_models/index.html` and `claude_engineering/index.html`.

---

## 9. Known divergence, and what to do about it

Lectures 1 to 8 were written in one session and 9 to 18 in later ones, and they differ in the ways tabulated above: two figures rather than one, the Tailwind palette rather than the token palette, `<defs><marker>` arrows, "vignette from the field" callouts, few `.worked` blocks, short recall lists, and around a thousand more words each. Both sets are correct, complete and verified; the divergence is stylistic.

Do not retrofit lectures 1 to 8 as a task in its own right. If you substantively edit one, bring it into line while you are there. If someone does want a consistency sweep, the palette is the change with the highest visual return and the lowest risk, since it is a mechanical substitution inside the SVGs and touches no prose.
