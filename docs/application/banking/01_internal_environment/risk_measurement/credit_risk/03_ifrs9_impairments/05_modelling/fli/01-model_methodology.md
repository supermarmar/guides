# Forward Looking Information

In IFRS 9, Forward-Looking Information (FLI) ensures that Expected Credit Losses (ECLs) are not solely based on historical data but also incorporate anticipated macroeconomic conditions (e.g., GDP growth, unemployment rates). The process involves calibrating Point-in-Time (PIT) Probability of Default (PD) values to reflect the influence of future economic scenarios.

## Credit Cycle Forecasts

The credit cycle refers to movements in credit conditions that are shared by a portfolio or cohort of borrowers, which vary across the economic cycle. In an ideal world, a credit cycle index is based on internal default data. However, for corporate portfolios this can be particularly difficult as these portfolios tend to have a low number of observed default.

### Discrete Scenarios

### Stochastic Scenarios (Monte Carlo Simulation)

## FLI PD

Use a statistical model (e.g., linear regression, logistic regression) to link historical default rates to macroeconomic factors. A model can be regressed for all outcome periods (1m, 2m, ... etc). Normally in an audit only the 12m is looked at typically. The lifetime will be the same as the FLI PD since it averages out.

$y=\text{Average Default Rate}_{12m}=\beta_0+\beta_1\text{GDP Growth}_{12m}+\beta_2\text{Interest Rate}_{12m}+\Epsilon$

Standard normalization involves transforming a variable so that it has a mean of 0 and a variance of 1. This transformation is common in regression and machine learning models to ensure that all variables are on a comparable scale, making coefficients more interpretable and improving numerical stability.

Given a macroeconomic variable X (e.g., GDP growth, inflation rate), the standardized value Z is computed as:

$Z=\Large\frac{X-\mu_X}{\sigma_X}$

Removes the original unit of measurement (e.g., percentages or absolute values) for easier comparison across variables.

The regression identifies the sensitivity of PDs to each macroeconomic variable. With calibrated coefficients, obtain **forecasts** for macroeconomic variables for each future time period under:

- Baseline Scenario: Expected economic performance.
- Upside Scenario: Optimistic economic conditions.
- Downside Scenario: Pessimistic economic conditions.

Plug the forecasted macroeconomic variables into the regression model to estimate future default rates under each scenario. Example:

- Baseline PD: 4.5%
- Upside PD: 3.8%
- Downside PD: 5.7%

If you plus in 0 for the variables you should end up with your PD equal to $\beta_0$ (the intercept). This should be equal to the historical TTC PD since all the macroeconomic variables are at their averages.

Calculate the ratio or FLI adjustment factor for each scenario by comparing forward-looking PDs to historical or baseline PDs.

$\text{Factor } X=\Large\frac{\text{FLI-Adjusted PD Scenario }X}{\text{Base PD}}$

Multiply the base PDs (calibrated without considering macro factors) by the FLI adjustment factor.

$\text{PD}_X = \text{Base PD} \times \text{Factor } X $

Weight the adjusted PDs across scenarios using their assigned probabilities

$\text{Weighted PD}=(\text{PD}_{\text{baseline}}\times 50\%)+(\text{PD}_{\text{upside}}\times 20\%)+(\text{PD}_{\text{downside}}\times 30\%)$

The best way to test a FLI model is to plot its expected PDs against the historical default rates and using a visual test to see if the **peaks** and **trophs** are aligned.
