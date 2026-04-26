---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/feature-engineering/pd/target-variable
  - difficulty/unknown
  - study-status/new
aliases:
---
# <mark style="background: #FFF3A3A6;">PD Target Variable</mark>

The target variable for PD model is the default flag ("m12_default" in the MRD) indicating whether a default event occurs **at any point over the next 12 months (worst-case default indicator)**. A default is defined according to the DoD detailed in above, which includes accounts that trigger either the 90 DPD or UTP criteria on any day within the 12-month outcome period, and not just at the end of the 12-month period. This 12-month time horizon is mandated by [[crr|CRR]] Article 180(2)(a), which requires PD estimates to reflect one-year default rates. In summary:

* The **dependent variable** for PD modelling in capital modeling is the **12-month default indicator** (e.g., `m12_default`).
* The indicator column flags whether the obligor defaults or not **at any time** within the 12 months following the observation date.
* This binary classification is in accordance with **[[crr|CRR]] Article 180(2)(a)**, which requires the estimation of **1-year default rates**.
* The identification of default is based on the rules and classifications already described in the **Definition of Default (DoD)** section and includes both **90+ DPD** and **Unlikeliness to Pay (UTP)** events.

In practice, PDs and ratings are often linked and banks generally create a mapping between PDs and ratings. The PDs used for this purpose are expected, according to [[bis|Basel]], to be 1-year PDs, i.e. the probability of an entity defaulting over the next year. In this context, [[bis|Basel]] defines the PD as “the average percentage of obligors that default in this rating grade in the course of 1 year”.
