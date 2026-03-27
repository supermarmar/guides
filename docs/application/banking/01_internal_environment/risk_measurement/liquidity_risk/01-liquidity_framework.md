# Liquidity Framework

This file covers the **conceptual foundations of liquidity [[01-risk_management|risk management]]** used in bank treasury and ALCO functions, including the definition of liquidity risk, its structural link to maturity transformation, the sources of bank funding, and the behavioural characteristics of different liability types.

For the quantitative [[02-liquidity_metrics|liquidity metrics]] (LDR, CLM, LRF, HQLA) used to measure and monitor these risks, see [Liquidity Metrics](02-liquidity_metrics.md). For the balance sheet treatment of liquidity (HQLA on the asset side, deposit types on the liability side), see [Annual Financial Statements](../../02-afs.md). For the broader [[01-business_model|business model]] context of maturity transformation, see [Business Model](../../01-business_model.md). For the regulatory minimum liquidity standards ([[04-lcr|LCR]], [[05-nsfr|NSFR]]) introduced under [[basel_framework|Basel III]], see [Basel / BIS](../../../../../regulation/international/bis/bis.md).

## Defining Liquidity

**Liquidity risk** is the uncertainty in meeting (or not meeting) all obligations when they become due. A bank must at all times be able to service its obligations as they fall due on both sides of the balance sheet — if a depositor wants their money back, or if a customer wants to draw on their credit card or credit facility. Maintenance of liquidity at all times is therefore the paramount requirement of banking.

Three distinct types of liquidity are commonly distinguished:

- **Funding liquidity**: The ability of a bank to fund assets throughout their life and to meet demands for withdrawal of liabilities as and when they arise. This is the primary concern of liquidity [[01-risk_management|risk management]].
- **Trading liquidity**: The ease with which an asset may be bought or sold in the market, in size and with no material impact on the asset price. A liquid asset trades at a narrow bid-offer spread; an illiquid asset cannot.
- **Redemption liquidity**: Similar to trading liquidity but relevant only as an asset approaches maturity.

Holding a portion of the balance sheet in the form of liquid assets (see [Liquidity Metrics](02-liquidity_metrics.md) for HQLA classification) facilitates funding liquidity — these assets can be monetised in a stress event.

## Maturity Transformation and the Source of Liquidity Risk

The core business of banking — **maturity transformation** — creates liquidity risk structurally. Banks originate long-dated assets (residential mortgages, project finance loans with maturities up to 50 years, committed but undrawn credit facilities) funded by shorter-duration liabilities (current accounts, short-term deposits). This creates a **maturity mismatch** between assets and liabilities, and the uncertainty underlying this mismatch is the fundamental source of liquidity risk.

Banks therefore assume a continuous ability to roll over or obtain new funding. Were this assumption to fail, banks would never originate long-dated illiquid assets in the first place. The challenge of liquidity management is twofold:

1. **Asset funding**: Securing funding for assets over their full life, including committed but as yet undrawn assets such as credit cards and contingency funding lines.
2. **Liability withdrawal**: Meeting immediate withdrawal requests from depositors, given that a large proportion of customer liabilities are demand deposits — current accounts (also known as chequing or money transmission accounts) and instant-access savings accounts.

Banks also need to understand the **behavioural nature of their deposits** in order to fund term assets: certain contractually on-demand deposits (e.g. current accounts) exhibit sticky or term behaviour and can be modelled as providing longer-dated funding than their contractual maturity implies.

## Lender of Last Resort

In every jurisdiction, the central bank operates as a **lender of last resort**, providing emergency liquidity to a bank that cannot generate liquidity through the liquidation of assets. However, recourse to central bank funding is the last option for the bank — it signals a compromised standalone viability and should not be considered a BAU source of liquidity.

Post-2009, banks in the Eurozone accessed the [[ecb|ECB]]'s 3-year repo facility as a quasi-BAU source; this reflected structural funding instability after the financial crisis rather than sound practice, and the facility was designed as a temporary measure. Under normal conditions, central bank funding (other than daily open market operations) lies outside the scope of ordinary liquidity management.

## Sources of Liquidity

Bank funding sources fall into two categories: **customer funds** and **wholesale funds**. A proper understanding of both categories is necessary because the different types within each exhibit very different behavioural characteristics with respect to tenor, pricing, and customer behaviour.

### Customer Funds

Customer funds include traditional deposit-taking from retail and corporate customers. They exhibit more stable behavioural characteristics than wholesale funds and form the preferred base of bank funding. In South Africa, low levels of discretionary savings — with contractual savings channelled via pension funds, provident funds, and asset managers — mean that banks cannot source sufficient customer deposit funding for all their liquidity needs. South African banks therefore rely on institutional/wholesale funding to supplement customer deposits, making them structurally more dependent on wholesale markets than banks in savings-rich economies.

### Wholesale Funds

Wholesale funds are sourced from institutional depositors: asset managers, pension funds, other banks, money market instruments (certificates of deposit, commercial paper), and interbank deposits. They are generally more rate-sensitive, shorter-dated, and more volatile under stress than customer deposits. Professional/institutional depositors are typically multi-banked and move funds rapidly in response to perceived credit stress — as evidenced by the aggressive outflows from wholesale funding sources observed during historical stress events.

Contractually long-dated wholesale liabilities (e.g. a 3-year capital markets bond issuance) are stable regardless of their institutional source. The behavioural instability of wholesale funds is primarily a concern for contractually short-dated instruments.

### Central Bank Funding

The central bank is a **last resort** source of funding liquidity and should not under any circumstances be considered a BAU source. A bank that has recourse to central bank funding outside of daily open market operations may be considered to be a compromised standalone viable entity.

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

A bank's medium-term liability strategy should seek to maximise funding based on higher-stability liabilities and minimise reliance on wholesale funding, while also considering the trade-off with [[03-nii_nim|NII]] / [[03-nii_nim|NIM]] and customer franchise considerations.

## Behavioural Assumptions

Pure liquidity stress events are rare, and many senior managers have never experienced one. This makes it difficult to calibrate deposit behaviour under stress purely from historical observation. **Conservatism and prudence** are therefore the appropriate approach for both liability strategy and liquidity [[01-risk_management|risk management]].

Key nuances in [[03-behavioural_modelling|behavioural modelling]] include:

- Digital/mobile-based accounts may behave differently from branch or postal accounts, varying by customer demographic.
- In markets such as South Africa, very low-income customers may withdraw entire salary payments in cash on pay day, creating predictable but concentrated outflow events.
- The best approach for optimum liability strategy must be based on conservatism, with supplementary forward-looking stress scenarios, as covered in [Liquidity Metrics](02-liquidity_metrics.md).
