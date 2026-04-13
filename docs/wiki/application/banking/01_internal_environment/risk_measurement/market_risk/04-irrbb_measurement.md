---
tags:
  - application/banking/internal-environment/risk-measurement/market-risk/irrbb-measurement
  - difficulty/unknown
  - study-status/new
aliases:
---
# IRRBB Measurement: PV01, EVE, and EaR

As a result of maturity transformation and intermediation, banks run significant structural mismatches between their assets and liabilities. Before calculating IRRBB measures, the bank must set assumptions regarding the duration of assets and liabilities and how these change under different interest rate scenarios (e.g. increased withdrawals on non-maturity deposits as rates increase). These assumptions can significantly influence the IRRBB calculated, so proper modelling is essential before applying the measures below.

The standard starting point is **gap analysis**, which groups assets and liabilities into contractual or behavioural maturity buckets (1 day, 1 week, 1 month, etc.). Floating rate obligations are measured by their next repricing date rather than final maturity, as interest rate risk analysis requires repricing dates. The mismatch in each bucket is calculated; modified duration formulas are then applied to calculate price sensitivity.

Limitations of gap analysis:
- It is a snapshot at a point in time and does not incorporate future developments in the balance sheet.
- Interest rate changes do not always occur uniformly across the yield curve.
- Asset performance (loan losses, rescheduling) is uncertain.
- Customer optionality exercise may or may not be linked to interest rate movements.
- Gap periods are arbitrary.

## PV01 / Interest Rate Shift Method

The interest rate shift method considers the impact on the **net present value (NPV)** of expected cashflows of the banking book's assets less liabilities due to a shift in the yield curve. The **PV01** (also called DV01, PVBP, or IR Delta) measures the change in NPV from a 1 basis point change in interest rates.

```math
\text{PV01} = \text{NPV}(\text{base} + 1\text{bp}) - \text{NPV}(\text{base})
```

The position is described as **paid** (for liabilities) or **received** (for assets), or by the varying legs of an interest rate swap.

**Example** — a match-funded balance sheet (R100m 5-year bullet asset at 10%, R100m 5-year bullet liability at 8%):

| Interest Scenario | Assets (Rm) | Liabilities (Rm) | Net NPV (Rm) | PV01 |
|---|---|---|---|---|
| Base | 17.79 | −14.71 | 3.0844 | — |
| Base + 1bp | 17.75 | −14.67 | 3.0794 | −0.0050 |
| Base − 1bp | 17.83 | −14.74 | 3.0894 | +0.0100 |

Based on the results, the NPV decreases by 0.16% for a 1bp parallel increase in rates.

**Limitations:** only considers parallel curve shifts; does not provide tenor-specific sensitivity insight.

**Enhancement — bucketed PV01:** Decompose the PV01 across maturity buckets (e.g. 1–3m, 3–6m, 6–12m, 1–2y, 2–3y, 3–4y, 4–5y) to understand which tenor contributes most to rate sensitivity, and to allow non-parallel shifts to be modelled.

## Economic Value of Equity (EVE)

The EVE is the net present value of all cashflows from the banking book's assets and liabilities (including off-balance sheet items), assuming all positions run off to maturity.

```math
\text{EVE} = PV(\text{Assets}) - PV(\text{Liabilities})
```

```math
PV(\text{Assets}) = \sum_t CF_t^A \cdot V_t \qquad PV(\text{Liabilities}) = \sum_t CF_t^L \cdot V_t
```

where $V_t$ is the discount factor at time $t$.

**Treatment of equity capital:** the bank's equity (ordinary shares, preference shares, retained earnings) represents interest-free, perpetual funding. Including it as-is can distort the EVE calculation. It can be split into maturity buckets that roll off with assets, with a fixed rate cost assigned to each bucket.

**Liability-sensitive bank example** (assets have longer duration than liabilities — funding long-term fixed/long-repricing-period assets with short-term liabilities): when interest rates increase:
1. [[03-nii_nim|NII]] is squeezed as the cost of liabilities increases while asset yields stay fixed for an extended period.
2. From a behavioural perspective, customers have reduced incentive to prepay loans (as alternatives have higher yields), further increasing asset duration.
3. Higher discount rates reduce the PV of forecasted cashflows.

All three effects reduce the EVE as rates increase.

**Key trade-off:** stabilising [[03-nii_nim|NII]] (earnings) vs stabilising EVE involves opposing structural positions. A bank needs to consider both perspectives when managing IRRBB. [[basel_framework|Basel III]] requires banks to measure the impact of interest rate shocks on EVE (six prescribed shock scenarios) and [[03-nii_nim|NII]] (two shock scenarios) as part of [[02-stress_testing|Pillar 2]] supervisory review.

## Earnings at Risk (EaR)

The earnings perspective focuses on how rate changes affect the bank's [[03-nii_nim|NII]] and earnings over a given time horizon (typically short to medium term, not more than 2 years). Accuracy of the forecast decreases as the time horizon increases.

### Step 1: Re-pricing Gap Analysis

The re-pricing gap analysis allocates assets and liabilities into pre-defined time bands based on when they mature or reprice (for variable rate instruments, the repricing date is used). This implicitly assumes a **static balance sheet** (assets and liabilities are replaced as they mature).

**Example — 1-year re-pricing gap in 3-month bands:**

| Time band | Total | 0–3m | 3–6m | 6–9m | 9–12m |
|---|---|---|---|---|---|
| Assets (Rm) | 90 | 40 | 10 | 15 | 25 |
| Liabilities (Rm) | 100 | 60 | 25 | 5 | 10 |
| Re-pricing gap (Rm) | −10 | −20 | −15 | +10 | +15 |

The bank has R10m more liabilities repricing over the next 12 months than assets. An interest rate increase will therefore reduce [[03-nii_nim|NII]] over this period, as more liabilities reprice to higher rates than assets.

### Step 2: [[03-nii_nim|NII]] Sensitivity

Given a change in rates, the [[03-nii_nim|NII]] sensitivity in each time band is:

```math
\text{NII Sensitivity} = \frac{\text{Re-pricing gap} \times \text{Remaining term (months)} \times \Delta r}{12}
```

**Example — 100bp rate increase:**

| Time band | Gap (Rm) | Remaining term (months) | Rate change (bps) | [[03-nii_nim|NII]] Sensitivity (R) |
|---|---|---|---|---|
| 0–3m | −20 | 12 | 100 | −200,000 |
| 3–6m | −15 | 9 | 100 | −112,500 |
| 6–9m | +10 | 6 | 100 | +50,000 |
| 9–12m | +15 | 3 | 100 | +37,500 |
| **Total** | **−10** | | | **−225,000** |

A 100bp increase in rates reduces [[03-nii_nim|NII]] by R225,000 over the following year.

The analysis can be enhanced by allowing for: a dynamic balance sheet (new business volumes, new products, funding plan changes); gradual rate increases; pricing time lags; and behavioural assumptions (prepayments, withdrawal behaviour as rates change).

### Step 3: Earnings at Risk (EaR)

The final step introduces a stochastic element. An appropriately calibrated stochastic interest rate process (e.g. the Vasicek model) is used to generate a distribution of potential interest rate scenarios at a given confidence level. Monte Carlo simulations then produce a distribution of [[03-nii_nim|NII]] changes over the time horizon.

```math
\text{EaR}_{1-\alpha} = \text{VaR}_{1-\alpha}(\Delta\text{NII})
```

EaR is effectively the VaR with respect to the bank's [[03-nii_nim|NII]] for a given confidence level over the time horizon of interest. For example, the 95% EaR is the level such that only 5% of simulations produce a worse [[03-nii_nim|NII]] outcome.
