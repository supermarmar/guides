---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/counterparty-credit/regulatory-capital
  - difficulty/unknown
  - study-status/new
aliases:
---
# Regulatory Capital (Trading Book)

Most of the credit risk that has been discussed in the banking book originates where assets are held to maturity. The trading book, on the other hand, consists mainly of [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]], but credit risk also originates here. The trading book is primarily made up of shorter-term trades for outcomes such as short-term gains, hedging risk, and placing trades on the market for clients.

For the broader treatment of bank [[03-capital_management|capital management]] (Pillar 1/2/3 framework, buffers, [[tlac|TLAC]]/[[mrel|MREL]]), see [Capital](../../../03-capital_management.md). For the historical evolution of [[bis|Basel]] CCR/CVA reforms, see [Basel / BIS](..\..\..\..\..\..\regulation\international\bis\bis.md). For the mathematical foundations of counterparty exposure measurement (EE, EPE, EEPE, survival curves, Monte Carlo), see [Counterparty Exposures](02-counterparty_exposures.md). For banking book regulatory capital computation (SA, IRB, ASRF), see [Regulatory Capital (Banking Book)](../a-irb_capital/01_introduction/01-context.md). This file focuses on the **computation of regulatory capital for credit risk in the trading book**: CCR and CVA.

## Trading Book Boundary

[[bis|Basel]] defines the boundary between the trading book and banking book quite strictly. An asset is classified as a trading book exposure if it satisfies any of the following:

- Held for short-term gain
- Traded to profit from short-term price movements
- Held to profit from arbitrage
- Held to hedge risks incurred by the above three categories.

Assets included must be financial instruments, foreign exchange (FX), and commodities, and banks must be able to hedge these assets completely (i.e. buy the exact same asset in the opposite direction). Trading book assets measure capital primarily in terms of [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]], but certain assets present credit risk components that must be captured separately.

Trading book exposures are managed actively and held for "trading intent" or short-term gain. Credit risk may occur as the risk of default of the issuer of the securities, as well as in the form of [[02-counterparty_exposures|counterparty credit risk]] — where the counterparty could default before settlement, with the position needing to be replaced at a worse price. However, most securities trade on a delivery-vs-payment (DVP) basis or via Central Clearing Parties (CCPs), so there is little or no settlement risk in exchanging securities and cash.

## Trading Book Assets Containing Credit Risk

[[bis|Basel]] regulation clearly identifies the trading book asset types that produce credit risk:

- **Derivatives** (OTC): Over-the-counter derivatives are bilateral contracts with substantial CCR that must be carefully measured and managed. Exchange-traded derivatives are margined and guaranteed by exchanges, minimising credit risk. For detailed product descriptions of derivatives (swaps, options, forwards), see [Banking Products](../../../05-products.md).
- **Long settlement transactions**: Similar to derivatives but longer term, and thus present higher credit risk due to the extended period over which a counterparty could default.
- **Securities financing transactions (repo)**: Involve counterparties using owned assets to secure funding. If counterparties default, they could lose their assets or make losses on selling assets.

## Netting and Hedging Sets

### Netting

Netting is the offsetting of positive and negative amounts between two counterparties to obtain a net total. In terms of trading book assets such as derivatives, netting agreements allow parties to net the mark-to-market values of their trades so that in the event of default the credit exposure is limited to the net positive value of the total.

Netting agreements are usually formalised under an **ISDA Master Agreement** signed between the parties, which specifies methods for calculating a single settlement amount in the termination currency. The ISDA has obtained legal opinions from major jurisdictions confirming the enforceability of netting. For securities finance transactions, netting is generally executed under the **ICMA Global Master Repurchase Agreement**.

Benefits of netting:

- Reduction in capital requirements as exposures are netted
- Reduction in the volume and size of payments, reducing costs and administration
- Netting upon default reduces the complexity of recoveries (only the net payment is required)
- Reduced exposures may allow banks to do more business within regulatory limits

### Netting Sets

A **netting set** refers to all transactions that fall under the same netting agreement between two counterparties. The capital calculation for CCR is performed at the netting set level. In the figure below (from the F107 textbook), Bank A and Bank B have three transactions (100, 50, 75). Without netting, there are three separate payments. With a netting agreement, only the net amount (125 to Bank B) is exchanged — simplifying capital requirements and settlement.

### Hedging Sets

A **hedging set** is a set of transactions within an asset class in the same netting set that are partially or fully offset against one another for capital requirement purposes. Whereas a netting set is a legal agreement and is used to aggregate transactions, hedging sets are used in the calculation of capital directly where exposures are calculated. Hedging set types are:

- Each currency for interest rate transactions
- Each currency pair for FX transactions
- Credit transactions (e.g. CDS)
- Equity transactions (e.g. equity swap)
- Commodity transactions (depending on commodity type)
- Basis transactions (e.g. 3-month vs 6-month reference rate)
- Volatility transactions (e.g. volatility swap)

## [[02-counterparty_exposures|Counterparty Credit Risk]] (CCR)

[[02-counterparty_exposures|Counterparty credit risk]] (CCR) is a risk type that borders between market and credit risk. It is the risk that a counterparty to a trade defaults before settlement. CCR is subject to both the creditworthiness of the counterparty to the trade and general market changes that may affect the trade. It is important to note that CCR is applicable in cases where there is a bilateral risk of loss — i.e. either party to a transaction could default.

For example, in a derivative trade, if the market moves and this negatively impacts either counterparty, either counterparty could default. This means that the party that would have benefited from a positive position essentially loses that benefit. This is unlike a mortgage, for example, where the bank only considers the unilateral risk of the borrower defaulting.

CCR encompasses OTC and exchange-traded derivatives, and long settlement and securities financing transactions. For the CCR capital charge, the primary concern is estimating the **EAD** (Exposure at Default) of the transaction in question. The PD and LGD of a counterparty are calculated as per the internal processes in the bank for [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]], but the EAD is calculated according to a different methodology from other credit risk and [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] exposures.

[[basel_framework|Basel III]] allows for banks to use either the **SA-CCR** (standardised approach for CCR) or the **IMM** (Internal Model Method) approach to calculate this EAD estimate. The SA must be used if the bank does not have regulatory approval for the IMM.

### Standardised Approach (SA-CCR)

The SA-CCR is applied according to the following formula:

$$EAD = 1.4 \times (RC + PFE)$$

Where:

- **Replacement cost (RC)**: The cost incurred, or loss, if a counterparty had to default and the transaction had to be replaced immediately. RC is calculated at the **netting set level**.
- **Potential future exposure (PFE)**: The cost incurred, or loss, between the point of default and the initiation of a new transaction. PFE is calculated for each **asset class (hedging set) within the netting set**, then aggregated over the netting set.

The replacement cost also depends on whether or not transactions in a netting set are **margined** or **unmargined**:

- **Unmargined transactions**: The source of larger CCR since there is little to no collateral. If collateral is held, it does not fluctuate according to market movements (no margining requirements).
- **Margined transactions**: Lower risk, as collateral is posted and updated with market movements. However, margining only limits losses — it does not mitigate them entirely.

Swaps, foreign exchange and interest rate forwards, options, other derivatives, and securities finance transactions (repo) are all subject to fluctuations in value over the life of the contract. Besides replacement cost, credit [[04-risk_measurement|risk measurement]] must consider PFE as the maximum expected credit exposure. PFE is important because some transactions have longer maturities where losses may emerge over time, and positions with large downsides in extreme markets (e.g. options sold) are more fully captured.

The alpha factor of 1.4 in the SA-CCR formula is a regulatory scaling factor designed to provide a conservative estimate, accounting for the uncertainty in the model and the tendency for exposures to be correlated with default events (wrong-way risk). For the mathematical underpinning of exposure measurement (including EE, EPE, and EEPE), see [Counterparty Exposures](02-counterparty_exposures.md).

### Internal Model Method (IMM)

The IMM approach can be used by banks where both regulatory approval is received and the IMM is used for [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] (either the SA or IRB can be used for credit risk). The IMM approach is applied according to the following formula:

$$EAD = 1.4 \times EEPE$$

Where **EEPE** (Effective Expected Positive Exposure) is the weighted average over time of the Effective Expected Positive Exposure of a netting set, weighted according to the date at which the last transaction matures (capped at 1 year). The mathematical derivation of EEPE from EE and EPE, and the Monte Carlo methodology typically used to compute it, is covered in [Counterparty Exposures](02-counterparty_exposures.md).

Under the IMM approach, a specific modelling approach is not prescribed but is left to the discretion of the bank, subject to regulatory approval.

## Credit Valuation Adjustment (CVA)

Credit valuation adjustments (CVA) were introduced as part of [[basel_framework|Basel III]], with further amendments finalised in 2019. CVA forms part of [[01-risk_management|risk management]] alongside CCR and is essentially a capital charge to cover mark-to-market losses from counterparty credit deterioration — which were twice as large as CCR losses from defaults in the 2007–09 financial crisis.

A CVA is applied to eligible trading book assets where a loss may be incurred owing to a reduction in the **creditworthiness** of the counterparty — i.e. a CVA incorporates default risk into capital calculations for trading book assets. Assets will generally decline in value if the creditworthiness of the counterparty declines, which is a risk of loss that the CVA capital charge attempts to cater for.

Transactions through a recognised **central counterparty (CCP)** (e.g. a central clearing house for derivatives) are exempted by [[bis|Basel]].

CVA capital charges are first assessed on an **individual client/counterparty level**, then on an **aggregate portfolio level**. The entire portfolio eligible for this charge is assessed after adjustments for:

- Netting
- Collateral
- Offsetting internal and external hedges.

By allowing for these adjustments, [[bis|Basel]] aims to incentivise banks to follow efficient [[01-risk_management|risk management]].

[[bis|Basel]] outlines three approaches for the calculation of capital requirements for CVA risk:

| Approach | Description |
|---|---|
| **BA-CVA (reduced)** | For banks not actively utilising hedges against CVA risk. All banks must calculate this as it feeds into the other approaches. |
| **BA-CVA (full)** | Accounts for hedging against counterparty credit spreads (e.g. credit default swaps). |
| **SA-CVA** | More complex than BA-CVA; requires regulatory approval and a dedicated CVA desk. |

### Basic Approach (BA-CVA)

Banks may use either the reduced or full BA-CVA, depending on their [[01-business_model|business model]].

**Step 1 — Individual counterparty capital requirement:**

For each counterparty $c$, $SCVA_c$ is calculated. The components of $SCVA_c$ include regulatory-defined parameters such as: risk weights, EAD, discount factors, and effective maturity.

**Step 2 — Portfolio aggregation:**

$$K_{\text{reduced}} = \sqrt{\left(\rho \cdot \sum_c SCVA_c\right)^2 + (1-\rho^2) \cdot \sum_c SCVA_c^2}$$

Where $\rho = 50\%$ reflects the correlations between individual counterparties' credit spreads.

**Step 3 — Capital charge:**

$$C_{\text{reduced}} = 0.65 \times K_{\text{reduced}}$$

$$C_{\text{full}} = 0.25 \times K_{\text{reduced}} + 0.75 \times K_{\text{hedged}}$$

Where $K_{\text{hedged}}$ is calculated similarly to $K_{\text{reduced}}$, but the effects of hedging (e.g. CDS used to hedge CVA risk) are incorporated. The full BA-CVA may benefit from hedging, but this benefit is limited by the weighting between reduced and full capital, ensuring an adequate capital floor is maintained.

### Standardised Approach (SA-CVA)

The SA-CVA is adapted from [[bis|Basel]]'s [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] standardised approach and is much simpler than an internal model approach, but requires more sophisticated infrastructure. To use the SA-CVA, banks must meet the following criteria:

- Ability to calculate and report capital and CVA sensitivities to [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] factors on **at least a monthly basis**
- A dedicated **CVA desk** that will manage and, if necessary, hedge CVA risk.

Under the SA-CVA, individual counterparty capital requirements are determined using internal estimates of:

- **PD**: Market-implied PDs estimated from credit spreads observable in the market, or from proxy credit spreads for illiquid counterparties. For the derivation of market-implied PDs from credit spreads and survival curves, see [Counterparty Exposures](02-counterparty_exposures.md).
- **LGD**: Market-implied LGDs estimated using credit spreads in line with the estimation of PDs (credit spreads inherently contain both PD and LGD, so the estimation of one leads to the estimation of the other).
- **Discounted future exposure**: Determined by discounting all future transactions within the counterparty using a risk-free interest rate and relevant [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] factors. Collateral may be taken into account for margined counterparties.

Alongside the quantitative elements of capital calculation, [[basel_framework|Basel III]] includes enhanced management requirements for policies, processes, reporting, and testing for CVA risk, similar to those for credit risk.
