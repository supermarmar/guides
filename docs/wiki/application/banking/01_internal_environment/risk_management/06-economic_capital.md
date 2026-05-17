---
tags:
  - application/banking/internal-environment/risk-management/economic-capital
  - difficulty/unknown
  - study-status/new
aliases:
---
# Economic capital

**Economic capital** is the amount of capital a bank estimates it needs to remain solvent over a one-year horizon at a confidence level linked to its target credit rating, covering all material risks, using the bank's own models and current (point-in-time) inputs, and recognising portfolio diversification across risk types. It is the bank's own answer to the question "how much capital do we really need?", as distinct from "how much capital does the regulator say we must hold?". The two answers do not coincide, and the gap is where this file lives.

Four words in that definition do most of the work. **Target credit rating** sets the confidence level: a bank aiming at an A rating, with an implied one-year default probability around 0.1%, calibrates economic capital at 99.9%; a AA bank, at around 0.03%, calibrates at 99.97%. The confidence level is a strategic choice, not a regulatory prescription. **All material risks** means everything the bank considers significant, not only the Pillar 1 trio: IRRBB, credit concentration, pension, business risk, model risk, and anything else surfaced by [[03-risk_identification|risk identification]]. **PIT inputs** mean that economic capital is a current view of risk, not a through-cycle average: it answers "how much capital do we need today?" rather than "on average across a cycle?". **Diversification** means recognising that credit losses, market losses, and operational losses do not all peak at the same time, which Pillar 1 ignores and economic capital does not.

Economic capital is therefore a management tool first, and only a regulatory input second. It drives the [[07-icaap|ICAAP]] submission, sets internal capital allocation across business units, anchors risk-adjusted performance measurement (RAROC), and feeds the [[02-risk_appetite|risk appetite]] statement's solvency limits. It is not a regulatory minimum, and a bank that has high economic capital but fails its Pillar 1 ratio is still in breach. The two ratios sit in parallel: regulatory capital is the floor, economic capital is the bank's own view, and the [[08-srep|SREP]] dialogue is where the gap between the two is negotiated.

## The link to Pillar 1

Pillar 1 sets the minimum regulatory floor and covers three prescribed risk types. **Credit risk** captures default losses on loans and exposures, **market risk** captures losses from trading-book positions, and **operational risk** captures losses from failed processes, systems, or external events. The illustrative numbers for a stylised bank "BankBSM" are below; the absolute values are illustrative, the relationships are not.

| Risk type | RWA | Capital at 8% |
|---|---|---|
| Credit risk | R10bn | R800m |
| Market risk | R2bn | R160m |
| Operational risk | R1bn | R80m |
| **Total Pillar 1** | **R13bn** | **R1,040m** |

This is the regulatory minimum: necessary but not sufficient. It deliberately excludes IRRBB, concentration risk, pension risk, business or strategic risk, and the wider tail of management-identified risks. Economic capital fills the gap, and does so with bank-specific methodology rather than a one-size formula.

### Credit risk under economic capital

The Pillar 1 [[01-context|IRB formula]] is hardcoded to 99.9% confidence: the Vasicek quantile G(0.999) is baked into the formula. For economic capital at a higher confidence level the bank substitutes G(0.9995), producing a higher conditional PD and therefore higher capital per exposure. Three other changes are typically made at the same time. First, **point-in-time PDs** replace through-the-cycle PDs, because economic capital is a forward-looking management view rather than a through-cycle regulatory floor. Second, **full portfolio simulation** (Monte Carlo over a multi-factor structural or factor model) replaces the analytical ASRF formula, which allows the bank to model actual name concentrations and sector correlations rather than assuming a single systematic factor. Third, **diversification within the credit portfolio** is captured explicitly, which the portfolio-invariant ASRF formula by design ignores.

### Market risk under economic capital

Under FRTB, regulatory market risk uses 97.5% expected shortfall over liquidity-adjusted horizons ranging from 10 to 250 days. For economic capital, the bank recalculates using its chosen confidence level (here 99.95%) and typically a one-year time horizon to match the wider economic capital framework. This usually produces a materially larger capital figure than the regulatory number, particularly for illiquid positions where the one-year horizon captures far more potential loss than the regulatory liquidity-adjusted horizon. See [[02-models|market risk models]] for the underlying VaR / ES treatment.

### Operational risk under economic capital

Regulatory operational risk under the standardised measurement approach is formula-driven and does not use an explicit VaR confidence level. For economic capital, banks often use a **loss-distribution approach**, fitting frequency and severity distributions to internal and external loss data, and read off the chosen percentile directly. The result is more tailored than the regulatory number but is highly sensitive to tail assumptions, particularly where the bank has thin internal loss data and relies heavily on external consortium data and expert scenarios.

### IRRBB and other risks

IRRBB is not in Pillar 1. Economic capital captures it through an EVE sensitivity at the chosen confidence level, typically using interest-rate shocks of a magnitude and direction calibrated to the bank's balance sheet. Concentration risk, pension risk, and business risk follow similar logic: each is modelled in a way that fits its data and supervisory expectations, then added to the cross-risk aggregation step. See [[05-irrbb_measurement|IRRBB measurement]] for the underlying EVE / EaR treatment.

The illustrative economic capital build for BankBSM:

| Risk type | EC at 99.95% |
|---|---|
| Credit risk | R900m |
| Market risk | R200m |
| Operational risk | R80m |
| IRRBB | R200m |
| Credit concentration | R150m |
| Pension risk | R50m |
| Business / strategic risk | R100m |
| **Gross sum** | **R1,680m** |

The R1,680m number is the bank's gross sum across risk types before any diversification benefit. It is materially above the R1,040m Pillar 1 floor, and the gap represents the genuine risk the bank carries that Basel's prescribed formulae were not designed to capture.

## Cross-risk diversification

The single most consequential difference between economic capital and regulatory capital is the treatment of cross-risk correlation. Pillar 1 simply adds credit RWA, market RWA, and operational RWA, with no recognition that the three risk types are imperfectly correlated. Economic capital models the correlation structure across risk types and applies a diversification benefit.

The standard variance-covariance formulation gives:

```
EC_total = sqrt( EC^T * Sigma * EC )
```

where `EC` is the vector of risk-type capital and `Sigma` is the inter-risk correlation matrix. The matrix is symmetric, the diagonal is one by construction, and the off-diagonals are typically set in the 0.3 to 0.5 range, conservatively, from expert judgement or supervisory guidance. There is no recent data set rich enough to estimate, say, the credit-operational correlation at the firm level with anything resembling statistical precision; the matrix is a documented judgement that the supervisor will probe directly. See [[04-risk_measurement|risk measurement]] for a fuller treatment of the aggregation taxonomy.

The diversification benefit at firm level usually lands in the 10 to 25% range. For BankBSM, a 5% benefit gives a net economic capital figure around R1,600m, sitting between the bank's gross sum of R1,680m and a hypothetical perfectly-correlated upper bound. This benefit is the line on which a well-diversified universal bank can sometimes report economic capital below the sum of its regulatory pillars, and it is the single most heavily debated entry in the ICAAP.

A summary of how each risk type is treated under each capital basis:

| Risk | Regulatory capital basis | EC basis at 99.95% |
|---|---|---|
| Credit | 99.9% ASRF, TTC PD, downturn LGD | 99.95% Monte Carlo, PIT PD, full correlation |
| Market | 97.5% ES, liquidity-adjusted horizon | 99.95% VaR / ES, one-year horizon |
| Operational | SMA formula | 99.95% loss-distribution approach |
| IRRBB | Not in Pillar 1 | EVE sensitivity at 99.95% shock |
| Concentration | Implicit in IRB formula only | Explicit single-name and sector add-on |
| Pension, business, model | Not in Pillar 1 | Explicit management overlay |
| Diversification | None | Correlation benefit applied |

The economic capital number that emerges is the bank's own best estimate of its true capital need. It is more granular, more forward-looking, and more portfolio-specific than Pillar 1, but it is also less conservative in its treatment of cross-risk offsets and is highly sensitive to the chosen confidence level and correlation matrix.

## The link to Pillar 2A

Pillar 2A is the supervisor's formalisation of the gap between Pillar 1 and the bank's economic capital view. After reviewing the [[07-icaap|ICAAP]], the supervisor agrees the additional risks are material and sets binding add-ons. For BankBSM:

| Risk | P2A add-on |
|---|---|
| IRRBB | R200m |
| Credit concentration | R150m |
| Pension risk | R50m |
| **Total P2A** | **R400m** |

The supervisor does not rubber-stamp the bank's own economic capital estimates. They challenge assumptions, apply their own benchmarks, and may set a different number. But the source of Pillar 2A is the economic capital analysis: without an economic capital framework, the bank cannot evidence that the risks the supervisor is being asked to capitalise are real and material.

At this point P1 + P2A is R1,040m + R400m, which equals R1,440m. This corresponds closely to the bank's own economic capital view of R1,680m gross or R1,600m net of diversification, the difference being business and strategic risk, which the supervisor may not require explicit capital for but which the bank models internally.

## The link to Pillar 2B

Pillar 2A captures risks at a going-concern, baseline level. Pillar 2B asks a different question: if a severe stress materialises, how much extra capital does the bank need to absorb the losses and still remain above its P1 + P2A floor? It is a stress-test answer rather than a baseline-risk answer, and it sits on top of the going-concern stack.

For BankBSM, the severe scenario is a sharp recession: unemployment rises to 12%, property values fall 30%, and interest rates spike 200 basis points. Under this scenario, credit losses on retail mortgages surge as point-in-time PDs rise, IRRBB losses bite as the EVE of the banking book falls, and wholesale exposures suffer rating migrations and defaults. The stressed capital position falls R300m below the P1 + P2A minimum, so P2B is set at R300m.

Economic capital (R1,600m net) sits roughly between P1 + P2A (R1,440m) and P1 + P2A + P2B (R1,740m). It represents the bank's own going-concern view of capital need, while the full stack including P2B represents the stress-resilient position the supervisor requires. Note that P2B sits inside the **combined buffer requirement** and is met with CET1 only; breach forces a Maximum Distributable Amount (MDA) calculation that restricts dividends, AT1 coupons, and variable remuneration.

## The capital stack at a glance

The full stack, from the regulatory floor up to the bank's available capital:

| Layer | Composition | Function |
|---|---|---|
| Pillar 1 minimum | 4.5% CET1 + 1.5% AT1 + 2.0% T2 | Minimum solvency floor across the three Pillar 1 risks |
| Pillar 2A | Bank-specific, CET1 mostly | Going-concern add-on for risks not captured in Pillar 1 |
| Capital conservation buffer | 2.5% CET1 | Restricts distributions if breached, prevents capital eroding silently |
| Countercyclical buffer | 0 to 2.5% CET1 | Time-varying, set by the macroprudential authority |
| Systemic risk buffers | G-SII / O-SII / SyRB, CET1 | Bank-specific structural add-on |
| Pillar 2B | Bank-specific, CET1 | Stress-test add-on; covers the gap that materialises under severe scenarios |
| Management buffer | Bank choice, mostly CET1 | Cushion above all of the above to avoid breaching in normal volatility |
| Available capital | What the bank actually holds | Should sit comfortably above the management buffer in normal conditions |

Economic capital, in this picture, is the bank's parallel internal answer to the same solvency question. The regulatory stack is binding; the economic capital framework is informative and feeds the dialogue with the supervisor through the ICAAP.

## Uses of economic capital

Economic capital is not an academic exercise. It is used in five places, all of which depend on the same underlying number being available at the right level of granularity.

**Capital allocation across business units.** The bank's total economic capital is allocated to business units in proportion to their contribution to total risk. A business unit running a high-tail-risk portfolio receives a larger allocation than one running a steady fee book of the same size, and the allocation is what each unit must earn a return on.

**Risk-adjusted performance measurement (RAROC).** Risk-adjusted return on capital, defined as net income (after expected loss and operating cost) divided by allocated economic capital, is the standard internal measure of whether a business unit is creating shareholder value. A unit with a high RAROC justifies growth; a unit with a RAROC below the bank's cost of equity is destroying value, however large its revenue line.

```
RAROC = (Net revenue - Expected loss - Cost) / Allocated EC
```

**Pricing.** Loan pricing should at least cover the cost of capital tied up against the loan. The economic capital allocated to a single facility, multiplied by the bank's required return on capital, is the capital component of the price. See [[../pricing/03-loan_pricing|loan pricing]] for the wider build.

**Limit setting.** Concentration limits, sector limits, and counterparty limits are typically calibrated against the economic capital impact of a hypothetical maximum exposure, not against notional. This lets the limit framework be risk-sensitive without manually re-calibrating for every product or counterparty type.

**Strategic and acquisition decisions.** A proposed acquisition or new business line is evaluated against its economic capital impact: how much capital it consumes, what its standalone RAROC looks like, and what its impact on the bank's diversification benefit is. The diversification impact can flip the sign of the decision: an acquisition that is loss-making on its own can be capital-accretive at the group level if it diversifies the bank's risk mix, and vice versa.

## Governance and model risk

The economic capital framework is a Tier 1 model and sits squarely inside the bank's [[04-risk_measurement|model risk]] and [[../risk_measurement/credit_risk/a-irb_capital/01_introduction/05-use_tests|use test]] discipline. Three governance questions matter most.

First, **who owns the framework**. The standard pattern places ownership with the Chief Risk Officer, with the model development team building the framework, the model validation team validating it independently, and a model risk committee approving material changes. The board approves the high-level methodology, the confidence level, and the inter-risk correlation matrix. The same board accountability that applies to Pillar 1 internal models applies here.

Second, **how the confidence level is governed**. Moving from 99.9% to 99.95% changes the capital number materially. The choice is a board-level decision linked to the target credit rating, and it has to be documented, debated, and re-examined when the target rating or the business mix changes.

Third, **how the correlation matrix is governed**. Because the off-diagonals are judgemental, the documentation around them carries the supervisory weight. The standard expectation is that the matrix is reviewed annually, that sensitivities are run on the diversification benefit at plus or minus 0.1 on each correlation, and that the choice between, say, a 0.3 and a 0.5 credit-operational correlation can be defended on the basis of business mix rather than convenience.

The wider point is that economic capital is a model output, and like every model output it carries model risk. Margins of conservatism on the inputs, sensitivity analysis on the outputs, and explicit documentation of known weaknesses are the standard mitigants. See [[04-risk_measurement|risk measurement]] section on model risk for the wider framework.
