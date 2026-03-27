# [[05-market_risk|Market Risk]] Capital in the Trading Book

To comply with the minimum capital requirements for [[05-market_risk|market risk]] set by the [[bis|BCBS]], a bank may choose between two methodologies: the **standardised approach** and the **internal models approach (IMA)**. The methodology chosen must be approved by national authorities (in South Africa, the [[sarb|SARB]]).

## Standardised Approach

The capital requirement under the standardised approach is the sum of three components:

```math
K_{\text{SA}} = K_{\text{SBM}} + K_{\text{DRC}} + K_{\text{RRAO}}
```

### Sensitivities-Based Method (SBM)

The SBM capital requirement is calculated by aggregating three risk measures: **delta**, **vega**, and **curvature**.

- **Delta** — a risk measure based on sensitivities to regulatory delta risk factors (the sensitivity of an option portfolio to the price change of the underlying asset: equity, FX, commodity, or interest rates).
- **Vega** — a risk measure based on sensitivities to regulatory vega risk factors (the sensitivity of an option portfolio to changes in underlying volatility).
- **Curvature** — captures the incremental risk not captured by delta for price changes in options. Based on two stress scenarios — an upward shock and a downward shock to each regulatory risk factor. Colloquially known as gamma in Greek sensitivity parlance.

For each risk class, the bank determines the sensitivity of trading book instruments to a set of risk factors (interest rate, equity, FX, etc.), risk-weights those sensitivities, and aggregates them separately for delta and vega risk.

### Default Risk Capital (DRC)

The DRC is intended to capture **jump-to-default (JTD)** risk that may not be captured by credit spread shocks under the SBM. The process for each risk class:

1. Compute gross JTD risk for each exposure separately. Net long and short JTD amounts for the same obligor. Allocate net JTD risk positions to buckets. Within each bucket, calculate a hedge benefit ratio (from net long and short JTD positions) as a discount factor that reduces the netting of short positions against long positions.
2. Aggregate bucket-level DRC requirements as a simple sum across buckets.

### Residual Risk Add-On (RRAO)

The RRAO is calculated for all instruments bearing residual risk, in addition to other components:

1. RRAO = simple sum of gross notional amounts of instruments bearing residual risks × risk weight.
2. Risk weight for instruments with an **exotic underlying** = **1.0%**.
3. Risk weight for instruments bearing **other residual risks** = **0.1%**.

## Internal Models Approach (IMA)

The use of internal models to determine [[05-market_risk|market risk]] capital is conditional on explicit supervisory approval. This approval requires at minimum:

1. The supervisory authority is satisfied that the bank's [[01-risk_management|risk management]] system is conceptually sound and implemented with integrity.
2. The bank has a sufficient number of staff skilled in sophisticated models — not only in trading but also in risk control, product control (finance), audit, and back office.
3. The bank's trading desk [[01-risk_management|risk management]] model has a proven track record of reasonable accuracy in measuring risk.
4. The bank regularly conducts stress tests.
5. Positions included in the bank's internal models are held in trading desks approved for the use of those models.

The bank must maintain a documented set of internal manuals, policies, controls, and procedures. Models must be validated by suitably qualified parties independent of model development, both at initial development and when any significant changes are made, and revalidated periodically.

A bank intending to use the IMA must conduct and successfully pass **back-testing** at the bank-wide level and both **back-testing** and **P&L attribution** at the trading desk level.

Expected shortfall (see [VaR Limitations](07-var_limitations.md)) plays a key role in setting [[05-market_risk|market risk]] capital under the IMA.

## Revised [[05-market_risk|Market Risk]] Framework (FRTB — effective 1 January 2023)

The **Fundamental Review of the Trading Book (FRTB)** is a set of [[bis|BCBS]] proposals transforming [[05-market_risk|market risk]] capital requirements.

### Three Key Areas of the Revised Framework

**1. Updated banking/trading book boundary** — in an attempt to discourage arbitrage of regulatory capital requirements between the two books, the split has been updated and made more explicit. Instruments are assigned to the trading book or banking book at inception based on clearly defined intent criteria.

**2. Updated internal models approach** — updated to ensure risks are better captured (specifically tail risks and illiquidity risks); models are approved at a more detailed level (trading desk level); and limits are placed on the impact of hedging and diversification on capital requirements.

**3. Updated standardised approach** — revised to remain fit for purpose for banks with little trading activity, while remaining a reliable floor and alternative to the IMA, and being sufficiently risk-sensitive.

### FRTB Key Points

- **Trading/banking book boundary** — reduces incentives for regulatory capital arbitrage between the two books.
- **Credit treatment** — securitised and non-securitised products are treated differently.
- **Risk measure** — the move from VaR to **expected shortfall**, so that tail risk is better captured.
- **IMA vs SA alignment** — large differences in capital calculations between IMA and SA users are to be reduced; FRTB seeks to align them.
- **Revised SA** — provides a method for banks with business models not requiring sophisticated [[05-market_risk|market risk]] measures.
- **FRTB goes live** from 1 January 2023, replacing VaR with expected shortfall, which will most likely increase bank capital charges.
