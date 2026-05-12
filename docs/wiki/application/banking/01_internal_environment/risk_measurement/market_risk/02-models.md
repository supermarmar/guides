---
tags:
  - application/banking/internal-environment/risk-measurement/market-risk/market-risk
  - difficulty/unknown
  - study-status/new
aliases:
---
# Modelling Approaches

A **coherent measure of risk** satisfies the following axioms. Let $L_1, L_2$ denote loss random variables and $\rho(\cdot)$ denote the risk measure:

| Axiom | Condition | Interpretation |
|---|---|---|
| Monotonicity | If $L_1 \leq L_2$ then $\rho(L_1) \leq \rho(L_2)$ | Greater risk → higher risk measure |
| Translation invariance | $\rho(L_1 + c) = \rho(L_1) + c$ | Adding a constant loss $c$ increases the measure by $c$ |
| Positive homogeneity | $\rho(\alpha L_1) = \alpha \rho(L_1)$ for $\alpha \geq 0$ | Risk is proportional to the size of exposure |
| Subadditivity | $\rho(L_1 + L_2) \leq \rho(L_1) + \rho(L_2)$ | Combining exposures cannot increase total risk — diversification is recognised |
| Convexity | $\rho(\alpha(\mu L_1 + (1-\mu) L_2)) \leq \alpha\mu\rho(L_1) + \alpha(1-\mu)\rho(L_2)$ | Follows from positive homogeneity and subadditivity |

## [[03-var_limitations|Value at Risk]] (VaR)

VaR is the maximum possible loss that a portfolio can suffer with a specific level of confidence over a certain time frame. Expressed formally:

$$
\text{VaR}[\alpha] = \sup\{x \in \mathbb{R} : P(X < x) \leq 1 - \alpha\}
$$
where $X$ is the return random variable and $\alpha$ is the confidence level.

For example, if 1-day VaR is $25 million at 95% confidence, there is an estimated 5% chance of a single trading day loss exceeding $25 million — roughly one loss of that magnitude per 20 trading days. VaR focus is on P&L probabilities given a confidence level and specific time frame.

A **"VaR break"** is when actual losses exceed the VaR threshold. In a perfectly accurate model, the number of VaR breaks would equal $(1 - \alpha)$ of trading days. Banks must back-test their models daily; regulators penalise banks with capital add-ons when poor back-testing highlights deficient models.

South African banks commonly use 1-day and 10-day holding period assumptions for [[01-risk_management|risk management]].

**Advantages of VaR:**
- Easily understood — expressed in simple, intelligible units (e.g. "the 99% VaR represents a one-in-a-hundred-year loss event").
- Can be used across all [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] types and allows for interaction between risks.
- Comparable across different business units.
- Easily translated into risk benchmarks and limits.

**Disadvantages of VaR:**
- No indication of the distribution of losses in the tail — only the threshold, not the magnitude of tail losses.
- Underestimates losses for risks with asymmetric and/or fat-tailed distributions.
- **Not a coherent measure of risk** — VaR fails to satisfy the subadditivity property, meaning it can discourage diversification as a risk-reduction strategy.

VaR is coherent only if losses are assumed to follow an elliptical distribution (e.g. normal or lognormal). It is therefore a requirement to use an elliptical distribution when applying VaR to measure risk — but this is often an unrealistic assumption for actual market returns.

### Observed Distributions vs Normal/Lognormal Distributions

Asset prices have historically been modelled using the lognormal distribution because it produces non-negative prices and is mathematically tractable. Under the lognormal assumption:

$$
S_t = e^{X_t}, \quad X_t = X_0 + \mu t + \sigma B_t, \quad B_t \sim N(0, t)
$$

where $\mu$ is the drift (mean) and $\sigma$ is the diffusion (standard deviation).

**Empirical characteristics of actual market returns that deviate from the normal/lognormal assumption:**

- **Leptokurtosis** — returns have kurtosis greater than the normal distribution, resulting in more concentration about the mean together with thicker tails. Extreme returns occur more often than the normal distribution implies.
- **Long-run mean reversion** — returns over long periods display mean-reverting characteristics.
- **Time-varying volatility** — volatility varies in a systematic way over time; a constant variance assumption is inappropriate (ARCH/GARCH effects).
- **Discontinuous jumps** — returns sometimes display jumps (can be modelled using a Poisson jump process).
- **Momentum effects** — evidence of autocorrelation of returns (as prices rise, volume of buyers increases, further inflating prices), though not to the extent of generating risk-free profits net of transaction costs.
- **Skewness** — assets exposed to credit risk display negative skewness, as upside is capped at the contractual obligation while downside is unbounded.

These properties mean VaR underestimates risk for fat-tailed distributions — VaR captures the threshold but not the severity of losses beyond it.

## Stressed VaR (sVaR)

sVaR considers the worst losses of a portfolio observed from historical data — most commonly the 2008 financial crisis. Banks run simulations to identify the most stressful 1-year period from 2007 to the current date, and use that time series to calculate sVaR. sVaR is used alongside current VaR to set regulatory capital levels, while point-in-time VaR is the primary metric for limit monitoring. Both VaR and sVaR are used to set [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/credit_concentration_risk/01-context|economic capital]] levels.

## Expected Shortfall (ES)

Expected shortfall addresses the key limitation of VaR by measuring the **average loss in the worst $(1-\alpha)$% of scenarios**. For a return random variable $X$ at confidence level $\alpha$:

$$
\text{ES}[\alpha] = E[-X \mid X \leq \text{VaR}[\alpha]]
$$

**Advantages of ES:**
- Allows for losses beyond the VaR threshold.
- Is a **coherent measure of risk** (satisfies all four axioms, including subadditivity).
- Can be aggregated across business units.

**Disadvantages of ES:**
- Has little intuitive meaning and cannot be directly linked to the current value of the asset.

The **shortfall-to-quantile ratio** (ES / VaR) demonstrates the difference between ES and VaR under different distributional assumptions:

- Under the normal distribution: ES / VaR is relatively small.
- Under the Student-$t$ distribution with $g$ degrees of freedom: the ratio increases as $g$ decreases (thicker tails). VaR increasingly underestimates risk as distribution tails thicken.

FRTB (effective 1 January 2023) replaces VaR with expected shortfall for trading book capital to better capture tail risk.

## Tail Value at Risk (TVaR)

The TVaR is closely related to the expected shortfall and indicates the **size of the loss given that the loss exceeds the confidence level**. For $X \sim N(\mu, \sigma^2)$:

$$
\text{TVaR}[\alpha] = \mu + \sigma \cdot \frac{\phi(\Phi^{-1}(\alpha))}{1 - \alpha}
$$

where $\phi$ is the standard normal PDF and $\Phi^{-1}$ is the inverse standard normal CDF.

**Advantages (similar to ES):**
- Allows for losses beyond VaR.
- Coherent measure of risk.
- Can be aggregated across business units.
- Better intuitive meaning than ES — it is the **conditional expected loss**, given that losses exceed the VaR level.

**Disadvantages:**
- More complicated to explain than VaR, as it requires understanding of conditional probabilities.
