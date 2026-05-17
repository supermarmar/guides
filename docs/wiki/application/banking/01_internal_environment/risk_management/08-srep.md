---
tags:
  - application/banking/internal-environment/risk-management/srep
  - difficulty/unknown
  - study-status/new
aliases:
---
# SREP

The **Supervisory Review and Evaluation Process** (SREP) is the supervisor's structured annual assessment of whether a bank's capital and liquidity are adequate for its risk profile, whether its business model is viable, and whether its governance and internal controls are sound. The output is a single supervisory decision setting the bank's binding capital and liquidity requirements, any required management actions, and the supervisory intensity that follows. The SREP is what the supervisor says back to the bank's [[07-icaap|ICAAP]]: same risk profile, different vantage point, binding consequences.

SREP sits inside Pillar 2 of the Basel framework. Pillar 1 is the prescribed regulatory floor; Pillar 2 is the supervisor's discretion to require more, and SREP is the process by which that discretion is exercised. The regulatory anchor is Articles 97 to 101 of CRD V in the EU, the equivalent rules in the PRA rulebook in the UK, the SARB's Regulations relating to Banks in South Africa, and the Federal Reserve's supervisory programme (LISCC, CCAR, the Capital Plan Rule) in the United States. The standard methodology is set out in the EBA's Guidelines on common procedures and methodologies for SREP, revised in 2022, which most European supervisors apply directly and most non-European supervisors take as a reference.

SREP differs from ICAAP in three important ways. First, **the supervisor owns it**, not the bank. The supervisor sets the methodology, the scoring, the benchmarks, and the conclusions. Second, **the output is binding**. The Total SREP Capital Requirement is enforceable, breach triggers prompt corrective action, and the Pillar 2 Requirement that comes out of the SREP cannot be negotiated away after the fact. Third, **the scope is broader than capital**. SREP assesses the business model, the governance and controls, the risks to capital, and the risks to liquidity, and the supervisor can act on any of the four through capital add-ons, liquidity requirements, or qualitative measures.

## The four-element supervisory assessment

The EBA SREP framework structures the assessment around four elements. Each element is scored on a one-to-four scale, where one is the strongest and four is the weakest. The four element scores combine into an **overall SREP score**, which determines the supervisor's overall view of the bank and the intensity of the supervisory engagement that follows.

**Business model analysis** assesses the viability and sustainability of the bank's business model. The supervisor looks at the profit and loss trajectory, the strategic plan, the competitive position, the cost-to-income ratio, and the ability of the business model to generate adequate returns through a cycle. A business model that does not earn its cost of capital, or that depends on conditions that are no longer present, scores poorly regardless of the bank's current capital position.

**Governance and internal control assessment** covers the board's effectiveness, the three-lines-of-defence operation, the risk and compliance frameworks, the data quality (BCBS 239), the risk culture, the remuneration framework, and the bank's ability to identify, measure, and manage risks. This is the element where the [[07-icaap|ICAAP]] governance chapter is most directly tested.

**Risks to capital** covers credit, market, operational, IRRBB, and any other risk material to the bank's capital position. Each risk is scored individually and the supervisor's overall view feeds the capital requirement. This is the element where the ICAAP's MIRA and capital assessment are most directly tested.

**Risks to liquidity and funding** covers the bank's short-term liquidity (LCR, intraday), structural funding (NSFR), funding diversification, and the resilience of the funding profile under stress. This is the element where the [[../../../../regulation/uk/pra|ILAAP]] is most directly tested.

## The SREP scoring scale

Each element is scored on the same four-point scale, and the same scale applies to individual risks within an element.

| Score | Meaning | Supervisory consequence |
|---|---|---|
| 1 | Low risk to the bank's viability | Standard supervisory engagement, lighter touch |
| 2 | Medium-low risk | Standard engagement with focused attention on weaker areas |
| 3 | Medium-high risk | Heightened supervisory attention, more frequent reporting and on-site inspections |
| 4 | High risk to viability | Continuous, intensive supervision; potential early intervention measures |

The overall SREP score is not a simple average of the four elements. It is a holistic supervisory judgement, weighted toward the weakest element, because a bank with strong capital but weak governance is in a different position from one with the same capital and strong governance. The score is communicated to the bank in the SREP decision letter and is a confidential supervisory output; banks do not publish their SREP scores, though analysts can sometimes infer them from disclosed capital requirements.

## Capital outcomes: P2R, P2G, TSCR, and OCR

The capital arm of the SREP decision produces two numbers. The **Pillar 2 Requirement** (P2R) is a binding additional capital requirement on top of Pillar 1, set to cover risks not adequately captured by Pillar 1 or by the bank's own risk management. P2R is the formal successor to the UK's old "Pillar 2A" and is met predominantly with CET1. The **Pillar 2 Guidance** (P2G) is a non-binding supervisory expectation, set on top of the combined buffer requirement, to ensure the bank can withstand a severe but plausible stress without breaching its binding requirements. P2G is the successor to the UK's old "Pillar 2B" or "capital planning buffer" and is met with CET1.

The four standard composite numbers that emerge from the SREP decision:

| Composite | Definition | Function |
|---|---|---|
| TSCR | Total SREP Capital Requirement = Pillar 1 + P2R | Binding minimum; breach triggers prompt corrective action |
| OCR | Overall Capital Requirement = TSCR + Combined Buffer Requirement | The MDA threshold; breach triggers automatic distribution restrictions |
| OCR + P2G | OCR plus Pillar 2 Guidance | Supervisory expectation; non-binding but operates as a soft trigger for heightened supervision |
| Available CET1 | What the bank actually holds | Must sit comfortably above OCR + P2G in normal conditions |

The mechanical difference between P2R and P2G is critical. **P2R breach** means the bank has fallen below the binding minimum, the supervisor is empowered to take prompt corrective action, and the bank is in a regulatory non-compliance position. **P2G breach** means the bank has fallen into the supervisor's expected stress buffer; the bank is not in non-compliance, but the supervisor will demand a credible remediation plan, may restrict capital distributions informally, and will increase supervisory engagement. The Maximum Distributable Amount mechanism is triggered when CET1 falls below the OCR (i.e., into the combined buffer requirement), not by P2G breach.

## The supervisory toolbox

Beyond capital and liquidity requirements, the SREP decision can impose a wider menu of measures. The EBA SREP guidelines list four categories.

**Capital measures.** The headline P2R and P2G outputs are the standard capital tools. The supervisor can also require capital of higher quality than the minimum (more CET1 than the floor), restrict distributions even in the absence of an MDA trigger, or require capital additions for specific identified risks (a "macroprudential overlay" linked to systemic risk).

**Liquidity measures.** Higher LCR or NSFR requirements specific to the bank, restrictions on funding mix, requirements to hold additional High-Quality Liquid Assets, and limits on intraday liquidity reliance.

**Other supervisory measures.** Requirements to strengthen governance, change board composition, replace senior management, address remuneration practices, improve data quality, remediate model weaknesses, divest specific business lines, or limit growth in particular portfolios. The supervisor has broad discretion in this category and uses it for governance and business-model weaknesses that capital alone cannot remediate.

**Early intervention measures.** Where the bank is approaching the conditions for resolution, the supervisor can require the activation of recovery plan actions, the appointment of a temporary administrator, or the preparation for resolution. These are the most severe tools and are rarely used; their existence is the credible threat that backs the rest of the SREP decision.

## SREP frequency and proportionality

SREP frequency scales with the bank's size and complexity, under the EBA's four supervisory categories. Category 1 banks (large, complex, internationally active, including all G-SIIs and O-SIIs) receive an annual SREP with continuous supervisory engagement, regular on-site inspections, and a comprehensive review of every element. Category 4 banks (small, domestic, simple) receive a SREP on a three-year cycle with a lighter methodology. The intermediate categories sit between these poles. The methodology is the same; the depth, frequency, and supervisory resource are not.

The proportionality principle is itself a SREP output: a bank's category can change based on the SREP score, growth, business-model changes, or systemic relevance. Movement from category 3 to category 2 typically follows a substantial growth in size or complexity; movement from category 2 to category 1 follows designation as a systemic institution. The supervisor reviews the category annually.

## Joint decisions for cross-border banks

For cross-border banking groups, the consolidating supervisor coordinates a **joint decision** with the host supervisors of material subsidiaries. The joint decision covers the capital and liquidity requirements at both the consolidated level and the level of each material subsidiary, and it has to be reached within four months of the consolidated SREP decision. Where the supervisors cannot agree, the EBA mediates and can impose a binding decision. The framework is set out in Article 113 of CRD V and the related EBA Implementing Technical Standards.

The joint decision is one of the most complex parts of the SREP machinery because each host supervisor has its own view of subsidiary-level capital adequacy, and the home-host tension can be material. The standard friction points are the allocation of capital between consolidated and subsidiary levels, the treatment of intragroup exposures, and the host supervisor's right to ring-fence local capital and liquidity. A bank that anticipates these tensions and engages early with host supervisors runs a faster joint decision.

## Dialogue, evidence, and the SREP cycle

The SREP is not a single event; it is a year-round dialogue that culminates in the formal decision. The supervisor reads the ICAAP, attends board meetings, conducts on-site inspections, reviews regulatory returns, benchmarks the bank against peers, and tracks the bank's actual capital and risk metrics throughout the year. The annual SREP decision is the formal output of this continuous engagement, not a standalone review.

The supervisor's evidence base includes the ICAAP submission, the ILAAP submission, the recovery plan, the regulatory returns (FINREP, COREP), the bank's audited financial statements, board minutes, internal audit reports, the bank's own model validation outputs, and any specific reports requested through ad-hoc supervisory requests. The strongest banks make this evidence base coherent: the same numbers appear in the same places, the same scenarios drive ICAAP and ILAAP, and the same management actions appear in the recovery plan and the capital contingency plan.

## Comparison with related frameworks

The SREP has analogues in other jurisdictions. The Federal Reserve's **Comprehensive Capital Analysis and Review** (CCAR) for large US banks is similar in scope but with a more prescribed stress-test scenario set, run annually by the Fed itself rather than by the bank. The **Dodd-Frank Act Stress Test** (DFAST) is the public-facing element of CCAR. The Bank of England's **Annual Cyclical Scenario** (ACS) plays an equivalent role in the UK SREP for the largest banks, alongside the bank's own internal stress tests. South Africa's SARB applies the SREP framework via Banks Act Directives and produces an Individual Capital Requirement equivalent to the P2R.

The convergence is real but not complete. EBA SREP is the most structured framework, with explicit scoring and a published methodology. CCAR is the most prescriptive, with a single supervisory scenario applied uniformly. The UK PRA approach sits between the two, with a published methodology but more supervisory discretion than the EBA template. The South African approach is closer to the EBA template, applied with national-banking-system overlays.

## Outcomes and remediation

The SREP decision letter typically contains four sections. **Quantitative outcomes** set the P2R, P2G, any liquidity requirements, and any other quantitative measures. **Qualitative findings** describe weaknesses identified in business model, governance, capital, or liquidity, each with a severity rating and a remediation deadline. **Required actions** are the specific things the bank must do, with named ownership and deadlines. **Areas for management attention** are the lighter-touch issues that the supervisor expects to see addressed in the next ICAAP but that do not require immediate remediation.

Findings and required actions feed directly into the bank's next ICAAP. A bank that ignores a SREP finding and submits an ICAAP that does not address it will have the finding re-issued, often with an escalated severity, and the supervisor's view of governance will deteriorate accordingly. The discipline runs in both directions: the supervisor follows up on findings between SREPs and reads each follow-up as a signal about the bank's responsiveness.
