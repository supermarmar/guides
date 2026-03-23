# Pricing Framework

This file covers the overarching principles governing how banks price their products — the distinction between fundamental and tactical pricing, the internal and external factors that shape pricing decisions, and how banks manage net interest margins and the price-volume trade-off over time. For the pricing of specific product types see [Deposit Pricing](02-deposit_pricing.md), [Loan Pricing](03-loan_pricing.md), and [DCF Models](04-dcf_model.md). For investment bank derivative pricing see [Derivative Pricing](05-derivative_pricing.md).

## Fundamental vs Tactical Pricing

**Fundamental pricing** derives a theoretically fair price for a product, typically using a discounted cashflow (DCF) model that captures all expected income, costs, credit losses, and required return on capital. It answers the question: what rate makes this product economically viable?

**Tactical pricing** is the adjusted, market-facing price that incorporates competitive dynamics and strategic objectives. Common tactical mechanisms include:

- **Customised pricing** — price set based on individual customer characteristics (standard in credit pricing and risk-based lending)
- **Non-linear pricing** — price does not scale proportionally with volume (e.g. bulk discounts, tiered deposit rates)
- **List pricing** — seller publishes a price; customers choose whether to transact (e.g. share prices, listed property)
- **Markdown management** — price reduction below "normal" to clear inventory (common in retail)
- **Revenue management** — dynamic pricing to manage aggregate revenue (e.g. deposit rate changes to attract or deter inflows)

## Internal and External Pricing Factors

**Internal factors** driving pricing decisions include financial hurdle rates (minimum ROE or RORAC targets), strategic objectives (volume targets, NIM goals, market share), and system functionality (the ability to operationalise granular risk-based pricing).

**External factors** include:

- **Competition** — the primary driver of headline prices for most banking products. Competition is strongest in secured lending (mortgages) and fixed deposits; weakest in unsecured lending and investment banking advisory. Large banks typically price headline rates close to competitors. Online banks intensify competition further.
- **Regulation** — South Africa's **National Credit Act (NCA)** imposes maximum pricing on consumer credit facilities, covering both interest rates and fees (e.g. unsecured personal loans capped at repo rate + 21%). **Treating Customers Fairly (TCF)** regulation limits discriminatory or opaque pricing. In retail banking, at least 51% of loans issued in the UK must be at the advertised headline rate (restricting risk-based pricing breadth).

## Pricing Objectives for Loans and Deposits

The key income and cost components that loan pricing must cover are: funds transfer pricing (FTP) — the internal cost assigned by treasury for term-matched funding; credit risk — expected credit losses over the product life; non-interest expenses — origination, maintenance, and collections; and profit — a return sufficient to satisfy shareholders on the CET1 capital deployed. The construct is:

```
Loan rate = FTP cost + credit risk premium + operating cost margin + profit margin
```

For this to be adequate, the bank measures **return on capital (ROC)** and sets **hurdle rates** by product risk category. The more precise measure of economic profit is **Net Income After Cost of Capital (NIACC)** — the bank aims for NIACC-positive pricing.

Deposit pricing objectives include managing inflow volumes, minimising the marginal cost of new deposits, and supporting the bank's NIM targets. Deposit rates must also factor in the liquidity value of each product type (see [Deposit Pricing](02-deposit_pricing.md)).

## Net Interest Margin Management

**Net interest income (NII)** = interest earned on assets − interest paid on liabilities. **Net interest margin (NIM)** = NII ÷ average interest-earning assets. Banks track NIM by "front book" (new business) and "back book" (existing book) to identify trends, since margins may erode on the front book during competitive growth phases.

Several forces compress NIM over time: competitive pressure reduces loan spreads during economic expansions; credit losses increase during recessions; and rate mismatches between fixed-rate loans and variable-rate deposits create margin exposure when interest rates move. NIM management therefore requires active product design and repricing capability.

Banks must also match the NIM concept to the funding structure. For corporate and investment banking, the **term liquidity premium (TLP)** methodology is essential — treasury charges lending products the true cost of term-matched funding, discouraging cheap short-term funding of long-term assets. For retail banking, the same concept applies but TLP rates must reflect the actual retail deposit mix, not just the wholesale curve, to avoid mispricing loans relative to competitors.

## Price vs Volume Trade-Off

Because banks have large fixed and semi-fixed cost bases (head office, IT, branch networks, central functions), loan pricing cannot be set purely by DCF fundamentals. A bank pricing above market rates risks sub-scale volumes that fail to cover fixed costs; a bank pricing below DCF fundamentals generates volume but destroys value.

The practical approach is:
- Set fundamental (DCF) prices as the floor below which value is destroyed.
- Adjust to market pricing given competitive dynamics.
- Use **credit cut-off scores** to exclude borrowers for whom even risk-adjusted rates are insufficient to break even.
- Price new business at marginal (not fully-loaded) cost for the cut-off decision, but monitor fully-loaded profitability across the portfolio to ensure fixed costs are covered.

This is analogous to the pricing discipline in general insurance and in industrial businesses: volume below the break-even point produces losses, but volume above marginal cost provides contribution to fixed costs even if it does not cover fully-loaded costs.
