## **Risk Differentiation – EAD**

### **Model Design**

* The EAD model is developed at an **account level** using a **Generalised Linear Model (GLM)** framework.
* GLMs are chosen because they **relax the restrictive assumptions of linear regression**, in particular:

  * They allow for **non-normality** in the dependent variable distribution.
  * They permit flexible link functions between predictors and the response variable.
* The target variable is the **Exposure at Default Factor (EADF)**.
* The general GLM form is:

[
g(E[y]) = \beta_0 + \beta_1x_1 + \dots + \beta_kx_k
]

Where:

* (y) = account-level EADF,

* (g(\cdot)) = link function,

* (\beta) = model parameters estimated using **Maximum Likelihood Estimation (MLE)** in Python.

* **EADF distribution is heavily right-skewed**. Several candidate families were tested:

  * **Distributions**: Gamma vs Gaussian
  * **Link functions**: Identity vs Log

* Following diagnostic testing, all final models were specified as **Gaussian distribution with Identity link**, as this combination provided the best fit and interpretability across portfolios.

---

### **Literature Review**

* Academic and industry studies suggest that **direct EAD models** can outperform traditional **Credit Conversion Factor (CCF) models**, particularly for accounts with high utilisation.
* In line with **Tong (2016)**:

  * **Direct EAD models** provide better accuracy at high utilisation levels.
  * **CCF-based models** may be more effective for low utilisation exposures.
* This study informs our modelling choice, balancing interpretability, predictive accuracy, and regulatory acceptance.

---

### **Segmentation**

Segmentation follows a similar process to PD:

* **Data construction**: 12 monthly cohorts of Core and Gap data from 2023.
* **Metrics for risk differentiation**: (R^2), Gini, and Lift ratio were used to assess discriminatory power across candidate segments.
* **Key segmentation drivers**:

  * **Utilisation** and **Limits** were the most significant factors.
  * **Decision trees** were applied to determine optimal cut-offs for key splits.

**Final segmentation structure:**

1. **Delinquency status** (current vs delinquent)
2. **Seasoning** (Early MOB vs Seasoned, cut-off determined via decision tree)
3. **Limit banding** (low limit < 1,000 vs higher limits)
4. **Activity** (active vs inactive accounts)
5. **Internal utilisation bands**: 10%, 20%, 50%, 60%, 90% (decision tree splits using EADF as target)
6. **External utilisation segmentation**

* For each final segment, a summary table is constructed showing:

  * Average **EADF**
  * Average **EAD**
  * Default count
  * Good book limit, balance, and volume

This segmentation ensures that the EAD model is **granular, interpretable, and capable of capturing key drivers of exposure behaviour**.

---

✅ Next natural piece would be **Differentiation Testing Results for EAD** (parallel to PD: Accuracy, Discrimination, Stability, Robustness, Stress Testing, Benchmarking).

Do you want me to draft the **Differentiation Testing Results for EAD** section now, reusing the PD test framework but adapting the test definitions (e.g., error metrics for continuous EAD instead of PDs, Gini on EADF prediction, PSI/CSI for stability, sensitivity to utilisation shocks for stress)?
