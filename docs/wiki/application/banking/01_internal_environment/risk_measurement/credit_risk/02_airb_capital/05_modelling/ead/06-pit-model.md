---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/modelling/ead/pit-model
  - difficulty/unknown
  - study-status/new
aliases:
---

## **PiT EAD Estimation**

* The **Point-in-Time EAD** is estimated by applying the fitted GLM to each account, generating PiT EADF predictions.
* A summary table is produced showing the **direction of risk** by variable category:

| Variable Category  | Direction of Risk |
| ------------------ | ----------------- |
| Limit              | – (negative)      |
| Credit History     | – (negative)      |
| Purchase Behaviour | + (positive)      |
| Utilisation        | + (positive)      |
| # of Accounts      | + (positive)      |
| Revolver Flag      | + (positive)      |
| Debit Activity     | + (positive)      |

* The **impact of limit increases** is not explicitly included as a separate feature in the EAD model.
* Instead, this is **implicitly captured**:

  * The model is calibrated using historical data which already includes exposures where accounts had limit increases (or decreases) prior to default.
  * This ensures that the estimated PiT EADs reflect realistic behaviour under varying credit line dynamics.

---

✅ Next natural step would be the **Calibration of EAD estimates** (LRA EADF, DT EADF, Regulatory EADF, and MoC adjustments) — basically the same structure as PD calibration but adapted to EAD.

Do you want me to draft that **EAD Calibration** section next?
