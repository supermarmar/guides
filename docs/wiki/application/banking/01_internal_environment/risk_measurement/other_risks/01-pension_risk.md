---
tags:
  - application/banking/internal-environment/risk-measurement/market-risk/proprietary-trading-xva-pension
  - difficulty/unknown
  - study-status/new
aliases:
---
# Pension Fund Risk

A bank's pension fund only poses a [[wiki/application/banking/01_internal_environment/risk_measurement/market_risk/02-models|market risk]] to the bank where the bank operates a **defined benefit (DB)** pension scheme or any scheme where benefits are not directly aligned to the performance of the pension fund's assets (e.g. providing minimum guaranteed benefits). In South Africa, most pension funds (allowing for legacy books) are **defined contribution (DC)** and therefore do not pose a direct risk to the bank.

Pension risk arises from defined benefit (DB) pension schemes where the bank has an obligation to fund any deficit in scheme assets relative to scheme liabilities. The liability is sensitive to the discount rate (typically a corporate bond yield), inflation assumptions, and longevity assumptions.

The Pillar 2A pension capital charge is typically computed as the **stressed deficit** under an adverse scenario, over and above the funded deficit already deducted from CET1 capital:

$$\text{EC}_{\text{pension}} = \max(0,\ \text{Pension deficit}_{\text{stressed}} - \text{Pension deficit}_{\text{base}} - \text{CET1 deduction})$$

Standard stresses applied include: a parallel shift down in risk-free rates (increasing the present value of liabilities), a fall in equity markets (reducing scheme assets), and an adverse change in inflation (increasing indexed liabilities).

## Risk Issue

The [[bank_of_england|Bank of England]] (BOE) defines pension obligation risk as: the risk to a firm caused by its contractual or other liabilities to or with respect to a pension scheme; or that a firm will make payments or contributions to a pension scheme because of a moral obligation or because the firm considers it needs to do so for some other reason.

To the extent that a pension fund is in deficit, the bank must cover that deficit using its **CET1 capital**. Adverse conditions in the pension fund therefore directly impair the bank's regulatory capital position. Note that surpluses in the pension fund are **not** included in the bank's capital supply.

## Quantification

The bank must quantify pension obligation risk as part of its **ICAAP process**. Stress and scenario testing are used to gauge the probability and severity with which the pension fund may experience a deficit over the ICAAP time horizon. Allowance can be made for offsets and management actions that the bank has put in place.

## Capital and Supervisory Review

Regulators review the bank's pension obligation risk assessment in the ICAAP and may adjust the implied capital requirement. Regulators may apply a standard set of stress scenarios across banks for comparability; results are then compared to the banks' internal ICAAP assessments to identify deviations requiring justification.

[[05-risk_mitigation|Risk mitigation]] in the form of offsets and management actions is only permitted if it meets the following criteria:

- **Financial performance** — the efficacy of offsets and management actions must not depend on assumptions about the future financial performance of the firm, either before or after a stress.
- **Independence from third parties** — the efficacy must not depend on the future agreement or behaviour of third parties, before or after a stress.
- **Immediacy** — recognised offsets should reflect a [[05-risk_mitigation|risk mitigation]] benefit already effective when the offset is taken. Management actions must be capable of taking effect quickly enough to mitigate the relevant stress.