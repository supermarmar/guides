---
tags:
  - application/banking/internal-environment/risk-measurement/market-risk/proprietary-trading-xva-pension
  - difficulty/unknown
  - study-status/new
aliases:
---
# Proprietary Trading and xVA

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

| Adjustment                         | Description                                                                                                                                                                                                        |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CVA** — Credit Value Adjustment  | The cost of a counterparty defaulting before maturity of the contract                                                                                                                                              |
| **DVA** — Debit Value Adjustment   | The benefit a bank will receive in the case of its own default                                                                                                                                                     |
| **FVA** — Funding Value Adjustment | The cost of funding a derivative in the event the bank has to post more collateral on a trade                                                                                                                      |
| **MVA** — Margin Value Adjustment  | The funding costs of initial margin specific to centrally cleared transactions                                                                                                                                     |
| **KVA** — Capital Value Adjustment | The cost for regulatory capital that must be held by the bank against the trade throughout its life (to be replaced by SA-CCR — standardised approach for [[02-counterparty_exposures\|counterparty credit risk]]) |

Significant changes to derivative valuation and [[04-risk_measurement|risk measurement]] in the trading book have occurred since 2008, and further changes are expected.
