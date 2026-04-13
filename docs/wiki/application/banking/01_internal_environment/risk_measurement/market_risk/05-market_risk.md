---
tags:
  - application/banking/internal-environment/risk-measurement/market-risk/market-risk
  - difficulty/unknown
  - study-status/new
aliases:
---
# Market Risk: Definition, VaR, Funding and Hedging

## Market Risk Definition

Market risk is defined as the **risk of loss from movements in prices in the financial markets**. It can arise from any position — on- or off-balance sheet — in cash, securities, derivatives, or from customer lending, market making, or trading. Market risks tend to arise from movements in interest rates, foreign exchange rates, and market prices (commodities and equities). Interest rate risk is therefore a form of market risk. Banks also have market risk from FX, commodity, and equity positions depending on the scale of their global operations and trading businesses.

## [[07-var_limitations|Value at Risk]] (VaR)

VaR is the maximum possible loss that a portfolio can suffer with a specific level of confidence over a certain time frame. Expressed formally:

```math
\text{VaR}[\alpha] = \sup\{x \in \mathbb{R} : P(X < x) \leq 1 - \alpha\}
```

where $X$ is the return random variable and $\alpha$ is the confidence level.

For example, if 1-day VaR is $25 million at 95% confidence, there is an estimated 5% chance of a single trading day loss exceeding $25 million — roughly one loss of that magnitude per 20 trading days. VaR focus is on P&L probabilities given a confidence level and specific time frame.

A **"VaR break"** is when actual losses exceed the VaR threshold. In a perfectly accurate model, the number of VaR breaks would equal $(1 - \alpha)$ of trading days. Banks must back-test their models daily; regulators penalise banks with capital add-ons when poor back-testing highlights deficient models.

South African banks commonly use 1-day and 10-day holding period assumptions for [[01-risk_management|risk management]].

### Stressed VaR (sVaR)

sVaR considers the worst losses of a portfolio observed from historical data — most commonly the 2008 financial crisis. Banks run simulations to identify the most stressful 1-year period from 2007 to the current date, and use that time series to calculate sVaR. sVaR is used alongside current VaR to set regulatory capital levels, while point-in-time VaR is the primary metric for limit monitoring. Both VaR and sVaR are used to set [[01-economic_capital|economic capital]] levels.

For limitations of VaR and alternative coherent measures (Expected Shortfall, TVaR) see [VaR Limitations](07-var_limitations.md).

## Market and Systemic Risk and Funding

Money market funding includes deposits, interbank borrowing, commercial paper, certificates of deposit, repo transactions, and medium-term notes. Access to funding markets can change rapidly due to investor concerns about a given bank or systemic concerns about the broader financial system.

Money market liquidity diminished significantly in the 2008 global financial crisis. Short-term investors are the most conservative and can withdraw funding at any sign of trouble. Banks face a risk of a "run on the bank" where short-term investors rush to withdraw savings fearing insolvency. Bank funding is therefore highly sensitive to the economic climate.

Best practice is to establish a funding programme across as many instruments and market segments as possible, even when interest rates are not always attractive — this creates diversified funding and reduces the risk of a liquidity constraint in any single market or instrument.

South African banks face interest rate risk from large liquid asset portfolios that tend to be fixed rate in nature, funded by floating rate liabilities.

## Hedging: Tools, Strategy and Risks

Banks mitigate risk when exposure to a counterparty or risk factor becomes large. The instruments below are used to manage interest rate risk, foreign exchange risk, and market risk in both the trading and banking books.

### Forward Rate Agreements (FRAs)

FRAs are over-the-counter (OTC) trades between two parties. Both parties agree to buy or sell an instrument in the future with a predefined amount, maturity, and rate fixed. At maturity, funds are exchanged to reflect the change in value from interest rate movements. FRAs can be tailored to specific needs.

### Futures

Futures are exchange-traded with standard terms (e.g. Eurodollar futures are $1 million for 90-day periods settling quarterly). Banks can sell consecutive futures contracts ("strips") to create long-dated hedges. Futures positions are **margined** — the exchange requires an initial margin to cover potential losses and variation margin (adjusted daily) to mitigate credit risk. The standard terms and strict margining rules allow for liquid trading. Both FRAs and futures are priced off the yield curve.

### Swaps (OIS)

**Overnight Index Swaps (OIS)** are a popular form of interest rate hedging. One party pays a fixed rate for a fixed period on a nominal amount; the other pays the average floating overnight rate based on a benchmark index. Nominal amounts are not exchanged; settlement involves paying the difference between fixed and floating leg cashflows. OIS allows a treasury function to separate interest rate and liquidity positions.

Interest rate swaps are one of the main methods used by banks to hedge floating rate debt. A **pay-fixed-receive-floating** swap receiving JIBAR 3-months, for example, offsets liabilities referencing JIBAR 3-months — the only remaining exposure is the fixed leg payment.

### Options

Options provide protection against adverse market movements without the firm commitment of FRAs, futures, or OIS. Buying an option is like buying an insurance policy.

- **Swaption (swap option)** — an option on an interest rate. A **payer swaption** gives the holder the right but not the obligation to enter a pay-fixed-receive-floating swap at the expiry date; useful for a bank with floating rate debt exposed to rising rates.
- **FX option** — gives the holder the right but not the obligation to fix the price at which two currencies are exchanged in the future; used to hedge FX exposure.

### The Basis Challenge

The "basis" is a key challenge in hedging: there is no certainty that rates on the bank's exposure will move in tandem with the instrument used to hedge. If a bank earns prime on its assets but pays JIBAR 3-months on liabilities, entering a pay-fixed-receive-JIBAR swap eliminates the JIBAR liability exposure, leaving only the fixed leg and the prime-JIBAR basis as residual risks.

[[01-risk_management|Risk management]] reports must identify hedging so that basis risk can be analysed separately. Aggregating long and short positions could show little net risk while basis risk is substantial.

### JSE Interest Rate Derivatives

The Johannesburg Stock Exchange lists interest rate derivatives including futures and options on government and state-owned company debt, futures on JIBAR, and futures on swaps. JSE-traded interest rate derivatives are margined and guaranteed by the central clearing counterparty **SAFCOM** (Safex Clearing Company).
