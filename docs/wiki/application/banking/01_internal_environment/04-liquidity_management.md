---
tags:
  - application/banking/internal-environment/risk-measurement/liquidity-risk/liquidity-metrics
  - difficulty/unknown
  - study-status/new
aliases:
---
# Liquidity Management

## Purpose of Liquidity

The core [[01-business_model|business model]] of banking — **maturity transformation** — creates liquidity risk structurally. Banks originate long-dated assets (residential mortgages, project finance loans with maturities up to 50 years, committed but undrawn credit facilities) funded by shorter-duration liabilities (current accounts, short-term deposits). This creates a **maturity mismatch** between assets and liabilities, and the uncertainty underlying this mismatch is the fundamental source of liquidity risk.

Banks therefore assume a continuous ability to roll over or obtain new funding. Were this assumption to fail, banks would never originate long-dated illiquid assets in the first place. The challenge of liquidity management is twofold:

1. **Asset funding**: Securing funding for assets over their full life, including committed but as yet undrawn assets such as credit cards and contingency funding lines.
2. **Liability withdrawal**: Meeting immediate withdrawal requests from depositors, given that a large proportion of customer liabilities are demand deposits — current accounts (also known as chequing or money transmission accounts) and instant-access savings accounts.

Banks also need to understand the **behavioural nature of their deposits** in order to fund term assets: certain contractually on-demand deposits (e.g. current accounts) exhibit sticky or term behaviour and can be modelled as providing longer-dated funding than their contractual maturity implies.
## Sources of Liquidity

Bank funding sources fall into two categories: **customer funds** and **wholesale funds**. A proper understanding of both categories is necessary because the different types within each exhibit very different behavioural characteristics with respect to tenor, pricing, and customer behaviour.

### Deposits

Customer funds include traditional deposit-taking from retail and corporate customers. They exhibit more stable behavioural characteristics than wholesale funds and form the preferred base of bank funding. In South Africa, low levels of discretionary savings — with contractual savings channelled via pension funds, provident funds, and asset managers — mean that banks cannot source sufficient customer deposit funding for all their liquidity needs. South African banks therefore rely on institutional/wholesale funding to supplement customer deposits, making them structurally more dependent on wholesale markets than banks in savings-rich economies.

### Wholesale Market Funding

Wholesale funds are sourced from institutional depositors: asset managers, pension funds, other banks, money market instruments (certificates of deposit, commercial paper), and interbank deposits. They are generally more rate-sensitive, shorter-dated, and more volatile under stress than customer deposits. Professional/institutional depositors are typically multi-banked and move funds rapidly in response to perceived credit stress — as evidenced by the aggressive outflows from wholesale funding sources observed during historical stress events.

Contractually long-dated wholesale liabilities (e.g. a 3-year capital markets bond issuance) are stable regardless of their institutional source. The behavioural instability of wholesale funds is primarily a concern for contractually short-dated instruments.

### Central Bank Funding

The central bank is a **last resort** source of funding liquidity and should not under any circumstances be considered a BAU source. A bank that has recourse to central bank funding outside of daily open market operations may be considered to be a compromised standalone viable entity.

## <mark style="background: #FFF3A3A6;">Types of Liquidity</mark>

A bank must at all times be able to service its obligations as they fall due on both sides of the balance sheet — if a depositor wants their money back, or if a customer wants to draw on their credit card or credit facility. Maintenance of liquidity at all times is therefore the paramount requirement of banking.

Three distinct types of liquidity are commonly distinguished:

### <mark style="background: #FFF3A3A6;">Funding Liquidity</mark>

**Funding liquidity**: The ability of a bank to fund assets throughout their life and to meet demands for withdrawal of liabilities as and when they arise. This is the primary concern of liquidity [[01-risk_management|risk management]]. 

**Funding liquidity** is your monthly salary vs. your bills. Even if you own a house worth R5 million, if your salary stops arriving you cannot pay rent, groceries, or your car instalment. The house's value is irrelevant in that moment — you need _cash flow over time_ to meet obligations as they arise. A bank faces the same problem: deposits can be withdrawn, funding lines can dry up, and the bank must be able to service those demands day to day regardless of what's on the balance sheet.

Holding a portion of the balance sheet in the form of liquid assets (see [Liquidity Metrics](04-liquidity_management.md) for HQLA classification) facilitates funding liquidity — these assets can be monetised in a stress event.
### <mark style="background: #FFF3A3A6;">Trading Liquidity</mark>

**Trading liquidity**: The ease with which an asset may be bought or sold in the market, in size and with no material impact on the asset price. A liquid asset trades at a narrow bid-offer spread; an illiquid asset cannot.

**Trading liquidity** is your investment portfolio. Shares in Naspers can be sold in seconds at a tight spread — many buyers, transparent price. An unlisted stake in a small private company might take months to sell, and you'd likely have to discount heavily to find a buyer. The bid-offer spread is the cost of that illiquidity. For a bank, this is whether it can sell its bond or loan portfolio quickly without moving the market against itself.
### <mark style="background: #FFF3A3A6;">Redemption Liquidity</mark>

**Redemption liquidity**: Similar to trading liquidity but relevant only as an asset approaches maturity.

**Redemption liquidity** is a fixed deposit maturing in two weeks. You know exactly what you'll receive and exactly when. There's no price uncertainty, no counterparty search required — it's essentially cash-in-waiting. Compare that to the same deposit four years from maturity: early redemption penalties, uncertainty, illiquidity. As the maturity date approaches, the asset _becomes_ liquid simply by the passage of time.

## Liquidity Requirements

This file covers the **quantitative liquidity risk metrics** used by bank treasury functions and Asset Liability Committees (ALCOs) to monitor and manage liquidity risk, including six baseline management information metrics, and the stock of high-quality liquid assets (HQLA) that forms the liquid asset buffer (LAB).

For the conceptual framework of liquidity risk — definitions, sources of funding, liability stability hierarchy — see [Liquidity Framework](01-liquidity.md). For the balance sheet treatment of HQLA, see [Annual Financial Statements](../../02-afs.md). For the regulatory minimum [[01-short_term_metrics|LCR]] and [[03-long_term_metrics|NSFR]] requirements that consume these metrics, see [Basel / BIS](bis.md).
### Internal Requirements

Banks calculate and monitor six key baseline metrics as a matter of course. 

- Short term view
	- Loan-to-Deposit Ratio (LDR)
	- 1m Liquidity Ratio (LR) 
	- Cumulative Liquidity Model (CLM)
	- Liquid Asset Buffer (LAB)
- Long term view
	- Liquidity Risk Factor (LRF)
	- Concentration and Funding Source Report
	- Inter-Entity Lending Report

These measure different elements of liquidity risk and, for consolidated or group banking entities, are prepared at country level, legal entity level, and group level. Together, they provide visibility on:

- The exposure of the bank to funding rollover ("gap") risk
- The daily funding requirement and a forecast of future requirements
- The extent of self-sufficiency of a branch or subsidiary

Liquidity risk must be managed and monitored at a material currency level, as it should not be assumed that all currencies are freely convertible.

### Regulatory Requirements

Two other metrics are monitored as part of the Basel III requirements namely:
- Short term view
	- Liquidity Coverage Ratio (LCR)
- Long term view
	- Net Stable Funding Ratio (NSFR) $\geq$ 100%

## Liability Stability Hierarchy

Different liabilities have materially different behavioural characteristics under both normal (BAU) and stressed conditions. The following hierarchy reflects their relative stability, from most to least stable:

1. Retail current accounts
2. Retail deposit accounts
3. Corporate operational cashflow / call accounts
4. Retail savings accounts
5. Retail fixed-term deposits
6. Private bank deposits
7. Corporate savings accounts
8. Corporate fixed-term deposits
9. Wholesale market fixed-term deposits
10. Money market term funding (CD / CP)
11. Money market deposits / interbank deposits

Retail current accounts are the best example of the distinction between contractual and behavioural tenor: they are contractually payable on demand (immediate maturity) but exhibit sticky behaviour — customers maintain large, stable balances over long periods. Regulators permit banks to treat a proportion of such balances as term funding, with the exact amount and tenor determined by statistical analysis of historical account behaviour. Banks include such historical analyses in their liquidity reporting to the regulator.

At the other end of the spectrum, short-term wholesale liabilities sourced in interbank markets exhibit the most volatile characteristics under stress: professional depositors are market-aware and multi-banked and have historically shown aggressive outflow behaviour during stress events. Non-bank financial institutions (NBFIs) are similarly classified as behaviourally non-stable depositors, as they are sensitive to market conditions and can withdraw at no notice.

A bank's medium-term liability strategy should seek to maximise funding based on higher-stability liabilities and minimise reliance on wholesale funding, while also considering the trade-off with [[04-nii_nim|NII]] / [[04-nii_nim|NIM]] and customer franchise considerations.
