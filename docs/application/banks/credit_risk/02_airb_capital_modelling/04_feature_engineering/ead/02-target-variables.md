Here's the continuation of the **Data Manipulation / Feature Transformation** section, focusing on the **target variables for PD, EAD, and LGD**. This write-up keeps the structure suitable for regulatory documentation or internal model governance reporting, linking the target variable choices to both regulatory standards and practical modelling trade-offs.

---

## 3. 🎯 Target Variables for PD, EAD, and LGD Models

### 3.1 📉 Probability of Default (PD)

#### Target Variable

* The **dependent variable** for PD modelling is the **default indicator** over a 12-month outcome window.
* The column (e.g., `m12_default`) flags whether the obligor defaults **at any time** within the 12 months following the observation date.
* This binary classification is in accordance with **CRR Article 180(2)(a)**, which requires the estimation of **1-year default rates**.
* The identification of default is based on the rules and classifications already described in the **Definition of Default (DoD)** section and includes both **90+ DPD** and **Unlikeliness to Pay (UTP)** events.

#### Key Characteristics

* **Type**: Binary (1 = default, 0 = no default)
* **Window**: Rolling 12 months from each observation date
* **Coverage**: Includes all IRB-eligible exposures in the development population
* **Usage**: Core target for PD model development, calibration, and performance tracking

---

### 3.2 💰 Exposure at Default (EAD)

The EAD target is more complex due to the variety of ways in which utilisation and credit availability can change over time, especially for revolving products like credit cards or overdrafts.

#### 3.2.1 Raw Outstanding Amount (Untransformed)

* This refers to the **total outstanding amount** at default (`EAD_tD`), which serves as the basis for calculating transformed targets.

* It can differ from:

  * **IFRS carrying values** (due to inclusion of off-balance sheet items or accrued interest),
  * **Internal account balances** (which may or may not include fees, interest, or accrued charges), and
  * **Post-default drawings** (depending on the bank’s recovery or workout policy).

* This amount is used:

  * As a **numerator** in LGD calculations (Loss = EAD - Recoveries),
  * To define the transformed EAD modelling targets described below.

#### 3.2.2 Transformed EAD Targets

Different target variable transformations are applied to better align with model performance, business use, and interpretability. Each has distinct pros and cons:

| Target   | Formula                                                                   | Description                         | Strengths                                                                           | Weaknesses                                                                                               | Typical Range               |
| -------- | ------------------------------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------- |
| **EAD**  | EAD<sub>tD</sub>                                                          | Dollar value of exposure at default | Simple, easy to understand                                                          | Scale-sensitive, hard to model across balances, doesn’t use limit or available credit                    | ≥ 0                         |
| **LEQ**  | EAD<sub>tD</sub> / Total Balance<sub>t0</sub>                             | Loan Equivalent                     | Good for high-utilisation, closed accounts                                          | Unstable with low balances, undefined for 0 balance                                                      | 0–2 (but can spike)         |
| **EADF** | EAD<sub>tD</sub> / Credit Limit<sub>t0</sub>                              | Exposure as % of credit limit       | Smooths volatility, stable trends, combines drawn & undrawn, intuitive for business | Omits current balance, can crowd out impact of other drivers, >1 possible if limit increases pre-default | Typically 0–1, can exceed 1 |
| **CCF**  | (EAD<sub>tD</sub> – Balance<sub>t0</sub>) / Available Credit<sub>t0</sub> | Credit Conversion Factor            | Focuses on undrawn portion, precise tracking of conversion                          | Can be volatile, undefined for 0 avail credit                                                            | -∞ to ∞ (often > 0)         |
| **UCF**  | (EAD<sub>tD</sub> – Balance<sub>t0</sub>) / Credit Limit<sub>t0</sub>     | Utilisation Conversion Factor       | Normalised undrawn draw                                                             | Ignores full drawn usage                                                                                 | 0–1+                        |

#### 3.2.3 Selection Considerations

* **EADF** is often preferred due to:

  * Its **stability across credit cycles**,
  * Strong correlation with utilisation at t0,
  * Intuitive interpretation for business users and regulators.

* However, banks may choose **EAD** or **LEQ** where:

  * Business decisions rely on absolute amounts,
  * Balance volatility is low, or
  * Simplified interpretation is needed.

* Model developers should evaluate:

  * **Goodness-of-Fit** (Gini, RMSE, AIC),
  * **Holdout performance** (on out-of-time sample),
  * **Predictor interpretability**, and
  * **Business and regulatory alignment**.

Here is a write-up for **Section 3.2: EAD Target Variable Analysis**, based on your notes:

---

## 3.2 Selection of EAD Target Variable

To determine the most appropriate target variable for **Exposure at Default (EAD)** modelling, we undertook a structured comparative analysis between two candidate target transformations: **EADF** (EAD as a proportion of credit limit) and **CCF** (Credit Conversion Factor).

### 3.2.1 Candidate Target Definitions

* **EADF** = EAD at default / Credit limit at observation
* **CCF** = (EAD at default – Balance at observation) / Available credit at observation

These were chosen due to their interpretability and use in industry, and their alignment with both internal practice and regulatory expectations.

---

### 3.2.2 Segmented Preliminary Modelling

A toy model was developed using four intuitive portfolio segments to test performance under each target transformation:

* **EMOB** buckets (Early Months on Book)
* **Inactive accounts** (no activity >4 months)
* **Utilisation <10%**
* **Utilisation between 10–95%**

This segmentation allowed early identification of structural biases or volatility in target variables across key behavioural clusters.

---

### 3.2.3 Volatility Analysis

Results showed:

* **CCF exhibited significantly higher variance**, especially in:

  * High utilisation accounts (where balance ≈ credit limit)
  * Low utilisation or inactive accounts (where available credit is high)
* **EADF showed more stable distributions** across all segments, with lower susceptibility to extreme values.

---

### 3.2.4 Predictive Performance Evaluation

We compared actual vs predicted EAD values on both candidate models using the following diagnostics:

* **Relative Error** (|Predicted EAD – Actual EAD| / Actual EAD)
* **Visual comparison** of predicted vs actual EAD

This was conducted:

* Across full portfolio (excluding accounts with utilisation >95% where **CCF becomes unstable**)
* On **Good Book** vs **Bad Book** (accounts that defaulted vs didn’t)
* By **FICO band**, **credit limit band**, and **utilisation band**

**EADF consistently showed lower error volatility**, better central tendency alignment, and smoother trends across segmentation variables.

---

### 3.2.5 Considerations on CCF Definition Complexity

**CCF introduces practical modelling complications** due to its conditional nature:

* When balance ≈ limit → **available credit ≈ 0** → CCF explodes or is undefined.
* To resolve:

  * If balance = limit → define CF = 1
  * If balance = 0 → define CF = EAD / limit
  * Else → define CF = EAD / balance
    Each approach introduces an **assumption** that must be **justified and tested**. Sensitivity analysis is required to confirm robustness across these edge cases, making deployment more complex.

---

### 3.2.6 Final Selection and Justification

**EADF was selected** as the final EAD target transformation for the following reasons:

* **Industry standard** — commonly used in IRB portfolios
* **Simpler modelling assumptions** and better model interpretability
* **Lower volatility** in outcome variable, supporting better generalisation
* **Consistency** with other Business Units and past validation work

---

### 3.2.7 Supporting Diagnostics

We plotted historical trends of **EADF** across the portfolio, including:

* **Median and mean EADF** over time
* **Account volume** supporting each monthly or quarterly view
* Stability of EADF distributions in different portfolio segments

These showed strong and stable behaviour over time, adding to the robustness of this choice.

---

Let me know if you'd like the accompanying plots or summary tables drafted as well.


---

### 3.3 💸 Loss Given Default (LGD)

LGD is modelled using a **component-based approach** to capture the complex nature of post-default outcomes. The target is not a single value but built from two or more sub-models:

#### 3.3.1 Component Targets

1. **Loss Rate (LGW)**

   * Formula: `(EAD_tD – Total Recoveries) / EAD_tD`
   * This continuous variable captures the **loss severity** as a proportion of exposure.

2. **Probability of Loss / Recovery (PWGD or PR)**

   * Binary flag indicating whether **any recovery occurs** post-default.
   * Enhances model granularity by predicting whether the account will experience full, partial, or no recovery.

#### 3.3.2 Considerations

* Losses and recoveries are tracked over a **maximum resolution period**, typically **5 years**, in accordance with **Basel and PRA** expectations.
* LGD estimates should reflect **long-run average (LRA)** and **downturn (DT)** conditions, with proper segmentation by:

  * Security type (secured vs. unsecured),
  * Product type,
  * Recovery channels (e.g., internal collection, legal, third-party),
  * Default and recovery vintage.

---

Would you like a comparison matrix or visual decision tree added to help stakeholders choose between EAD target definitions for different products or portfolios?
