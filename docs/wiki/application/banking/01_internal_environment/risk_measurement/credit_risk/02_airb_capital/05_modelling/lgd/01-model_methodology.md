---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/modelling/lgd/model-methodology
  - difficulty/unknown
  - study-status/new
aliases:
---
# Model Methodology

Methods used to estimate the LGD for credit facilities fall into one of two categories.

- Subjective methods are primarily driven by expert judgement and used mainly on portfolios with few defaults and/or by banks in the early stage of internal model development.
- Objective methods largely rely on formal mathematical procedures and can be further divided into two methods. The decision to select one of these objective methods is largely driven by the nature of portfolio, exposure type (e.g. loan vs bond), and the availability of data.
  - Explicit methods, i.e. the market LGD approach and workout LGD approach
  - Implicit methods, i.e. the implied market LGD approach.

To calculate estimates of LGDs, first “realised” LGDs must be calculated. These are essentially historical losses on defaulted assets, which can be used to infer estimates of LGDs using varied modelling techniques. There are four objective LGD estimation methods for realised LGDs.

## Explicit Methods

- Market LGD – The LGD is observed from market prices of defaulted bonds and marketable loans soon after default events, i.e. their residual values which indicate the value lost. The main benefit is that actual prices can be used and reflect market views, though data can be scarce. This is the methodology used most by the rating agencies.
  
  >_When appropriate:_ Only usable where a liquid secondary market exists for the defaulted instruments — typically large corporate bonds or leveraged loans. Not applicable for retail or SME portfolios where debt isn't traded.
  
- Workout LGD – The LGD is estimated cashflows from the workout process, based on estimated exposure and a discount rate. Users must monitor the timing of payments received and consider the riskiness of any restructured debt, i.e. expected losses and recoveries are discounted to calculate the estimated LGD. This method requires extensive data.
  $$\text{LGD} = 1 − \frac{\text{PV of Recoveries}}{\text{EAD}}$$
  
  > _When appropriate:_ The most widely used method for **bank loan portfolios** (mortgages, corporate loans, retail). It's backward-looking — you need a historical database of resolved defaults. Requires sufficient history of completed workouts to be statistically credible.
## Implicit Methods

- Implied market LGD – The LGD is derived from prices of bonds deemed to be high risk (but not defaulted), where the credit spreads are used in the estimation process. A credit spread between a risk-free and a risky bond will indicate the risk premium, which can be used to determine an implied LGD if the PD is already known (or can be estimated). This is the least developed of the methods but has the benefit of a large pool of market data and is often used within the derivative space.
  
  > _When appropriate:_ Useful when you have **market prices but no default history** — for example, investment-grade corporates that rarely default. It's forward-looking (market-implied) rather than historical. Less reliable because it bundles risk premium into the estimate.
  
- Implied historical LGDs – The LGD is estimated using long-term historical average losses for similar asset types. [[bis|Basel]] requires current information to be used where available to supplement this method, and only allows for this method to be used in a retail context.
  
  > _When appropriate:_ Applied when a bank lacks resolved individual workout data but has **pooled historical loss experience** — common in retail portfolios (credit cards, personal loans) where defaults are frequent but individual recovery tracking is difficult.

The above estimation methods may be subject to various assumptions and approximations, depending on the individual bank and regulators. For example, the Workout LGD method may involve using aggregate portfolio losses and recoveries, or even assuming all recoveries and losses are incurred at the write-off date. The discount rate that should be used is a subject of debate, and if regulators do not prescribe this, most banks follow best practice in the industry or set this rate internally. Once the realised LGDs have been calculated, or estimated, various methodologies can be used to estimate LGDs on current exposures. These methods would be in line with those used for PD.

Consideration must be given to collateral treatment when modelling LGDs. [[bis|Basel]] outlines steps banks should take to incorporate collateral, and a conservative view is recommended. Collateral providers can also default, or collateral can take a long time to access, so collateral does not mean losses can be offset entirely.

## Workout LGD Approach

Two separate LGD models are developed:

- LGD1: applicable to the non-defaulted (performing) book; and
- LGD2: applicable to the defaulted (non-performing) book.

The overall model methodology decomposes LGD into probability and severity components. [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/05_modelling/pd/03-risk-differentiation|Risk differentiation]] is achieved via a segmented set of logistic regression and generalised linear model (CLM) components. Internally this step is referred to as [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]], and the outputs referred the as Point in Time (PiT) LGDs.

The modelled components comprise:

- Estimating the probability of an account being classified into one of these payer types (zero/partial/full payment); and
- The estimated recovery rate for each payer type to be assigned
An account-level CLM framework with relevant dependent variable distributions for each component in the reference data were used to capture the underlying risk drivers.

The non-modelled components consist of implied probabilities achieved via a "one minus" formula, as well as 0% and 100% undiscounted recovery rate assumptions for zero and full payers. The 100% undiscounted recovery rate is adjusted downwards to account for the effect of discounting.

These modelled and non-modelled components are then combined to produce the PiT LGD estimates:

```math

LGD = 1-[(R_{\text{Zero}} + R_{\text{Full}} + R_{\text{Partial}})+E[r({\text{Debt Sale})}]-\text{CoR}]
```

where:

```math
R_{\text{Zero}} = P(\text{Zero}) \times E[r(\text{Zero})]
\\ 
R_{\text{Full}} = (1-P(\text{Zero})) \times P(\text{Full}) \times E[r(\text{Full})]
\\
R_{\text{Partial}} = (1-P(\text{Zero})) \times (1-P(\text{Full}))) \times E[r(\text{Partial})])
```

- $P(\text{Zero})$ is the probability of zero percent recoveries given default. This is determined as the unconditional probability of an account having zero repayments over a 24-month post default observation period.
- $E(r(\text{Zero}))$ expected recovery rate given Zero Payer i.e. net discounted recovery rate excluding costs conditional on the account making zero percent recoveries and staying in default. This was set to 0% when applying the model.
- $P(\text{Full})$ The probability of paying in full (100% or more recoveries) given default. This is determined as the conditional probability on the account not being a Zero Payer.
- $E(r(\text{Full}))$ Expected recovery rate given Full Payer i.e. the expected net discounted recovery rate excluding costs, conditional on the account paying in full.
- $E(r(\text{Partial}))$ Expected recovery rate given Partial Payer, where Partial Payer means the account is neither Zero Payment or Full Payment i.e. net discounted recovery rate excluding costs, conditional on the account making some recoveries but neither paying in full nor curing throughout the model outcome window.
- $E[r({\text{Debt Sale})}]$ The expected recovery rate from debt sale proceeds.
- $\text{CoR}$ The total estimated direct and indirect cost of recoveries.

PiT LCDs are grouped into risk grades. In line with regulatory requirements, each risk grade was calibrated to the empirically observed Long Run Average (LRA) and Downturn (DT) loss given default. Appropriate Adjustments (AA) and where applicable. Margin of Conservatism (MoC) were added to account for residual uncertainties in estimates, to return a final regulatory LGD. Internaily the calibration step is referred to as [[07-risk_quantification|risk quantification]].