# How banks price credit cards: from FTP to RAROC

**Banks construct credit card interest rates as an additive stack of four cost components plus a profit margin, each derived from distinct internal models.** The standard decomposition — Cost of Funds + Expected Loss + Operating Expenses + Cost of Capital + Profit Margin — forms the "pricing floor" below which the bank destroys shareholder value. Every component is calibrated using different methodologies: Treasury sets the funding cost via matched-maturity FTP curves; credit risk models supply through-the-cycle PD × LGD × EAD for the expected loss layer; activity-based costing allocates overhead; and the Basel IRB risk-weight function determines how much CET1 equity capital each exposure consumes, which must earn the target ROE. Credit cards present unique pricing challenges — revolving utilisation uncertainty, behavioural EAD estimation, and a multi-revenue-stream profit model — that distinguish them from term lending products.

---

## The pricing equation and how the components stack

The foundational pricing identity in retail lending is an additive decomposition:

$$r_{\text{loan}} = \underbrace{r_{\text{FTP}}}_{\text{Cost of Funds}} + \underbrace{\text{PD}_{\text{TTC}} \times \text{LGD} \times \text{EAD factor}}_{\text{Expected Credit Loss \%}} + \underbrace{c_{\text{OpEx}}}_{\text{Operating Cost \%}} + \underbrace{\frac{K \times 12.5 \times \text{CET1\%} \times r_{\text{ROE}}}{\text{EAD}}}_{\text{Cost of Capital \%}} + \underbrace{\pi}_{\text{Profit Margin}}$$

The Federal Reserve Bank of Minneapolis gives an illustrative decomposition: a 10% loan rate = 5% cost of funds + 2% operating costs + 2% default risk premium + 1% profit margin. In practice, for a credit card with a **21% APR**, a representative decomposition might look like:

| Component | Typical range | Illustrative value |
|---|---|---|
| FTP (cost of funds) | 4–6% | 5.0% |
| Expected credit loss (TTC) | 2–9% | 4.0% |
| Operating expenses | 4–6% | 5.0% |
| Cost of capital (CET1 charge) | 0.8–1.5% | 1.0% |
| Profit margin / residual | 1–4% | 2.0% |
| **Total minimum required rate** | | **~17%** |
| **Actual charged APR** | | **~21%** |

The gap between the pricing floor (~17%) and the charged APR (~21%) reflects competitive positioning, cross-subsidy from non-interest revenue streams (interchange, fees), and product-level margin targets. The bank assesses whether the all-in product RAROC clears the hurdle rate — not just the interest margin in isolation.

A critical distinction: the **expected loss component in pricing uses through-the-cycle (TTC) parameters**, while IFRS 9 provisioning uses point-in-time (PIT) estimates. The pricing EL is a long-run cost that must be recovered over the cycle; the accounting provision reflects current forward-looking conditions. During benign periods, the pricing EL exceeds the IFRS 9 provision (building an implicit buffer), while in stress the relationship inverts.

---

## Funds Transfer Pricing: how Treasury sets the internal cost of funds

### Matched-maturity FTP — the industry standard

The **matched-maturity marginal cost method** is the gold standard for large banks and is effectively mandated by the US Interagency Guidance on FTP (SR-16-3, March 2016) and the CEBS/EBA Guidelines on Liquidity Cost Benefit Allocation (2010). Treasury acts as a central counterparty: it "buys" funds from deposit-gathering units and "sells" them to lending units at an internal transfer price that reflects the marginal cost of funding each specific instrument.

Each instrument's FTP rate is matched to its maturity, repricing characteristics, and cash flow profile on the bank's internal FTP curve. This **completely isolates interest rate risk in Treasury** — business unit margins reflect only credit spread and pricing discipline. For a 5-year fixed-rate mortgage originated at 6.50% with a 5-year FTP rate of 4.80%, the lending unit's clean margin is **170 bps** — purely the credit and pricing contribution.

### Components of the FTP curve

The FTP curve is built as:

$$r_{\text{FTP}}(T) = r_{\text{swap}}(T) + \text{LP}(T) + \text{CC}(T) + \text{Optionality}(T)$$

The **base rate** is the risk-free rate at the matching tenor — typically the SOFR swap curve (US) or SONIA swap curve (UK) post-LIBOR transition. Since SOFR is a secured rate, a compensating **credit/liquidity spread** must be added to approximate the bank's actual unsecured funding cost. The **liquidity premium (LP)** — also called the term liquidity premium (TLP) — represents the spread above the risk-free rate that the bank pays for term wholesale funding, derived by stripping the bank's own senior unsecured issuances into their floating-rate equivalent and observing the spread over the reference rate. Pre-2007, bank 5-year unsecured spreads were negligible; post-crisis they widened to **100+ bps** and have remained structurally elevated. The **contingency cost (CC)** allocates the carry cost of LCR/NSFR-compliant HQLA buffers to the instruments creating the liquidity requirement.

### The credit card FTP challenge

Credit cards pose the most complex FTP problem because they have no fixed maturity, variable utilisation, and embedded borrower optionality (draw, repay, or default at will). The solution involves **separating the interest rate component from the liquidity component**:

The **interest rate FTP** matches the repricing frequency. Since most credit card rates are variable (Prime + margin in the US, or Bank Rate-linked in the UK), the interest rate risk is short-duration — typically **1-month or 3-month** tenor on the swap curve. The **liquidity FTP**, however, must reflect the full behavioural duration of the revolving portfolio. Moorad Choudhry's principle states that the liquidity premium for a revolving facility should **never be lower** than for an equivalent term loan — because the borrower holds a drawdown option that is most valuable precisely when market liquidity spreads are highest (adverse selection / wrong-way risk, as demonstrated in March 2020). Conservative practice treats the full contractual limit as requiring long-term liquidity funding, typically charging a **3–5 year TLP**.

A less conservative but common approach uses a **replicating portfolio**: the aggregate credit card balance is decomposed into a synthetic portfolio of fixed-maturity instruments that replicate observed cash flow behaviour, with core (stable) balances receiving long-term FTP and volatile balances receiving shorter-term rates. For undrawn commitments, the FTP cost reflects the **probability of drawdown × cost of funding at the time of draw** — analogous to pricing a contingent liquidity put option. The US Interagency Guidance explicitly permits modelling based on "customer drawdown history, credit quality, and other factors."

---

## Expected credit loss: TTC parameters in pricing versus PIT in provisioning

### The annual expected loss formula

The ECL loading embedded in the interest rate is:

$$\text{EL\%} = \text{PD}_{\text{TTC}} \times \text{LGD}_{\text{downturn}} \times \text{EAD factor}$$

For a fully drawn term loan, the EAD factor is 1.0. For revolving credit, the EAD factor incorporates the Credit Conversion Factor (CCF) applied to the undrawn portion. For example, a credit card with a \$10,000 limit, \$6,000 drawn, and CCF = 0.50 has EAD = \$6,000 + (0.50 × \$4,000) = \$8,000. If TTC PD = 3% and downturn LGD = 80%, the annual expected loss is 3% × 80% × (\$8,000/\$6,000) = **3.2% of the drawn balance** — embedded directly in the interest rate.

Banks use **TTC PDs** for pricing because the interest rate on a credit card must remain economically viable across the full credit cycle. A TTC PD reflects the long-run average default frequency — if observed annual default rates ranged from 1.5% in expansion to 5% in recession, the TTC central tendency would be approximately **2.8%**. This prevents pro-cyclical pricing that would underprice risk in booms and overprice in recessions. Calibration methods include long-run averaging of observed default rates, mapping to external rating agency TTC default tables, or using the Vasicek single-factor model to condition out the systematic factor from PIT estimates.

**Downturn LGD** (rather than best-estimate LGD) is used in pricing to provide conservatism — reflecting the empirical reality that recovery rates decline during recessions. For unsecured credit cards, downturn LGD typically falls in the **75–90%** range, compared to **10–25%** for first-lien residential mortgages.

### Why pricing ECL differs from IFRS 9 provisioning ECL

| Dimension | Pricing (TTC) | IFRS 9 Provisioning (PIT) |
|---|---|---|
| PD basis | Through-the-cycle (long-run average) | Point-in-time (forward-looking, macro-adjusted) |
| LGD basis | Downturn LGD (conservative) | Best-estimate PIT LGD |
| Time horizon | 1-year annualised (for revolving products) | 12-month (Stage 1) or lifetime (Stages 2–3) |
| Stability | Stable across the cycle | Volatile — tracks macro scenarios |
| Purpose | Recover average losses over time through the rate | Reflect current expected losses on the balance sheet |
| Conservatism | Includes margin of conservatism | Must be unbiased — best estimate |

During a benign credit environment, IFRS 9 PIT PDs will be **lower** than TTC pricing PDs, meaning the bank is implicitly accumulating a buffer through the interest rate. During a recession, the relationship inverts: IFRS 9 provisions spike above the pricing EL, and the buffer built in good years absorbs the difference. This asymmetry is a feature, not a bug — it is why TTC pricing creates economic stability in the lending model.

### EAD and the Credit Conversion Factor for credit cards

The CCF captures the proportion of currently undrawn credit that will be drawn down by the time of default. Empirical CCF values for credit cards are characteristically **bimodal** — probability mass concentrates near 0 (no additional drawdown) and near 1 (borrower maxes out the card before default, the "race to default" phenomenon). Mean empirical CCFs for credit cards range from **0.42 to 0.52** across published studies. Under the Basel III standardised approach, unconditionally cancellable credit card commitments attract a **10% CCF** (revised upward from 0% under Basel II). Under A-IRB, banks estimate their own CCFs subject to floors. Combined modelling approaches — using CCF models for low-utilisation accounts and direct EAD models for high-utilisation accounts — show the best predictive performance.

---

## Risk-based pricing: from scorecards to rate cards

### How internal risk grades map to individual pricing

The pricing pipeline flows from **score → rating grade → PD → EL% → pricing tier**. At origination, the **application scorecard** evaluates the applicant using demographics, income, employment, requested amount, and bureau data, producing a numerical score that predicts 12–24 month default probability. Post-origination, the **behavioural scorecard** continuously updates the risk assessment using payment history, usage patterns, delinquency, and balance trends. This behavioural score feeds IFRS 9 staging decisions (SICR assessment) and, in jurisdictions permitting it, repricing decisions.

Each score maps to an internal risk grade, and each grade carries a calibrated TTC PD. The EL% for that grade is then computed and added to the common cost base (FTP + OpEx + capital charge) to determine the minimum required rate for that risk band:

| Risk grade | TTC PD | LGD | EL% | FTP | OpEx | Capital charge | Profit | **APR** |
|---|---|---|---|---|---|---|---|---|
| A (Super-prime) | 0.5% | 80% | 0.4% | 5.0% | 4.0% | 0.6% | 2.0% | **12.0%** |
| B (Prime) | 2.0% | 80% | 1.6% | 5.0% | 4.0% | 0.8% | 2.0% | **13.4%** |
| C (Near-prime) | 5.0% | 85% | 4.3% | 5.0% | 5.0% | 1.2% | 2.0% | **17.5%** |
| D (Subprime) | 10.0% | 90% | 9.0% | 5.0% | 5.0% | 1.8% | 2.0% | **22.8%** |

Note that the capital charge also increases with PD because the IRB risk-weight function produces higher K (and thus higher RWA) at higher PDs, requiring more CET1 per unit of exposure.

### Bureau scores and pricing tiers in practice

Federal Reserve research on Y-14M data (284,914 credit card accounts, 2013–2024) confirms a **strong positive relationship** between expected default rates and pricing at origination. The interest rate spread over Prime ranges from approximately **6 percentage points at FICO 850** to **21 percentage points at FICO 600**. FDIC research found charge-off rates decrease almost linearly with FICO: from **9.3% per annum at FICO 600** to near-zero at FICO 850. Banks typically segment into 20-point FICO bins from 580 to 780, each receiving a distinct pricing tier. Typical US credit card APRs by risk tier as of late 2025 are roughly **18–20%** for super-prime (760+), **22–23%** for prime, and **27–30%** for subprime. Research by Scott Nelson (Econometrica, 2025) found a pre-CARD Act gradient of approximately **1 APR percentage point per 30 FICO points**.

### Floor and ceiling rates

Banks set **floor APRs** (e.g., "Prime + 12.99%, minimum 14.99%") to ensure minimum profitability when benchmark rates decline. On the ceiling side, **no general federal usury cap** exists for credit cards in the US — most major issuers are chartered in Delaware or South Dakota, which impose no caps. The Military Lending Act caps rates at **36% APR** for active-duty personnel. Federal credit unions face a statutory cap of **18%**. In the UK, there is no statutory interest rate cap for credit cards, though the FCA's persistent debt rules require issuers to intervene when customers pay more in interest and fees than principal repayment over 18 months. Proposed US legislation in the 119th Congress includes bills for 10% and 36% caps, though none has been enacted. Bank Policy Institute analysis suggests a 10% cap would deny credit access to approximately **14 million US households**, concentrated among subprime borrowers.

---

## RAROC: the capital charge and the hurdle rate

### From the IRB risk-weight function to the pricing capital charge

The Basel IRB capital requirement for retail exposures derives from the Vasicek asymptotic single-risk-factor (ASRF) model. The capital requirement K represents the **unexpected loss** at 99.9% confidence — the difference between the conditional worst-case loss and the expected loss:

$$K = \text{LGD} \times \left[ \Phi\!\left( \frac{\Phi^{-1}(\text{PD})}{\sqrt{1-R}} + \sqrt{\frac{R}{1-R}} \times \Phi^{-1}(0.999) \right) - \text{PD} \right]$$

where $\Phi$ is the standard normal CDF, $\Phi^{-1}$ is its inverse, and R is the asset correlation. For **Qualifying Revolving Retail Exposures (QRREs)** — credit cards, charge cards, overdrafts — the asset correlation is fixed at **R = 0.04**, the lowest in the entire Basel framework. This reflects the empirical finding that credit card defaults are driven predominantly by idiosyncratic (borrower-specific) factors rather than systematic economic conditions — i.e., highly granular, diversified portfolios.

For retail exposures, **no maturity adjustment** applies (unlike corporate exposures, which include the factor $\frac{1 + (M-2.5) \times b}{1-1.5b}$). The conversion to risk-weighted assets is RWA = K × 12.5 × EAD, where the **12.5 multiplier** is simply the reciprocal of the 8% minimum total capital ratio.

**Worked example** (PD = 3%, downturn LGD = 80%, R = 0.04):

- $\Phi^{-1}(0.03) = -1.8808$; $\Phi^{-1}(0.999) = 3.0902$
- $\sqrt{1/(1-0.04)} = 1.02062$; $\sqrt{0.04/(1-0.04)} = 0.20412$
- Conditional PD = $\Phi(1.02062 \times (-1.8808) + 0.20412 \times 3.0902) = \Phi(-1.2885) \approx 0.0988$
- **K = 0.80 × (0.0988 − 0.03) = 5.50%**
- Risk weight = 5.50% × 12.5 = **68.75%**

This is consistent with the reported US advanced-approaches average risk weight for credit cards of approximately **73%** (FFIEC 101 data, 2014–2022).

The capital charge embedded in the price is then:

$$\text{Capital charge (\% of EAD, p.a.)} = \text{RW} \times \text{CET1 requirement} \times r_{\text{ROE}}$$

For our example: 68.75% × 10.5% CET1 (4.5% minimum + 2.5% CCB + 3.5% illustrative Pillar 2/G-SIB buffers) × 12% target ROE = **0.87%**, or **87 basis points** per annum. This is the minimum annual return on the credit card EAD that must be earned purely to compensate shareholders for the equity capital consumed.

### Basel III/IV parameter floors for QRREs

The finalised Basel III reforms introduce new parameter floors that constrain IRB estimates:

| Parameter | QRRE transactors | QRRE revolvers |
|---|---|---|
| PD floor | 0.05% (5 bps) | **0.10%** (10 bps) |
| LGD floor (unsecured) | 50% | 50% |
| EAD floor | On-balance-sheet + 50% × off-balance-sheet × SA CCF | Same |

The **output floor** requires that aggregate IRB RWA cannot fall below **72.5%** of standardised RWA, phased in over five years. For credit cards in most jurisdictions, the IRB risk weight (~73%) already sits near or above the output floor applied to the standardised weight (72.5% × 75% revolver SA weight = ~54%), so the output floor is generally not binding for card portfolios — except under the significantly more punitive US Basel III Endgame proposal, where proposed standardised risk weights of 85% (revolvers) plus a 10 pp add-on and stress-test capital overlays would push the effective all-in risk weight to approximately **174%** per Bank Policy Institute analysis.

### The RAROC decision framework

RAROC (Risk-Adjusted Return on Risk-Adjusted Capital, often just called "RAROC" in practice) is:

$$\text{RAROC} = \frac{\text{Interest income} + \text{Fee income} - \text{FTP cost} - \text{OpEx} - \text{Expected Loss} - \text{Tax}}{\max(\text{Economic Capital}, \text{Regulatory Capital})}$$

The **hurdle rate** is the minimum RAROC a transaction, product, or business unit must achieve. It is typically derived from the **cost of equity via CAPM** — not the WACC — because the cost of debt (deposits, wholesale funding) is already deducted in the numerator as the FTP charge. Typical bank hurdle rates fall in the **10–15%** range. FDIC supervisory guidance cites 10%; Zachary Scott reports 12% as a representative large-bank target; McKinsey Working Paper No. 24 (2011) recommends **granular hurdles** that differ by business unit based on each unit's marginal beta contribution to systematic risk.

The minimum required loan rate can be **back-solved** from the RAROC hurdle:

$$r_{\text{min}} = r_{\text{FTP}} + (\text{PD} \times \text{LGD}) + c_{\text{OpEx}} + \left(\frac{\text{EC}}{\text{EAD}} \times r_{\text{hurdle}}\right)$$

Any rate charged above $r_{\text{min}}$ generates economic value added (EVA). Banks use RAROC at multiple levels: **transaction-level** (approve/reject/reprice individual applications), **product-level** (assess whether the credit card portfolio as a whole clears the hurdle), **business-unit level** (compare retail versus wholesale returns), and **portfolio optimisation** (reallocate capital from low-RAROC to high-RAROC segments). McKinsey's survey of 11 global banks found that approximately 75% of economic capital at one institution was deployed in business units earning **below** the cost of capital — illustrating why RAROC discipline matters.

Post-2008, the distinction between **economic capital** (internal VaR-based estimate calibrated to a target solvency standard, e.g., AA rating ≈ 99.95% confidence) and **regulatory capital** (Basel-prescribed minimum) has collapsed somewhat. Stringent post-crisis regulatory requirements mean regulatory capital is now often the binding constraint. Most banks therefore use **max(EC, RC)** as the RAROC denominator, or compute dual metrics.

---

## Credit card specifics: what makes revolving credit different

### Transactors versus revolvers and the cross-subsidy

Federal Reserve Y-14M data from the 13 largest US issuers reveals a stark segmentation. **Heavy revolvers** (~20% of accounts) carry ~53% of balances and pay ~72% of all interest charges, with an average monthly interest charge of **\$60.50**. **Transactors** (~21% of accounts) carry ~10% of balances, pay less than 1% of interest, but generate ~39% of purchase volume. The average spread earned on heavy revolvers is **14.97%**, versus **12.30%** on transactors. A deep cross-subsidy exists: revolvers fund the rewards programmes that attract high-spending transactors.

Basel III recognises this asymmetry by assigning different standardised risk weights: **45%** for transactor balances versus **75%** for revolver balances — reflecting the substantially lower credit risk of customers who pay in full each month. Classification follows a 12-month lookback: an account is a transactor if total accrued interest over the prior 12 months is less than $50.

### The multi-stream revenue model

Credit card profitability is not captured by the interest margin alone. The Federal Reserve's definitive breakdown using Y-14M data shows:

- **Credit function (net credit margin × revolving share)**: ~80% of product ROA
- **Fee income (late fees, cash advance fees, FX, annual fees)**: ~16% of product ROA
- **Transaction function (interchange minus rewards minus fraud minus funding)**: ~−4% of product ROA

This means the **transaction function has turned net-negative** in recent years as rewards expenses grew approximately 25% from 2015 to 2020, now consuming most of the interchange revenue. Interchange fees of approximately **2% of purchase value** (split between network, acquirer, and issuer) represent ~29% of gross industry revenue, but after deducting rewards costs, fraud losses, and transaction processing, the net contribution is marginal or negative. The pre-pandemic quarterly ROA for US credit cards was approximately **1.10%**, significantly exceeding all-bank ROA of 0.30–0.40%, confirming cards as a high-return product driven overwhelmingly by the credit function.

For product-level pricing decisions, the bank models all-in profitability:

$$\text{Product ROA} = \frac{(\text{Interest income} + \text{Interchange} + \text{Fees}) - (\text{FTP} + \text{ECL} + \text{Rewards} + \text{Fraud} + \text{OpEx} + \text{Capital charge})}{\text{Average assets}}$$

Promotional 0% balance transfer offers illustrate how this works in practice. The issuer earns zero interest during the promotional period (typically 12–21 months) but charges a **3–5% upfront transfer fee** (US) or **1–3%** (UK). The economics depend on whether the customer converts to a revolver at the revert rate (typically 22–25%) post-promotion or transfers away — the risk of serial "rate tarts" is managed through credit scoring and targeting.

### Operating cost allocation

The OpEx loading in credit card pricing is higher than for most other lending products because of transaction processing infrastructure, fraud prevention, rewards programme administration, customer servicing, and collections. Banks allocate overhead to individual products using **activity-based costing (ABC)**, which traces costs to the activities that drive them rather than applying a flat overhead allocation. Typical credit card operating costs run **4–6% of outstanding balances** — substantially above mortgages (~0.5–1.0%) or personal loans (~2–3%). This high OpEx loading is a key reason credit card APRs are structurally elevated even for prime customers.

---

## How pricing has evolved under Basel III and regulatory pressure

The post-crisis regulatory environment has reshaped credit card pricing in several ways. Higher CET1 requirements (minimum 4.5% plus the 2.5% CCB, plus G-SIB surcharges of 1.0–3.5%, plus Pillar 2 add-ons) have increased the capital charge embedded in pricing — BIS research estimates that a **1 percentage point increase in CET1/RWA translates into a 0.12% median decline in economic output**, suggesting capital costs do pass through to loan pricing, though the Fed estimated the US Basel III Endgame proposal's impact on average lending costs at only **3 basis points**.

The CARD Act (US, 2009) fundamentally altered pricing dynamics by restricting repricing of existing balances. Pre-CARD Act, issuers used **penalty repricing** based on privately observed behaviour (sub-30-day delinquencies, over-limit transactions) to manage adverse selection — effectively a form of ex-post risk-based pricing. Post-CARD Act, issuers must provide 45-day notice before rate increases and cannot increase rates on existing balances in the first year. This has forced banks to **front-load risk into origination pricing** (higher initial APRs), tighten acceptance criteria, and use credit limits rather than rates as the primary non-price risk management lever. Nelson (Econometrica, 2025) documents how this reduced the ability to price private information, exacerbating adverse selection costs that are ultimately borne by borrowers through higher average rates.

In the UK, the FCA's **persistent debt rules** (2018) require providers to intervene when customers are paying more in interest and fees than principal over 18 months, and to offer forbearance at 36 months. This effectively caps the lifetime profitability extractable from vulnerable revolvers and has pushed UK issuers toward higher upfront pricing with greater emphasis on affordability assessment. Average UK credit card interest rates reached **24.66%** by late 2025 — the highest in 30 years — partly reflecting higher base rates but also the structural pricing impact of tighter regulatory expectations.

---

## Conclusion

Credit card pricing is a precise engineering exercise that integrates market-driven funding costs, actuarial credit risk estimates, activity-based cost allocation, and regulatory capital mathematics into a single interest rate. Three insights stand out for the F107 candidate. First, the distinction between TTC parameters in pricing and PIT parameters in IFRS 9 provisioning is not merely academic — it is the mechanism by which banks maintain cycle-stable pricing while still reflecting current conditions on the balance sheet. Second, the **QRRE asset correlation of R = 0.04** — the lowest in the Basel framework — produces capital charges that are surprisingly moderate relative to the high LGDs on unsecured credit, reflecting the powerful diversification in granular retail portfolios. Third, credit card profitability is overwhelmingly driven by the **credit function** (revolving interest), not interchange — the transaction function has turned net-negative — making the accuracy of risk-based pricing and EAD estimation the primary determinants of whether the product creates or destroys shareholder value. The RAROC framework ties these components together: if the all-in return on the capital consumed does not exceed the hurdle rate of 10–15%, the bank should either reprice, restructure, or exit the exposure.