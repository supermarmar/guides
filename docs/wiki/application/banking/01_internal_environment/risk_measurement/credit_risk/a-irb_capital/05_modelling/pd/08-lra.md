---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/modelling/pd/lra
  - difficulty/unknown
  - study-status/new
aliases:
---
Perfect — you’re now in the **Long-Run Average (LRA) section of PD quantification**. Let’s reframe what you’ve written into a clear **narrative for “LRA Period”** with the regulatory references and the 4-step process explained in context.

---

### **LRA Period**

Under **[[crr|CRR]] Article 180(2)(a)**, probability of default (PD) estimates must be calibrated to the **long-run average (LRA)** default rate per grade. The selection of an appropriate LRA period is therefore critical.

* **Minimum requirements:**

  * **[[crr|CRR]] Article 180(2)(e)** specifies that the observation period for PD estimation must cover **at least 5 years** and include both **good** and **bad** years of the credit cycle.
  * **[[pra|PRA]] [[ss4-24|SS4/24]] paragraph 11.13** expands on this, stating that banks should consider:

    * The variability of all observed one-year default rates (ODRs),
    * The relative frequency of good and bad years in relation to the most relevant macroeconomic variables (MEVs) that drive default risk for the exposures, and
    * Any significant structural changes in the economic, legal, or business environment that could affect comparability over time.

Together, these requirements ensure that the LRA period captures a representative distribution of credit outcomes and avoids bias towards benign conditions.

---

### **4-Step Process for Determining the LRA Period**

1. **Derive factors of the conjunction representation**

   * Identify the macroeconomic variables (MEVs) most strongly associated with default risk for the exposure class.
   * Use these to build a representation of the [[03-economic_envrionment|economic environment]] over time.

2. **Determine good and bad periods**

   * Split historical data into “good” (benign) and “bad” (stressful) years, based on observed default experience and movements in the MEVs.

3. **Identify the economic cycle**

   * Map out the full cycle by linking good and bad periods, ensuring cyclical patterns are properly captured.
   * This prevents over-reliance on one type of economic condition.

4. **Define the range of ODRs**

   * Calculate the distribution of one-year observed default rates (ODRs) across the cycle.
   * This provides the empirical basis for setting the LRA by balancing the contribution of both good and bad periods.

---

✅ **Paraphrase / Summary:**
The LRA period should be chosen to reflect a balanced view of credit risk across the cycle. Regulations require that it spans at least 5 years, includes both good and bad years, and is sensitive to macroeconomic drivers of default. A structured 4-step process is followed: (i) identify relevant macroeconomic drivers, (ii) classify years as good or bad, (iii) map the economic cycle, and (iv) assess the observed default rate distribution.

---

Would you like me to also write up the **“LRA Calibration” subsection** next, in the same structured style, so you can directly use both in your [[07-risk_quantification|risk quantification]] section?

Perfect — I’ve amended your **LRA Period subsection** to incorporate the detailed methodology you’ve just outlined. Here’s a clean, structured draft you can use directly:

---

### **LRA Period**

Under **[[crr|CRR]] Article 180(2)(a)**, probability of default (PD) estimates must be calibrated to the **long-run average (LRA)** default rate per grade. The selection of an appropriate LRA period is therefore critical.

* **Minimum requirements:**

  * **[[crr|CRR]] Article 180(2)(e)** specifies that the observation period for PD estimation must cover **at least 5 years** and include both **good** and **bad** years of the credit cycle.
  * **[[pra|PRA]] [[ss4-24|SS4/24]] paragraph 11.13** expands on this, requiring firms to consider:

    * The variability of all observed one-year default rates (ODRs),
    * The relative frequency of good and bad years reflected by relevant macroeconomic variables (MEVs), and
    * Any significant structural changes in the economic, legal, or business environment.

---

### **4-Step Process for Determining the LRA Period**

1. **Derivation of Economic Factor**

   * **Macroeconomic variables (MEVs)** were selected based on their relevance to US credit card default risk, guided by business intuition and alignment with the key drivers in the [[ifrs9_standard|IFRS 9]] model.
   * Variables included: **Unemployment rate, debt-to-income ratio, CPI, industry charge-off rate, consumer confidence index (CCI), disposable income, GDP, and house price index (HPI)**.
   * Transformations such as **quarter-on-quarter relative or absolute changes** and **6/12-month moving averages** were explored.
   * **Principal Component Analysis (PCA)** was then applied to consolidate the MEVs into a single factor, capturing the overall economic trend.

2. **Classification of Good and Bad Periods**

   * **PCA scores** were used to classify quarterly cohorts:

     * **Positive PCA score → Good economic period**
     * **Negative PCA score → Bad economic period**
   * The balance between good and bad periods was assessed to ensure that the LRA period contained a representative mix of both conditions.

3. **Identification of the Economic Cycle**

   * There is no strict rule for defining an economic cycle. A common approach is to capture a **full expansion and contraction** by considering periods from one **peak to the next (or trough to trough)**.
   * For this exercise, a **peak-to-peak definition** of the cycle was selected to ensure both phases of the cycle are captured.

4. **Assessment of ODR Variability**

   * The variability of one-year observed default rates (ODRs) within the LRA period was tested against that of the full economic cycle.
   * An **F-test** was applied:

     * **H₀:** Variability of ODRs in the LRA period = Variability of ODRs in the economic cycle.
     * **H₁:** Variability of ODRs in the LRA period ≠ Variability of ODRs in the economic cycle.
   * A **p-value greater than 5%** indicates that the variability ranges are not statistically different, supporting the representativeness of the chosen LRA period.

---

✅ This version is fully aligned with your methodology and regulatory references, but also reads cleanly and professionally for documentation.

Would you like me to now move on and prepare the **LRA Calibration subsection** in the same style (objectives, regulatory reference, methodology)?

Great — thanks for sharing the additional context. I’ll extend and integrate this into your **LRA Period** section so it captures both the **exclusions (COVID-19)**, the **chosen downturn (DT) and LRA period**, the **macro/ODR relationships**, and the **PCA option selection** with visuals you mentioned. Here’s a polished version:

---

### **LRA Period**

Under **[[crr|CRR]] Article 180(2)(a)**, probability of default (PD) estimates must be calibrated to the **long-run average (LRA)** default rate per grade. The selection of an appropriate LRA period is therefore critical.

* **Minimum requirements:**

  * **[[crr|CRR]] Article 180(2)(e)** specifies that the observation period for PD estimation must cover **at least 5 years** and include both **good** and **bad** years of the credit cycle.
  * **[[pra|PRA]] [[ss4-24|SS4/24]] paragraph 11.13** requires firms to also consider:

    * The variability of one-year observed default rates (ODRs),
    * The balance of good and bad years represented by relevant macroeconomic variables (MEVs), and
    * Any significant changes in the economic, legal, or business environment.

---

### **Scope of Periods Considered**

* **Exclusions:** Data from **2020–2022 (COVID-19)** was excluded from the calibration period. Default rates during this period were distorted by **government stimulus packages, payment holidays, and the suppression of recovery activities**, and therefore were not representative of true credit risk.
* **Downturn (DT) period:** Defined as **2008–2009**, capturing the global financial crisis when default rates materially spiked.
* **LRA period selected:** **2008 Q1 – 2017 Q1**, ensuring sufficient coverage of both good and bad years.
* **Reference economic cycle:** Defined from **2008 Q2 – 2018 Q1 (peak-to-peak)** to capture a full cycle of expansion and contraction.

---

### **Macro-Economic Variable (MEV) Relationships**

* **Line plots** of MEVs against ODRs showed clear cyclical relationships:

  * **Unemployment rate (UR):** Strong positive correlation with ODRs (**R² = 62%**)
  * **Industry charge-off rate:** High positive correlation with ODRs
  * **GDP and House Price Index (HPI):** Negative correlation with ODRs
* These relationships confirmed the **economic drivers of default risk** and were consistent with business intuition.

---

### **PCA Methodology and Options**

* **MEVs considered:** unemployment rate (UR), debt-to-income ratio (DTI), consumer price index (CPI), GDP, HPI, CCI, disposable income, industry charge-off rate.
* **Transformations explored:** quarter-on-quarter relative and absolute changes, and 6/12-month moving averages.
* **Principal Component Analysis (PCA):** used to consolidate MEVs into a single factor representing overall economic conditions.

**Option 1 (selected):** UR, CPI, and DTI

* Produced a balanced mix of **48/52 good vs bad quarters** in the chosen LRA period,
* Mirrored the balance in the reference economic cycle,
* Passed the **F-test** for ODR variability (p-value > 5%),
* Aligned with the **[[ifrs9_standard|IFRS 9]] impairment model**, ensuring methodological consistency across accounting and regulatory credit risk models.

---

### **Supporting Visuals**

1. **Line plots**: Quarterly Unemployment Rate vs ODR, showing strong positive relationship.
2. **Correlation heatmap**: Demonstrating direction and strength of MEV-ODR relationships (UR, charge-off rate positive; GDP, HPI negative).
3. **PCA score plot**: PCA factor vs actual default rates over time, showing close alignment.

---

✅ This version sets up the **LRA period choice** cleanly with regulatory alignment, explains why COVID was excluded, specifies the downturn, and documents why Option 1 was selected.

Do you want me to now draft the **LRA Calibration** subsection in the same structured way (objectives, regulatory references, methodology, tests, graphs)?

Perfect — thanks for laying out the detail. I’ll now turn that into a structured, polished **LRA Calibration** subsection that ties the regulatory requirements, methodology, and validation tests together. Here’s the draft:

---

## **LRA Calibration**

### **Regulatory Requirements**

* **[[crr|CRR]] Article 169(3):** PD estimates must be assigned on a **discrete rating scale**. All accounts allocated to the same **risk grade** (based on their PiT PD) are assigned a single PD estimate, equal to the **long-run average default rate (LRA DR)** of that grade.
* **[[pra|PRA]] [[ss4-24|SS4/24]] (11.10c):** Permits both **overlapping** and **non-overlapping** performance windows. However, if overlapping windows are used, firms must perform an analysis of **potential bias** due to overweighting observations in the overlap.
* **[[pra|PRA]] [[ss4-24|SS4/24]] (11.31):** Requires that **PDs increase monotonically across grades**, ensuring consistency and interpretability of the risk scale.

---

### **Methodology**

1. **Default Rate Definition:**

   * For each quarter, the default rate is defined as the proportion of accounts that transition into default within the next 12 months (**T=1 to T=12**) relative to all accounts **not in default at T=0**.
   * This approach implies that **performance windows for consecutive quarters overlap**, since each quarter launches a new 12-month observation horizon.

2. **LRA DR Calculation:**

   * For each risk grade, the **quarterly default rates** were averaged across the full **LRA period (2008 Q1 – 2017 Q1)** to produce the LRA PD estimate per grade.

3. **Bias Assessment – Overlap vs Non-Overlap:**

   * In line with [[ss4-24|SS4/24]] 11.10c, an assessment of bias from overlapping windows was performed.
   * The LRA DR was recalculated using **non-overlapping windows** (i.e., selecting a non-overlapping set of performance periods).
   * The **overall LRA DR** for each grade was then **ranked against the distribution** of quarterly LRA DRs.
   * This analysis confirmed that overlapping did not materially bias the estimates, since the LRA DRs derived were stable relative to non-overlapping measures.

---

### **Validation and Tests**

* A **summary table** was created showing:

  * Risk Grade,
  * Minimum and Maximum PiT PD within the grade,
  * Assigned LRA PD,
  * Ratio of each grade’s LRA PD relative to the prior grade.
* Results demonstrated that:

  * **Monotonicity** was achieved (i.e., higher grades consistently mapped to higher PDs), meeting [[ss4-24|SS4/24]] 11.31.
  * Ratios between grades provided evidence of meaningful separation and discrimination power.

---

### **Portfolio-Level Performance**

* A **line graph** was plotted of:

  * **Quarterly observed portfolio-level average default rates (ODRs)**, and
  * The **assigned LRA PDs**.
* As expected:

  * **During stressed periods (e.g., 2008–2009 downturn):** the LRA PD underestimates actual observed default rates.
  * **During benign periods:** the LRA PD overestimates observed default rates.
* This demonstrates that the calibration appropriately smooths through the cycle, balancing good and bad years, in line with regulatory intent.

---

✅ This structure captures the **regulatory references**, explains the **bias check for overlap**, documents the **monotonicity validation**, and closes with the **expected portfolio behaviour** of LRA PDs relative to actual ODRs.

Would you like me to also draft the **table layout** (with sample column headers for PiT PD range, LRA PD, monotonicity ratio) so you have a ready-made structure to fill in with results?
