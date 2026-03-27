Here is the structured write-up for the **Data Representativeness** section, incorporating all your detailed notes in a professional, regulatory-aligned format:

---

## 5. Data Representativeness

### 5.1 Objective and Regulatory Context

The objective of this section is to demonstrate that the modelling data is **sufficiently representative** of the portfolio to which the IRB models will be applied, in accordance with:

* **[[crr|CRR]] Article 174(c)** – requiring that development and application populations be comparable,
* **[[pra|PRA]] [[ss4-24|SS4/24]] Paragraphs 8.2–8.15**, which set out expectations for assessing representativeness, including statistical comparisons of key characteristics and structural portfolio features.

Where data representativeness limitations exist, **appropriate adjustments must be made**, and these are further addressed in the **Model of Conservatism (MoC)** section.

---

### 5.2 Methodology

Multiple tests were carried out to assess representativeness:

* **Population Stability Index (PSI)** and **Chi-Square tests** were used to compare the development ([[03-risk-differentiation|risk differentiation]]) and calibration ([[07-risk_quantification|risk quantification]]) samples against the **application portfolio**.
* These tests were performed at both **portfolio level** and **segmented level**, across multiple time points.

---

### 5.3 Results – Probability of Default (PD)

#### 5.3.1 Scope of Application

Comparisons were made across the following key risk drivers:

* **Current credit limit bands**
* **Current utilisation bands**
* **Current balance bands**
* **Delinquency buckets**
* **Product group**
* **Revolver vs. Transactor status**
* **Months on Book (MoB)**
* **FICO score bands**
* **PiT [[06-segmentation|segmentation]]**

A notable structural shift was identified during the analysis:

* A **change in product mix** occurred following the **acquisition of a new business line**.
* In response, a **product flag** was incorporated into the [[06-segmentation|segmentation]] logic to ensure representativeness across new and legacy products.
* All other characteristics showed:

  * **PSI values close to 0**, indicating stable distributions,
  * **Chi-Square statistics close to 1**, indicating no statistically significant difference between the development and application datasets.

#### 5.3.2 Default Definition (DoD)

* **Time series plots** of DoD components (e.g., bankruptcy, forbearance types, fraud) were used to validate **temporal consistency** of default drivers.
* These plots confirmed that the definition and observed behaviour of default remained consistent across the development and application periods.

#### 5.3.3 Risk Driver Distribution Checks (CDI)

* A **Characteristic Stability Index (CDI)** was applied using the same formula as PSI, but focused on **individual model variables**.
* For **continuous variables**, comparisons were made using **decile distributions**.
* Analysis covered:

  * **Key risk drivers within each PiT segment** used for [[03-risk-differentiation|risk differentiation]],
  * **Final model variables** used for [[07-risk_quantification|risk quantification]].
* Outliers and missing data were also profiled and found to be consistent across samples.

---

### 5.4 Lending Standards and Recovery Policies

* A key qualitative and quantitative check involved assessing changes in **[[00_underwriting|underwriting]] or collections strategies**.
* Example: For **March 2009**, the 12-month average PiT segment distribution before and after a known **strategy change in April 2009** was compared.
* No material shift in the key PiT [[06-segmentation|segmentation]] or risk profile was identified.
* Discussions with **model owners** and **collections teams** confirmed:

  * No foreseeable **policy or strategy changes** in the near term,
  * No expectation of deviation from the development environment.
* Therefore, **no Adjustment Allowance (AA)** or **MoC** was required in this context.

---

### 5.5 Macroeconomic Environment (Calibration Only)

* This analysis applies only to the **[[07-risk_quantification|risk quantification]] (calibration)** samples.
* Representativeness was assessed by comparing:

  * **Observed Default Rates (ODRs)** over time,
  * With changes in **Macro-Economic Variables (MEVs)** on a quarter-on-quarter basis.
* Example: Unemployment rate bands were tracked against overall portfolio ODRs to validate **economic sensitivity**.
* Results confirmed that the chosen **Long-Run Average (LRA)** and **Downturn (DT)** periods captured representative economic conditions.

---

Let me know if you want to go straight into the **Model [[06-segmentation|Segmentation]]** section next or wrap this into a compiled draft.
