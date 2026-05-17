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

Knowledge content lives under `docs/wiki/`. Sibling folders inside `docs/` are `flashcards/` (F107 daily decks), `raw/` (source PDFs, read-only), and `copilot/` (reserved). See `docs/CLAUDE.md` for the `docs/` shell; the tree below documents `docs/wiki/`, which is the authoritative knowledge base.

```
docs/wiki/
├── application/
│   └── banking/
│       ├── 01_internal_environment/
│       │   ├── 01-business_model.md … 06-structure.md      ← bank-level overview (business model, financial management, capital management, liquidity management, products, structure)
│       │   ├── examples/                                    ← worked examples (e.g. FNB AFS)
│       │   ├── pricing/                                     ← pricing framework, FTP, loan/deposit/derivative pricing, DCF model, segmentation
│       │   ├── risk_management/                             ← risk management process, risk appetite, identification, measurement, mitigation, economic capital, ICAAP, SREP
│       │   └── risk_measurement/
│       │       ├── credit_risk/
│       │       │   ├── 01_models.md, 02_probability_of_default.md, 03_notation.md  ← credit-risk overview
│       │       │   ├── a-irb_capital/             ← deepest area: 9-stage lifecycle (intro → monitoring), pd/lgd/ead splits
│       │       │   ├── application_scoring/       ← origination and behavioural scorecards
│       │       │   ├── ifrs9_impairments/         ← 8-stage lifecycle, FLI + SICR included
│       │       │   ├── counterparty_credit_risk/  ← context, counterparty exposures
│       │       │   └── credit_concentration_risk/ ← single-name, sector concentration
│       │       ├── market_risk/             ← context, models, proprietary trading & XVA
│       │       ├── operational_risk/        ← sources, loss data, capital (Basel II, SMA), AML/KYC
│       │       ├── liquidity_risk/          ← short-term metrics, LCR, long-term metrics, NSFR, behavioural modelling
│       │       ├── interest_rate_risk/      ← IRRBB sources, yield curves, NII/NIM, measurement
│       │       ├── climate_risk/            ← context, modelling approach
│       │       ├── stress_testing/          ← Pillar 2B (stub)
│       │       └── other_risks/             ← pension risk, other Pillar 2A risks
│       └── 02_external_environment/         ← regulatory environment, accounting environment, economic environment, ratings agencies, central banks
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
    ├── eu/          ← CRR (substantive); EBA, ECB stubs (empty)
    ├── international/
    │   ├── bis/     ← Basel I, II, framework, BIS overview (all substantive); BCBS 144, 188, 189 (filename typo: bcbcs_189.md), 239, d424; BCBS 219 stub
    │   ├── fsb/     ← FSB overview, G-SIBs, TLAC (all short)
    │   └── ifrs/    ← IFRS 9 standard (substantive), IFRS Foundation (substantive), IFRS 9 staging (short)
    ├── south_africa/ ← Banks Act (short); FSCA, NCA, PA, SARB stubs (all empty)
    ├── uk/          ← CRR near-final, SS3-24, SS4-24 (substantive); Bank of England, MREL (short); FCA, PRA stubs (empty)
    └── usa/         ← GAAP stub (empty)
```

**`docs/wiki/application/`** — applied, institution-type-specific content. Currently only `banking/` exists. New material about insurance or asset management should go into sibling folders, not inside `banking/`.

**`docs/wiki/application/banking/`** — split into `01_internal_environment/` (the bank itself: business model, financial management, products, structure, plus pricing/, risk_management/, risk_measurement/, examples/) and `02_external_environment/` (regulatory, accounting, and economic context that the bank operates within, including ratings agencies and central banks).

**`docs/wiki/application/banking/01_internal_environment/risk_management/`** — the risk management *process* (appetite, identification, measurement, mitigation) and the supervisory framework that sits on top of it (economic capital, ICAAP, SREP). This is distinct from the `risk_measurement/` folder, which contains quantification methodology for each individual risk type.

**`docs/wiki/application/banking/01_internal_environment/risk_measurement/`** — quantification methodology organised by risk type. Credit risk is by far the deepest. Market, operational, liquidity, IRRBB, climate, stress testing, and other risks each have their own subfolder.

**`docs/wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/`** — the deepest and most developed part of the repo, organised by credit-risk *type* first. Each subdirectory then mirrors a model development lifecycle (introduction → data engineering → portfolio description → feature engineering → modelling → testing → … → monitoring), with `pd/`, `lgd/`, `ead/` (and for IFRS 9, `fli/` and `sicr/`) splits inside the lifecycle stages.

- `a-irb_capital/` — A-IRB regulatory capital modelling end-to-end. Nine lifecycle stages (01_introduction → 09_monitoring) including 07_moc, 08_rwa.
- `application_scoring/` — origination and behavioural scorecard methodology.
- `ifrs9_impairments/` — IFRS 9 ECL modelling. Eight lifecycle stages, with dedicated `fli/` and `sicr/` modules.
- `counterparty_credit_risk/` — counterparty credit risk context and exposures.
- `credit_concentration_risk/` — single-name and sector concentration.

**`docs/wiki/application/banking/01_internal_environment/pricing/`** — bank pricing methodology: pricing framework, fund transfer pricing (FTP), loan pricing, deposit pricing, derivative pricing, DCF model, segmentation. Newer addition since the previous version of this file was written.

**`docs/wiki/fundamentals/`** — domain-agnostic technical skills: software engineering conventions, SQL and data engineering, pandas/polars/visualisation, mathematics, statistics (descriptive, probability, GLMs, time series, survival analysis, Bayesian, Markov chains), machine learning (feature engineering, train/test split, supervised, unsupervised, deep learning, hyperparameter tuning, evaluation, interpretation), a near-empty actuarial science stub, and Power BI.

**`docs/wiki/regulation/`** — regulatory and accounting frameworks organised by jurisdiction. The `international/bis/` and `international/ifrs/` subfolders are substantive, as is `uk/` (for CRR near-final and supervisory statements SS3-24 and SS4-24) and `eu/crr.md`. Most jurisdiction stubs outside BIS/IFRS/UK/EU-CRR are empty placeholders.

**`data/`** — standard data science folder layout (raw, external, interim, processed, predictions, mappings, template, database). Currently empty except for placeholder `.gitkeep` files and a DuckDB WAL file. Not a knowledge base; do not place reference notes here.

**`src/`** — Python source code: config, constants, schema definitions, DQA utilities, and function stubs for the modelling pipeline (data engineering, EDA, feature engineering, train/test split, model estimation, model validation), organised by PD/LGD/EAD. Most function stubs are empty.

---

## 3. F107 syllabus coverage map

The table below maps standard F107 Banking Principles syllabus topics to existing content. Coverage status uses three values: **present** (substantive content exists), **partial** (some content but material gaps), or **absent** (no dedicated content found).

All paths below are relative to `docs/wiki/`.

| F107 syllabus area | Coverage | Primary locations | Notes |
|---|---|---|---|
| **Basel history and architecture** (Basel I → IV, BCBS structure) | Present | `regulation/international/bis/basel_1.md`, `basel_2.md`, `basel_framework.md`, `bis.md` | Strong; Basel IV finalisation captured in framework doc |
| **Pillar 1 — credit risk capital** (standardised, F-IRB, A-IRB, RWA) | Present | `application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/01_introduction/`; `regulation/international/bis/bcbs_d424.md` | Deep A-IRB coverage; standardised approach less developed |
| **Pillar 1 — market risk capital** (VaR, ES, FRTB) | Partial | `application/banking/01_internal_environment/risk_measurement/market_risk/` (3 files: context, models, proprietary trading & XVA) | Overview present; FRTB SBM/IMA detail absent |
| **Pillar 1 — operational risk capital** (BIA, TSA, SMA) | Partial | `application/banking/01_internal_environment/risk_measurement/operational_risk/` (5 files: sources, loss data, capital Basel II, capital NSA, AML/KYC) | BIA/TSA/SMA capital approaches captured; RCSA and scenario analysis detail thinner |
| **Pillar 2 — ICAAP / SREP** | Present | `application/banking/01_internal_environment/risk_management/06-economic_capital.md`, `07-icaap.md`, `08-srep.md` | Both ICAAP and SREP have dedicated files |
| **Pillar 3 — market discipline** | Partial | `application/banking/01_internal_environment/03-capital_management.md` (Pillar 3 referenced in context) | No standalone Pillar 3 disclosure-template file |
| **Capital structure** (CET1, AT1, T2, buffers, leverage ratio) | Present | `application/banking/01_internal_environment/03-capital_management.md`; `regulation/international/bis/basel_framework.md` | Capital ratios and buffers well documented |
| **Resolution — TLAC, MREL, bail-in** | Present | `regulation/international/fsb/tlac.md`, `g_sibs.md`; `regulation/uk/mrel.md` | Solid coverage for a UK/international context |
| **IFRS 9 — ECL framework, staging, SICR** | Present | `regulation/international/ifrs/ifrs9_standard.md`, `ifrs9_staging.md`; `application/banking/01_internal_environment/risk_measurement/credit_risk/ifrs9_impairments/` | Excellent; most developed area alongside A-IRB |
| **Credit risk — PD/LGD/EAD modelling** | Present | `application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/` and `ifrs9_impairments/` (both with pd/, lgd/, ead/ splits) | Deep coverage; PIT vs TTC, LRA, SICR, FLI all present |
| **Counterparty credit risk and concentration** | Partial | `application/banking/01_internal_environment/risk_measurement/credit_risk/counterparty_credit_risk/`, `credit_concentration_risk/` | Context and exposure / concentration types covered; CVA capital and SA-CCR detail thinner |
| **Market risk — trading book, VaR, FRTB** | Partial | `application/banking/01_internal_environment/risk_measurement/market_risk/` | See Pillar 1 market risk row above |
| **Operational risk — taxonomy, scenarios, RCSA** | Partial | `application/banking/01_internal_environment/risk_measurement/operational_risk/` | See Pillar 1 operational risk row above |
| **Liquidity risk — LCR, NSFR, stress testing** | Present | `application/banking/01_internal_environment/risk_measurement/liquidity_risk/` (5 files: short-term metrics, LCR, long-term metrics, NSFR, behavioural modelling); `application/banking/01_internal_environment/04-liquidity_management.md` | LCR/NSFR and behavioural modelling covered; intraday liquidity less developed |
| **Interest rate risk in the banking book (IRRBB)** | Present | `application/banking/01_internal_environment/risk_measurement/interest_rate_risk/` (5 files: context, IRRBB sources, yield curves & benchmarks, NII/NIM, IRRBB measurement) | EVE/NII methodology now covered; BCBS 368 supervisory framework reference could be deeper |
| **Climate risk** | Partial | `application/banking/01_internal_environment/risk_measurement/climate_risk/` (context, modelling approach) | Newer addition not on traditional F107 syllabus; worth knowing as supervisory theme |
| **Bank structure, products, and business model** | Present | `application/banking/01_internal_environment/01-business_model.md` … `06-structure.md` (six overview files); `pricing/07-segmentation.md` | Overview level; detailed product mechanics still light |
| **Ratings agencies and external credit assessment** | Partial | `application/banking/02_external_environment/04-ratings_agencies.md` | Single overview file |
| **Bank pricing and funds transfer pricing** | Present | `application/banking/01_internal_environment/pricing/` (7 files: pricing framework, FTP, loan pricing, DCF model, deposit pricing, derivative pricing, segmentation) | FTP and product-pricing methodology now substantive |
| **Bank strategy, governance, risk appetite** | Present | `application/banking/01_internal_environment/risk_management/01-risk_management.md` through `08-srep.md` (risk management process, appetite, identification, measurement, mitigation, economic capital, ICAAP, SREP); `regulation/international/bis/bcbs_239.md` | Process and supervisory framework covered; board-level governance and three-lines-of-defence detail thinner |
| **Stress testing frameworks** (EBA, BoE, DFAST) | Partial | `application/banking/01_internal_environment/risk_measurement/stress_testing/01-pillar_2b.md` | Only Pillar 2B stub; named jurisdictional programmes (EBA, BoE, DFAST/CCAR) absent |
| **Climate risk and other Pillar 2A risks** | Partial | `application/banking/01_internal_environment/risk_measurement/other_risks/` (pension risk, other Pillar 2A risks) | Pension covered; remaining Pillar 2A risks at overview level |
| **UK and EU regulatory environment** | Partial | `regulation/uk/` (CRR near-final, SS3-24, SS4-24 substantive); `regulation/eu/crr.md` (substantive); EBA, ECB, PRA, FCA stubs empty | UK supervisory expectations strong; EBA/ECB supervisory guidance gaps |
| **South African regulatory environment** | Absent | `regulation/south_africa/` (Banks Act stub only; FSCA, NCA, PA, SARB empty) | Important for ASSA F107 specifically — priority gap |

**Summary of F107 gaps requiring priority attention:**
1. Stress testing frameworks (only Pillar 2B stub; EBA/BoE/DFAST programmes absent)
2. South African regulatory environment (FSCA, PA, SARB, NCA all stubs) — priority for an ASSA exam
3. Pillar 3 disclosure templates (referenced but no dedicated file)
4. FRTB detail within market risk (SBM and IMA approaches)
5. Operational risk depth (RCSA process, scenario analysis methodology)
6. Counterparty credit risk capital approaches (SA-CCR, IMM, CVA capital)
7. Board-level governance and three-lines-of-defence framing

---

## 4. Ingestion priorities and workflow

When new material is provided (PDFs, transcripts, lecture notes, articles), follow this workflow in order.

**Step 1 — Classify by F107 syllabus area first.** Determine which F107 topic the material belongs to before deciding where to place it. Use the coverage map in section 3 as the primary routing guide. Do not default to the nearest existing folder if a more precise syllabus location is appropriate. For absent or partial topics (see the gap summary at the bottom of section 3), create new files in the most logical location within `docs/wiki/application/banking/` or `docs/wiki/regulation/` — do not defer ingestion because no folder exists yet.

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

**Internal links.** Cross-references between files are encouraged. Use relative paths from the current file's location. Example: `[A-IRB introduction](../a-irb_capital/01_introduction/01-context.md)`.

**PDFs.** Many files have a companion `.pdf` with the same stem. Treat the `.md` as the authoritative editable version. The PDF is a static snapshot.

**Naming.** File names use lowercase with hyphens or underscores (existing files mix both styles; match the dominant style within the folder you are working in). Folder names use underscores with a numeric prefix where ordering matters.

---

## 6. Session startup instructions

At the start of every new session in this repository, follow these steps before taking any action:

1. **Read this file (`CLAUDE.md`) in full.** Do not proceed until you have done so.
2. **Check the F107 coverage map** (section 3 above) to understand the current state of the knowledge base.
3. **Confirm the session goal with the user** before writing, editing, or restructuring anything. Ask: what topic or material are we working on today, and what is the desired outcome?

Do not ingest material, restructure folders, or create new files speculatively. Wait for explicit instruction from the user in each session.
