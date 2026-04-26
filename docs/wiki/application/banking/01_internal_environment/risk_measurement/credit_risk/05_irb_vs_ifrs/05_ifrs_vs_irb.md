---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/ifrs9-impairments/introduction/ifrs-vs-irb
  - difficulty/unknown
  - study-status/new
aliases:
---
# [[ifrs9_standard|IFRS 9]] vs IRB

Banks around the globe leverage their well-established IRB models as starting point to satisfy the [[ifrs9_standard|IFRS 9]] modelling needs. The IRB PD, LGD and EAD parameters are typically TTC with some flooring and Margin of Conservatism (MoC) added. [[ifrs9_standard|IFRS 9]] requires the use of forward looking PIT parameters or conditional FiT parameters. The outcome of the IRB models is adjusted for [[ifrs9_standard|IFRS 9]] purposes to reflect forward looking and macro-economic information.

IRB models will be designed and implemented to estimate PDs and LGDs in order to calculate capital requirements. [[ifrs9_standard|IFRS9]] models are designed to estimate PDs and LGDs in order to calculate provision requirements. It should be noted that, though the purposes and calculations may differ, many banks choose to combine elements of the modelling process for these different risk parameters in order to reduce costs.

The level of provisions will not necessarily affect capital requirements but will affect the amount of capital available to meet these requirements.

## Standards & Setters

- IRB: Based on [[bis|Basel]] Accords created by [[bis|BIS]]. Specific approaches and guidance per asset class.
- [[ifrs9_standard|IFRS 9]]: Based on [[ifrs9_standard|IFRS9]] accounting regulation produced by IASB. Guidance and different approaches based on business models and cash flow characteristics of the assets.

## Purpose

- IRB: Focused on estimation of PDs and LGDs for use in the calculation of regulatory capital requirements. Focused on identifying possible defaults on assets and setting aside capital for these. Ensures banks can estimate and prepare for unexpected losses.
- [[ifrs9_standard|IFRS 9]]: Focused on estimation of PDs and LGDs for use in the calculation of regulatory provision requirements. Focused on identifying impaired assets and setting aside provisions for these. Ensures banks can estimate and prepare for expected losses.

## Data

- IRB: Explicit data requirements (e.g. 7 years for non-retail exposures)
- [[ifrs9_standard|IFRS 9]]: Data requirements are outcomes-focused and not explicit

## Modelling Methodology

- IRB: Multiple modelling approaches, including both FIRB and AIRB approaches. A more conservative approach is used to estimate losses, including the use of floors outlined in the IRBA.
- [[ifrs9_standard|IFRS 9]]: A general or simplified approach is possible. A best-estimate basis is used to estimate losses, over multiple economic scenarios.

## PDs

- IRB: Combinations of PIT and TTC PDs used when estimating default within the next 12 months
- [[ifrs9_standard|IFRS 9]]: PIT PDs estimating default within the next 12 months (Stage 1) or over the remaining lifetime (Stage 2/3).

## LGD

- IRB: Downturn LGDs used to estimate expected losses, using conservative scenarios, and these include both direct and indirect costs related to recoveries. Floor on certain types of assets.
- [[ifrs9_standard|IFRS 9]]: “PIT” LGDs used to estimate losses, using a range of economic scenarios, and these include only direct costs related to recoveries. No floor.

## EAD

- IRB: Amortization not included.
- [[ifrs9_standard|IFRS 9]]: Model includes expected lifetime changes in the balance outstanding that are permitted by the contractual terms: amortization, repayments and (partial) prepayments.

## Outpus

- IRB: Outputs of models to be used to calculate risk-weighted assets (RWAs), and risk parameters to be refreshed annually
- [[ifrs9_standard|IFRS 9]]: Outputs of models to be used to calculate expected [[02-credit_losses|credit losses]] (ECLs) on an ongoing, continuous basis

## AFS

- IRB: Capital estimates will primarily affect the balance sheet statement.
- [[ifrs9_standard|IFRS 9]]: Provisions will affect the balance sheet and income statement, primarily profit and loss

## Disclosures

- IRB: Specific disclosures detailed (e.g. ICAAP), primarily within risk-based functions
- [[ifrs9_standard|IFRS 9]]: Detailed disclosures requiring linkages between risk and accounting / finance functions