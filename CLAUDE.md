# CLAUDE.md

This file governs how Claude Code should behave in this repository. Read it in full at the start of every session before taking any action.

---

## 1. Repo purpose and context

This repository serves two related but distinct purposes. First, it is a general banking and financial risk reference knowledge base, covering regulatory frameworks, credit risk modelling methodology, and supporting quantitative disciplines. Second, it is an active exam preparation resource for the **ASSA F107 Banking Principles** actuarial exam.

The primary user is an actuary with deep hands-on experience in **credit risk modelling**, specifically A-IRB capital models (PD, LGD, EAD), IFRS 9 impairment modelling, and Basel regulatory capital. Coverage in these areas is strong. Coverage in the following areas is materially weaker and should be treated as **priority ingestion targets** whenever new material becomes available:

- **Operational risk** — taxonomy, Basel IV standardised measurement approach, RCSA, scenario analysis
- **Liquidity risk** — LCR, NSFR, intraday liquidity, stress testing
- **Market risk** — trading book, VaR/ES, FRTB, sensitivities-based method
- **Interest rate risk in the banking book (IRRBB)** — EVE, NII, BCBS 368
- **Bank pricing and transfer pricing** — funds transfer pricing, loan pricing, NIM
- **Bank strategy and governance** — risk appetite, stress testing frameworks, board governance

---

## 2. Folder structure and conventions

The repository root contains three content-bearing directories (`docs/`, `data/`, `src/`) plus standard Python project scaffolding (`pyproject.toml`, `requirements.txt`, `setup.cfg`, `main.py`).

> **Note:** The `README.md` at the root describes a structure that diverges from the actual folder layout. The README refers to `docs/credit_risk_modelling/` and `docs/azure/`, neither of which exists. The actual structure is documented below. Do not trust the README as a structural reference; trust this file.

### `docs/` — all knowledge content

```
docs/
├── application/
│   └── banks/
│       ├── [overview files: notation, structure, segmentation, AFS, risks, Pillar 3, products, ratings]
│       └── credit_risk/
│           ├── 01_application_scorecards/
│           ├── 02_airb_capital_modelling/
│           ├── 03_ifrs9_impairment_modelling/
│           └── 04_pillar_2a_modelling/
├── fundamentals/
│   ├── 01_software_engineering/
│   ├── 02_data_engineering/
│   ├── 03_data_analysis/
│   ├── 04_mathematics/
│   ├── 05_statistics/
│   ├── 06_machine_learning/
│   ├── 07-actuarial_science/     ← nearly empty; one stub notebook
│   └── 08-business_intelligence/
└── regulation/
    ├── [top-level overview: regulatory_environment, accounting_environment]
    ├── eu/          ← CRR (substantive); EBA, ECB stubs (empty)
    ├── international/
    │   ├── bis/     ← Basel I, II, framework; BCBS 144, 188, 189, 239, d424
    │   ├── fsb/     ← FSB overview, G-SIBs, TLAC
    │   └── ifrs/    ← IFRS 9 standard, staging, IFRS Foundation
    ├── south_africa/ ← Banks Act (stub); FSCA, PA, SARB stubs (all empty)
    ├── uk/          ← Bank of England, CRR near-final, FCA stub, MREL, PRA stub, SS3-24, SS4-24
    └── usa/         ← GAAP stub (empty)
```

**`docs/application/`** — applied, institution-type-specific content. Currently only `banks/` exists. New material about insurance or asset management should go into sibling folders, not inside `banks/`.

**`docs/application/banks/`** — bank-level overview files covering notation conventions, bank structure, customer segmentation, available-for-sale accounting, risk taxonomy, Pillar 3 disclosures, banking products, and ratings agencies.

**`docs/application/banks/credit_risk/`** — the deepest and most developed part of the repo. Four subdirectories mirror a model development lifecycle:

- `01_application_scorecards/` — origination scorecard methodology: underwriting, data requirements, sampling, origination PD models.
- `02_airb_capital_modelling/` — A-IRB regulatory capital modelling end-to-end: regulatory capital theory, PD/LGD/EAD definitions, data engineering, feature engineering, modelling, testing. Organised by risk parameter (pd/, lgd/, ead/ subfolders within modelling stages).
- `03_ifrs9_impairment_modelling/` — IFRS 9 ECL modelling: provisions framework, IFRS vs IRB comparison, SICR methodology, PD/LGD/EAD for ECL, forward-looking information (FLI), staging. Also organised by risk parameter.
- `04_pillar_2a_modelling/` — economic capital and ICAAP: economic capital theory, ICAAP vs IRB comparison.

**`docs/fundamentals/`** — domain-agnostic technical skills: software engineering conventions, SQL and data engineering, pandas/polars/visualisation, mathematics, statistics (descriptive, probability, GLMs, time series, survival analysis), machine learning (supervised, unsupervised, deep learning, evaluation, interpretation), a near-empty actuarial science stub, and Power BI.

**`docs/regulation/`** — regulatory and accounting frameworks organised by jurisdiction. The `international/bis/` subfolder is substantive. Most jurisdiction stubs outside BIS/IFRS/UK are empty placeholders.

**`data/`** — standard data science folder layout (raw, external, interim, processed, predictions, mappings, template, database). Currently empty except for placeholder `.gitkeep` files and a DuckDB WAL file. Not a knowledge base; do not place reference notes here.

**`src/`** — Python source code: config, constants, schema definitions, DQA utilities, and function stubs for the modelling pipeline (data engineering, EDA, feature engineering, train/test split, model estimation, model validation), organised by PD/LGD/EAD. Most function stubs are empty.

---

## 3. F107 syllabus coverage map

The table below maps standard F107 Banking Principles syllabus topics to existing content. Coverage status uses three values: **present** (substantive content exists), **partial** (some content but material gaps), or **absent** (no dedicated content found).

| F107 syllabus area | Coverage | Primary locations | Notes |
|---|---|---|---|
| **Basel history and architecture** (Basel I → IV, BCBS structure) | Present | `docs/regulation/international/bis/basel_1.md`, `basel_2.md`, `basel_framework.md`, `bis.md` | Strong; Basel IV finalisation captured in framework doc |
| **Pillar 1 — credit risk capital** (standardised, F-IRB, A-IRB, RWA) | Present | `docs/application/banks/credit_risk/02_airb_capital_modelling/01_introduction/01-regulatory_capital.md`, `05-irb_approach.md`; `docs/regulation/international/bis/bcbs_d424.md` | Deep A-IRB coverage; standardised approach less developed |
| **Pillar 1 — market risk capital** (VaR, ES, FRTB) | Absent | — | No dedicated content; priority gap |
| **Pillar 1 — operational risk capital** (BIA, TSA, SMA) | Absent | — | No dedicated content; priority gap |
| **Pillar 2 — ICAAP / SREP** | Partial | `docs/application/banks/credit_risk/04_pillar_2a_modelling/01_economic_capital.md`, `02_icaap_vs_irb.md` | Credit risk Pillar 2A covered; broader SREP process absent |
| **Pillar 3 — market discipline** | Partial | `docs/application/banks/06-pillar_3.md` | Overview file exists; detailed disclosure requirements absent |
| **Capital structure** (CET1, AT1, T2, buffers, leverage ratio) | Present | `docs/regulation/international/bis/basel_framework.md`; images in `bis/images/basel/` | Capital ratios and buffers well documented |
| **Resolution — TLAC, MREL, bail-in** | Present | `docs/regulation/international/fsb/tlac.md`, `g_sibs.md`; `docs/regulation/uk/mrel.md` | Solid coverage for a UK/international context |
| **IFRS 9 — ECL framework, staging, SICR** | Present | `docs/regulation/international/ifrs/ifrs9_standard.md`, `ifrs9_staging.md`; `docs/application/banks/credit_risk/03_ifrs9_impairment_modelling/` | Excellent; most developed area alongside A-IRB |
| **Credit risk — PD/LGD/EAD modelling** | Present | `docs/application/banks/credit_risk/02_airb_capital_modelling/` and `03_ifrs9_impairment_modelling/` (both with pd/, lgd/, ead/ subfolders) | Deep coverage; PIT vs TTC, LRA, SICR all present |
| **Market risk — trading book, VaR, FRTB** | Absent | — | No content; priority gap for exam |
| **Operational risk — taxonomy, scenarios, RCSA** | Absent | — | No content; priority gap for exam |
| **Liquidity risk — LCR, NSFR, stress testing** | Absent | — | No content; priority gap for exam |
| **Interest rate risk in the banking book (IRRBB)** | Absent | `docs/regulation/uk/ss4-24.md` may be adjacent | SS4-24 covers model risk, not IRRBB; EVE/NII methodology absent |
| **Bank structure and products** | Partial | `docs/application/banks/02-bank_structure.md`, `03-segmentation.md`, `07-products.md` | Overview level; detailed product pricing absent |
| **Ratings agencies and external credit assessment** | Partial | `docs/application/banks/07-ratings_agencies.md` | Stub-level only |
| **Bank strategy, governance, risk appetite** | Partial | `docs/application/banks/05-risks.md`; `docs/regulation/international/bis/bcbs_239.md` | BCBS 239 (data governance) present; risk appetite framework, board governance, and stress testing frameworks absent |
| **Stress testing frameworks** (EBA, BoE, DFAST) | Absent | — | No dedicated content |
| **UK and EU regulatory environment** | Partial | `docs/regulation/uk/` (substantive); `docs/regulation/eu/crr.md` (substantive); EBA, ECB, PRA, FCA stubs empty | UK CRR near-final requirements present; supervisory guidance gaps |

**Summary of F107 gaps requiring priority attention:**
1. Market risk (entire topic)
2. Operational risk (entire topic)
3. Liquidity risk (entire topic)
4. IRRBB (entire topic)
5. Stress testing frameworks
6. Risk appetite and governance frameworks
7. Bank pricing and funds transfer pricing

---

## 4. Ingestion priorities and workflow

When new material is provided (PDFs, transcripts, lecture notes, articles), follow this workflow in order.

**Step 1 — Classify by F107 syllabus area first.** Determine which F107 topic the material belongs to before deciding where to place it. Use the coverage map in section 3 as the primary routing guide. Do not default to the nearest existing folder if a more precise syllabus location is appropriate. For absent topics (market risk, op risk, liquidity risk, IRRBB), create new files in the most logical location within `docs/application/banks/` or `docs/regulation/` — do not defer ingestion because no folder exists yet.

**Step 2 — Scan for duplicates before writing.** Open the relevant existing file(s) and identify any concepts that overlap with the incoming material. Consolidate: extend or revise the existing content rather than appending a new section that restates the same idea. When in doubt, merge under the more precise heading.

**Step 3 — Flag knowledge gaps.** If the incoming material reveals a concept, formula, or regulatory requirement not covered anywhere in the repo, insert a gap note at the point in the file where coverage should exist. Use this exact callout format:

```markdown
> **<!-- GAP -->** *[Topic name]: Brief description of what is missing and why it matters for F107.*
```

This tag is machine-searchable. Run `grep -r "<!-- GAP -->"` to get a full gap inventory at any time.

**Step 4 — Apply the style guide.** Before saving any file, verify it conforms to section 5 below.

---

## 5. Markdown style guide

These conventions apply to all `.md` files in `docs/`. Apply them to any file you create or substantively edit.

**Headings.** Use sentence case throughout — capitalise only the first word and proper nouns. Never use title case. H1 is the file title; H2 and below are section headings.

**File structure.** Every markdown file must open with a single H1 title, followed immediately by a one-paragraph summary of the file's scope and what a reader should expect to learn from it. No content should appear before this summary paragraph.

**Prose vs bullets.** Default to prose paragraphs. Use a bulleted list only when the items are genuinely enumerable and have no natural connective flow. If you find yourself writing bullets where each item is a sentence with a subordinate clause, rewrite as prose.

**Bold.** Use bold exclusively to define a term on its first appearance in a file, in the form "**Term** is defined as...". Do not use bold for general emphasis within prose.

**Nesting.** Bullet lists must not exceed two levels of nesting. If you need a third level, restructure the content.

**Code and formulas.** All mathematical expressions, formulas, and pseudocode must appear in fenced code blocks. Use plain text notation inside the block rather than LaTeX, unless the rendering environment is confirmed to support LaTeX.

```
K = LGD * N(sqrt(1/(1-R)) * G(PD) + sqrt(R/(1-R)) * G(0.999)) - PD * LGD
```

**Internal links.** Cross-references between files are encouraged. Use relative paths from the current file's location. Example: `[IRB approach](../02_airb_capital_modelling/01_introduction/05-irb_approach.md)`.

**PDFs.** Many files have a companion `.pdf` with the same stem. Treat the `.md` as the authoritative editable version. The PDF is a static snapshot.

**Naming.** File names use lowercase with hyphens or underscores (existing files mix both styles; match the dominant style within the folder you are working in). Folder names use underscores with a numeric prefix where ordering matters.

---

## 6. Session startup instructions

At the start of every new session in this repository, follow these steps before taking any action:

1. **Read this file (`CLAUDE.md`) in full.** Do not proceed until you have done so.
2. **Check the F107 coverage map** (section 3 above) to understand the current state of the knowledge base.
3. **Confirm the session goal with the user** before writing, editing, or restructuring anything. Ask: what topic or material are we working on today, and what is the desired outcome?

Do not ingest material, restructure folders, or create new files speculatively. Wait for explicit instruction from the user in each session.
