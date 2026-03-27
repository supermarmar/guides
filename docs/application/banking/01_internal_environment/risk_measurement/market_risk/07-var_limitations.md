# VaR Limitations and Alternative Risk Measures

## Coherent Risk Measures

A **coherent measure of risk** satisfies the following axioms. Let $L_1, L_2$ denote loss random variables and $\rho(\cdot)$ denote the risk measure:

| Axiom | Condition | Interpretation |
|---|---|---|
| Monotonicity | If $L_1 \leq L_2$ then $\rho(L_1) \leq \rho(L_2)$ | Greater risk → higher risk measure |
| Translation invariance | $\rho(L_1 + c) = \rho(L_1) + c$ | Adding a constant loss $c$ increases the measure by $c$ |
| Positive homogeneity | $\rho(\alpha L_1) = \alpha \rho(L_1)$ for $\alpha \geq 0$ | Risk is proportional to the size of exposure |
| Subadditivity | $\rho(L_1 + L_2) \leq \rho(L_1) + \rho(L_2)$ | Combining exposures cannot increase total risk — diversification is recognised |
| Convexity | $\rho(\alpha(\mu L_1 + (1-\mu) L_2)) \leq \alpha\mu\rho(L_1) + \alpha(1-\mu)\rho(L_2)$ | Follows from positive homogeneity and subadditivity |

## Value at Risk (VaR)

VaR measures the maximum expected loss over a given time period that will not be exceeded with a given probability. For a return random variable $X$ at confidence level $\alpha$:

```math
\text{VaR}[\alpha] = \sup\{x \in \mathbb{R} : P(X < x) \leq 1 - \alpha\}
```

**Advantages of VaR:**
- Easily understood — expressed in simple, intelligible units (e.g. "the 99% VaR represents a one-in-a-hundred-year loss event").
- Can be used across all [[05-market_risk|market risk]] types and allows for interaction between risks.
- Comparable across different business units.
- Easily translated into risk benchmarks and limits.

**Disadvantages of VaR:**
- No indication of the distribution of losses in the tail — only the threshold, not the magnitude of tail losses.
- Underestimates losses for risks with asymmetric and/or fat-tailed distributions.
- **Not a coherent measure of risk** — VaR fails to satisfy the subadditivity property, meaning it can discourage diversification as a risk-reduction strategy.

VaR is coherent only if losses are assumed to follow an elliptical distribution (e.g. normal or lognormal). It is therefore a requirement to use an elliptical distribution when applying VaR to measure risk — but this is often an unrealistic assumption for actual market returns.

## Observed Distributions vs Normal/Lognormal Distributions

Asset prices have historically been modelled using the lognormal distribution because it produces non-negative prices and is mathematically tractable. Under the lognormal assumption:

```math
S_t = e^{X_t}, \quad X_t = X_0 + \mu t + \sigma B_t, \quad B_t \sim N(0, t)
```

where $\mu$ is the drift (mean) and $\sigma$ is the diffusion (standard deviation).

**Empirical characteristics of actual market returns that deviate from the normal/lognormal assumption:**

- **Leptokurtosis** — returns have kurtosis greater than the normal distribution, resulting in more concentration about the mean together with thicker tails. Extreme returns occur more often than the normal distribution implies.
- **Long-run mean reversion** — returns over long periods display mean-reverting characteristics.
- **Time-varying volatility** — volatility varies in a systematic way over time; a constant variance assumption is inappropriate (ARCH/GARCH effects).
- **Discontinuous jumps** — returns sometimes display jumps (can be modelled using a Poisson jump process).
- **Momentum effects** — evidence of autocorrelation of returns (as prices rise, volume of buyers increases, further inflating prices), though not to the extent of generating risk-free profits net of transaction costs.
- **Skewness** — assets exposed to credit risk display negative skewness, as upside is capped at the contractual obligation while downside is unbounded.

These properties mean VaR underestimates risk for fat-tailed distributions — VaR captures the threshold but not the severity of losses beyond it.

## Expected Shortfall (ES)

Expected shortfall addresses the key limitation of VaR by measuring the **average loss in the worst $(1-\alpha)$% of scenarios**. For a return random variable $X$ at confidence level $\alpha$:

```math
\text{ES}[\alpha] = E[-X \mid X \leq \text{VaR}[\alpha]]
```

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

```math
\text{TVaR}[\alpha] = \mu + \sigma \cdot \frac{\phi(\Phi^{-1}(\alpha))}{1 - \alpha}
```

where $\phi$ is the standard normal PDF and $\Phi^{-1}$ is the inverse standard normal CDF.

**Advantages (similar to ES):**
- Allows for losses beyond VaR.
- Coherent measure of risk.
- Can be aggregated across business units.
- Better intuitive meaning than ES — it is the **conditional expected loss**, given that losses exceed the VaR level.

**Disadvantages:**
- More complicated to explain than VaR, as it requires understanding of conditional probabilities.
