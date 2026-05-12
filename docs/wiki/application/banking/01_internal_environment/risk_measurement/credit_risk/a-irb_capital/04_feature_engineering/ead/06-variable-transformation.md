---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/feature-engineering/ead/variable-transformation
  - difficulty/unknown
  - study-status/new
aliases:
---
## **Variable Transformation – EAD**

* As with PD, variables are transformed to ensure robustness and monotonicity.
* **EASFs (Exposure at Default Scaling Factors)** are **capped and floored at the 1st and 99th percentiles** of the development sample.
* Predicted and actual values are also capped/floored at the same thresholds to ensure **consistency** when comparing predicted vs observed.
* This treatment reduces the impact of outliers and extreme exposures, ensuring model stability in live use.

---
