---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/modelling/pd/risk-differentiation
  - difficulty/unknown
  - study-status/new
aliases:
---
# Risk Differentiation

As PDs are estimates of likelihoods, statistical methods are used to estimate PDs. These include:

- Linear or logistic regression (most commonly used)
- Discriminant analysis
- Logit and probit models
- Panel models
- Cox proportional hazards model
- Neural networks

### [[02-model-design|Model Design]]

A **binary logistic regression** model was selected for risk differentiation. This approach is widely adopted in the banking industry for default prediction due to its interpretability, regulatory acceptance, and ability to rank-order accounts effectively.

The logistic regression model predicts the probability of default ( p ) using the equation:

[
p = \frac{e^y}{1 + e^y}
]

Where ( y = f(X) ) is the linear predictor. The **logit link function** relates the linear predictor to the log-odds of default:

[
\log\left(\frac{p}{1-p}\right) = y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n
]

An increase of one unit in variable ( X_j ) changes the log-odds of default by ( \beta_j ) units.

The model parameters were estimated using **Maximum Likelihood Estimation (MLE)**. As no closed-form solution exists, the **Iteratively Reweighted Least Squares (IRLS)** algorithm was applied until convergence criteria were met.

---

### Alternative Approaches Considered

* **Multinomial Logistic Regression**: Discarded due to the Independence of Irrelevant Alternatives (IIA) assumption, which is unrealistic as credit outcomes are often correlated.
* **Nested (Sequential) Logistic Regression**: Relaxes the IIA assumption and is widely used, but not required for a binary default/non-default framework.
* **Decision Trees / Random Forests**: Handle non-linearities well but lack interpretability and transparency for regulatory compliance. These methods are also prone to overfitting despite potentially higher accuracy.

---

### [[08-segmentation|Segmentation]] Strategy

[[08-segmentation|Segmentation]] was undertaken prior to model estimation to maximise risk differentiation. The aim was to identify **homogeneous risk groups** that:

1. Share underlying risk drivers with a similar relationship to default
2. Have sufficient volume
3. Exhibit stability over time

Four **stacked snapshots** were used: **June 2016, March 2018, Dec 2022, and Sept 2023**. This period spans both benign and stressed conditions, including the pre- and post-GAP acquisition period and the COVID-19 pandemic. Seasonal biases were mitigated by sampling across quarters.

Initial splits were identified using **decision tree analysis** with historical default rates as the target. The following splits were established:

1. **Delinquency Status at Observation**

   * *In Order Accounts*
   * *Early Delinquency*: 1 cycle past due (1 month in arrears)
   * *Late Delinquency*: 2–3 cycles past due (2–3 months in arrears)

2. **Seasoned vs. Early Month on Book (EMOB)** for In Order Accounts

   * EMOB defined as MOB ≤ 3 (based on Gini optimisation)
   * EMOB risk is primarily driven by application and bureau data, as behavioural data is limited.

3. **Active vs. Inactive Accounts** for Seasoned Accounts

   * Inactive accounts receive proactive credit limit decreases and show distinct risk patterns.

4. **Clean vs. Dirty History** for Active Accounts

   * *Clean*: No delinquency in past 12 months
   * *Dirty*: ≥1 delinquency in past 12 months

5. **Internal Utilisation** Split for Clean Accounts

   * Preliminary model identified internal utilisation as a key risk driver.
   * Initial cut-offs at 41.1% and 81.8%, rounded to avoid overfitting → *Low*, *Medium*, *High Utilisation* groups.

6. **Further Split of Low Utilisation Segment** (~40% of population)

   * Key drivers:

     * Max external bureau utilisation (last 6 months)
     * Revolver vs. Non-Revolver status
     * % of missed payments (last 6 months)
   * Bureau utilisation split at 60% based on decision tree analysis.

7. **Low Internal + Low Bureau Utilisation Segment** (~30% of population)

   * Further split using *Revolver vs. Non-Revolver* flag.

---

### Final [[08-segmentation|Segmentation]] Schema

This multi-step approach resulted in segments that are internally homogeneous, stable over time, and exhibit clear differences in observed default rates. This [[08-segmentation|segmentation]] underpinned the subsequent variable selection and model estimation, ensuring strong discriminatory power while maintaining business interpretability and regulatory compliance.

---

```python
import pandas as pd

# Manually reconstructing the table from visible data in the image
data = [
    ["Late Delinquency", 364_110, "0.67%", 275_338, "75.62%"],
    ["Early Delinquency", 704_521, "1.30%", 215_702, "30.62%"],
    ["Early MOB", 2_124_588, "3.93%", 64_032, "3.01%"],
    ["Inactive", 14_244_707, "26.36%", 64_765, "0.45%"],
    ["Seasoned Clean Low Internal & Bureau Utilisation - Non-Revolver", 10_671_024, "19.75%", 30_971, "0.29%"],
    ["Seasoned Clean Low Internal & Bureau Utilisation - Revolver", 4_171_311, "7.72%", 24_691, "0.59%"],
    ["Seasoned Clean Low Internal & High Bureau Utilisation", 5_996_218, "11.10%", 85_530, "1.43%"],
    ["Seasoned Clean Mid Internal Utilisation", 4_444_902, "8.23%", 331_635, "7.66%"],
    ["Seasoned Clean High Internal Utilisation", 4_328_455, "8.01%", 516_928, "7.40%"],
    ["Dirty", 6_045_086, "12.93%", 1_737_966, "3.22%"],
]

df = pd.DataFrame(data, columns=["Segment", "Total Volume", "% Volume", "Total Defaults", "Default Rate"])

import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user(name="Segmentation Volume and Default Rates Table", dataframe=df)

```

Perfect — you’re now at the **Risk Differentiation** section for EAD, which should echo the PD structure ([[02-model-design|Model Design]] → Literature Review → [[08-segmentation|Segmentation]] → Risk Differentiation Tests), but tailored to the peculiarities of **EAD modelling**. Based on what you wrote, here’s a clean draft:

---
