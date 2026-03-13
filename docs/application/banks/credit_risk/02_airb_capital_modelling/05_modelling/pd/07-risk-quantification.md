# Risk Quantification for PD

### **1. Risk Grade Construction**

In accordance with **CRR Article 172(2)** and to meet the requirements of **CRR Article 171(1)**, all exposures are **jointly calibrated** across the portfolio.

* **No further calibration segmentation** is required.
* Risk grade boundaries are **defined directly from the scores** of all PiT PD segment models.
* This design allows **accounts to migrate** between grades to reflect **changes in PiT PD estimates** over time.

Here’s your **expanded Risk Grade Construction** section with the **iterative process** and **candidate grade testing** integrated in the same structured style as before.

---

## **Risk Quantification for PD**

### **1. Risk Grade Construction**

In line with **CRR Article 172(2)** requirements, all exposures are **jointly calibrated** to meet **CRR Article 171(1)**.

* Risk grade boundaries are derived from **scores of all PiT PD segment models**.
* This approach allows **accounts to migrate** between grades over time as PiT PD estimates change.

---

#### **1.1 Regulatory & Design Objectives**

(As per the table in the previous section – Minimum/Maximum volume, Homogeneity, Heterogeneity, Granularity, Stability – retained here for reference.)

---

#### **1.2 Grade Construction Methodology**

Grades were constructed using the **June 2024 cohort** and tested on historical data from **March 2008 to June 2024**, assessed at the end of each quarter.

* **COVID-19 period excluded** to avoid distortion in calibration.
* The process was **iterative** to ensure regulatory compliance and portfolio relevance.

---

**Step-by-Step Process**

1. **Back-score PiT PD Model**

   * Apply the final PiT PD model to historical data to generate **PD scores** for each account across all quarters.

2. **Create Initial Grades**

   * Rank **June 2024 accounts** by PiT PD score.
   * Split into **200 granular grades**, each containing **0.5% of the total portfolio volume**.

3. **Combine Granular Grades**

   * Merge initial grades to achieve:

     * **Monotonicity** in observed default rates across grades.
     * Minimum grade size requirements.
     * Avoidance of excessive volume concentration in any single grade.

4. **Test Constructed Grades**

   * Apply the constructed grades to all **52 historical cohorts**.
   * Assess:

     * **Rank ordering breaks** between grades.
     * **Heterogeneity** (distinct default rates between grades).
     * **Migration patterns** across grades over time.
     * **Concentration** within grades.
     * **Homogeneity** (similar default rates within grades).
   * If any test is breached, return to **Step 3** and adjust grade boundaries, then retest.

---

#### **1.3 Candidate Risk Grades**

Four candidate grade schemes were considered and tested for performance against regulatory and portfolio objectives.

**Table – Candidate Grade Structures & Test Results**

| Candidate # | Number of Grades | Min Volume per Grade | Max Volume per Grade | Rank Order Breaks | % Breach in Heterogeneity | Migration Stability | Meets CRR 170(3) Tests? |
| ----------- | ---------------- | -------------------- | -------------------- | ----------------- | ------------------------- | ------------------- | ----------------------- |
| 1           | 25               | X%                   | X%                   | X%                | X%                        | Yes/No              | Yes/No                  |
| 2           | 30               | X%                   | X%                   | X%                | X%                        | Yes/No              | Yes/No                  |
| 3           | 46               | X%                   | X%                   | X%                | X%                        | Yes/No              | Yes/No                  |
| 4           | 26               | X%                   | X%                   | X%                | X%                        | Yes/No              | Yes/No                  |

*(Values to be populated from test output; X% placeholders above.)*

---

This structure clearly shows **methodology**, **iterative logic**, and **candidate selection**, while leaving room for your actual results table.

If you’d like, I can also prepare a **flow diagram** for this grade construction process so it’s easy for a reader to follow visually alongside the text. That would make it match the earlier “variable reduction” and “transformation” sections visually.

Here’s the table extracted from the image:

| Key Metrics                                       | Option 1 | Option 2 | Option 3 | Option 4 (Proposed) |
| ------------------------------------------------- | -------- | -------- | -------- | ------------------- |
| No. of grades                                     | 25       | 30       | 46       | 26                  |
| Average % Rank order reversals across all cohorts | 0.6%     | 0.0%     | 4.1%     | 0.7%                |
| Average % Homogeneity fails across all cohorts    | 5.6%     | 6.0%     | 5.5%     | 3.9%                |
| Average % Heterogeneity fails across all cohorts  | 1.0%     | 0.3%     | 14.0%    | 1.0%                |
| Max % volume in any grade in Jun 2024             | 18.5%    | 32.0%    | 15.0%    | 20.0%               |
| Min % volume in any grade in Jun 2024             | 0.5%     | 0.5%     | 1.0%     | 1.0%                |

Here are the top 5 rows from the table, including the headers:

| Risk Grade | Min PiT PD | Max PiT PD | Total Volume | Total Defaults | % Volume | % Defaults | Observed Default Rate |
| ---------- | ---------- | ---------- | ------------ | -------------- | -------- | ---------- | --------------------- |
| 1          | 0.00%      | 0.13%      | 3,342,860    | 2,483          | 20%      | 0.5%       | 0.07%                 |
| 2          | 0.13%      | 0.17%      | 1,254,329    | 1,946          | 8%       | 0.4%       | 0.16%                 |
| 3          | 0.17%      | 0.23%      | 1,255,992    | 2,712          | 8%       | 0.5%       | 0.22%                 |
| 4          | 0.23%      | 0.30%      | 1,065,989    | 3,131          | 6%       | 0.7%       | 0.29%                 |
| 5          | 0.30%      | 0.40%      | 1,086,742    | 4,275          | 6%       | 0.9%       | 0.39%                 |


---

#### **Objectives of Risk Grading**

The risk grading framework is designed to ensure regulatory compliance, risk sensitivity, and operational effectiveness.

**Table 1 – Risk Grade Design Principles & Tests**

| Objective                                                                                       | Regulatory Reference | Test / Methodology                                             | Target Threshold                           |
| ----------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------- | ------------------------------------------ |
| Minimum volume per grade not lower than 1% of total population                                  | CRR 170(3)(b)        | Grade exposure %                                               | ≥ 1%                                       |
| Maximum volume per grade not higher than 30%                                                    | CRR 170(3)(b)        | Grade exposure %                                               | ≤ 30%                                      |
| Homogeneity – exposures in same grade have similar default rates                                | CRR 170(3)(c)        | Chi-square test: average proportion of failures across grades  | ≤ 5% difference                            |
| Heterogeneity – default rates between different grades are distinct and monotonic               | CRR 170(3)(c)        | Z-test: average proportion of failures between adjacent grades | ≤ 5% difference; Rank order breaks < 5%    |
| Granularity – number of risk grades provides meaningful discrimination                          | CRR 170(3)(c)        | Review of grade count vs portfolio distribution                | As per rating methodology                  |
| Stability – account migrations and annual ODR changes align with selected PiT rating philosophy | CRR 170(3)(c)        | Migration matrix analysis; ODR trend analysis                  | Stable over time, consistent with PiT view |

---

**Key Features:**

* **Joint calibration** ensures that risk grades are comparable across all portfolio segments.
* **Boundaries derived from PiT PD scores** ensure the grades remain dynamic and sensitive to risk changes.
* **Monotonicity** and **homogeneity/heterogeneity tests** ensure the grading system is both statistically sound and interpretable from a business perspective.

---

If you like, I can now prepare the **LRA (Long-Run Average) section** next so the **Risk Quantification** chapter is complete before we move to the next major part of the framework. That way, you’ll have Risk Differentiation → Risk Quantification flowing without any gaps.
