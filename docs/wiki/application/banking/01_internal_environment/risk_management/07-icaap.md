# ICAAP

The ICAAP is a bank's comprehensive written self-assessment of whether its capital is adequate for its risk profile, now and over a forward-looking planning horizon. It is submitted annually to the regulator as the primary input to the SREP.

## Business Model and Strategy

The ICAAP opens with a description of what the bank does, how it makes money, and where it is heading. This matters because the business model determines the risk profile — a bank growing its wholesale book aggressively is taking on different and larger risks than one running off legacy retail exposures.

## Risk Appetite Framework

The bank must articulate its **risk appetite** — the level and types of risk it is willing to accept in pursuit of its strategy — and show that this appetite is formally approved by the Board, embedded in limits, and monitored consistently. The ICAAP should demonstrate that capital planning flows from the risk appetite, not the other way around.

## Governance and Risk Management

A section on the governance structure supporting the ICAAP: Board and executive ownership, the three lines of defence, model validation arrangements, and the process by which the ICAAP itself is produced, challenged, and approved. Regulators pay close attention to this — a technically sophisticated ICAAP that was produced by a back-office team and rubber-stamped by the Board will be treated very differently from one with genuine senior engagement.

## Risk Identification (MIRA)

The bank must identify **all material risks** it faces and assess the materiality of each (MIRA). This is not limited to Pillar 1 risks. 

- Credit risk (including retail and wholesale sub-segments)
- Market risk (trading book)
- Operational risk
- IRRBB
- Credit concentration risk (name, sector, geographic)
- Liquidity and funding risk
- Pension risk (if a defined benefit scheme exists)
- Reputational and strategic risk
- Model risk
- Residual risk (e.g. credit risk mitigation that doesn't perform as expected)

Risks assessed as immaterial must be documented and justified — regulators will challenge omissions.

## Capital Assessment

The key components required in an ICAAP include the following two types of capital assessment:

1. **Current Capital Assessment**: Evaluation of capital at the current reporting date.
   - Pillar 1: 8% of RWA of credit, market, and operational risks.
   - Pillar 2A: additional capital requirements for risks not captured in Pillar 1 (e.g. [[02-irrbb_sources|Interest Rate Risk in the Banking Book]] ([[05-irrbb_measurement|IRRBB]]), Pension Risk and Credit Concentration Risk).
1. **Forward-Looking Assessment ([[01-pillar_2b|Stress Testing]])**: Evaluating capital sufficiency under adverse scenarios.
   - Quantitative: Applying specific stress scenarios.
   - Qualitative: Assessing the bank's ability to absorb losses and identifying mitigation steps.
   - [[01-pillar_2b|Pillar 2B]] (Capital Planning Buffer (CPB)): A buffer set to the level of additional capital required in a downturn to ensure the bank remains in surplus. This buffer is drawn upon when there is a downturn in the [[03-economic_envrionment|economic environment]] and adverse circumstances appear in the economic cycle.

```
ICAAP
├── Risk identification & quantification  → feeds P2A / P2R
│     (concentration, IRRBB, op risk, etc.)
└── Stress testing (base / adverse / severe) → feeds P2B / P2G
      (capital adequacy under forward scenarios)
```

### Current Assessment 

#### Pillar 1: Regulatory Capital

A summary of the minimum regulatory capital requirements under credit, market, and operational risk — the starting point for the capital adequacy assessment. 
#### Pillar 2A: Economic Capital for Unmodelled Risks

For each material risk not captured (or undercaptured) in Pillar 1, the bank quantifies the additional capital required. This is the economic capital assessment, and it is the analytical core of the ICAAP. Each risk needs a methodology, assumptions, and a capital number:

- **IRRBB:** EVE and NII sensitivity to prescribed and bank-defined rate shocks; capital sized to cover the EVE loss under a severe shift.
- **Credit concentration:** Granularity adjustment or single-name concentration add-on above what the ASRF model already captures.
- **Pension risk:** Sensitivity of the defined benefit deficit to asset/liability assumptions; capital to cover a stressed deficit.
- **Operational risk top-up:** If the bank believes its Pillar 1 op risk charge undercaptures its true exposure (e.g. due to known litigation or cyber risk), an add-on is quantified.

The sum of these add-ons, after the bank's own view on diversification, is its P2A estimate — the number the regulator will review and may adjust upward or downward in the SREP.

Using TTC parameters here keeps the comparison consistent — you're measuring the gap between your internal view and Pillar 1 on the same basis. Most banks use TTC PDs and downturn LGDs for this layer. You do not want your core capital requirement to balloon in the middle of a crisis — that is the procyclicality trap Basel was designed to avoid.

#### Internal View of Economic Capital

The ICAAP is not forced to choose one or the other. It must present **both** views, with a reconciliation between them, because they serve different purposes:

**The regulatory view (P1 + P2A)** is what the regulator acts on — it sets the binding capital requirement through the SREP. P1 uses Basel's prescribed assumptions (TTC PDs, downturn LGDs, 99.9% confidence, no cross-risk diversification). P2A adds the risks Basel omits (IRRBB, concentration, pension). The regulator uses this as the floor the bank cannot breach.

The internal view is the bank's own best estimate of true capital need — PIT assumptions, 99.95% confidence, full portfolio simulation, cross-risk diversification. This is a management tool used for pricing, performance measurement (RAROC), and strategic capital allocation. It informs the P2A submission but does not directly determine it.

In practice, the ICAAP will contain a **reconciliation table** showing why these numbers differ and which direction they diverge — because the direction itself is informative.

The P2A number the bank submits to the regulator is typically derived from its EC methodology applied to the P2A risk types — but using assumptions the regulator will find defensible (often closer to downturn/TTC than pure PIT). The regulator will benchmark these against peers and may adjust them upward. The full EC number with diversification and PIT inputs is presented as the internal view, but the regulator does **not** simply accept the diversification benefit at face value — they will scrutinise the correlation assumptions carefully.

### Forward-Looking Assessment

An important step in the process is [[01-pillar_2b|stress testing]], where the required capital is assessed under stressed conditions to determine if the amount is sufficient ([[01-pillar_2b|Pillar 2B]]). These stress tests require both quantitative and qualitative elements. Quantitative elements include identifying and applying stress scenarios. Qualitative elements include assessing the ability of the bank to absorb losses under these scenarios and determining steps that should be taken to mitigate these risk scenarios. The ICAAP process also includes assessing the correlations between risk types, as when risk is being assessed on an aggregate level, certain risks will be correlated and there may be a "diversification benefit".
#### Pillar 2B: Stressed P1 + P2A

The bank designs and runs a suite of stress tests to assess how capital holds up under adverse conditions:

- **Baseline scenario:** Management's central economic forecast.
- **Adverse scenario:** A plausible but severe downside (e.g. a sharp recession, property price correction, rate spike).
- **Severe scenario:** A more extreme tail event.
- **Reverse stress test:** Working backwards from the point of non-viability to identify what combination of events would break the bank.

For each scenario the bank projects its income statement, credit losses (using PIT stressed PDs and LGDs), IRRBB impacts, RWA evolution, and resulting capital ratios over the planning horizon. The **P2B buffer** is sized as the maximum capital shortfall observed across scenarios — the amount of additional capital needed so the bank stays above P1+P2A minimums throughout the stress.

---

## Capital Adequacy

Having assembled Pillar 1, P2A, and P2B estimates, the bank presents its **total capital requirement** and compares it to **available capital** (CET1, Additional Tier 1, Tier 2). The resulting headroom — or deficit — drives the capital plan. The bank must also show that its capital composition is appropriate: holding the P2A requirement predominantly in CET1, for example, rather than lower-quality Tier 2 instruments.

---

## Capital Planning

A forward-looking projection (typically 3–5 years) showing how capital requirements and available capital evolve under the baseline and stress scenarios. This includes planned capital actions — retained earnings, dividend policy, potential issuance — and demonstrates that the bank can maintain adequate capitalisation through its strategic plan. A **capital contingency plan** should also be included: what management actions are available if capital falls toward trigger levels (dividend suspension, RWA reduction, asset sales, capital raising).

---

## Linkage to ILAAP

The ICAAP should cross-reference the **ILAAP** (Internal Liquidity Adequacy Assessment Process) and demonstrate that capital and liquidity planning are consistent — a stress that depletes capital often also creates liquidity pressure, and the two cannot be managed in isolation.

---

## What the Regulator Does With It

The ICAAP feeds directly into the SREP. The supervisor reviews each section, challenges the risk identification, benchmarks the EC methodologies against peers, and stress-tests the stress tests. The output is a SREP decision setting the bank's total capital requirement — which may accept, reduce, or increase the bank's own P2A estimates, and sets the supervisory expectation for P2B.
