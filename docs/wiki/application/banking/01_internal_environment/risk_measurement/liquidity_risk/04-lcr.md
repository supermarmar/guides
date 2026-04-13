---
tags:
  - application/banking/internal-environment/risk-measurement/liquidity-risk/lcr
  - difficulty/unknown
  - study-status/new
aliases:
---
# Liquidity Coverage Ratio (LCR)

## Purpose and Formula

The [[basel_framework|Basel III]] short-term liquidity metric is the **liquidity coverage ratio (LCR)**. Its purpose is to promote short-term resilience of a bank's liquidity risk profile by ensuring it holds sufficient high-quality liquid assets (HQLA) to survive a significant 30-day stress scenario.

```math
\text{LCR} = \frac{\text{Stock of HQLA}}{\text{Total net cash outflows over the next 30 calendar days}} \geq 100\%
```

Total net cash outflows = total expected cash outflows − total expected cash inflows in the stress scenario over 30 days, subject to a cap: inflows may not exceed 75% of total outflows. Banks may not double-count items — an asset included in HQLA cannot also generate a cash inflow.

The LCR must be ≥ 100% on an ongoing basis in normal conditions. During a period of stress, it is appropriate for banks to draw down HQLA and fall below the minimum. The LCR also captures off-balance-sheet commitments (e.g. undrawn customer facilities may be drawn under stress).

## Stress Scenario Assumptions

The combined idiosyncratic and market-wide stress scenario entails:

- Run-off of a proportion of retail deposits
- Partial loss of unsecured wholesale funding capacity
- Partial loss of secured, short-term financing with certain collateral and counterparties
- Additional contractual outflows from a downgrade in the bank's public credit rating by up to three notches (including collateral posting requirements)
- Increases in market volatility, which may require larger collateral haircuts or additional collateral on derivative positions
- Unscheduled draws on committed but unused credit and liquidity facilities provided by the bank to customers
- Potential need to buy back debt or honour non-contractual obligations to mitigate reputational risk

## HQLA Characteristics

For LCR purposes, HQLA must be **unencumbered** and possess the following fundamental characteristics:

- **Low risk** — high credit standing of the issuer, low sensitivity to interest rate and [[05-market_risk|market risk]], low legal and inflation risk, denomination in a convertible currency with low FX risk.
- **Ease and certainty of valuation** — pricing must be straightforward, not dependent on strong assumptions, and based on publicly available inputs. Structured and exotic products are effectively excluded.
- **Low correlation with risky assets** — the stock of HQLA must not be subject to wrong-way (highly correlated) risk.
- **Listed on a developed and recognised exchange** — listing increases transparency and supports liquidity under stress.

Level 2 assets may represent at most 40% of total HQLA; Level 2B assets may not exceed 15% of total HQLA. See [Liquidity Metrics](02-liquidity_metrics.md) for the [[sarb|SARB]] HQLA tier classifications (Level 1, 2A, 2B).

## Outflow Assumptions by Deposit Type

### Operational vs Non-Operational Deposits

| Deposit type | Definition |
|---|---|
| **Operational deposits** | Deposits where the customer has a substantive dependency on the bank for clearing, custody, or cash management. The relationship must be governed by a legally binding agreement, the customer cannot terminate services with fewer than 30 days' notice without significant switching cost, and the customer must rely on the bank to perform these services in the next 30 days. Assigned lower outflow rates. |
| **Non-operational deposits** | All deposits that do not meet the operational criteria above. Assigned higher outflow rates. |

### Stable vs Less Stable Retail Deposits

| Deposit type | Run-off factor | Definition |
|---|---|---|
| Stable (lower rate) | **3%** | Fully covered by a deposit insurance scheme funded by periodic levies on banks, which has ready access to adequate funds; depositors have established relationships and hold transactional accounts. |
| Stable (standard rate) | **5%** | Fully covered by a deposit insurance scheme or equivalent public guarantee; depositors have established relationships and hold transactional accounts. |
| Less stable | **10%** | All retail and small business deposits not covered by an effective deposit insurance scheme. |

An **effective deposit insurance scheme** must: guarantee prompt pay-outs with clearly defined and publicly known coverage; have the formal legal powers to fulfil its mandate; and operate with operational independence, transparency, and accountability.

**South African context:** South Africa does not have a deposit insurance scheme. Consequently, all retail and small business deposits are classified as **"less stable"** (10% run-off factor), creating a structurally more demanding LCR environment for South African banks compared to many other jurisdictions. Industry discussions with the [[pa|Prudential Authority]] (PA) on establishing deposit insurance were underway at the time of writing.

### Broader Outflow Rate Schedule

The LCR applies differentiated outflow rates by counterparty type and product:

| Deposit classification | LCR outflow weight |
|---|---|
| Retail — stable | 3% |
| Retail — non-stable | 10% |
| SME — covered by deposit insurance | 5% |
| SME — not covered by deposit insurance | 10% |
| Corporates — operational deposits | 25% |
| Financial customers — operational deposits | 25% |
| Corporates — non-operational | 40% |
| Financial customers — non-operational | 100% |

An alternative to granular product/customer-type outflow rates is to apply a single conservative blanket estimate, which avoids the over-engineering of distinguishing between 2%, 4%, 10%, 15%, and 20% across every product and counterparty combination.

## Deposit Liquidity Value Factors

The liquidity value of a deposit (i.e. its LCR outflow rate) is driven by four characteristics:

**(a) Counterparty type** — Retail customers are "stickier" because they are less financially sophisticated, hold smaller balances spread across a large number of accounts, and are less likely to have an alternative bank account. Corporates are more financially astute, with treasury functions actively managing deposits. Financial institutions and public sector entities are considered the least sticky due to sophisticated treasury management and concentration in larger deposits.

**(b) Deposit type** — Current accounts (MTAs) are stickier than term deposits because the lead time to set up a new current account makes rapid transfer difficult within the 30-day stress window.

**(c) Counterparty relationship** — Customers with long-standing, multi-product relationships are stickier than standalone rate-chasing depositors.

**(d) Maturity and cliff risk** — For corporate deposits with residual maturity outside the 30-day stress window, a breakage rate is assumed rather than a full outflow weight, since customers would incur a financial penalty for early withdrawal. However, this creates **cliff risk**: when the residual maturity falls within 30 days, the outflow weight steps up sharply, potentially creating a large re-financing requirement concentrated in that period.

## LCR and Liabilities Strategy

### Improving the LCR

A bank can address the LCR from the numerator or denominator (or both):

**Numerator (increase HQLA):** This is straightforward in principle — purchase more HQLA assets. The HQLA itself must be funded with long-term liabilities, so a deposit-raising strategy may be required simultaneously. In South Africa, government paper (Treasury bills and government bonds) is the only Level 1 HQLA available. Given limited issuance volumes by National Treasury, a structural HQLA shortage emerged for South African banks, prompting the [[sarb|SARB]] to provide a **committed liquidity facility (CLF)** (available for a fee against pledged collateral) as a substitute for Level 2 assets. A bank can also simply hold surplus funds as cash at the central bank, though this carries a P&L cost.

**Denominator (reduce net cash outflows):** A bank should target its optimal liabilities profile and implement a funding strategy that strengthens the LCR. Specific measures include:

- Greater targeting of longer-term fixed deposits (residual maturity > 30 days falls outside the LCR denominator)
- Increased focus on retail, SME, operational, and stable deposit customers
- Introduction of unbreakable fixed-term deposits that remove the risk of early withdrawal
- Reduction of undrawn committed facility balances
- Pricing for liquidity risk (e.g. charging for undrawn headroom, pricing longer-dated products to encourage term extension)
- Targeting online/instant-access accounts structured at the 10% outflow assumption
- Introducing 91- or 95-day notice accounts (LCR-friendly) and phasing out 7-day or 30-day notice accounts (LCR-unfriendly)
- Adding breakage clauses to fixed-rate fixed-term deposits (e.g. no access for 95 days on breakage)

### Deposits Analysis Template

Best practice is to maintain a regular (weekly or fortnightly) deposits analysis report for the products committee, covering: year-end and forecast deposits; articulation of the high-level deposits strategy; treasury's view on market rates and FTP implications; product emphasis (MTAs, instant access, or term); competitor rate analysis; and tracking of current funding levels versus plan.

A competitor analysis is essential — banks typically aim to offer deposit rates in the middle of the competitive range to avoid both under-pricing (losing deposits) and over-paying ([[03-nii_nim|NIM]] compression). In South Africa, competitor information can be sourced from the monthly **BA900 Economic Returns** published by the [[sarb|SARB]] and from competitors' quarterly/annual [[bis|Basel]] Pillar 3 reports.
