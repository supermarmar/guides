---
tags:
  - application/banking/internal-environment/risk-management/risk-measurement
  - difficulty/unknown
  - study-status/new
aliases:
---
# Risk measurement

Risk measurement is the step that turns a named risk into a quantified exposure. The output feeds the [[02-risk_appetite|appetite statement]], the [[06-economic_capital|economic capital]] model, the [[../pricing/01-pricing_framework|pricing engine]], and the regulatory return. The inputs are data, statistics, and management judgement, in roughly equal weight. This primer covers the methodology families banks use, the aggregation step that combines them, the tail and extreme-value theory that determines how much capital sits behind the 99.9% quantile, and the model-risk and validation discipline that keeps the whole exercise honest.

When choosing a model, banks weigh five competing concerns: clarity and simplicity, IT cost, data availability, non-linearity of the underlying risk, and over-reliance on assumptions. A model nobody can explain to the board is a model nobody can challenge; a model that takes three days to run cannot price a same-day deal; a model calibrated on a benign sample will mis-price the tail. These five tensions sit behind every choice in this file.

[[01-risk_management|Risk management]] models must work in both normal and extreme conditions. Variance-covariance [[03-var_limitations|Value at Risk]] was commonly calibrated at the 95% level (two standard deviations) in the 1990s, which did not cover the late-1990s emerging-market and LTCM dislocations. Tail risk (events beyond three sigma) has to be captured separately, and risks with disproportionate probability of extreme outcomes are described as **fat-tailed**. Almost every loss distribution that matters in banking is fat-tailed, and normal-distribution approximations systematically understate the tail.

Any model is conditional on its assumptions, and those assumptions are generally drawn from historical experience. The key assumption is that the past represents the future. Numbers from a model are not therefore a final assessment of risk: management judgement remains integral, and some risks (reputational, strategic, conduct) are largely unquantifiable. Banks may benchmark against peers to validate models, but if every bank uses the same model with the same assumptions, the error common to all of them becomes systemic rather than idiosyncratic. The 2008 mortgage CDO crisis was exactly this dynamic at industry scale.

A separate but related expectation is the **use test**. Pillar 1 IMA, IMM, and IRB approvals all require the bank to demonstrate that the model is used in actual day-to-day decisions (pricing, limit setting, capital allocation, performance measurement), not only for the regulatory return. A model that sits in a corner producing a number nobody acts on fails the test, even if its mathematics are impeccable. See [[05-use_tests|IRB use test]] for the credit-risk version of this requirement.

## The measurement toolkit

The techniques banks use fall into five methodology families, distinguished by the kind of information they consume and the kind of output they produce. Machine learning is treated separately as a cross-cutting estimator class rather than a sixth family, because it can sit inside any of the five. Most real measurement exercises ([[02_probability_of_default|PD]] estimation, [[03-var_limitations|VaR]], [[05-irrbb_measurement|IRRBB]], operational risk capital, behavioural deposit modelling) combine several families, and the choice between them is driven by data availability, the linearity of the underlying risk, regulatory expectation, and the materiality of the exposure.

### Sensitivity and analytical methods

**Sensitivity methods** measure how a position's value changes in response to a small movement in a single risk factor, using closed-form derivatives rather than full revaluation. The canonical examples are the option Greeks (delta, gamma, vega, rho, theta) for market risk, [[05-irrbb_measurement|PV01 or DV01]] for fixed-income positions, key-rate durations across the term structure, and convexity for second-order interest-rate sensitivity. The same logic extends to credit (spread DV01, jump-to-default) and to FX (delta per currency pair).

These methods are fast and transparent, which is why they dominate intraday market-risk monitoring and the FRTB Sensitivities-Based Method (SBM), in which capital is calculated as a weighted combination of delta, vega, and curvature sensitivities aggregated under prescribed correlations. The weakness is that linearisation around the current state breaks down for large moves and for products with discontinuous payoffs (digital options, structured credit tranches), where higher-order or full-revaluation methods are required.

### Scenario analysis and stress testing

**Scenario analysis** evaluates the impact of a defined set of risk-factor moves on the portfolio, without imposing a distributional assumption on those moves. Scenarios may be **historical** (the 2008 dislocation, the 1998 LTCM event, the 2020 pandemic week), **hypothetical** (a synthetic recession, a 200 bp parallel rate shock, a sovereign downgrade), or **reverse stress tests** (what set of moves would breach the bank's capital floor or render the business model unviable). Reverse stress testing under PRA SS3/18 is now an explicit Pillar 2A expectation for UK banks, because forward scenarios tend to anchor on plausible loss paths while reverse engineering exposes the cliff edge.

Stress testing is the supervised, often regulator-prescribed variant: the EBA EU-wide stress test, the Bank of England's annual cyclical scenario, the US DFAST and CCAR programmes, and the [[01-pillar_2b|Pillar 2B]] framework all sit in this family. Scenarios are particularly powerful where historical data does not support a distributional approach: operational risk tail events, climate transition pathways, sovereign default, and concentrated wholesale exposures. They are also the dominant technique for [[01-short_term_metrics|liquidity]] survival horizon analysis, where the LCR's prescribed run-off rates are effectively a regulatory stress scenario.

### Statistical and econometric models

**Statistical and econometric models** fit a closed-form distribution or regression to historical experience and project future outcomes from it. The family covers logistic regression and gradient-boosted scorecards for [[02_probability_of_default|PD]], GLMs for LGD, time-series models (ARMA, GARCH, EGARCH) for market-risk volatility, Cox proportional-hazards models for time to default or prepayment, the variance-covariance form of [[03-var_limitations|VaR]], and the loss-distribution approach for operational risk where frequency (often Poisson) and severity (often lognormal or generalised Pareto) distributions are calibrated separately and convolved to give an aggregate loss distribution. Retail credit portfolios, where data is plentiful and homogeneous segments can be defined by loan type, LTV, tenor, and region, are the natural home of these techniques. See [[01_models|credit models]] for the credit-specific treatment and [[03-capital_basel2|the AMA section]] for the LDA in operational risk.

The same family also includes the workhorses of portfolio risk: factor decomposition (industry, region, size) for concentration analysis, copula models for joint default behaviour, and the asymptotic single-risk-factor model that underpins the [[01-context|Basel A-IRB formula]].

A recurring choice inside this family is between **through-the-cycle** (TTC) and **point-in-time** (PIT) estimators. A TTC estimator smooths cyclical variation and produces a stable long-run average; a PIT estimator tracks the current state of the economy. IRB capital uses TTC PD; IFRS 9 ECL uses PIT (or hybrid) PD. Using PIT estimators inside a capital model creates **procyclicality**: capital requirements rise as the cycle deteriorates, forcing banks to deleverage exactly when credit is most needed, which deepens the downturn. The Basel countercyclical capital buffer was introduced precisely to lean against this dynamic. The defining limitation of the whole family is reliance on historical experience: if the calibration data does not contain the regime now being projected (negative rates, a pandemic, a structural correlation shift), the output is unreliable, which is why statistical models are typically paired with stress overlays and management judgement.

### Simulation methods

**Simulation methods** generate a large number of possible portfolio outcomes and read risk measures off the resulting empirical distribution, rather than relying on a fitted parametric form. The three standard implementations are **historical simulation** (replay the last N days of observed risk-factor moves on today's portfolio), **Monte Carlo** (sample risk factors from a chosen joint distribution and revalue), and **filtered historical simulation** (combine historical innovations with a current-volatility filter to capture changing regimes). The latter dominates regulatory VaR in trading books with non-linear instruments.

Simulation is the standard approach for [[03-var_limitations|VaR]] and expected shortfall on trading books containing non-linear instruments, for [[06-economic_capital|economic capital]] aggregation across risk types where dependence is captured via copulas, and for full balance-sheet projections under stochastic [[04-nii_nim|NII / NIM]] models. Wholesale credit portfolios with few defaults, where parametric calibration is unstable, typically rely on Monte Carlo over a structural or factor model, with external agency ratings from Moody's, S&P, and Fitch often used as an auxiliary input where internal default experience is too thin.

Two technical choices matter inside simulation. First, **the joint distribution being sampled is itself a modelling assumption**, no less critical than the parametric form it replaces; a Gaussian copula in a Monte Carlo gives qualitatively different tail behaviour from a Student-t copula on the same marginals. Second, **variance-reduction techniques** (antithetic variates, control variates, importance sampling) can cut the number of paths required by an order of magnitude, which matters because simulation is the most computationally expensive family and capital runs typically operate on overnight batch windows.

### Qualitative and expert methods

**Qualitative methods** capture risks that cannot be calibrated from historical data, either because the data does not exist (a new product, a one-off event, an emerging risk) or because the loss is intrinsically hard to quantify (reputational damage, conduct, strategic missteps). The principal techniques are **risk and control self-assessment** (RCSA), **Delphi panels**, **expert scenario workshops**, and **judgemental overlays** applied to model output.

These methods are central to operational risk, where scenario analysis sits alongside internal and external loss data in the Basel framework and remains relevant for institutions running internal scenario libraries under the standardised measurement approach. They are also the principal tool for climate and emerging-risk assessment, and for the management of the [[03-risk_identification|reputational, conduct, and strategic risks]] that fall outside the quantifiable perimeter. They are the standard mechanism for setting inter-risk correlation assumptions in [[06-economic_capital|economic capital]] aggregation, where data is too sparse to estimate dependencies directly.

### Machine learning as a cross-cut

Machine learning is not a parallel family so much as a class of estimator that can sit inside any of the others: as the regression engine inside a PD scorecard (replacing logistic regression), as the conditional density used to generate Monte Carlo paths, as the producer of economic-state inputs for stress scenarios, or as the pattern detector inside operational-risk early-warning indicators. **Machine learning** covers tree ensembles (random forests, gradient boosting), neural networks, and the broader class of non-linear, high-dimensional estimators that bypass explicit distributional assumptions in favour of learning patterns directly from data.

Banking adoption has favoured lower-risk applications first: fraud detection, marketing propensity, document extraction, transaction monitoring, and credit early-warning indicators. Adoption in regulatory PD, LGD, and EAD is constrained by the model-risk burden and by the supervisory expectation (US SR 11-7, PRA SS1/23) that material models be auditable and explainable.

Key adoption considerations:

- **Explainability and interpretability**. Outputs must be sense-checkable. SHAP values, partial-dependence plots, monotonic features, and surrogate models help, but cannot fully resolve the "black box" concern for the most complex architectures.
- **Bias**. Bias in the training data propagates into the model. For credit decisions this creates regulatory and reputational exposure under fair-lending and anti-discrimination law.
- **Overfitting and feature engineering**. Flexible estimators will fit noise as readily as signal; rigorous out-of-time validation and disciplined hyperparameter tuning are essential.
- **Infrastructure**. Production deployment requires latency, monitoring, and recalibration pipelines that many bank IT estates do not yet support.
- **Dynamic recalibration**. Models that learn from new data adapt quickly but can drift outside the original validation envelope without anyone noticing.
- **Regulation**. GDPR's right to explanation, the EU AI Act, and local supervisory guidance constrain what can be deployed and how.

The headline risk is **model risk** itself: ML compounds the standard sources of model risk (specification, parameter, and implementation error) with reduced transparency, which makes the model-validation function the binding constraint on adoption in many banks.

### How these families combine in practice

The five families plus the ML cross-cut are methodology categories, not application areas. Most real measurement exercises combine several. **Asset-liability management** uses sensitivity methods (duration gap), scenario analysis (NII and EVE under prescribed shocks), and simulation (stochastic balance-sheet projections) in parallel. **Cashflow projection** for funding planning combines deterministic scenarios with statistical or ML [[05-behavioural_modelling|behavioural modelling]] of non-maturity deposits and prepayment. **Credit portfolio management** combines statistical factor models for attribution, copula or structural simulation for joint loss distributions, and scenario analysis for concentrations. **Operational risk capital** combines LDA (statistical), internal and external loss data, scenario analysis (qualitative), and increasingly ML for early-warning indicators.

The supervisory expectation under [[07-icaap|ICAAP]] and [[08-srep|SREP]] is that the bank can articulate why each technique is appropriate for the risk type and exposure being measured. Benchmarking against peers, while helpful for validation, is itself a source of systemic risk when everyone converges on the same assumptions, so the justification has to rest on the risk profile of the bank, not on what others are doing.

## Risk aggregation

Once each risk has been measured at the sub-portfolio level, the numbers must be combined to give a firm-wide picture. Aggregation matters because risks offset (a long EUR position and a short USD position partially cancel), and because risk action at the sub-portfolio level may be unnecessary if a firm-level offset already exists. It is inefficient to take aggressive steps in one part of the bank when the exposure is hedged in another. The wider point is that risk measurement should not consider only position size but also potential loss and effect on capital.

Five aggregation approaches dominate, in increasing order of sophistication:

| Approach | Method | Trade-off |
|---|---|---|
| Summation | Add together individual capital components | Most conservative; ignores diversification entirely |
| Constant diversification | Subtract a fixed percentage from summation | Captures some diversification; percentage is judgement |
| Variance-covariance | Weight components using pairwise correlations | Clean for elliptical distributions; assumes constant correlations |
| Copulas | Multivariate probability theory linking marginals | Captures tail dependence; requires copula family and calibration |
| Full modelling | Simulate every risk factor on every position | Most accurate; most data-hungry and computationally expensive |

Total economic capital across the bank under the variance-covariance formulation is:

```
EC_total = sqrt( EC^T * Sigma * EC )
```

where `EC` is the vector of risk-type economic capital and `Sigma` is the inter-risk correlation matrix. In practice, the correlation assumptions between risk types (credit and operational, market and credit, climate and credit) are difficult to estimate from data and are often set conservatively from expert judgement or supervisory guidance, typically in the 0.3 to 0.5 range. The diversification benefit at firm level usually lands in the 10 to 25% range. The line is one of the most heavily debated entries in the [[07-icaap|ICAAP]].

### Copula families and tail behaviour

A **copula** is a function that links a multivariate joint distribution to its marginal distributions: it lets the bank specify each risk's marginal distribution independently and then choose how the joint dependence behaves separately. Four copula families dominate in practice, and they differ most importantly in how they treat joint extremes:

- **Gaussian copula**. Tractable, easy to calibrate from a correlation matrix, and the workhorse of CreditMetrics and the original synthetic CDO market. Has **no tail dependence**: in the limit, joint extremes are no more correlated than the body of the distribution. This is the failure mode that the 2008 mortgage CDO market hit.
- **Student-t copula**. Same elliptical structure as the Gaussian but with a degrees-of-freedom parameter that controls tail heaviness. Has **symmetric tail dependence** in both upper and lower tails. Often the first improvement over Gaussian when joint stress matters.
- **Clayton copula** (Archimedean family). Has **lower-tail dependence only**, which makes it suitable for joint default modelling where the concern is co-movement in losses rather than gains.
- **Gumbel copula** (Archimedean family). Has **upper-tail dependence only**, used in operational risk and insurance for joint large-loss modelling.

The tail-dependence coefficient `lambda_L` is the limiting conditional probability that one variable lies in its lower tail given that the other does, as the threshold approaches the marginal extreme. For the Gaussian, `lambda_L = 0` regardless of correlation; for the Student-t, `lambda_L > 0` as long as the degrees of freedom are finite. Choosing the copula therefore choses how the model behaves in exactly the region capital is set against.

### Diversification and correlation

The concept of diversification is intuitive ("don't put all your eggs in one basket"). Diversification helps protect against losses arising from **idiosyncratic risk**. It does not help with **systemic risk**, which is what would lead to catastrophic losses or total failure of the financial system. A well-diversified portfolio performs in line with overall markets and the economy, and has more predictable volatility.

Limitations of diversification:

- Specialised and regional banks may have no realistic path to diversify (US banks prior to interstate banking deregulation were forced to lend within state lines, often into a few dominant local industries).
- Diversification is not a solution to risks the bank does not understand. A bank diversifying by lending to sectors where it has no expertise is exchanging one risk for several others.
- It is not a substitute for credit quality. Provisions and capital absorb losses only up to a point.
- Default correlation rises sharply in deteriorating conditions, faster than asset return correlation. The diversification calculated in benign periods is materially weaker in a stress.
- Diversification for investment returns is not the same as diversification for credit risk: the former is about the upside, the latter about the downside, and downside correlations behave very differently.

On the correlation side, the US Comptroller of the Currency has identified as highly correlated credit exposures to borrowers that are related through group structure, dependent on the same guarantor, dependent on the selling of the same manufacturer's product, in the same industry or sector, all in the financial sector, concentrated within a geographic area dominated by few business enterprises, owned by a foreign government, or secured by a common debt or equity instrument. Product areas where correlation has historically produced large concentration risk include retail (credit cards, home equity), leveraged loans, collateralised debt obligations, and commercial real estate.

Hedging instruments introduce their own correlation risk. A credit derivative bought to hedge exposure to bank X introduces correlation between X defaulting and the selling counterparty being unable to pay. The AIG / Lehman dynamic in 2008 is the largest realised instance.

### Wrong-way risk

**Wrong-way risk** arises in counterparty credit exposure when the size of the exposure is positively correlated with the probability of the counterparty's default. **General wrong-way risk** is driven by macroeconomic factors (a swap counterparty whose creditworthiness deteriorates with the same factor that increases the swap's mark-to-market). **Specific wrong-way risk** is structural (an option bought from a counterparty referencing the counterparty's own equity). Both are explicitly addressed in the Basel framework's IMM and SA-CCR rules, and they are the canonical reason for collateral haircuts and CVA capital charges.

### BCBS 239

The [[fsb|Financial Stability Board]] reported in 2011 that aggregate data reporting at [[g_sibs|global systemically important banks]] was inadequate, and set a deadline of January 2016 to meet supervisory expectations. The standard, [BCBS 239](../../../../regulation/international/bis/bcbs_239.md), set out fourteen principles for risk data aggregation and risk reporting and required G-SIBs to be able to aggregate risk data quickly, accurately, and across business lines. Complex group structures and businesses spanning legal entities and regions must not hinder aggregation. Compliance remains uneven a decade later and BCBS 239 deficiencies are a routine finding in supervisory reviews.

## Tail risk and extreme value theory

The body of a normal distribution and a fat-tailed distribution looks similar. The tails do not. A model calibrated to the body of a normal and used to set capital at 99.9% can underestimate the tail loss by a multiple. Almost every realised loss event in banking history sits in the part of the distribution where the normal approximation has already broken down, which is why tail-aware risk measures and extreme value theory are central rather than incidental.

### Coherent risk measures

A coherent risk measure satisfies four axioms (Artzner, Delbaen, Eber, Heath, 1999):

| Axiom | Meaning |
|---|---|
| Monotonicity | If portfolio A always loses at least as much as portfolio B, then A carries at least as much risk |
| Subadditivity | Risk(A + B) <= Risk(A) + Risk(B); diversification cannot increase risk |
| Positive homogeneity | Risk(k * A) = k * Risk(A) for k > 0; doubling the position doubles the risk |
| Translation invariance | Adding cash c reduces risk by c |

**VaR fails subadditivity** in general. A portfolio of two independent exposures can have a higher VaR than the sum of their individual VaRs, which contradicts the basic intuition that diversification reduces risk. **Expected shortfall** (ES, also called CVaR or TVaR) satisfies all four axioms. This is the theoretical reason FRTB replaced VaR with ES at the 97.5% level for trading-book capital, effective January 2023. See [[02-models|market risk models]] for the detailed VaR / ES treatment.

### Extreme value theory

**Extreme value theory** (EVT) provides the asymptotic distribution of extreme observations under weak assumptions about the underlying loss distribution. Two approaches dominate.

**Block maxima**. Partition the sample into blocks (monthly, quarterly), take the maximum loss per block, and fit the **generalised extreme value** (GEV) distribution to the resulting series. The Fisher-Tippett-Gnedenko theorem guarantees that block maxima of any well-behaved underlying converge to one of three GEV types (Gumbel, Fréchet, Weibull), parameterised by a single shape parameter `xi`. The approach is data-hungry: most of the sample is discarded.

**Peaks over threshold** (POT). Fit a **generalised Pareto distribution** (GPD) to losses exceeding a chosen high threshold. The Pickands-Balkema-de Haan theorem guarantees that exceedances over a sufficiently high threshold converge to a GPD, again parameterised by a shape parameter. POT uses the data more efficiently than block maxima but requires the analyst to choose a threshold, and the result is sensitive to that choice. Mean-excess plots and Hill plots are the standard diagnostics for threshold selection.

EVT is the standard approach for the **tail of operational loss distributions** (where the LDA's body is fitted with a lognormal and the tail with a GPD), for **stressed-VaR** and **stress-ES** calibration, and for **climate transition** loss distributions where the tail is the entire point. The principal caveat is that EVT is an asymptotic result: in finite samples, with the very few observations a tail produces, both the shape parameter and the tail-VaR are estimated with wide confidence intervals. EVT does not eliminate tail uncertainty, it bounds it.

### Spectral and distortion measures

A **distortion risk measure** assigns weights to the loss distribution that depend on the quantile. VaR weights the loss at a single quantile (97.5%, 99%, 99.9%) and ignores everything else. ES weights all losses beyond a threshold equally. A **spectral risk measure** generalises ES: it allows arbitrary weighting functions over the quantile range, so a risk-averse investor can place heavier weight on more extreme losses than ES does. The **Wang transform** is a specific distortion that has analytical tractability and is used in insurance pricing.

Spectral measures retain coherence as long as the weighting function is non-increasing in the quantile (the worse the loss, the higher the weight). They are not currently used in regulatory capital, but they appear in economic capital frameworks at banks that want to express management risk-aversion explicitly rather than implicitly through a chosen confidence level.

### Tail dependence

Two random variables are **lower tail dependent** if the conditional probability that one falls in its lower tail, given that the other does, remains positive in the limit. The coefficient is `lambda_L = lim P(X1 < F1^-1(q) | X2 < F2^-1(q))` as `q` approaches 0. **Upper tail dependence** is defined analogously. The Gaussian copula has `lambda_L = lambda_U = 0` for any correlation strictly below 1, which is precisely the modelling sin that the synthetic CDO market committed: a model that says joint defaults in the extreme are no more likely than its body suggests, applied to a market where joint defaults in the extreme are the only thing that matters. Student-t, Clayton, and Gumbel copulas all admit non-zero tail dependence, and choosing among them is a choice about which corner of the joint distribution the bank thinks needs modelling care.

## Model risk and validation

Every measurement model has **model risk**: the risk that the model is wrong. This is now a regulated risk type in its own right, with two anchor texts: SR 11-7 in the US (Federal Reserve, 2011) and SS1/23 in the UK (PRA, 2023, superseding SS3/18). Both formalise the discipline of validating, monitoring, and governing the models that produce regulatory and management numbers.

### Sources of model risk

Three sources, conventionally:

- **Specification error**. The functional form, assumed distribution, or set of risk factors does not represent the underlying risk. A linear regression on a non-linear payoff is the canonical example.
- **Parameter error**. The functional form is correct but the parameter estimates are wrong, usually because the calibration sample is too small, biased, or drawn from a non-representative regime.
- **Implementation error**. The mathematics and the parameters are correct but the production code does not faithfully implement them. Spreadsheet errors, version drift between research and production, and silent failures in upstream feeds all live here.

### Validation pillars

SR 11-7 organises validation around three pillars:

- **Conceptual soundness**. Does the model's design and theory match the risk it is meant to measure? Validators challenge the assumptions, the functional form, the data sources, and the documentation.
- **Ongoing monitoring**. Does the model continue to perform in production? Validators monitor accuracy, stability, and exception rates over time, and re-check the calibration when material drift is observed.
- **Outcomes analysis**. Do the model's predictions match realised outcomes? Backtesting, benchmarking, and out-of-time testing all live in this pillar.

### Backtesting

For VaR, three tests dominate. The **Kupiec proportion-of-failures** test asks whether the number of observed VaR breaches in a window matches the model's stated confidence level (for 99% one-day VaR over 250 trading days, the expected count is 2.5; the test is a binomial-likelihood ratio). The **Christoffersen independence test** asks whether breaches cluster in time, because clustered breaches indicate that the model misses regime changes even if the count is correct. Both are combined in Christoffersen's conditional coverage test. The **Basel traffic-light approach** translates breach counts into a multiplier on the regulatory capital charge: zero to four breaches in 250 days is the green zone (multiplier of 3.0), five to nine is the yellow zone (multiplier scaling up to 3.85), ten or more is the red zone (multiplier of 4.0 plus a likely model revocation conversation).

For credit risk PD and LGD, backtesting moves to comparing realised default rates and recoveries against predicted, segmented by grade and vintage. The Hosmer-Lemeshow chi-squared and the binomial test by grade are the standard tools. For ES, backtesting is harder because ES is not an elicitable quantity from a single realisation; current practice combines Acerbi-Szekely's test with a VaR backtest at the underlying confidence level.

### Challenger models and benchmarking

A **challenger model** is an independent model run in parallel with the production model on the same exposures, calibrated under different assumptions or with a different functional form. Material divergence between the two prompts investigation. Challenger models protect against three specific failure modes: model overfitting (the production model fits its sample well but a simpler challenger generalises better), specification bias (a single specification can be very wrong; two independent specifications rarely both fail in the same direction), and supervisory groupthink (everyone using the same model with the same assumptions).

Benchmarking against external comparators (peer banks, vendor models, supervisory benchmarks) complements challenger modelling but introduces the systemic-risk problem flagged at the top of this file: convergence on the same answer is not the same as convergence on the correct answer.

### Margins of conservatism

A **margin of conservatism** (MoC) is an explicit add-on to a model output, sized to cover identified weaknesses in the data, methodology, or scope. The EBA Guidelines on PD estimation, LGD estimation, and the treatment of defaulted exposures structure MoCs into three categories: category A covers data and methodology deficiencies, category B covers shifts between the calibration sample and the current application portfolio, and category C is a general add-on covering residual uncertainty. MoCs are documented, reviewed periodically, and reduced as the underlying deficiency is remediated. They are how the model risk that cannot be removed is carried explicitly on the capital plan rather than ignored.

### Governance

The standard governance pattern: a board-level model risk policy, a model inventory covering every material model in the bank, a tiering scheme that scales validation intensity to materiality, an independent model validation function reporting to the Chief Risk Officer (not to model development), a model risk committee that approves new models and material changes, and an annual cycle of revalidation. SR 11-7 and SS1/23 are the supervisory anchors; both require board-level ownership of the framework and explicit identification of accountable individuals under the senior managers regime. This section is the natural seed for a future standalone wiki file on model risk management; for now it remains the primer's responsibility.

## The actuarial control cycle

The actuarial control cycle is useful to the [[01-risk_management|risk management]] function of any bank. Every model should be evaluated against all four of its stages: monitor and assess experience, determine assumptions, apply relevant approaches and techniques to valuation and pricing, and measure, report, and manage results. The model that does not move when experience does is the model that is silently failing.

The cycle closes the gap between measurement and management. A risk number that arrives in a committee pack but does not surface in a decision is theatre. The strongest risk functions build the loop explicitly: every metric on the committee dashboard has an attached decision criterion, and the meeting minutes record which decisions were made in response. Measurement is only useful when it changes a decision.
