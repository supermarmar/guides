# Systemically Conditional PDs

The mapping function used to derive systemically conditional PDs from average PDs is derived from an adaptation of Merton’s (1974) single asset model to credit portfolios. According to Merton’s model, borrowers default if they cannot completely meet their obligations at a fixed assessment horizon (e.g. one year) because the value of their assets is lower than the due amount. Merton modelled the value of assets of a borrower as a variable whose value can change over time. He described the change in value of the borrower’s assets with a normally distributed random variable.

Vasicek (cf. Vasicek, 2002) showed that under certain conditions, Merton’s model can naturally be extended to a specific ASRF credit portfolio model. With a view on Merton’s and Vasicek’s ground work, the Basel Committee decided to adopt the assumptions of a normal distribution for the systematic and idiosyncratic risk factors.

## Vasicek Model

Vasicek applied to firms’ asset values what had become the standard geometric Brownian motion model. Expressed as a stochastic differential equation:

$dA_i = \mu_iA_i~dt + \sigma_iA_i~dx_i$

Where $A_i$ is the value of the ݅ith firm’s assets, $\mu_i$ and $\sigma_i$ are the drift rate and volatility of that value, and $x_i$ is a Wiener process or Brownian motion, i.e. a random walk in continuous time in which the change over any finite time period is normally distributed with mean zero and variance equal to the length of the period, and changes in separate time periods are independent of each other. Solving this stochastic differential equation one obtains the value of the ith firm’s assets at time $T$ as:

$A_i(T)=e^{\small A(0) + \mu_iT-\frac{1}{2}\sigma_i^2T+\sigma_i\sqrt T X_i}$

The $݅i$ th firm defaults if $A_i(T)<B$ so the probability of such an event is

$P[A_i(T)<B]=P[X_i<c_i]=p^*$

where $c_i$ is easily derived from equation (1). That is, default of a single obligor happpens if the value of a normal random variable happens to fall below a certain $c_i$.

**$p^*$ is the average loss rate in 1-year or the 1-year through-the-cycle (TTC) PD.**

Correlation between defaults is introduced by assuming correlation in the $A_i$ processes, and thus in the terminal values, $A_i(T)$. In particular, it is assumed that the $X_i$ s in equation (1) are pair-wise correlated according to factor $\rho$. The higher $\rho$, the more dependent the borrowers are on systematic environment. When $\rho = 0$ this implies total independence between borrowers.

Being normal and equi-correlated, each random variable can then be represented as the sum of two other random variables: one common across firms, and the other idiosyncratic that are both standard normal ~$N(0,1)$.

$X_i = \text{S}_{t'}\sqrt{\rho}+Z_i\sqrt{1-\rho}$

where $\text{S}_{t'}$ and $Z_i$ are respectively the normalised systematic and the idiosyncratic (asset specific) components. An economic index over the interval $(0,T)$ is given by $\text{S}_{t'}=\Large\frac{\text{FLI}_{t'}-\mu}{\sigma}$. Hence the probability of default of obligor $i$, conditional on $\text{S}_{t'}$, can also be written as:

$P[X_i < c_i | \text{S}_{t'}] = P[X_i < N^{-1}(p^*)|\text{S}_{t'}]$

$= P[\text{S}_{t'}\sqrt{\rho}+Z_i\sqrt{1-\rho}<N^{-1}(p^*)]$
$= P[Z_i<\frac{N^{-1}(p^*)-\text{S}_{t'}\sqrt{\rho}}{\sqrt{1-\rho}}]$
$= N(\large\frac{N^{-1}(p^*)-\text{S}_{t'}\sqrt{\rho}}{\sqrt{1-\rho}})$

By taking the inverse of the standard normal distribution applied to confidence level one can derive conservative value of systematic factor $S$.

Rewriting this in terms of the 99.9% quantile for Basel

$\text{PD}_{i,t}^\text{SysPiT}(12,x_{i},x_{i,t}|\text{S}_{99.9^{th}}=N^{-1}(0.999)) = N(\large\frac{N^{-1}(p^*)+\sqrt{\rho}N^{-1}(0.999)}{\sqrt{1-\rho}})$

where $p^* = \text{PD}_{i}^\text{TTC}(12,x_{i},[t_a',t_b'])$

This is component is the same one that appears Basel:

$K=\text{LGD}[N(\frac{G(\text{PD})+\sqrt{R}\times G(0.999)}{\sqrt{1-R}})-\text{PD}]$

## Systemtic Risk

Given a macroeconomic scenario, a time series $S_t'$ can be computed, which can then be used in the Vasicek framework to  calculate the loss rate conditional to that specific scenario. The common component $S_t'$ may be viewed as representing aggregate macro-financial conditions which can be extracted from observable economic data. Aggregate credit risk depends on the stochastic common factor $S_t'$, because when we face good economic times the expected loss rate tends to below the long-term average, while during bad times the expected loss rate is expected to be above the long-term average. $S_t'$ can be estimated empirically using the Kalman filter algorithm.

## Asset Correlations

A portfolio with high correlations produces greater default oscillations over the cycle $S_t'$, compared with a portfolio with lower correlations. Correlations do not affect the timing of the default; higher correlations do not imply that defaults earlier or later than other portfolios. Thus, during good times a portfolio with high correlations will produce fewer defaults than a portfolio with low correlations. While in bad times the opposite is true, high correlations are creating more defaults. Some benchmark values of ρ are available from the regulatory regimes. The Basel II IRB risk-weighted formulae, which are based on the Vasicek model, prescribes, for corporate exposures, correlations between 12% and 24%, where the actual number is computed as a probability of default weighted average.

Following the Vasicek framework, two borrowers are correlated because they are both linked to the common factor $S_t'$. Clearly this is a simplification of the true correlation structure.

