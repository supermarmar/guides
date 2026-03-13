# Model Methodology

Methods used to estimate the LGD for credit facilities fall into one of two categories.

- Subjective methods are primarily driven by expert judgement and used mainly on portfolios with few defaults and/or by banks in the early stage of internal model development.
- Objective methods largely rely on formal mathematical procedures and can be further divided into two methods. The decision to select one of these objective methods is largely driven by the nature of portfolio, exposure type (e.g. loan vs bond), and the availability of data.
  - Explicit methods, i.e. the market LGD approach and workout LGD approach
  - Implicit methods, i.e. the implied market LGD approach.

## Implied Market LGD Approach

Two separate LGD models were developed:

- LGD1: applicable to the non-defaulted (performing) book; and
- LGD2: applicable to the defaulted (non-performing) book.

The overall model methodology decomposes LGD into probability and severity components. Risk differentiation is achieved via a segmented set of logistic regression and generalised linear model (CLM) components. Internally this step is referred to as risk differentiation, and the outputs referred te as Point in Time (PiT) LGDs.

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

PiT LCDs are grouped into risk grades. In line with regulatory requirements, each risk grade was calibrated to the empirically observed Long Run Average (LRA) and Downturn (DT) loss given default. Appropriate Adjustments (AA) and where applicable. Margin of Conservatism (MoC) were added to account for residual uncertainties in estimates, to return a final regulatory LGD. Internaily the calibration step is referred to as risk quantification.