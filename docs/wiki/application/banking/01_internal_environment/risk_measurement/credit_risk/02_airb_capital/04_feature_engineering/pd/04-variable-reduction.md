---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/feature-engineering/pd/variable-reduction
  - difficulty/unknown
  - study-status/new
aliases:
---
Here’s a clean, structured write-up of your **[[05-variable-reduction|Variable Reduction]]** section, based on your notes, with expanded clarity so it reads smoothly in a model development document.

---

## **[[05-variable-reduction|Variable Reduction]]**

The original model ready dataset (**MRD**) contained approximately **1,000 variables**, including trend variables.
Certain variables were **excluded from the [[05-variable-reduction|variable reduction]] process** from the outset because they were either [[01-target-variables|target variables]], identifiers, or considered essential baseline predictors. These included:

* **Default flag, type and date**
* **Product type**
* **Account identifiers**
* **External bureau scores**
* **Application variables**

### **Sampling for Computational Efficiency**

For each segment, **simple random sampling** was applied to reduce dataset size when the number of observations exceeded **1 million**, to manage computational demands while retaining statistical representativeness.

---

### **Reduction Process – Steps**

#### **Step 1: Data Quality Checks**

Variables were screened for basic quality criteria. The following were removed:

* **Categorical variables** with an excessive number of categories (**>100**), to prevent overfitting.
* Variables with **no variance** (only 1 unique value).
* **Date/time variables**, since they are not direct predictors of default risk.
* **Numeric variables** with **>20% missing values**, to maintain data integrity and reduce bias from excessive imputation.

---

#### **Step 2.1: Predictive Power Assessment**

Remaining variables were evaluated for predictive strength:

* **Information Value (IV)** – applied to both numeric and categorical variables.
* **Gini** and **R²** – applied to numeric variables.
* Variables with **predictive metrics below the 50th percentile** were removed.
* Where variables had **identical predictive metrics**, one was removed to avoid duplication.

---

#### **Step 2.2: Correlation Clustering**

Highly correlated variables were grouped to reduce redundancy. Within each correlated group, the most representative variable (highest predictive power, stability) was retained.

To identify and remove redundancy, Pearson correlation coefficients were calculated for all pairs of numeric variables.
Highly correlated variables were grouped into clusters, and within each cluster, the most predictive variables were retained based on their Gini coefficient.

The reduction process was performed in three iterations with progressively looser thresholds:

First iteration:

Correlation threshold: >99%

From each cluster, keep only 1 variable (the one with the highest Gini).

Second iteration:

Correlation threshold: >85%

For clusters >10 variables, keep 2 variables.

For clusters ≤10 variables, keep 1 variable.

Third iteration:

Correlation threshold: >70%

For clusters >10 variables, keep 3 variables.

For clusters 5–9 variables, keep 2 variables.

For clusters <5 variables, keep 1 variable.

The variables removed at each iteration were determined independently from the results of previous iterations.

For certain segments — particularly those with a large portfolio share or low observed default rates — thresholds and criteria were adjusted to avoid excessive or insufficient variable removal. Adjustments could include:

Introducing IV alongside Gini as an additional ranking criterion.

Relaxing the independence assumption between iterations to allow retention of more variables.

This multi-stage approach was chosen over a single correlation threshold method, as it reduces the risk of removing too many variables in small portfolios or too few in highly correlated datasets, thus balancing model parsimony with predictive power.

---

#### **Step 3: Variable Clustering**

Broader clustering was applied across the reduced set to identify groups of variables representing similar concepts or patterns.

he objective of this step was to identify groups of correlated variables that are not collinear, enabling the retention of diverse information for model fitting.

A Principal Component Analysis (PCA) approach was used to form clusters that maximise correlation within a cluster while minimising correlation between clusters.
The process was iterative:

Clusters with a second eigenvalue >1 were split further.

The process continued until a maximum of 35 clusters was reached.

Variable Selection Within Clusters:

For each cluster, RS Own, IV, Gini, and R² were calculated and ranked.

The top variable was retained based on a combined ranking of IV and Gini.

If the top variable had a low RS Own rank (<60th percentile), a second variable was kept if it had:

High RS Own rank, and

High IV and Gini (>50th percentile).

Conversely, if the top variable had a high RS Own rank, a second variable was kept if it had:

Low RS Own rank, and

High IV and Gini (>50th percentile).

This ensured that both the most similar and the most dissimilar variables (in terms of information overlap) within each cluster were retained.

Judgemental Adjustments:
The development team also applied domain knowledge to remove redundant variables where multiple had the same business meaning.
Examples include:

External variables with the same suffix (e.g. exp_ variables with the same number).

Variables with the same prefix but different derivation windows (e.g. _3mo vs _6mo) where predictive strength differed.

---

#### **Step 4: Collinearity Assessment**

The remaining variables were tested for **multicollinearity** (e.g., using VIF thresholds). Highly collinear variables were removed to ensure model stability and interpretability.

The purpose of this step is to eliminate variables that are highly correlated with other retained variables following Step 3.

Multicollinearity can undermine model stability because:

Strong predictors become less effective if they are collinear with other predictors.

Estimated coefficients may become highly sensitive to small changes in the data due to increased variance in the estimates.

Coefficient magnitudes may not accurately reflect the true relationship between predictors and the [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/04_feature_engineering/pd/01-target_variable|target variable]].

Methodology:
A “one-drop” approach was used:

The correlation matrix of the remaining variables was decomposed into linear combinations.

The condition index was calculated for each combination.

A value >30 indicates severe multicollinearity.

For each high condition index, the variance decomposition matrix was assessed to determine how much each variable contributed to the multicollinearity.

If two or more variables contributed more than 0.5 to the same condition index, the variable with the highest variance proportion was removed.

This process was repeated iteratively until no severe multicollinearity remained.

This systematic approach ensured that the final set of predictors retained strong predictive power while minimising redundancy and instability in coefficient estimates.

---

#### **Step 5: Univariate Analysis**

Final variable candidates were examined individually to confirm:

* Predictive relationship with the [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/04_feature_engineering/pd/01-target_variable|target variable]].
* Plausibility from a business and risk perspective.
* Consistency across different time periods and segments.

The final stage of [[05-variable-reduction|variable reduction]] involved a detailed univariate assessment of each remaining predictor.

Purpose:

Ensure that each variable has an intuitive relationship with the [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/04_feature_engineering/pd/01-target_variable|target variable]].

Confirm that patterns are stable and monotonic (i.e., risk consistently increases or decreases with the variable’s value).

Identify variables with unstable or erratic relationships that could introduce noise into the model.

Methodology:

Distribution Analysis

Review the distribution of each variable to detect anomalies such as extreme skewness, outliers, or irregular groupings.

Univariate Regression Performance

Assess each variable individually against the dependent variable using logistic regression.

Evaluate the strength and direction of the relationship.

Bivariate Rank Plots

Create rank-ordered plots of the variable against the dependent variable.

Check for a clear monotonic trend.

Variables with non-monotonic or highly unstable patterns were flagged for removal or transformation.

By combining distribution review, predictive strength assessment, and stability checks, this step ensured that only predictive, interpretable, and stable variables progressed to model development.

---

If you like, I can also **add Steps 2.2–5 with more quantitative details** (e.g., correlation thresholds, VIF cut-offs, stability index criteria) so this reads like a regulatory-ready PD model methodology.

Do you want me to expand it in that formal style? That would make it fully consistent with how [[pra|PRA]] and [[ecb|ECB]] expect IRB documentation.

Got it 👍 — so now we’re documenting the **[[05-variable-reduction|Variable Reduction]]**, **Transformation**, and then the **PiT EAD Estimation** section. Since this mirrors PD, I’ll keep it parallel for consistency but highlight the EAD-specific adjustments you gave. Here’s a draft you can drop in:
