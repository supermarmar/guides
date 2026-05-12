---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/modelling/pd/model-methodology
  - difficulty/unknown
  - study-status/new
aliases:
---
# Model Methodology

A further consideration when developing a model, is that models must be able to provide a PD in both unstressed and stressed economic scenarios. Higher interest rates, which make debt more costly, can be integral to stress scenarios. PIT PDs will be volatile as the economy evolves, while TTC PDs will be more stable. Obligors must be classified as to how they are likely to respond to the economic cycle at both peaks and troughs.

## PD Rating Philosophy

### Regulatory Requirements

* [[crr|CRR]] Art. 180(2)(a): Grade-level PDs must be consistent with observed long-run average (LRA) default rates over a mix of good and bad economic periods.
* [[ss4-24|SS4/24]] (10.10): Rating systems can be Point-in-Time (PiT), Through-the-Cycle (TTC), or a blend.
* PS9/24 (3.129): Firms may opt for dynamic recalibration with a suitable buffer to achieve a PiT approach.

### Philosophy Options

| Philosophy              | Description                                                                     | Characteristics                                                                        | Pros                                                                                                                                            | Cons                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Through-the-Cycle (TTC) | Risk grades based only on static characteristics.                               | - No rating migrations. <br> - Observed default rate (ODR) varies with cycle.          | Simple; minimal maintenance; no forecast assumptions.                                                                                           | Fails to reflect current risk profile; non-compliant with [[crr \| CRR]] Art. 180(2)(a) if it ignores relevant current information; poor business usability. |
| Point-in-Time (PiT)     | Ratings driven by both [[06-segmentation\|segmentation]] and scorecard outputs. | - Ratings migrate as risk drivers change. <br> - ODR per grade varies semi-cyclically. | Reflects current portfolio composition and lending standards; supports onboarding without historical partner data; reduced recalibration needs. | Some volatility in PDs; needs continuous monitoring for representativeness.                                                                                  |
| Dynamic PiT             | PiT model plus periodic recalibration to track the cycle exactly.               | - ODR per grade flat across the cycle; changes driven entirely by rating migrations.   | Strongest alignment to true PiT; accurate short-term capital reflection.                                                                        | Requires frequent recalibration; backward-looking calibration factors; RWA volatility; capital pro-cyclicality risk.                                         |

## PiT Approach

Chosen approach: Point-in-Time (PiT) without dynamic recalibration. Rationale:

  * Meets [[crr|CRR]] Art. 180(2)(a) by incorporating current, relevant risk drivers.
  * Avoids maintenance burden and operational risk of periodic recalibrations.
  * Allows semi-cyclical PD behaviour driven by meaningful risk driver changes (e.g., arrears, utilisation).
  * Avoids RWA volatility issues associated with dynamic PiT while remaining partner-resilient.
  * Rejected approaches:
	  * TTC: Non-compliant and lacks relevance to current risk profile.
	  * Dynamic PiT: Operationally burdensome, pro-cyclical RWA impact.