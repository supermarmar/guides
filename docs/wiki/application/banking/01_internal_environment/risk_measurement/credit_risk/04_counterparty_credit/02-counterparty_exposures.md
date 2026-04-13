---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/counterparty-credit/counterparty-exposures
  - difficulty/unknown
  - study-status/new
aliases:
---
# Counterparty Exposures

This file covers the **mathematical foundations of counterparty exposure measurement** used in trading book CCR capital calculation, including the exposure metric definitions (EE, EPE, EEPE), the derivation of market-implied probability of default from credit spreads and survival curves, and the simulation approaches used to compute these exposures.

For the regulatory capital formulas that consume these exposure measures (SA-CCR, IMM, BA-CVA, SA-CVA), see [Regulatory Capital (Trading Book)](wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/04_counterparty_credit/01-regulatory_capital.md). For the analogous mathematical foundations for banking book credit risk (Vasicek model, loss distributions, TTC PDs), see [Credit Losses](..\..\02_airb_capital_modelling\01_introduction\02-credit_losses.md). For the historical evolution of [[bis|Basel]]'s CCR/CVA framework, see [Basel / BIS](..\..\..\..\..\..\regulation\international\bis\bis.md).

## Exposure Concepts

The exposure of a netting set changes over time as market conditions change. Unlike a loan (where EAD is relatively stable), the exposure of a derivatives portfolio can fluctuate dramatically with market moves. The following hierarchy of exposure metrics is used in counterparty credit risk modelling.

### Expected Exposure (EE)

The **Expected Exposure (EE)** of a netting set is the average exposure at any future date $t$, capped at the date at which the last transaction matures or 1 year, whichever is earlier:

$$EE(t) = E[\max(V(t), 0)]$$

where $V(t)$ is the mark-to-market value of the netting set at future time $t$ from the perspective of the bank. Only positive values matter — if the mark-to-market is negative, the bank has no exposure (the counterparty owes us nothing). The exposure distribution takes multiple [[05-market_risk|market risk]] factors into account, such as interest rates, FX rates, equity prices, and commodity prices.

### Expected Positive Exposure (EPE)

The **Expected Positive Exposure (EPE)** of a netting set at a specific date $t$ is the maximum of the Expected Exposure (EE) for that date or any date preceding it:

$$EPE(t) = \max_{s \leq t} EE(s)$$

This non-decreasing transformation prevents the exposure profile from declining over time due to modelling artefacts, reflecting the fact that credit risk does not mechanically decrease as time passes.

### Effective Expected Positive Exposure (EEPE)

The **Effective Expected Positive Exposure (EEPE)** is the weighted average over time of the EPE of a netting set, weighted according to the fraction of time each date represents, capped at 1 year:

$$\text{EEPE} = \sum_{k=1}^{\min(\text{1 year, maturity})} EPE(t_k) \times \Delta t_k$$

where $\Delta t_k$ is the length of the time interval from $t_{k-1}$ to $t_k$.

EEPE serves two important purposes:

- It focuses on out-of-the-money positions that could become credit exposures in the future — capturing potential risk that may not currently exist
- It addresses **wrong-way risk**: the positions of counterparties can be correlated with their probability of default. For example, a bank selling credit protection (CDS) on a reference entity to a counterparty whose own creditworthiness is correlated with the reference entity faces wrong-way risk — the counterparty is most likely to default precisely when the exposure is largest.

The EEPE then feeds into the IMM capital formula:

$$EAD = 1.4 \times EEPE$$

The alpha factor of 1.4 is a regulatory scaling factor that partially accounts for wrong-way risk and model uncertainty.

## Market-Implied Probability of Default and Survival Curves

For CVA capital calculation under the SA-CVA, market-implied PDs and LGDs are required rather than the historical/statistical PDs used in banking book IRB models. These are extracted from observable market prices of bonds and credit default swaps (CDS).

### Credit Spreads and the Default Curve

A **credit spread** is the difference between the rate of return of two investments of similar maturity where the riskiness of the investments differs. Specifically, the credit spread between a risk-free rate (e.g. treasury bond yield) and a risky investment's yield represents the additional return expected by investors for bearing the higher level of risk. This can be interpreted as a combination of PD and LGD:

$$\text{Credit spread} \approx \text{PD} \times \text{LGD}$$

This is the **implied market LGD** — a combined measure rather than a separately estimated quantity. Since credit spreads contain both PD and LGD, estimating one directly implies the other.

**Default curves** are constructed by extracting these credit spreads over risk-free rates. The process — known as **bootstrapping** — uses as many securities and maturity pricing observations as possible in order to gain a full spectrum of implied risk premiums. Assumptions must be carefully made with respect to:

- **Linearity**: Interpolation between sparse data points
- **Discount rates**: The risk-free curve used to discount cash flows
- **Recovery rates**: The assumed LGD used to separate PD from the credit spread
- **Liquidity and volatility**: The contribution of illiquidity premium and volatility to the observed credit spread (these are not related to default risk and must be stripped out)

### Default Intensity (Hazard Rate)

The **default intensity** (or hazard rate) $\lambda(t)$ is the instantaneous probability of default per unit time for each time period $t$. It is the primary quantity estimated from credit spreads during bootstrapping. From the hazard rate, two complementary curves are derived:

- **Cumulative probability of default**: The probability that default occurs by time $t$:

$$PD(t) = 1 - \exp\left(-\int_0^t \lambda(s)\, ds\right)$$

- **Survival curve**: The probability that the counterparty has not defaulted by time $t$:

$$S(t) = \exp\left(-\int_0^t \lambda(s)\, ds\right) = 1 - PD(t)$$

The two curves are exactly inverse to each other. Investors generally demand relatively higher premiums for lower-rated credits earlier along the curve (implying **increasing default intensity with time** for investment grade names), while distressed names may show declining hazard rates if market participants expect an early resolution.

### Bond Prices vs CDS Prices

In practice, modellers use bond prices or CDS prices (rates of return) to construct these curves:

- **CDS prices** are more directly linked to credit risk. The purpose of a CDS is essentially to trade credit risk, so the risk premium is more closely linked to the risk of default without the confounding liquidity and market structure effects present in bond markets.
- **Bond prices** require additional assumptions to strip out factors affecting prices that are not directly related to the risk of default (e.g. liquidity premium, tax effects, repo specialness).

For this reason, CDS prices are the preferred input for survival curve construction where available. For illiquid counterparties with no observable CDS, proxy credit spreads from comparable entities are used.

## Closed-Form Approximations vs Monte Carlo Simulation

### Closed-Form Approximations

Early systems for managing CCR used closed-form approximations with limited and static credit categories, default probabilities, recovery rates, term structure, potential future exposure, and netting measures. Little focus was directed to correlation, diversification, and credit migration.

The most common closed-form approximation for CCR was the **Value-at-Risk (VaR) modelling approach** — leveraging existing VaR models to implement CCR models. This approach:

- Is computationally fast
- Can be implemented with existing [[05-market_risk|market risk]] infrastructure
- Works well for simple, low-dimensional portfolios

However, closed-form approaches struggle to capture correlation, diversification, and credit migration simultaneously, particularly for complex OTC derivatives with path-dependent payoffs.

### Monte Carlo Simulation

Given the complexity, number of dimensions, and uncertainty of the CCR of a bank's derivatives portfolio, Monte Carlo simulations are now the norm. While data and IT system intensive, Monte Carlo can incorporate:

- Multiple sources of risk (interest rates, FX, equities, commodities)
- Correlations between risk factors
- Credit migration (rating transitions over the life of the portfolio)
- Recovery rates and their uncertainty
- Mitigants including netting and collateral posting

In a Monte Carlo simulation model, large numbers of joint scenarios are generated based on numerous risk-based factors pertaining to market conditions, defaults, credit migration, correlations, and recovery over the term of the portfolio. This is especially necessary as credit events and in particular defaults are rare, yet have huge impacts. Monte Carlo simulations are primarily useful for **uncollateralised (OTC) transactions**, as these require more complex modelling owing to the higher inherent credit risk.

Besides estimating risk, the simulations provide many insights into profit maximisation and hedging. This fulfils the requirement of [[bis|Basel]] that models should not only be used for capital calculations, but also for general [[01-risk_management|risk management]].

[[bis|Basel]] specifically makes allowance for the Monte Carlo approach in its framework for modelling [[05-market_risk|market risk]] under the internal model approach (akin to the IRBA for credit risk). The result of the Monte Carlo simulation feeds directly into the EEPE calculation:

$$\text{EEPE} = \sum_{k=1}^{\min(\text{1 year, maturity})} EPE(t_k) \times \Delta t_k$$

where $EPE(t_k)$ at each simulation date $t_k$ is obtained by:

1. Generating a large number $N$ of market scenarios at date $t_k$
2. Computing the netting set mark-to-market $V_n(t_k)$ for each scenario $n$
3. Computing $EE(t_k) = \frac{1}{N} \sum_n \max(V_n(t_k), 0)$
4. Applying the non-decreasing EPE constraint: $EPE(t_k) = \max_{s \leq t_k} EE(s)$

### Wrong-Way Risk

**Wrong-way risk** arises when the exposure to a counterparty is adversely correlated with the counterparty's credit quality — i.e. the bank has its largest exposure to the counterparty precisely when the counterparty is most likely to default.

Examples:

- A bank that has written CDS protection (selling credit insurance) to a counterparty on a reference entity that is closely linked to the counterparty's own creditworthiness. If the reference entity deteriorates, the counterparty is most likely to default precisely when the CDS exposure is highest.
- A bank that has entered into an FX swap with a sovereign counterparty: if the sovereign's currency depreciates sharply (increasing the bank's exposure), the sovereign may simultaneously come under fiscal stress (increasing default probability).

Wrong-way risk is partially addressed by the 1.4 alpha factor in both the SA-CCR and IMM formulas, but sophisticated banks additionally model it explicitly within their Monte Carlo simulations by correlating [[05-market_risk|market risk]] factors with counterparty default events.
