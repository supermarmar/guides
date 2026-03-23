# Behavioural Modelling of Cash Flows

## Contractual vs Behavioural Tenor

All liquidity management requires a bank to model both contractual and behavioural tenor profiles and asset-liability gap profiles. Assets and liabilities may exhibit behavioural characteristics that are materially different from their underlying contractual characteristics:

- **Liabilities** (e.g. call accounts, demand deposits) have short contractual tenors but may exhibit stable, long-dated behavioural tenors if customers leave balances untouched.
- **Assets** (e.g. residential mortgages with 20–30 year contractual terms) typically repay earlier than contractual maturity due to prepayment behaviour, producing a shorter behavioural tenor.

Understanding both sides of this distinction drives more informed decisions on funding, liquidity management, and **fund transfer pricing (FTP)**, which is applied to behavioural (or expected) tenors rather than contractual tenors.

### Contractual ALM Gap

The **contractual ALM gap** places each cashflow into the time bucket corresponding to its contractual maturity. The typical bucket structure runs from overnight/1-day through to greater than 20 years. On a contractual basis, deposits are shorter and loans are longer, producing a pronounced maturity mismatch in short-dated buckets.

### Behavioural ALM Gap

The **behavioural ALM gap** adjusts cashflows to reflect observed behaviour rather than contract terms. On a behavioural basis, deposits shift to longer buckets (sticky retail balances extend tenor) and loans shift shorter (prepayments reduce average life). The resulting gap profile is materially less extreme than the contractual gap, and is the basis used for structural liquidity management and FTP purposes.

## Modelling Demand Deposits

The behavioural tenor of contractually short-dated deposits (call accounts, current accounts, instant-access savings) is set through statistical observation. The process is:

1. Observe month-end spot and average balances over time, grouped by product type (e.g. retail current accounts, corporate operational accounts, savings accounts).
2. Note behaviour at expected outflow points (month-end, quarter-end).
3. Note behaviour at times of stress (e.g. the interbank market freeze of October 2008 following the Lehman Brothers bankruptcy).

To better understand the stickiness of specific deposit pools, each liability should be assessed against the following criteria (originally proposed by Leonard Matz):

- Is it insured?
- Is it secured?
- Are the funds controlled by the owner?
- Does the customer have other relationships with the bank (e.g. loans)?
- Is there internet access enabling rapid transfer?
- Is the depositor a net borrower?
- Type of counterparty — level of financial sophistication?
- Direct depositor or via a third party?

Stable aggregate balances observed across a sufficiently long time period (including at least one stress period) support the assignment of a longer behavioural tenor, typically with a haircut applied (e.g. 90% of money transmission account balances treated as 5-year tenor).

**Conservative cap:** Regardless of what historical statistics suggest, the behavioural tenor for demand deposits (current accounts, instant-access accounts) should not be set at longer than **3 years**, and certainly not longer than **5 years**, because the nature of future liquidity stress events may differ materially from historical observations.

Multiple uses exist for this analysis, including FTP, calculation of an internal LCR view, determination of an appropriate LAB size, and informing customer pricing strategy.

## Modelling Prepayment Behaviour

Asset behavioural profiles — where assets repay earlier than contractual maturity — are obtained by combining historical observation with prepayment assumptions. For example, the historical average life of a residential mortgage is typically 6 to 7 years, and this behavioural tenor is used for FTP purposes even if the contractual term is 20 or 30 years.

For **undrawn facilities and revolving credit facilities**, best practice is to treat the asset as running to its full contractual tenor for FTP purposes. This is conservative but necessary, because back-up and other liquidity lines provided to customers are likely to be drawn precisely when the bank is seeking to preserve liquidity — i.e. during a funding crisis.

Prior to the 2008 crisis, commitment lines typically attracted only a flat standing charge (e.g. 10–20 bps). Post-crisis, these assets are treated as running to full contractual maturity (whether drawn or not), with the appropriate liquidity premium charged at origination to reflect the embedded liquidity risk.

## Modelling Contingency Funding Obligations

Contingent, off-balance-sheet, and collateral obligations also generate term funding requirements. The principal challenge is understanding the tenor characteristics of these cashflows.

**Derivatives and CSA arrangements:** Interbank derivatives trading takes place under the Credit Support Annex (CSA) of the standard ISDA contract. Under a two-way CSA, the mark-to-market value of each derivative is exchanged as cash collateral. In theory, a perfectly hedged book has netted zero collateral flows because what a bank posts on the negative leg it receives from the hedge counterparty.

However, many counterparties — corporates, sovereign authorities, debt management offices, central banks — do not sign CSA agreements. Under this **one-way CSA** arrangement, the bank must post cash collateral when mark-to-market negative but receives nothing when mark-to-market positive. This creates a structural funding requirement. The bank must apply the appropriate tenor liquidity premium to the net mark-to-market of all uncollateralised derivatives, based on the time-bucketed net cashflow profile of those positions.

## Behaviouralisation Exercise

The behaviouralisation exercise is the formal process by which a bank sets behavioural tenors for both assets and liabilities. The methodology is analogous to an actuarial experience investigation — using historical data to set credible behavioural assumptions based on actual observations.

**For deposits (liabilities):**
1. Group accounts by cohort: by opening date, by product, and by customer type.
2. Plot aggregate balances over time for each cohort.
3. Set the behavioural tenor based on actual observation of balance run-off, noting outliers and stress-period behaviour.

**For loans (assets):**
1. Group loan cohorts by product category (e.g. residential mortgage) and inception period (e.g. all contracts originated in January 2021).
2. Observe month-end spot balances to construct run-off profiles (repayments typically occur towards month-end).
3. Calculate run-off rates for each repayment month; use these to derive the behavioural tenor based on the observed run-off profile.

For revolving products (e.g. credit cards), it is common practice to additionally calculate the **stable portion** of outstanding balances — the core balance that is persistently utilised rather than transient.

Results are typically presented graphically by cohort to allow visual identification of stable cores and to support conservative but credible tenor assignments. A bank should not simply accept a deposit pool as very long-dated solely because statistics suggest it; tenor assumptions must incorporate judgment about how future stresses may differ from the historical observation period.
