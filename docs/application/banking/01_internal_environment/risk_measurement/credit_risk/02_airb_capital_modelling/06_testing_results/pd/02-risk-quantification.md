Perfect — thanks for laying out the details. I’ll draft a full **Quantification Testing Results** section that follows the same structured tone as the Differentiation Testing Results section. This way, it looks like part of a model development or validation pack.

---

## **Quantification Testing Results**

Quantification testing was performed on the final **risk grades** and **calibrated LRA PDs** across development, OOS and OOT samples. The objective of this testing is to ensure that the assigned risk grades are meaningful, statistically reliable, and consistent with the requirements of **CRR Article 170**, while also demonstrating accuracy and stability over time.

The following test dimensions were considered:

* **Concentration**
* **Homogeneity within grades**
* **Heterogeneity between grades**
* **Migration analysis**
* **Calibration accuracy**

---

### **1. Concentration**

* In line with **CRR Article 170.3(b)**, the assigned risk grades were tested to ensure that:

  * No excessive concentration exists in a single grade, and
  * Each grade has a sufficient level of exposure to support reliable calibration.
* Tests performed:

  * **Exposure concentration test:** confirmed that the proportion of exposures in each grade falls within **1%–30%** of the total population. Results were displayed via line charts of grade concentration over time.
  * **Herfindahl–Hirschman Index (HHI):** calculated per quarter to assess overall grade concentration.

    * HHI > 0.25 indicates a high degree of concentration in a single grade.
    * A line plot of HHI over time confirmed values remained within acceptable thresholds.

---

### **2. Homogeneity within Grades**

* Tested whether exposures within each grade have statistically similar observed default rates.
* Methodology:

  * **Chi-square test** performed using **bootstrapping**:

    * 20 random samples generated with a 5% sampling rate for each grade and cohort.
    * Formula used:

      [
      \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
      ]

      where (O_i) = observed default count, (E_i) = expected default count.
  * Null hypothesis (H_0): Default rates across bootstrapped samples within a grade are **not statistically different**.
  * Decision rule: if **p-value > 5%**, null is not rejected (homogeneity holds).
* Results:

  * **Tables** show, per grade, the number and percentage of fails across quarterly cohorts.
  * At the overall level, the failure rate was **below 5%**, demonstrating sufficient within-grade homogeneity.

---

### **3. Heterogeneity between Grades**

* Tested whether adjacent grades are statistically different in terms of observed default rates.
* Methodology:

  * **Binomial z-test**:

    [
    Z = \frac{p_1 - p_2}{\sqrt{p(1-p)\left(\frac{1}{n_1}+\frac{1}{n_2}\right)}}
    ]

    where (p_1, p_2) are default rates of two grades, and (p) is the pooled default rate.
  * Null hypothesis (H_0): default rates between two bands are **not statistically different**.
  * Decision rule: **10% two-tailed significance level** used.
* Results:

  * **Tables** summarise number of fails and % of fails across cohorts.
  * **Monotonicity test:** visually assessed by plotting average ODRs per grade over time. The number of crossovers (non-monotonic movements) was also counted.
  * Overall results confirm sufficient heterogeneity between adjacent grades, with limited monotonicity breaches.

---

### **4. Grade Migration**

* Under a PiT framework, some idiosyncratic migration between grades is expected, but stability is important to avoid undue volatility in **RWA**.
* Methodology:

  * For each cohort, migration counts were tallied between grade **T** and grade **T+1**.
  * Migration matrices were constructed to show transitions across grades over time.
  * Further analysis quantified migrations within **±1 band** and **±2 bands**, to confirm the majority of exposures remain close to their original grade.
* Results:

  * Migration patterns were stable across periods.
  * Most accounts migrated within ±1 band, with limited migration beyond ±2 bands.
  * This supports the stability of RWAs and the reliability of the grade assignment process.

---

### **5. Calibration Accuracy**

* Tested whether the calibrated **LRA PDs** align with observed default rates across overall and sub-population levels.
* Methodology:

  * **Relative error (MPE):**

    [
    MPE = \frac{LRA_PD}{ODR} - 1
    ]

  * Calculated at overall, segment, and sub-population levels (e.g., utilisation bands, limit bands, MOB, product types).

  * Accuracy also tracked across time using line charts of actual vs predicted.
* Results:

  * At the overall level, relative error remained within acceptable tolerance bands.
  * Sub-population analysis confirmed accuracy across different product and behavioural cohorts.

---

✅ This section now flows like a regulatory-style model documentation. It links **CRR requirements**, **methodology**, **formulas**, **decision criteria**, and **results presentation (tables/plots)**.

Would you like me to also **prepare illustrative visuals** (e.g., example migration matrix, HHI line chart, chi-square results table) that you could drop directly into the document, similar to how you structured the differentiation section?
