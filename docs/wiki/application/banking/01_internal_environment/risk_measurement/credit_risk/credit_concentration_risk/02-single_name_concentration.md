# Single-name Concentration

Name concentration arises when the portfolio is not sufficiently granular, meaning a single large borrower default could cause losses materially above those predicted by the ASRF model. 

The Pillar 1 IRB formula assumes an infinitely granular portfolio — the law of large numbers diversifies away all idiosyncratic risk, leaving only systematic factor exposure. Real portfolios are lumpy. A bank with 5 large corporate obligors cannot diversify away the idiosyncratic default risk of its biggest names. Both methods estimate the additional capital needed to cover that residual concentration risk.

Take the following example:

Total EAD = R1,000m. Five corporate obligors, all with identical risk parameters for simplicity: PD = 1.5%, LGD = 45%, asset correlation ρ = 15%.

|Obligor|EAD (Rm)|Weight wᵢ|
|---|---|---|
|A|300|0.30|
|B|250|0.25|
|C|200|0.20|
|D|150|0.15|
|E|100|0.10|
```
N⁻¹(0.015) = −2.17,   N⁻¹(0.999) = 3.09

IRB term = √(1/0.85) × (−2.17) + √(0.15/0.85) × 3.09
         = 1.085 × (−2.17) + 0.420 × 3.09
         = −2.354 + 1.298 = −1.056

N(−1.056) = 14.55%

K = 0.45 × (14.55% − 1.5%) = 0.45 × 13.05% = 5.87%
```

**Total Pillar 1 IRB capital = 5.87% × R1,000m = R58.7m**

This is the number Pillar 1 gives, assuming the portfolio is infinitely diversified. It is the baseline both methods adjust.
## Gordy-Lütkebohmert Granularity Adjustment

The standard approach uses the **Gordy-Lütkebohmert (2007) granularity adjustment**, which computes the additional capital needed relative to the infinitely granular ASRF benchmark:

$$\text{GA} = \frac{1}{2C} \sum_i w_i^2 \cdot \frac{\sigma_i^2(\text{UL}_i + \text{EL}_i)}{\text{EL}_i^2}$$

where $w_i$ is the weight of exposure $i$ in the portfolio, $\sigma_i$ is the idiosyncratic standard deviation of losses for $i$, and $C$ is total portfolio capital. 

The GA is more analytically rigorous. The IRB capital formula implicitly sets idiosyncratic loss variance to zero (infinite granularity). For a finite portfolio, each obligor contributes residual idiosyncratic variance proportional to the square of its weight. The GA estimates the additional capital required to cover this residual variance.

The add-on is larger for obligors that are:

- Larger (higher wᵢ² term)
- Higher risk (higher K)
- More correlated with the systematic factor (higher ρ, which amplifies concentration effects because correlated obligors offer less true diversification)

### Origin: Born Inside the Basel II Process

The GA has a far more specific and traceable lineage. It was invented to solve a problem that emerged during the construction of the Basel II IRB framework in the late 1990s.

The theoretical foundation of the IRB formula is the **Asymptotic Single Risk Factor (ASRF) model**, formalised by **Oldřich Vašíček** — a Czech mathematician working at KMV. His key insight, developed in working papers from 1987 and formalised in a widely circulated 2002 paper, was that if you assume a single systematic risk factor drives correlated defaults, and if the portfolio is infinitely granular, then the loss distribution has a closed-form expression. That closed form became the IRB capital formula. The 99.9th percentile of that distribution, minus expected loss, gives you the capital charge.

The critical phrase is _infinitely granular_. Vašíček's model works by invoking the law of large numbers — in an infinite portfolio of infinitesimally small exposures, idiosyncratic default risk cancels out entirely, leaving only systematic risk. This is mathematically elegant but obviously unrealistic for a real bank with concentrated large corporate exposures.

**Michael Gordy** at the Federal Reserve Board, who was central to the theoretical development of the IRB framework, recognised this problem explicitly. His 2003 paper in the _Journal of Financial Intermediation_, "A Risk-Factor Model Foundation for Ratings-Based Bank Capital Rules," provided the rigorous derivation of why the ASRF model justified the IRB formula — and made the infinite granularity assumption explicit as a limitation.

This prompted the Basel Committee to propose a correction. **Basel Committee Working Paper No. 8 (2001)** included a formal granularity adjustment appendix, and the **third consultative paper (CP3, 2003)** incorporated it as a proposed mandatory Pillar 1 add-on to the IRB formula. The formula was derived from first principles — the difference between the VaR of an infinitely granular portfolio and the VaR of the actual finite portfolio, approximated analytically.

Then the Basel Committee dropped it.

In the **final Basel II text published in 2004**, the granularity adjustment was removed from Pillar 1 on the grounds that it was too complex for mandatory global implementation and that the additional precision did not justify the compliance burden for most banks. It was explicitly preserved for Pillar 2 — banks with concentrated portfolios were expected to apply it (or an equivalent) in their ICAAP. The decision was pragmatic rather than theoretical.

**Gordy and Eva Lütkebohmert** at the Deutsche Bundesbank then published the definitive academic treatment in a 2007 Bundesbank discussion paper (later published in the _Review of Finance_ in 2013), which derived the GA rigorously under a two-factor model and provided the practical formula that most banks and regulators now reference.

## Herfindahl-Hirschman Index (HHI)

A simpler proxy is the **Herfindahl-Hirschman Index (HHI)**. The Herfindahl-Hirschman Index measures the degree of size concentration. It compares the actual portfolio to what an equally-weighted portfolio of the same number of obligors would look like. The more top-heavy the distribution, the higher the HHI and the larger the capital add-on.

$$\text{HHI} = \sum_{i=1}^N w_i^2$$

A higher HHI indicates a more concentrated portfolio. The capital add-on scales with HHI: a fully concentrated portfolio (HHI = 1) requires substantially more capital than a fully diversified portfolio (HHI → 0).

```
HHI = 0.30² + 0.25² + 0.20² + 0.15² + 0.10²
    = 0.090 + 0.063 + 0.040 + 0.023 + 0.010
    = 0.225

Effective N  = 1 / 0.225 = 4.44 obligors
               (the portfolio behaves like 4.4 equal obligors, not 5)

HHI_equal    = 1/5 = 0.200

Concentration scale = 0.225 / 0.200 = 1.125

HHI-adjusted capital = R58.7m × 1.125 = R66.0m
Concentration add-on = R66.0m − R58.7m = R7.3m  (+12.5%)
```

The add-on is driven almost entirely by Obligor A. If Obligor A were R200m (equal weight with B), HHI would drop to 0.200 and the add-on would be zero. That is the model's signal: the R100m overweight in A costs R7.3m in capital.

In practice most banks use both: HHI for real-time portfolio monitoring and limit utilisation, and GA (or a full credit portfolio simulation) for the ICAAP capital number submitted to the PA.

### Origin: Industrial Organisation Economics, Adapted into Banking

The Herfindahl-Hirschman Index has nothing to do with banking in its origins. It comes from **competition economics**.

**Orris Herfindahl** developed the index in his 1950 Columbia University doctoral dissertation on concentration in the US steel industry. He was trying to quantify how monopolistic a market was. **Albert Hirschman** had independently arrived at the same formulation in 1945 in his work _National Power and the Structure of Foreign Trade_, using it to measure export concentration across countries. The index was eventually named after both, though in competition economics it is sometimes called the Hirschman index.

The index became institutionally important when the **US Department of Justice adopted it in its 1982 Merger Guidelines** as the formal metric for assessing whether a proposed merger would create anticompetitive concentration. HHI thresholds — below 1,500 (unconcentrated), 1,500–2,500 (moderately concentrated), above 2,500 (highly concentrated) — became the basis for merger approvals and challenges. This gave the index enormous regulatory legitimacy and wide recognition.

The adaptation into credit risk came much later, pragmatically. Practitioners and regulators noticed that the same mathematical property that made the HHI useful for measuring market concentration — its sensitivity to the squared weight of large players — also made it a natural measure of single-name exposure concentration in a loan portfolio. There was no formal derivation. It was an analogy borrowed from a different field because it was simple, intuitive, and already well understood by regulators.

The Basel Committee referenced HHI-based approaches in its Pillar 2 guidance papers on concentration risk, and national regulators including the PRA and EBA incorporated it into their supervisory expectations. But it arrived in banking as a diagnostic tool, not as a theoretically derived capital formula.

## Large Exposure Limit

Under the **Basel large exposures framework (BCBS 2014)**:

- For exposures **between G-SIBs**, a tighter limit of **15% of Tier 1 capital** applies, reflecting the heightened systemic risk of interconnections between the largest global banks

 and implemented in South Africa by the SARB under the Banks Act:

- A bank's exposure to a **single counterparty or group of connected counterparties** must not exceed **25% of Tier 1 capital**
- An exposure of **10% or more of Tier 1 capital** must be reported to the supervisor as a large exposure, even if it is below the 25% limit

Note that the denominator shifted from **total capital (Tier 1 + Tier 2)** under the old framework to **Tier 1 capital only** in the 2014 standard — a deliberate tightening, since Tier 1 is the higher-quality loss-absorbing component.