---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/modelling/pd/pit-model
  - difficulty/unknown
  - study-status/new
aliases:
---
Here’s how we can structure that **PiT PD Model Estimation** section clearly and logically:

---

## **Point-in-Time (PiT) PD Model Estimation**

The PiT PD model estimation aims to ensure that the final logistic regression model reflects changes in customer risk profiles both **before** and **after** the COVID period, while meeting regulatory requirements for discriminatory power, stability, and interpretability.

### **1. Dual Model Approach**

Two separate logistic regression models were initially estimated:

1. **Full Development Sample** – all transformed variables, covering the entire model development period.
2. **Post-COVID Subset** – all transformed variables, restricted to post-COVID data within the development sample.

> **Purpose:** To capture potential structural changes in risk relationships and customer behaviours between the pre- and post-COVID periods.

---

### **2. Variable Selection Process**

* From both model outputs, the **top 25 variables** with the **highest marginal lift** were identified.
* Variables ranking highly in *both* the full sample and post-COVID models were prioritised.
* This ensured the final model was robust to temporal shifts in the drivers of default risk.

---

### **3. Iterative Refinement Against IRB Testing Guidance**

Variables were iteratively tested and refined to ensure compliance with regulatory standards:

| **Requirement**                         | **Criteria**                                                                                             | **Rationale**                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Statistical Significance**            | p-value < 1%                                                                                             | Ensures each variable has a meaningful contribution to the model.    |
| **Collinearity**                        | VIF < 3                                                                                                  | Reduces instability and redundancy among predictors.                 |
| **Intuitive Relationship**              | Signs and shapes consistent with business logic in the log-odds space                                    | Supports interpretability for model governance.                      |
| **Marginal Discrimination**             | Incremental Gini ≥ 0.25%                                                                                 | Ensures each retained variable provides measurable incremental lift. |
| **Coverage Across Information Sources** | At least 5 predictors per segment using both internal and external data, across multiple risk categories | Improves model balance and resilience.                               |

---

### **4. Outcome**

The resulting final logistic regression model:

* Retains the strongest predictors from both pre- and post-COVID datasets.
* Balances discriminatory power with interpretability.
* Meets the Internal Ratings-Based (IRB) framework requirements for **[[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]]** and **regulatory approval**.

---

If you like, I can now prepare a **flow diagram** showing how the full-sample and post-COVID models feed into the final model selection process — that visual could make the dual-model approach much clearer.

| **Category**     | **Direction of Risk / Coefficient Sign** |
| ---------------- | ---------------------------------------- |
| Balance          | +                                        |
| Payment          | -                                        |
| Utilisation      | +                                        |
| Cash Advance     | +                                        |
| Financial Charge | +                                        |
| Revolver         | +                                        |
| Delinquency      | +                                        |
| Late Fee         | +                                        |
| Inquiry          | +                                        |
| # of Accounts    | -                                        |
| Credit History   | -                                        |
| Limit            | -                                        |
| Open to Buy      | -                                        |
| MOB              | -                                        |

Here’s your section written up clearly and consistently with your earlier style:

---

### Testing and Adjustment on Key Business Sub-Populations

Once the final logistic regression model is trained, it is validated across **key business sub-populations** to ensure consistent performance and stability. These sub-populations include:

* **FICO score bands** (e.g., <600, 600–699, 700+)
* **Credit limit bands** (e.g., low, medium, high)
* **Utilisation bands** (e.g., <30%, 30–70%, >70%)
* **Key strategic partners**

**Post-Validation Adjustments**
Following the initial testing, the model is further refined by introducing and assessing **partner flags** and **interaction variables** to capture portfolio-specific risk patterns. This step ensures that the model is sensitive to characteristics unique to certain business lines or partners.

**Examples of partner or product-specific flags include:**

* **Newly acquired business** – accounts or portfolios not present in historical development data.
* **Run-off products** – products with no new originations and a shrinking customer base.
* **Products with increased mortality-related defaults** – segments where defaults are driven by customer death rather than financial distress.
* **Business cards issued to small business owners** – assessed using different metrics (e.g., cash flow, business financials) compared to consumer accounts.

This process is applied **within each model segment** to ensure the final model maintains accuracy, interpretability, and fairness across the portfolio.

---

If you’d like, I can now integrate this with your **PiT PD Model Estimation** write-up so it flows as one complete section.

Here’s a clean, structured version of your **Segment 1: Late Delinquency** write-up so it matches the style you’ve been using for earlier sections:

---

## **Segment 1: Late Delinquency**

### **Summary**

* **Initial variables:** 1,003
* **Final variables after reduction:** 72
* **Model Gini:** 64.44%
* **Final predictors:** 8 statistically significant, non-correlated variables with intuitive relationships to default risk.

---

### **Model Composition**

* **Variable composition:**

  * **2 Partner Indicators**
  * **3 Internal Predictors**
  * **3 External Predictors**

**Table 1 – Final Predictors and Key Statistics**

| Predictor | Estimate | Std. Error | p-Value | Contribution (%) | VIF | Incremental Gini (%) |
| --------- | -------- | ---------- | ------- | ---------------- | --- | -------------------- |
| ...       | ...      | ...        | ...     | ...              | ... | ...                  |

**Table 2 – Predictor Descriptions**

| Predictor | Source (Internal / External) | Driver Category | Description |
| --------- | ---------------------------- | --------------- | ----------- |
| ...       | Internal                     | Utilisation     | ...         |
| ...       | External                     | Inquiry         | ...         |

**Notes:**

* VIF < 3 for all predictors, confirming absence of high collinearity.
* All predictors are statistically significant (p-Value < 1%).
* Business sense confirmed through feedback from **Model Owners** and **1LOD** team.
* Approved in **Delegated Authority (DA)** process.

---

### **[[06-variable-transformation|Variable Transformation]]**

**Table 3 – Variable Treatment Summary**

| Variable | % Special Value | Special Value Treatment | % Missing | Missing Value Treatment   | Outlier Treatment (Floor / Cap) | Transformation |
| -------- | --------------- | ----------------------- | --------- | ------------------------- | ------------------------------- | -------------- |
| ...      | 2%              | Imputed with –1         | 5%        | Imputed to nearest decile | Floor: P1 (x) / Cap: P99 (y)    | log(x + 1)     |
| ...      | <1%             | None                    | 0%        | N/A                       | None                            | None           |

---

### **Variable Correlation**

* Correlation matrix confirms **maximum correlation < 70%**, ensuring independence between variables and absence of multicollinearity.

---

### **Model Performance**

**Table 4 – Performance Metrics by Sample**

| Sample Type | Gini (%) | Avg. ODR (%) | Avg. PiT PD (%) | Relative Error (%) |
| ----------- | -------- | ------------ | --------------- | ------------------ |
| Development | ...      | ...          | ...             | ...                |
| Application | ...      | ...          | ...             | ...                |

**Visual Outputs:**

* **Accuracy Curve** – compares predicted PD to observed default rates.
* **Lorenz Curve (Gini Plot)** – illustrates discriminatory power of the model.

---

If you want, I can also **fill in placeholders** for tables like predictors, treatments, and performance so it’s already formatted for your documentation, ready for when you have the actual numbers. That way it’s fully plug-and-play.

Here’s a polished draft for the **Overall PiT PD Model** section to align with the style we’ve been using for your [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]] documentation.

---

## **Overall PiT PD Model**

### **Overview**

The **Overall Point-in-Time Probability of Default (PiT PD) model** consolidates all segmented PD models into a single portfolio-level framework.
Performance is evaluated on both:

* **Development sample**
* **Out-of-Time (OOT) sample**

The combined model demonstrates strong discriminatory power, with an **overall Gini of ~80%**.

---

### **Categories of Drivers & Expected Direction**

The following table summarises the **categories of risk drivers**, their **expected direction of risk impact**, and whether the direction is consistent with the actual model coefficients in each PD segment.

**Table 1 – Driver Categories and Expected Direction by Segment**

| Source (Internal / External) | Category     | Expected Direction     | Seg 1 | Seg 2 | Seg 3 | Seg 4 | Seg 5 | Seg 6 | Seg 7 | Seg 8 | Seg 9 | Seg 10 |
| ---------------------------- | ------------ | ---------------------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ |
| Internal                     | Balance      | +                      | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓      |
| Internal                     | Payment      | –                      | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓      |
| Internal                     | Utilisation  | +                      | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓      |
| External                     | Inquiry      | +                      | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓      |
| Internal                     | Partner Flag | +/- (Segment Specific) | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓      |
| …                            | …            | …                      | …     | …     | …     | …     | …     | …     | …     | …     | …     | …      |

**Notes:**

* **✓** indicates direction of risk in the segment is aligned with the expected sign.
* Blank or ✗ indicates a deviation requiring business review.

---

### **Model Performance – Overall**

**Table 2 – Portfolio-Level Performance**

| Sample Type | Gini (%) | Avg. ODR (%) | Avg. PiT PD (%) | Relative Error (%) |
| ----------- | -------- | ------------ | --------------- | ------------------ |
| Development | ~80      | ...          | ...             | ...                |
| OOT         | ...      | ...          | ...             | ...                |

**Visual Outputs:**

* **Overall Accuracy Curve**
* **Overall Lorenz Curve (Gini Plot)**
* **ODR vs Predicted PD plot**

---

### **Model Performance – Key Sub-Populations**

Performance is also assessed at key business sub-population levels to ensure consistency and absence of bias.

**Table 3 – Performance by Sub-Population**

| Sub-Population     | Gini (%) | Avg. ODR (%) | Avg. PiT PD (%) | Relative Error (%) |
| ------------------ | -------- | ------------ | --------------- | ------------------ |
| Utilisation ≤ 30%  | ...      | ...          | ...             | ...                |
| Utilisation 31–70% | ...      | ...          | ...             | ...                |
| Utilisation > 70%  | ...      | ...          | ...             | ...                |
| Product Group A    | ...      | ...          | ...             | ...                |
| Product Group B    | ...      | ...          | ...             | ...                |

**Visual Outputs:**

* Accuracy curves and Lorenz curves for each sub-population.
* Comparative Gini chart across segments and sub-populations.

---

If you want, I can now **merge this with your earlier segment write-up** so your documentation flows cleanly from **[[05-variable-reduction|Variable Reduction]] → Transformation → Segment Modelling → Overall Model**, with consistent tables and formatting. That would make this whole [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]] section feel like one seamless narrative.
