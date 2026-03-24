Here’s your **Variable Transformation** section — expanded, cleaned up, and consistent in style with your previous steps:

---

## **Variable Transformation**

Once the final list of variables was obtained from the Variable Reduction stage, each variable was reviewed and transformed to ensure **linear and monotonic relationships** with the target variable. This process involved three sub-steps:

1. **Special Value Treatment**
2. **Missing Value Imputation**
3. **Outlier Treatment** (capping) and **Variable Scaling/Transformation**

---

### **1. Special Value Treatment**

**Definition:**
Special values are non-standard entries within variables (often external data feeds) that represent missing data, “no hit” results, or other coded exceptions. For example, in Experian bureau data, codes such as **997**, **998**, or **999** indicate missing or “not applicable” data.

**Approach:**

* If the proportion of a special value was **≤1%**, it was considered **immaterial** and left untreated.
* If the proportion was **>1%**, further analysis was conducted:

  1. The valid values of the variable were split into **deciles**.
  2. **Observed Default Rates (ODRs)** were calculated for each decile.
  3. The **average ODR** for the first two deciles was compared to the last two deciles to determine the **direction of default risk** as the variable increases.

**Rules Applied:**

* **If ODR trend is monotonic:**

  * No imputation was performed for the special value.
  * Variable was still subject to **outlier capping** and **scaling** later.
* **If ODR trend is not monotonic:**

  * Special values were imputed with **negative values** outside the valid range to enforce monotonicity (e.g., 998 → -1, 999 → -2 for Experian variables where the minimum valid value is 0).

**Validation:**

* ODR plots were generated **before and after** imputation to confirm that monotonicity was achieved.
* Manual adjustments were applied if results remained unstable.

---

Do you want me to now continue and **fully detail the Missing Values, Outliers, and Transformation steps** so this section flows all the way to the “ready-for-modelling” dataset? That would make it consistent with the level of detail you’ve given in Variable Reduction.

Got it — here’s the **Missing Values** section written up cleanly and in the same style as the previous parts.

---

### **2. Missing Value Treatment**

**Sources of Missingness:**
Missing values were classified into three categories:

1. **Missing at Random (MAR)** – Missingness is unrelated to the actual value of the variable but may be related to other variables.
2. **Missing Not at Random (MNAR)** – Missingness is systematically related to the value itself (e.g., higher-risk customers may be less likely to provide certain data).
3. **Structurally Missing** – Missingness is inherent to the variable definition (e.g., loan-to-value ratio is not applicable for unsecured loans).

---

**Treatment Approach:**

* **For MAR and Structurally Missing Values:**

  * Each missing observation was **imputed into the nearest decile** of non-missing values.
  * The “nearest” decile was defined as the one whose **Observed Default Rate (ODR)** was closest to the ODR of the missing group, or **more conservative** if multiple deciles were equally close.
  * This approach aligns the imputed values with similar risk behaviour observed in the data.

* **For MNAR (Known Missing Values with No Clear Inference):**

  * Where the missingness had a known cause but could not be reliably inferred from other data, missing values were imputed with **0**.
  * This ensured they were treated distinctly but without introducing arbitrary bias.

---

**Validation:**
Post-imputation, ODR distributions were rechecked to ensure that:

* Monotonicity was preserved.
* Missing value groups no longer exhibited unexplained risk discontinuities compared to non-missing groups.

---

If you want, I can now write the **Outlier Treatment** section next — covering capping rules, business overrides, and integration with the later transformation step. That will complete the pre-transformation data cleansing stage.

Here’s a clean, integrated write-up for **Outlier Treatment** and **Variable Scaling & Normalization** to match the style of your earlier sections:

---

### **3. Outlier Treatment**

**Identification:**

* Potential outliers were defined as values **below the 1st percentile** or **above the 99th percentile** of the variable’s distribution.
* For each case, judgement was applied to determine whether these extreme values should be **capped (floored)** or retained.
* The decision was based on whether the extreme values were data errors or genuine observations with meaningful risk patterns.

---

**Treatment Approach:**

* **Data errors or spurious extremes** (e.g., clear input mistakes) were capped at the respective 1st or 99th percentile.
* **True but sparse extremes** were capped if their small representation posed a risk of instability in model estimation.

---

### **4. Variable Scaling and Normalization**

**Rationale:**

* Not all extreme values are true outliers. In many cases, **large concentrations** exist at extreme values and their **Observed Default Rates (ODRs)** remain stable and meaningful.
* Removing or capping such values could distort predictive patterns.

---

**Treatment Approach:**

* For such cases, values were **scaled down by a constant factor** or **normalized** (e.g., divided by a large base or log-transformed).
* This preserved the predictive information but **produced more intuitive model coefficients** and improved numerical stability in estimation.
* Scaling/normalization did **not** alter model accuracy or rank ordering, as transformations were monotonic.

---

**Validation:**

* Post-treatment, variable distributions and ODR plots were rechecked to confirm that risk relationships were preserved and no artificial breaks were introduced.

---

If you want, I can now integrate this with your **special values** and **missing values** write-ups so you have one fully structured **Variable Transformation** section before we move into the modelling stage. That way it’ll read as a single, polished block in your documentation.

Here’s a polished, detailed version of your **Variable Transformation** section to match the structure of the earlier steps:

---

## **5. Variable Transformation**

**Application Timing:**
Variable transformation was applied **after** the treatment of special values, missing values, and outliers. This ensures that the variables entering the transformation stage already have consistent, valid, and interpretable values.

---

**Purpose:**

* The primary objective is to create a **linear relationship** between the transformed covariate and the target variable in **log-odds space**.
* Transformation is one of the most **consuming and critical** parts of model development.
* Care must be taken to avoid:

  * **Over-compression** of the data, which can make distinct values indistinguishable and lead to loss of predictive information.
  * **Over-expansion**, which can stretch data into an artificial range, producing spurious patterns and misleading increases in apparent predictive power.

---

**Guiding Principle – Tukey’s Ladder of Power & Bulging Rule:**

* **Tukey’s Ladder of Power** provides a systematic way to determine suitable power transformations (e.g., square, square root, log, reciprocal) to stabilise variance and improve linearity with the log-odds of default.
* **Bulging Rule**:

  * Plot the relationship between the covariate and the target (Observed Default Rate or log-odds).
  * If the pattern bulges **upwards** from left to right, apply a **root transformation** (e.g., square root, log) to compress the right tail.
  * If the pattern bulges **downwards**, apply a **power transformation** (e.g., square, cube) to expand the right tail.
  * This visual diagnostic ensures that transformation direction is guided by actual data behaviour.

---

**Methodology:**

1. **Plotting & Diagnosis:**

   * For each selected covariate, the target variable (ODR/log-odds) was plotted against the predictor.
   * The functional form of the relationship was visually inspected to guide transformation choice.

2. **Transformation Options Considered:**

   * **Logarithmic transformation** (log(x+1)) – for right-skewed variables with diminishing marginal effect on risk.
   * **Square root transformation** – mild compression of right tail without strong impact on mid-range values.
   * **Square transformation** – expansion of right tail for variables with convex relationship to risk.
   * **Binary transformation** – where relationship was best captured by an indicator of exceeding a certain threshold.
   * **Piecewise spline transformation** – for non-monotonic relationships where risk changes direction at specific points.

3. **Validation:**

   * Transformed variables were re-plotted against the target to confirm improved linearity.
   * Non-intuitive or unstable relationships were rejected or reworked, with judgement applied based on business knowledge.

---

If you like, I can prepare **a visual example of Tukey’s Ladder of Power and the Bulging Rule** so your documentation isn’t just text-heavy but shows the concept graphically. This is the kind of visual that impresses regulators because it demonstrates clear methodological understanding.