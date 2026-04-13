---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/feature-engineering/pd/sampling
  - difficulty/unknown
  - study-status/new
aliases:
---
## 4. Sampling Strategy

### 4.1 Overview

This section outlines the sampling design and logic underpinning the Probability of Default (PD) model, including the choice of observation windows for model development, calibration, and validation. The sampling strategy ensures statistical independence, business relevance, and robustness to economic and operational distortions.

---

### 4.2 Source Data and Snapshot Availability

* The **Model-Ready Data (MRD)** consists of **month-end account-level snapshots** beginning in **March 2007**.
* Each snapshot contains sufficient feature data and target outcome labels (e.g., default flags).
* The **most recent snapshot** available with a **full 12-month performance window** is **March 2024**, allowing performance outcomes to be observed through **March 2025**.

---

### 4.3 Development Sample ([[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/05_modelling/pd/03-risk-differentiation|Risk Differentiation]])

The development sample for [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]] was carefully selected to ensure robustness and exclusion of distorted periods:

* **COVID Period Exclusion:** Snapshots between **December 2018 and June 2022** were excluded from development due to multiple distortions:

  * Payment holidays
  * Regulatory forbearance measures
  * Reduced observed default rates
  * Unstable macroeconomic and behavioural trends
* **Development Window:** Snapshots from **March 2007** through **December 2018**, and again from **June 2022 to December 2023** were retained.
* **De-duplication:** Observations were selected such that **each account appears only once**, ensuring:

  * **Non-overlapping exposure windows**
  * **Independence** between observations
* **Random Sampling Approach:**

  * For **segments** with more than **5 million observations**, random **downsampling** was applied.
  * A **weighting approach** was introduced:
    [
    w = \frac{\text{Total observations in segment}}{5,000,000}
    ]
    The same weight (w) was assigned to all observations within a given segment to maintain proportionality during model estimation.
* **Stratified Sampling Considered But Not Used:**

  * While stratified random sampling could preserve distributions across certain variables, it introduces **subjectivity and potential bias**:

    * Choosing **which characteristics** to stratify on
    * Defining **bin boundaries**
    * Potential for oversampling/undersampling subtle but important cohorts
* **Dev/Holdout Split:** A simple **70/30 split** across the development window was avoided, as observations might overlap across different months—violating independence assumptions.

---

### 4.4 Calibration Sample ([[07-risk_quantification|Risk Quantification]] / LRA PD)

* A **Low Risk Adjustment (LRA)** period was defined for **calibration**.
* This period spans from the **start of a previous downturn** through to the **start of the next peak** in risk, ensuring observed defaults reflect **long-run average default behaviour**.
* This window was used exclusively for **PD quantification**, not for model training.

---

### 4.5 Out-of-Sample Testing (Model Validation)

* **Out-of-sample (OOS) testing samples** were drawn from cohorts **not included in development**.
* These OOS cohorts span snapshots from **June 2007 to December 2023**, excluding COVID-affected data.
* The **most recent valid snapshot with a 12-month outcome window**, **March 2024**, was used exclusively for **out-of-time (OOT) testing**.

  * It was not part of development or calibration.
  * It serves to validate **temporal generalisability** of the model and stress-test predictive power.

---

### 4.6 Application Sample (Monitoring and RWA Impact)

* The **application sample** consists of the most recent available snapshots (e.g., **June 2024 to December 2024**).
* It is used for:

  * **Model monitoring**
  * **Portfolio representativeness analysis**
  * **Risk-Weighted Asset (RWA) impact assessments**
  * **Stability testing** across time

---

Let me know when you’re ready to continue with **EAD** and **LGD** sampling strategies, or if you’d like this turned into a formatted document.

Here is the structured write-up for the **Sampling Strategy** section focused on **EAD modelling**: