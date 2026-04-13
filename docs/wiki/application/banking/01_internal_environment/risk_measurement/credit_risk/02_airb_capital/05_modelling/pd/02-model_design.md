---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/modelling/pd/model-design
  - difficulty/unknown
  - study-status/new
aliases:
---
Here’s a structured write-up for your **[[02-model-design|Model Design]]** section based on what you’ve provided, keeping it clear, regulatory-aligned, and consistent with your earlier sections:

---

## [[02-model-design|Model Design]]

**Objectives**
The model was designed to meet three primary objectives:

1. **Risk Separation** – ensuring the model effectively differentiates between obligors of differing credit quality.
2. **RWA Stability** – limiting undue volatility in capital requirements over time.
3. **Partner Resilience** – enabling the model to be applied to new partners without the need for 12 months of performance data.

**Model Development Process**
The development process followed a structured sequence:

1. **Point-in-Time (PiT) PD estimation**
2. **Risk grade assignment**
3. **Long-Run Average (LRA) PD calculation**
4. **Margin of Conservatism (MoC) calculation**
5. **Regulatory PD derivation**

This process was executed in two distinct phases:

---

### 1. [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/05_modelling/pd/03-risk-differentiation|Risk Differentiation]] (Risk Diff) Phase

**Objective:** Develop a rating model with strong discriminatory power, enabling robust rank ordering of accounts.

* **[[07-segmentation|Segmentation]] Analysis:** The portfolio was segmented into groups of accounts sharing common risk drivers and similar default relationships. This [[07-segmentation|segmentation]] allows for more accurate PiT PD estimation and maximises the model’s overall risk separation.
* **Variable Analysis:**

  * **Univariate analysis** to assess individual predictive power.
  * **Correlation analysis** to identify redundancy and ensure variable diversity.
  * **[[06-variable-transformation|Variable transformation]]** (e.g., binning, log transformations) to improve predictive strength and model stability.
* **Model Estimation:** Logistic regression models were developed for each segment to estimate PiT PDs.

---

### 2. [[07-risk_quantification|Risk Quantification]] (Risk Quant) Phase

**Objective:** Ensure appropriate absolute PD levels are assigned to obligors in line with regulatory expectations.

* **Historical Back-Scoring:** The PiT PD model was applied to historical data to obtain predicted PDs for all accounts.
* **Binning to Risk Grades:** PiT PDs were mapped into discrete risk grades via a binning procedure, grouping obligors into homogeneous pools.
* **Observed Default Rates:** One-year average default rates were calculated for each grade.
* **LRA PD Calculation:** For each grade, LRA default rates were computed using data spanning a mix of good and bad economic periods, in line with [[crr|CRR]] Article 180(1)(a). These LRA PDs represent the *Calibrated PD*.
* **Margin of Conservatism (MoC):** Applied at the grade level to account for estimation uncertainty, [[05-data_limitations|data limitations]], and potential future changes.
* **Final Regulatory PD:** The final PD assigned to each grade is the sum of the Calibrated PD and the MoC. The final regulatory PDs are discrete at the grade level (non-continuous).

---

**Regulatory Alignment:**

* **[[crr|CRR]] Articles 174, 179, and 180** – [[07-segmentation|Segmentation]], [[04-data-representativeness|data representativeness]], and calibration in line with long-run average default rates.
* **[[pra|PRA]] [[ss4-24|SS4/24]] Paragraph 11.20** – Quantitative and qualitative validation tests performed during [[07-risk_quantification|risk quantification]].
* **[[bis|Basel]] Requirements** – Incorporation of both rank-ordering capability and appropriate PD level setting.

---

If you’d like, I can also prepare a **visual process flow diagram** for this, which could help in explaining the two-phase approach clearly to both stakeholders and regulators. This will make the flow from PiT estimation to final regulatory PD more intuitive.

Do you want me to prepare that next?
