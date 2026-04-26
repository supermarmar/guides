---
tags:
  - application/banking/internal-environment/pricing/pricing-framework
  - difficulty/unknown
  - study-status/new
aliases:
---
# Pricing Framework

This file covers the overarching principles governing how banks price their products — the distinction between fundamental and tactical pricing, the internal and external factors that shape pricing decisions, and how banks manage net interest margins and the price-volume trade-off over time. For the pricing of specific product types see [Deposit Pricing](04-deposit_pricing.md), [Loan Pricing](05-loan_pricing.md), and [DCF Models](06-dcf_model.md). For investment bank [[07-derivative_pricing|derivative pricing]] see [Derivative Pricing](07-derivative_pricing.md).

## <mark style="background: #FFF3A3A6;">Fundamental Pricing</mark>

**Fundamental pricing** derives a theoretically fair price for a product, typically using a discounted cashflow (DCF) model that captures all expected income, costs, [[02-credit_losses|credit losses]], and required return on capital. It answers the question: what rate makes this product economically viable?

## <mark style="background: #FFF3A3A6;">Tactical Pricing </mark>

**Tactical pricing** is the adjusted, market-facing price that incorporates competitive dynamics and strategic objectives. Common tactical mechanisms include:

- **Customised pricing** — price set based on individual customer characteristics (standard in credit pricing and risk-based lending)
- **Non-linear pricing** — price does not scale proportionally with volume (e.g. bulk discounts, tiered deposit rates)
- **List pricing** — seller publishes a price; customers choose whether to transact (e.g. share prices, listed property)
- **Markdown management** — price reduction below "normal" to clear inventory (common in retail)
- **Revenue management** — dynamic pricing to manage aggregate revenue (e.g. deposit rate changes to attract or deter inflows)

## Internal Pricing Factors

**Internal factors** driving pricing decisions include financial hurdle rates (minimum ROE or RORAC targets), strategic objectives (volume targets, [[03-nii_nim|NIM]] goals, market share), and system functionality (the ability to operationalise granular risk-based pricing).

## External Pricing Factors

**External factors** include:

- **Competition** — the primary driver of headline prices for most banking products. Competition is strongest in secured lending (mortgages) and fixed deposits; weakest in unsecured lending and investment banking advisory. Large banks typically price headline rates close to competitors. Online banks intensify competition further.
- **Regulation** — South Africa's **National Credit Act (NCA)** imposes maximum pricing on consumer credit facilities, covering both interest rates and fees (e.g. unsecured personal loans capped at repo rate + 21%). **Treating Customers Fairly (TCF)** regulation limits discriminatory or opaque pricing. In retail banking, at least 51% of loans issued in the UK must be at the advertised headline rate (restricting risk-based pricing breadth).

## <mark style="background: #FFF3A3A6;"> Loan Pricing Components</mark>

The key income and cost components that [[05-loan_pricing|loan pricing]] must cover are: 
- funds transfer pricing (FTP) — the internal cost assigned by treasury for term-matched funding;
- credit risk — expected [[02-credit_losses|credit losses]] over the product life; 
- non-interest expenses — origination, maintenance, and collections; and 
- cost of capital;
- profit — a return sufficient to satisfy shareholders on the CET1 capital deployed. 

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

The gap between the pricing floor (~17%) and the charged APR (~21%) reflects competitive positioning, cross-subsidy from non-interest revenue streams (interchange, fees), and product-level margin targets. 

For this to be adequate, the bank measures **return on capital (ROC)** and sets **hurdle rates** by product risk category. The more precise measure of economic profit is **Net Income After Cost of Capital (NIACC)** — the bank aims for NIACC-positive pricing.

### Credit Losses

A critical distinction: the **expected loss component in pricing uses through-the-cycle (TTC) parameters**, while IFRS 9 provisioning uses point-in-time (PIT) estimates. The pricing EL is a long-run cost that must be recovered over the cycle; the accounting provision reflects current forward-looking conditions. During benign periods, the pricing EL exceeds the IFRS 9 provision (building an implicit buffer), while in stress the relationship inverts. 

The ECL loading embedded in the interest rate is:

$$\text{EL\%} = \text{PD}_{\text{TTC}} \times \text{LGD}_{\text{downturn}} \times \text{EAD factor}$$

Banks use **TTC PDs** for pricing because the interest rate on a credit card must remain economically viable across the full credit cycle. A TTC PD reflects the long-run average default frequency — if observed annual default rates ranged from 1.5% in expansion to 5% in recession, the TTC central tendency would be approximately **2.8%**. This prevents pro-cyclical pricing that would underprice risk in booms and overprice in recessions. Calibration methods include long-run averaging of observed default rates, mapping to external rating agency TTC default tables, or using the Vasicek single-factor model to condition out the systematic factor from PIT estimates.

**Downturn LGD** (rather than best-estimate LGD) is used in pricing to provide conservatism — reflecting the empirical reality that recovery rates decline during recessions. For unsecured credit cards, downturn LGD typically falls in the **75–90%** range, compared to **10–25%** for first-lien residential mortgages.

| Dimension | Pricing (TTC) | IFRS 9 Provisioning (PIT) |
|---|---|---|
| PD basis | Through-the-cycle (long-run average) | Point-in-time (forward-looking, macro-adjusted) |
| LGD basis | Downturn LGD (conservative) | Best-estimate PIT LGD |
| Time horizon | 1-year annualised (for revolving products) | 12-month (Stage 1) or lifetime (Stages 2–3) |
| Stability | Stable across the cycle | Volatile — tracks macro scenarios |
| Purpose | Recover average losses over time through the rate | Reflect current expected losses on the balance sheet |
| Conservatism | Includes margin of conservatism | Must be unbiased — best estimate |

During a benign credit environment, IFRS 9 PIT PDs will be **lower** than TTC pricing PDs, meaning the bank is implicitly accumulating a buffer through the interest rate. During a recession, the relationship inverts: IFRS 9 provisions spike above the pricing EL, and the buffer built in good years absorbs the difference. This asymmetry is a feature, not a bug — it is why TTC pricing creates economic stability in the lending model.

### Cost of Capital

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

### Scorecards → Ratecards

The pricing pipeline flows from **score → rating grade → PD → EL% and RWA → pricing tier**. At origination, the **application scorecard** evaluates the applicant using demographics, income, employment, requested amount, and bureau data, producing a numerical score that predicts 12–24 month default probability. Post-origination, the **behavioural scorecard** continuously updates the risk assessment using payment history, usage patterns, delinquency, and balance trends. This behavioural score feeds IFRS 9 staging decisions (SICR assessment) and, in jurisdictions permitting it, repricing decisions.

Each score maps to an internal risk grade, and each grade carries a calibrated TTC PD. The EL% for that grade is then computed and added to the common cost base (FTP + OpEx + capital charge) to determine the minimum required rate for that risk band:

| Risk grade | TTC PD | LGD | EL% | FTP | OpEx | Capital charge | Profit | **APR** |
|---|---|---|---|---|---|---|---|---|
| A (Super-prime) | 0.5% | 80% | 0.4% | 5.0% | 4.0% | 0.6% | 2.0% | **12.0%** |
| B (Prime) | 2.0% | 80% | 1.6% | 5.0% | 4.0% | 0.8% | 2.0% | **13.4%** |
| C (Near-prime) | 5.0% | 85% | 4.3% | 5.0% | 5.0% | 1.2% | 2.0% | **17.5%** |
| D (Subprime) | 10.0% | 90% | 9.0% | 5.0% | 5.0% | 1.8% | 2.0% | **22.8%** |

Note that the capital charge also increases with PD because the IRB risk-weight function produces higher K (and thus higher RWA) at higher PDs, requiring more CET1 per unit of exposure.

### Price vs Volume Trade-Off

Because banks have large fixed and semi-fixed cost bases (head office, IT, branch networks, central functions), [[05-loan_pricing|loan pricing]] cannot be set purely by DCF fundamentals. A bank pricing above market rates risks sub-scale volumes that fail to cover fixed costs; a bank pricing below DCF fundamentals generates volume but destroys value.

The practical approach is:
- Set fundamental (DCF) prices as the floor below which value is destroyed.
- Adjust to market pricing given competitive dynamics.
- Use **credit cut-off scores** to exclude borrowers for whom even risk-adjusted rates are insufficient to break even.
- Price new business at marginal (not fully-loaded) cost for the cut-off decision, but monitor fully-loaded profitability across the portfolio to ensure fixed costs are covered.

This is analogous to the pricing discipline in general insurance and in industrial businesses: volume below the break-even point produces losses, but volume above marginal cost provides contribution to fixed costs even if it does not cover fully-loaded costs.

### Floors & Ceilings

Banks set **floor APRs** (e.g., "Prime + 12.99%, minimum 14.99%") to ensure minimum profitability when benchmark rates decline. On the ceiling side, **no general federal usury cap** exists for credit cards in the US — most major issuers are chartered in Delaware or South Dakota, which impose no caps. The Military Lending Act caps rates at **36% APR** for active-duty personnel. Federal credit unions face a statutory cap of **18%**. In the UK, there is no statutory interest rate cap for credit cards, though the FCA's persistent debt rules require issuers to intervene when customers pay more in interest and fees than principal repayment over 18 months. Proposed US legislation in the 119th Congress includes bills for 10% and 36% caps, though none has been enacted. Bank Policy Institute analysis suggests a 10% cap would deny credit access to approximately **14 million US households**, concentrated among subprime borrowers.

### RAROC Decision Framework

RAROC (Risk-Adjusted Return on Risk-Adjusted Capital, often just called "RAROC" in practice) is:

$$\text{RAROC} = \frac{\text{Interest income} + \text{Fee income} - \text{FTP cost} - \text{OpEx} - \text{Expected Loss} - \text{Tax}}{\max(\text{Economic Capital}, \text{Regulatory Capital})}$$

The **hurdle rate** is the minimum RAROC a transaction, product, or business unit must achieve. It is typically derived from the **cost of equity via CAPM** — not the WACC — because the cost of debt (deposits, wholesale funding) is already deducted in the numerator as the FTP charge. Typical bank hurdle rates fall in the **10–15%** range. FDIC supervisory guidance cites 10%; Zachary Scott reports 12% as a representative large-bank target; McKinsey Working Paper No. 24 (2011) recommends **granular hurdles** that differ by business unit based on each unit's marginal beta contribution to systematic risk.

The minimum required loan rate can be **back-solved** from the RAROC hurdle:

$$r_{\text{min}} = r_{\text{FTP}} + (\text{PD} \times \text{LGD}) + c_{\text{OpEx}} + \left(\frac{\text{EC}}{\text{EAD}} \times r_{\text{hurdle}}\right)$$

Any rate charged above $r_{\text{min}}$ generates economic value added (EVA). Banks use RAROC at multiple levels: **transaction-level** (approve/reject/reprice individual applications), **product-level** (assess whether the credit card portfolio as a whole clears the hurdle), **business-unit level** (compare retail versus wholesale returns), and **portfolio optimisation** (reallocate capital from low-RAROC to high-RAROC segments). McKinsey's survey of 11 global banks found that approximately 75% of economic capital at one institution was deployed in business units earning **below** the cost of capital — illustrating why RAROC discipline matters.

Post-2008, the distinction between **economic capital** (internal VaR-based estimate calibrated to a target solvency standard, e.g., AA rating ≈ 99.95% confidence) and **regulatory capital** (Basel-prescribed minimum) has collapsed somewhat. Stringent post-crisis regulatory requirements mean regulatory capital is now often the binding constraint. Most banks therefore use **max(EC, RC)** as the RAROC denominator, or compute dual metrics.
## Deposit Pricing Components

[[04-deposit_pricing|Deposit pricing]] objectives include managing inflow volumes, minimising the marginal cost of new deposits, and supporting the bank's [[03-nii_nim|NIM]] targets. Deposit rates must also factor in the liquidity value of each product type (see [Deposit Pricing](04-deposit_pricing.md)).
