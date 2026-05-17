---
tags:
  - application/banking/internal-environment/risk-management/icaap
  - difficulty/unknown
  - study-status/new
aliases:
---
# ICAAP

The **Internal Capital Adequacy Assessment Process** (ICAAP) is a bank's comprehensive written self-assessment of whether its capital is adequate for its risk profile, both at the current reporting date and over a forward-looking planning horizon. It is owned by the board, produced annually, reviewed at least quarterly, and submitted to the supervisor as the primary input to the [[08-srep|SREP]]. The ICAAP is what the bank says about itself. The SREP is what the supervisor says back.

The regulatory anchor for ICAAP is Article 73 of CRD V in the EU and the equivalent rule in the PRA rulebook in the UK, supplemented by the EBA Guidelines on ICAAP and ILAAP information (2016) and the Basel Pillar 2 framework. The PRA's SS31/15 sets the UK supervisory expectations. The same principle exists in the US under the Capital Plan Rule for large banks and in South Africa under the SARB's Regulations relating to Banks. The language and depth vary; the structure does not.

The ICAAP has eight chapters in the standard EBA template: business model and strategy, risk appetite, governance, risk identification (MIRA), capital assessment (current and forward-looking), capital planning, linkage to ILAAP and recovery, and an executive summary that explicitly states the board's conclusion on capital adequacy. The eight chapters answer eight different questions, and a chapter that has been written generically rather than to a specific question fails the test.

## Business model and strategy

The first chapter describes what the bank does, how it makes money, where it is heading, and what its strategic vulnerabilities are. This matters because the business model determines the risk profile. A bank growing its wholesale book aggressively is taking on different and larger risks than one running off legacy retail exposures. A bank pivoting to digital channels is taking on operational and conduct risk that did not exist on its previous balance sheet. The ICAAP cannot identify the right risks until it is clear what the business actually is, and the supervisor reads this chapter first because everything that follows has to be consistent with it.

The chapter typically covers product lines and customer segments, geographic and legal-entity footprint, revenue and cost composition, key strategic initiatives, and the three- to five-year financial plan. The depth is proportional to the bank's complexity: a domestic retail bank can describe its business model in five pages, a universal bank cannot.

## Risk appetite

The bank articulates its **risk appetite**, the level and types of risk it is willing to accept in pursuit of its strategy, and shows that the appetite is formally approved by the board, embedded in limits, and monitored consistently. The ICAAP demonstrates that capital planning flows from the risk appetite, not the other way around: the bank does not first decide how much capital it wants to hold and then construct an appetite to fit, it decides what risk profile it wants and then sizes capital accordingly. See [[02-risk_appetite|risk appetite]] for the underlying framework.

The chapter has to reconcile three things: the high-level appetite statement, the cascade of limits derived from it, and the actual exposure metrics on the management dashboard. A supervisor will look for a clean chain from board-approved appetite to operational limit to live metric, and will challenge any link that is missing or unclear.

## Governance and the three lines of defence

The governance chapter describes how the ICAAP is produced, challenged, and approved. Board and executive ownership has to be visible: the chair of the risk committee, the CRO, the CFO, and the CEO all have named responsibilities, and the board's role is described in terms of the specific decisions it makes rather than in generic stewardship language. The three lines of defence operate inside the ICAAP itself: the business and finance functions produce the inputs (first line), the risk function challenges the methodology and the conclusions (second line), and internal audit reviews the process and the controls (third line). Model validation is named explicitly, with a clear separation from model development.

Regulators pay close attention to this chapter. A technically sophisticated ICAAP produced by a back-office team and rubber-stamped by the board is treated very differently from one with genuine senior engagement, even when the numbers are identical. The board's challenge of the ICAAP, captured in minutes and reflected in revisions to the document, is one of the most informative pieces of evidence available to the supervisor.

## Risk identification: the MIRA

The **Material Identification of Risk Assessment** (MIRA) is the cornerstone of the ICAAP. The bank identifies all material risks it faces and assesses the materiality of each. The assessment covers the full risk universe, not just Pillar 1, and includes at minimum:

- Credit risk, broken down by retail, SME, corporate, and sovereign segments
- Market risk on trading-book positions
- Operational risk, including conduct, cyber, and IT risks
- IRRBB
- Credit concentration risk (single-name, sector, geographic, product)
- Liquidity and funding risk (cross-referenced to the ILAAP)
- Pension risk, where a defined benefit scheme exists
- Reputational and strategic risk
- Model risk
- Residual risk where credit risk mitigation may not perform as expected
- Climate-related financial risk, increasingly treated as a stand-alone material category

Risks assessed as immaterial are documented and justified. The standard supervisory challenge is the omission test: what risks does the bank not consider material, and would a peer institution agree? An ICAAP that simply does not mention a risk that the supervisor considers material is the most common ground for a formal finding.

The MIRA also identifies which risks are captured in Pillar 1, which need a Pillar 2A add-on, and which are captured through stress testing or through scenario-based qualitative assessment. The output is a register of material risks, each with an owner, a measurement methodology, and a capital approach.

## Capital assessment: the current view

The capital assessment has two parts: the current view (what capital is needed today for the bank's risk profile) and the forward-looking view (what capital is needed under stress). Both are required, and the standard regulatory diagram looks like this:

```
ICAAP
├── Current view
│     ├── Pillar 1: prescribed regulatory capital
│     └── Pillar 2A: add-ons for risks not captured in Pillar 1
└── Forward-looking view
      └── Pillar 2B: capital planning buffer for severe scenarios
```

### Pillar 1: the regulatory floor

A summary of the minimum regulatory capital requirements under credit, market, and operational risk: the starting point for the capital adequacy assessment. The chapter describes the methodology in use (standardised or internal-models-based), the RWA composition, and the resulting Pillar 1 capital number broken down by risk type and by business unit.

### Pillar 2A: economic capital for unmodelled and undermodelled risks

For each material risk not captured (or undercaptured) in Pillar 1, the bank quantifies the additional capital required. This is where the [[06-economic_capital|economic capital]] framework provides its core output. Each risk needs a methodology, an assumption set, and a capital number.

- **IRRBB**: EVE and NII sensitivity to prescribed and bank-defined rate shocks, with capital sized to cover the EVE loss under a severe shift. See [[05-irrbb_measurement|IRRBB measurement]].
- **Credit concentration**: a granularity adjustment or single-name concentration add-on above what the ASRF formula captures.
- **Pension risk**: sensitivity of the defined benefit deficit to asset and liability assumptions, with capital to cover a stressed deficit.
- **Operational risk top-up**: where the bank believes its Pillar 1 op-risk charge undercaptures its true exposure (known litigation, cyber, or conduct), an add-on is quantified through scenario analysis and loss-distribution modelling.
- **Model risk overlay**: an add-on for material model risk identified through the validation function and not otherwise addressed.

The sum of these add-ons, after the bank's own view on diversification, is its Pillar 2A estimate. This is the number the supervisor reviews and may adjust upward or downward in the SREP. Most banks use through-the-cycle PDs and downturn LGDs for the Pillar 2A layer, because using point-in-time inputs here creates procyclicality in the binding capital requirement, which is exactly what Basel was designed to dampen.

### The two views: regulatory and internal

The ICAAP is not forced to choose between regulatory and internal economic capital. It presents both, with a reconciliation between them, because they serve different purposes. The **regulatory view** (Pillar 1 plus Pillar 2A) is what the supervisor acts on and sets the binding capital requirement through SREP. It uses Basel's prescribed assumptions: TTC PDs, downturn LGDs, 99.9% confidence, no cross-risk diversification.

The **internal view** is the bank's own best estimate of its true capital need: point-in-time assumptions, a confidence level tied to the target credit rating (often 99.95%), full portfolio simulation, and cross-risk diversification. It is a management tool used for pricing, RAROC, and strategic capital allocation. It informs the Pillar 2A submission but does not directly determine it.

In practice, the ICAAP contains a reconciliation table showing why the two numbers differ and which direction they diverge. The direction itself is informative. A bank whose internal view is materially lower than the regulatory view typically claims a large diversification benefit or uses point-in-time inputs that flatter a benign cyclical position; the supervisor will probe both. A bank whose internal view is materially higher is signalling that its own assessment of risk exceeds the regulatory floor, which is an honest position but invites the question of why Pillar 2A is not set higher.

The Pillar 2A number the bank submits is typically derived from its EC methodology applied to the Pillar 2A risk types, but using assumptions the supervisor finds defensible (often closer to downturn / TTC than pure PIT). The supervisor benchmarks these against peers and may adjust upward. The full internal economic capital number with diversification and PIT inputs is presented separately, and the supervisor does not simply accept the diversification benefit at face value: the correlation matrix is scrutinised line by line.

## Capital assessment: the forward-looking view

The forward-looking assessment, often called Pillar 2B or the **Capital Planning Buffer**, asks how capital holds up under adverse conditions over the planning horizon. The bank designs and runs a suite of stress tests:

- A **baseline scenario** built on management's central economic forecast.
- An **adverse scenario** that is plausible but severe: a sharp recession, a property price correction, a rate spike, a sovereign downgrade, a geopolitical shock.
- A **severe scenario** representing a more extreme tail event, typically calibrated to one-in-twenty-five or one-in-fifty-year severity.
- A **reverse stress test** working backwards from the point of non-viability to identify what combination of events would break the bank.

For each scenario, the bank projects its income statement, credit losses (using point-in-time stressed PDs and LGDs), IRRBB impacts, RWA evolution, and resulting capital ratios over the planning horizon. The Pillar 2B buffer is sized as the maximum capital shortfall observed across scenarios: the amount of additional capital needed so the bank stays above the Pillar 1 plus Pillar 2A minimum throughout the stress.

The qualitative side of the forward-looking assessment is equally important. The bank has to assess its ability to absorb losses under each scenario, identify management actions available before the stress materialises, and document the assumed effectiveness of each action. See [[01-pillar_2b|Pillar 2B]] for the underlying methodology and supervisory expectations.

## Capital planning

The capital planning chapter presents a forward-looking projection, typically three to five years, showing how capital requirements and available capital evolve under the baseline and stress scenarios. The chapter includes planned capital actions (retained earnings, dividend policy, potential issuance, share buy-backs), and demonstrates that the bank can maintain adequate capitalisation through its strategic plan.

The chapter also contains the **capital contingency plan**: what management actions are available if capital falls toward trigger levels. The standard menu is dividend suspension, AT1 coupon deferral, RWA reduction through portfolio sales or origination slowdown, cost cuts, asset disposals, and capital raising. Each action is documented with an expected capital impact, an execution timeline, and a description of the conditions under which it would be invoked. A supervisor reviewing the contingency plan looks for two things: that the actions are realistic (a bank claiming it can raise R5bn of equity in a stressed market when no such issuance has happened in years is not realistic) and that the triggers are unambiguous.

## Linkage to ILAAP and the recovery plan

The ICAAP cross-references the **Internal Liquidity Adequacy Assessment Process** (ILAAP) and demonstrates that capital and liquidity planning are consistent. A stress that depletes capital often creates liquidity pressure, and the two cannot be managed in isolation. The standard test is that the adverse scenario used in the ICAAP capital projection produces a liquidity profile in the ILAAP that is internally consistent: same macro assumptions, same balance-sheet response, same management actions.

The ICAAP also links to the **recovery plan**, which sets out the actions the bank would take if it crossed defined recovery indicators. Some recovery actions appear in the ICAAP's capital contingency plan, but the recovery plan goes further: it covers governance under stress, communications with stakeholders, the role of resolution authorities, and the bank's path to a credible going-concern position. The capital contingency plan operates within the recovery plan's framework but at an earlier, less severe trigger.

## What the supervisor does with the ICAAP

The ICAAP feeds directly into the [[08-srep|SREP]]. The supervisor reviews each chapter, challenges the risk identification, benchmarks the EC methodologies against peers, and stress-tests the stress tests. The output is the **Supervisory Examination and Evaluation Process decision**, which sets the bank's Total Capital Requirement. The TCR may accept, reduce, or increase the bank's own Pillar 2A estimates, and it sets supervisory expectations for the Pillar 2B buffer and any specific management actions the bank is required to take.

The supervisor's review focuses on a recurring set of weaknesses: weak risk identification (omitted risk types, generic materiality assessments), unrealistic stress scenarios (severity too low, narrative inconsistent with macro plausibility), unreconciled internal versus regulatory views (large diversification benefits that move with the convenience of the conclusion), thin board challenge (minutes that record approval but no debate), and inconsistency between the ICAAP and the ILAAP. A bank that addresses these in advance, with explicit documentation of how each potential weakness has been mitigated, runs a faster and less expensive SREP.

## Proportionality

ICAAP requirements scale with the bank. The EBA SREP guidelines categorise banks into four supervisory categories (1 to 4), with category 1 being the largest and most complex, and category 4 being small domestic banks with simple business models. The methodology depth, the scenario severity, the frequency of update, and the supervisory dialogue all scale accordingly. A category 1 bank's ICAAP runs into hundreds of pages and is reviewed continuously; a category 4 bank's ICAAP is shorter and reviewed on a multi-year cycle. The substance of the framework is the same; the depth is not.
