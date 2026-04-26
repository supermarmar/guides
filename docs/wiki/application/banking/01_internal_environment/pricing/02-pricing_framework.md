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

## Deposit Pricing Components

[[04-deposit_pricing|Deposit pricing]] objectives include managing inflow volumes, minimising the marginal cost of new deposits, and supporting the bank's [[03-nii_nim|NIM]] targets. Deposit rates must also factor in the liquidity value of each product type (see [Deposit Pricing](04-deposit_pricing.md)).

## [[03-nii_nim|Net Interest Margin]] Management

**[[03-nii_nim|Net interest income]] ([[03-nii_nim|NII]])** = interest earned on assets − interest paid on liabilities. **[[03-nii_nim|Net interest margin]] ([[03-nii_nim|NIM]])** = [[03-nii_nim|NII]] ÷ average interest-earning assets. Banks track [[03-nii_nim|NIM]] by "front book" (new business) and "back book" (existing book) to identify trends, since margins may erode on the front book during competitive growth phases.

Several forces compress [[03-nii_nim|NIM]] over time: competitive pressure reduces loan spreads during economic expansions; [[02-credit_losses|credit losses]] increase during recessions; and rate mismatches between fixed-rate loans and variable-rate deposits create margin exposure when interest rates move. [[03-nii_nim|NIM]] management therefore requires active product design and repricing capability.

Banks must also match the [[03-nii_nim|NIM]] concept to the funding structure. For corporate and investment banking, the **term liquidity premium (TLP)** methodology is essential — treasury charges lending products the true cost of term-matched funding, discouraging cheap short-term funding of long-term assets. For retail banking, the same concept applies but TLP rates must reflect the actual retail deposit mix, not just the wholesale curve, to avoid mispricing loans relative to competitors.

## Price vs Volume Trade-Off

Because banks have large fixed and semi-fixed cost bases (head office, IT, branch networks, central functions), [[05-loan_pricing|loan pricing]] cannot be set purely by DCF fundamentals. A bank pricing above market rates risks sub-scale volumes that fail to cover fixed costs; a bank pricing below DCF fundamentals generates volume but destroys value.

The practical approach is:
- Set fundamental (DCF) prices as the floor below which value is destroyed.
- Adjust to market pricing given competitive dynamics.
- Use **credit cut-off scores** to exclude borrowers for whom even risk-adjusted rates are insufficient to break even.
- Price new business at marginal (not fully-loaded) cost for the cut-off decision, but monitor fully-loaded profitability across the portfolio to ensure fixed costs are covered.

This is analogous to the pricing discipline in general insurance and in industrial businesses: volume below the break-even point produces losses, but volume above marginal cost provides contribution to fixed costs even if it does not cover fully-loaded costs.
