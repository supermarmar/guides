---
tags:
  - application/banking/internal-environment/risk-management/pillar-2-modelling/economic-capital
  - difficulty/unknown
  - study-status/new
aliases:
---
# Economic Capital (Banking Book)

Economic capital is internally calculated by the bank and is a measure of the bank's total risk as they see it, without reference to regulatory prescriptions. It is calculated as part of the Internal Capital Adequacy Assessment Process (ICAAP) and represents the amount of capital a bank believes it needs based on its own [[02-risk_appetite|risk appetite]] and strategy.
## Pillar 2A

Pillar 2A captures risks not fully covered by Pillar 1. The bank must quantify its own capital requirement for each material risk type. The following are the main Pillar 2A risk categories, each with its typical quantification approach.

### [[02-irrbb_sources|Interest Rate Risk in the Banking Book]] ([[05-irrbb_measurement|IRRBB]])

[[05-irrbb_measurement|IRRBB]] is the risk that changes in interest rates affect the bank's economic value or earnings. It is not captured in Pillar 1 credit or [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] RWAs (which are limited to the trading book). Under Pillar 2A, banks must quantify [[05-irrbb_measurement|IRRBB]] using two complementary perspectives:

#### Economic Value of Equity (EVE)

The EVE perspective measures the sensitivity of the present value of all future cash flows to changes in interest rates. A shock to the yield curve changes the value of fixed-rate assets and liabilities:

$$\Delta\text{EVE} = -\sum_i \Delta \text{PV}(\text{cash flows}_i) = -\sum_i \text{MD}_i \cdot \text{PV}_i \cdot \Delta r_i$$

where $\text{MD}_i$ is the modified duration of position $i$ and $\Delta r_i$ is the interest rate shock. The [[bis|Basel]] Committee specifies six standardised interest rate shock scenarios (parallel up/down, steepener, flattener, short-up, short-down). The Pillar 2A capital charge is based on the most adverse $\Delta\text{EVE}$ across scenarios. A bank is deemed an outlier if $|\Delta\text{EVE}| > 15\%$ of Tier 1 capital for a 200bp parallel shock.

#### [[04-nii_nim|Net Interest Income]] ([[04-nii_nim|NII]]) Sensitivity

The [[04-nii_nim|NII]] perspective measures the sensitivity of near-term (typically 1–2 year) interest income to rate changes. Unlike EVE, which captures the long-run economic value, [[04-nii_nim|NII]] focuses on short-term earnings volatility. Banks typically model [[04-nii_nim|NII]] sensitivity using assumptions about:

- **Repricing gaps**: The mismatch between assets and liabilities repricing at different dates.
- **Behavioural adjustments**: Non-maturity deposits (e.g., current accounts), prepayment options on mortgages, and pipeline hedges.
- **New business assumptions**: Whether modelled on a static or dynamic balance sheet basis.

$$\Delta\text{NII} = \sum_i \text{GAP}_i \cdot \Delta r_i \cdot \text{tenor}_i$$

where $\text{GAP}_i$ is the repricing gap for bucket $i$, $\Delta r_i$ is the rate shock, and $\text{tenor}_i$ is the fraction of the year the gap is open.