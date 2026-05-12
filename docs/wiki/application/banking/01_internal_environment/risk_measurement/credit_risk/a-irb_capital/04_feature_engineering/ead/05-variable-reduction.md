---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/feature-engineering/ead/variable-reduction
  - difficulty/unknown
  - study-status/new
aliases:
---
## **Variable Reduction – EAD**

The process for reducing variables is aligned with the PD framework but with some differences in diagnostic metrics:

1. **Initial Screening**:

   * Candidate variables are assessed for coverage, stability, and intuitive direction of risk.
   * Variables with insufficient coverage or instability across cohorts are removed.

2. **Univariate Analysis**:

   * Instead of using Information Value (IV) and Gini, the following measures are used:

     * **(R^2)** (goodness of fit measure)
     * **Lift ratio** (discriminatory power relative to random selection).
   * Variables showing **low explanatory power** or **non-monotonic / unintuitive risk relationships** are excluded at this stage.

3. **Multivariate Analysis**:

   * Remaining variables are tested in multivariate GLM specifications.
   * Variables contributing marginal incremental explanatory power are dropped, ensuring **parsimony**.
