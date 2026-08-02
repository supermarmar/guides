# MEMORY.md — docs/ session memory

This file is updated at the end of each working session. It gives Claude Code (and the user) a quick orientation: where we left off, what is in progress, and what to tackle next. It is not a knowledge base — substantive notes belong in `wiki/`. It is not a task list — it is a persistent context handoff.

---

## User profile

- **Role:** Actuary and credit risk modelling expert (ASSA).
- **Deep expertise:** A-IRB capital modelling (PD/LGD/EAD), IFRS 9 ECL impairment modelling, Basel regulatory capital (Pillar 1/2/3), South African banking regulation.
- **Exam target:** ASSA F107 Banking Principles.
- **Weaker areas (exam priority):** Market risk, operational risk, liquidity risk, IRRBB, stress testing frameworks, bank pricing / FTP, risk appetite and governance.

---

## F107 exam prep status

| Area | Wiki notes | Flashcards | Status |
|---|---|---|---|
| Credit risk (PD/LGD/EAD, IRB) | Strong | Regular daily decks | On track |
| IFRS 9 (ECL, staging, SICR) | Strong | Regular daily decks | On track |
| Basel capital structure (CET1/AT1/T2, buffers) | Strong | Regular daily decks | On track |
| Resolution (TLAC, MREL, bail-in) | Present | Occasional | On track |
| G-SIBs, systemic risk | Present | Occasional | On track |
| Pillar 3 / disclosures | Partial | Sparse | Needs attention |
| Market risk (VaR, ES, FRTB) | **Absent** | None | **Priority gap** |
| Operational risk (SMA, RCSA) | **Absent** | None | **Priority gap** |
| Liquidity risk (LCR, NSFR) | **Absent** | None | **Priority gap** |
| IRRBB (EVE, NII, BCBS 368) | **Absent** | None | **Priority gap** |
| Stress testing frameworks | **Absent** | None | **Priority gap** |
| Bank pricing / FTP | **Absent** | None | **Priority gap** |
| Risk appetite & governance | Partial | None | Needs attention |

---

## Active flashcard decks

Daily practice files in `docs/flashcards/` (most recent first):

| File | Cards | Topics covered |
|---|---|---|
| F107-2026-04-15.md | 8+ | Capital structure, Credit risk (EL, WCDR), IFRS 9 (staging, classification, FVOCI/FVPL), G-SIBs |
| F107-2026-04-14.md | — | — |
| F107-2026-04-13.md | — | — |
| F107-2026-04-07.md | — | — |
| F107-2026-03-31.md | — | — |
| F107-2026-03-30.md | — | — |

---

## Raw material awaiting ingestion

Files in `docs/raw/` not yet processed into wiki notes:

| File | Status |
|---|---|
| `2025-SAAJ-LarneyCo-FIN.pdf` | Not ingested |
| `A_teaser_expect_the_finished_version_in_a_few_months__1762899116.pdf` | Not ingested |
| `Machine_Learning_in_Credit_Risk_1756102284.pdf` | Not ingested |
| `anatomy_of_claude_folder.pdf` | Not ingested |
| `llm_knowledge_base.pdf` | Not ingested |
| `no_more_EAD_and_ECL_nonsense_1758314364.pdf` | Not ingested |

---

## Open items and session notes

### F105 investments lecture track, sequenced 2026-07-31

`docs/lectures/application/investments/` now carries eleven landing pages and a 99-lecture
sequence. No lectures are written yet. The plan lives at
`C:\Users\mario\.claude\plans\i-would-like-you-serialized-pnueli.md`.

Source is the user's own ASSA F105 summary, `Short Summary.pdf` in
`OneDrive\Documents\4. Career\8. Academic Material\1. ASSA\F105\`, checked against the official
syllabus PDF in the same folder. There is no `docs/wiki/application/investments/`; this track is
built straight from the PDF, the way `fundamentals/actuarial_science/` was built from the UP
summaries. Extract the PDF text with PyMuPDF (`import fitz`), which is installed; `pdftoppm` is not.

Structural decisions, agreed with the user, do not relitigate:

- Two top-level folders mirroring banking. Asset classes and derivatives sit **inside**
  `01_internal_environment/` as the institution's toolkit, not in the external environment.
- Overlap with `fundamentals/` and `regulation/` is handled by assume-and-cross-link. Each lecture
  names its prerequisite in the header and covers only the investor-specific angle.
- Gap lectures name a real academic source; the landing pages already record which source per module.

Next step is the `portfolio_construction/` module, ten lectures. It is first because chapter 11 of
the summary is a heading with nothing under it while syllabus objective (f) requires mean-variance
theory in full, so it is both the largest hole and the highest exam value. Sources are named on
that module's landing page. A syllabus objective (a) to (p) coverage map sits on the track landing;
keep it true if lectures are merged or cut.

Two things to watch. First, the summary is a revision compression: it is a complete memory hook for
someone who already knows the material and a thin teaching source, so more of the 99 lectures need
external sourcing than the fourteen-row gap table suggests. Build `portfolio_construction/` first
and judge the output quality before committing to the rest. Second, the reading order on the
landing pages follows the summary's chapter order, which puts portfolio construction after
everything that depends on it. The build order deliberately inverts this. If the reading order
should invert too, the landing pages need rewriting.

### Data engineering lecture track, built 2026-07-31

`docs/lectures/fundamentals/data_engineering/` carries a landing page and all twenty lectures, in
five parts: foundations (01-03), SQL and data modelling (04-09), ingestion (10-12), transformation
at scale (13-15), and the undercurrents (16-20). The spine is the Reis and Housley lifecycle, five
stages plus six undercurrents. Roughly half came from the eleven notes in
`docs/wiki/fundamentals/02_data_engineering/`; the rest is new material on dimensional modelling,
CDC, streaming, Iceberg and Delta, dbt, orchestration, observability and data contracts, governance,
and DataOps.

**Decision, agreed with the user, do not relitigate: for data engineering the lectures are the
source of truth, not the wiki notes.** This inverts the general repository convention. New data
engineering material goes into the lecture course. The reasoning and its consequences are recorded
in `docs/wiki/fundamentals/02_data_engineering/00-source_of_truth.md` and in a callout on the course
landing page.

Two consequences to remember. Gap inventory by `grep -r "<!-- GAP -->"` covers only the wiki, so
gaps noted in lectures are invisible to it; there is no lecture equivalent of the tag. And flashcard
authoring on a data engineering topic should read the lecture rather than the note, because several
notes are now much thinner than the lecture built on them (`02-sql-intro.md` is a stub against three
SQL lectures; `03-duckdb.md` is a comparison table against a full lecture).

The five notebooks in the wiki folder remain runnable and are the executable companion to Lectures
04 to 06, 11, and 16. The lectures reference them rather than reproducing their code.

Nothing is committed: the course is untracked and `docs/lectures/index.html` is modified.

### Design lecture track, complete 2026-08-01

`docs/lectures/fundamentals/design/` is finished: 28 lectures across 8 modules, all built, plus 8
machine-readable `DESIGN.md` token specifications. Roughly 11,900 lines of HTML. This is the only track
in the collection where the token specs were written before the lectures, at the user's explicit
request.

Structure, agreed with the user, do not relitigate:

- Module 0 foundations (11 lectures), then seven medium modules: blogs (2), reports (3), documents (2),
  presentations (3), posters (2), dashboards (3), emails (2).
- **Token specs carry no principles prose.** The user was explicit: the DESIGN.md files are pure token
  specs because the principles live in the lectures. Do not add explanation to them.
- **Shared DNA plus overrides.** `design/DESIGN.md` is the house style; each medium file states what it
  inherits, what it overrides and why. A medium file may change a value, never a token name.
- Lectures follow the writing-track seven-step format: 30-second version, why this matters, mental
  model, the detail, the grandmaster's perspective, test yourself, connections. Every lecture has at
  least one hand-drawn SVG figure and a worked example.

Three through-lines the track deliberately repeats, stated explicitly in lecture 28 step 5. Keep them
if the material is ever revised:

1. **The sentence title.** Exhibit titles, action titles, web headings, the poster finding, the memo
   subject line. State the takeaway, not the topic. The one convention that improves the analysis
   rather than the presentation.
2. **The configured default.** Word styles, slide masters, chart themes, email templates. A
   specification only reaches the work through a mechanism, and the mechanism is always a default
   somebody configured once.
3. **The discrete encoding.** Isotype repetition, IBCS fill patterns, bullet-graph bands. Counting and
   classifying are exact where estimating is not.

Where the track deliberately argues with its own sources, so these are not errors to "fix":

- Lecture 10 cites Bateman et al. (CHI 2010) showing embellished charts recall better, which partly
  refutes Tufte's data-ink prescription. Kept, with the note that banking never errs toward austerity.
- Lecture 17 overrules Butterick on system fonts for circulated `.docx` only, because a substituted
  font repaginates the document. The concession does not extend to PDFs.
- Lecture 19 treats the read-alone deck as a request for a different artefact, against common banking
  practice, because the redundancy effect does not diminish at a compromise setting.
- Lecture 22 admits it is the weakest-evidenced lecture in the track and names what is convention.
- Lecture 25 argues line charts do not need a zero baseline. This is the majority practitioner view,
  not universal; a house convention would override it.

Verification state: all internal links resolve both directions, all tags balance, no em or en dashes
including HTML-entity forms, every non-ASCII character audited as an intentional maths symbol.

**Two things left open.** The root `docs/lectures/index.html` hero claims 238 fundamentals lectures
while the directory holds 302 non-index HTML files; the discrepancy predates this track and another
session is editing that file concurrently, so it was left alone rather than guessed at. And the email
module (lectures 27 and 28) is the most perishable material here: client market shares, CSS support
and the fate of the Word-based Outlook renderer are a 2026 snapshot, flagged as such in the lectures
and the token file, and will need a refresh in a year.

Nothing is committed.

### Verification debt in the investments lectures

Every figure in the investments lectures is computed by a Python script in the session scratchpad
before it is written, but the discipline tightened partway through the module sequence, so the
lectures are not equally checkable. Three tools now exist alongside the scripts:

- `blockcheck.py` confirms every value a script emitted survives into the finished page. It needs the
  script to have called `emit()`, which only the later lectures do.
- `numcheck.py` is the general version: it checks every figure in a lecture's worked blocks against
  the script's whole output, so it works without `emit()`.
- `vacuity.py` parses a script and flags assertions whose condition contains no computed value. Those
  cannot fail, so they inflate a pass count without testing anything.

Outstanding at the end of this session, in priority order:

1. RESOLVED. `pc09` (liability hedging) failed three of its own assertions, and the lecture was right
   in all three cases. The script also crashed part-way on an unescaped `%` in a format string, so it
   had never run to completion, which is why its assertion list was truncated. All three stale
   assertions asserted the naive result the lecture disproves: that key-rate durations sum to the
   Macaulay duration (they sum to the modified figure, 12.6028 against a Macaulay 13.3590, with a
   0.31 per cent discretisation gap the lecture states and this now confirms independently); that
   matching N key-rate sensitivities forces the weights to sum to one (it does not, which is the
   lecture's central finding and the reason seven key rates need eight instruments); and that
   normalised key-rate durations agree when money sensitivities match (they do not, each being
   divided by a different present value). They are now counterexamples asserting the failure. The
   script passes 12 of 12 with no vacuous claims.
2. `pc06` (limitations and Black-Litterman) has 146 figures in its worked blocks that no variant of
   its script reproduces, and `pc04` has 63. Both went through several revisions. Given that `pc09`'s
   apparent 92 fell to 56 once its crash was fixed, check first whether these scripts run to
   completion at all before reading anything into the counts.
3. `der05` exits non-zero and has not been diagnosed. `der07` shows 11 unmatched figures.
4. `vacuity.py` has only been run against the performance measurement scripts and `pc09`. It found nine empty
   assertions across two of them, including two bare `True` constants and a table of percentages
   written by hand rather than computed. Both lectures were corrected and their sourcing notes now
   state the real counts. The other investments scripts have not been scanned.

The lesson worth carrying: a passing assertion count means nothing until the assertions have been
checked for whether they could fail, and a script's current state is not evidence about what a
lecture was built from.

### General

- Update this section at the end of each session with anything that would help the next session start cleanly.

---

## How to update this file

At the end of a session, update:
1. The F107 status table if any gaps were filled.
2. The flashcard decks table with new files or card counts.
3. The raw material table if anything was ingested.
4. The open items section with any unresolved questions, decisions deferred, or next steps.
