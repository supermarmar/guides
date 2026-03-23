# Proprietary Trading, xVA and Pension Fund Risk

## Proprietary Trading

### History and Moral Hazard

Historically, many bank treasury departments built proprietary trading teams that adopted full-range trading strategies and made comprehensive use of derivatives. Banks believed that with superior knowledge and expertise, outsized returns would be realised over time — even if trading meant earnings volatility.

Following the 2008 financial crisis, proprietary trading came under intense scrutiny. The concept of **"casino banking"** arose because banks' failures must be avoided (depositors need protection and failures can be systemic), governments generally bail out banks deemed "too big to fail." This creates **moral hazard** — a bank could take excessive risks knowing it would benefit on the upside and be protected on the downside, effectively playing with taxpayers' money.

### Regulatory Responses

**United States — Volcker Rule (Dodd-Frank Act, July 2010):** One of the key provisions of the US Dodd-Frank Act is the Volcker Rule, designed to ensure that banks do not take speculative bets with depositor funds. To a degree, this reverses the Gramm-Leach Act (1999) and re-instates elements of Glass-Steagall (1933) by establishing some separation between commercial and investment banking. However, banks retain the ability to make markets for investors, hedge, and trade US government securities.

**United Kingdom — Ring-Fencing (Independent Banking Commission, 2010):** The UK Independent Banking Commission developed two primary recommendations: (1) "ring-fence" retail banking from wholesale/investment banking within a banking group; and (2) increase the capital of retail banks to decrease the potential for taxpayer rescue. Retail banking activities would sit in a separate entity owned by the holding company with its own board. The extent to which the retail bank can interact with the investment bank remains actively debated.

## Post-Crisis Derivative Valuation: xVA

### Multi-Curve Framework

Before the 2008 financial crisis, a **single-curve framework** was used to both forecast and discount cashflows from the same yield curve. Spreads between curves such as LIBOR 3-month and LIBOR 6-month were close to zero. After the crisis, these spreads widened significantly to reflect the credit risk of cashflows with longer tenors (LIBOR 6-month was higher than LIBOR 3-month to compensate investors for the longer uncertainty period). As a result, derivative valuation changed from a single-curve to a **multi-curve framework** — forecasting and discounting now require different curves.

### Valuation Adjustments (xVA)

New valuation adjustments were introduced after the crisis to measure the "true value" of a financial derivative. These adjustments are applied as add-on charges to transactions not traded under a Credit Support Annex (CSA):

| Adjustment | Description |
|---|---|
| **CVA** — Credit Value Adjustment | The cost of a counterparty defaulting before maturity of the contract |
| **DVA** — Debit Value Adjustment | The benefit a bank will receive in the case of its own default |
| **FVA** — Funding Value Adjustment | The cost of funding a derivative in the event the bank has to post more collateral on a trade |
| **MVA** — Margin Value Adjustment | The funding costs of initial margin specific to centrally cleared transactions |
| **KVA** — Capital Value Adjustment | The cost for regulatory capital that must be held by the bank against the trade throughout its life (to be replaced by SA-CCR — standardised approach for counterparty credit risk) |

Significant changes to derivative valuation and risk measurement in the trading book have occurred since 2008, and further changes are expected.

## Pension Fund Market Risk

A bank's pension fund only poses a market risk to the bank where the bank operates a **defined benefit (DB)** pension scheme or any scheme where benefits are not directly aligned to the performance of the pension fund's assets (e.g. providing minimum guaranteed benefits). In South Africa, most pension funds (allowing for legacy books) are **defined contribution (DC)** and therefore do not pose a direct risk to the bank.

### Risk Issue

The Bank of England (BOE) defines pension obligation risk as: the risk to a firm caused by its contractual or other liabilities to or with respect to a pension scheme; or that a firm will make payments or contributions to a pension scheme because of a moral obligation or because the firm considers it needs to do so for some other reason.

To the extent that a pension fund is in deficit, the bank must cover that deficit using its **CET1 capital**. Adverse conditions in the pension fund therefore directly impair the bank's regulatory capital position. Note that surpluses in the pension fund are **not** included in the bank's capital supply.

### Quantification

The bank must quantify pension obligation risk as part of its **ICAAP process**. Stress and scenario testing are used to gauge the probability and severity with which the pension fund may experience a deficit over the ICAAP time horizon. Allowance can be made for offsets and management actions that the bank has put in place.

### Capital and Supervisory Review

Regulators review the bank's pension obligation risk assessment in the ICAAP and may adjust the implied capital requirement. Regulators may apply a standard set of stress scenarios across banks for comparability; results are then compared to the banks' internal ICAAP assessments to identify deviations requiring justification.

Risk mitigation in the form of offsets and management actions is only permitted if it meets the following criteria:

- **Financial performance** — the efficacy of offsets and management actions must not depend on assumptions about the future financial performance of the firm, either before or after a stress.
- **Independence from third parties** — the efficacy must not depend on the future agreement or behaviour of third parties, before or after a stress.
- **Immediacy** — recognised offsets should reflect a risk mitigation benefit already effective when the offset is taken. Management actions must be capable of taking effect quickly enough to mitigate the relevant stress.
