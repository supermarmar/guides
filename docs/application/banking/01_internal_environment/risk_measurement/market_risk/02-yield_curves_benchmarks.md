# Yield Curves and Interbank Benchmarks

## Yield Curves

The yield curve plots interest rates for the same type of debt contracts or instruments for different maturities. It is also referred to as the **term structure of interest rates**. As the yield curve expresses the cumulative input of all market participants, it influences all aspects of debt markets: trading and investment, borrowing and lending, bond issuance, and bank balance sheet decisions. Economists also use the yield curve to help predict the future direction of the economy.

### Types of Yield Curves

| Type | Shape | Implied Expectations |
|---|---|---|
| Normal | Moderately positive slope | Lenders demand higher yields for longer terms (default risk and opportunity cost). Borrowers accept higher rates for certainty of long-term funding. Expectation of normal growth and inflation. |
| Steep | Strongly positive slope | Heightened expectations of growth and/or inflation |
| Humped | Rises then falls | Mixed expectations; economy in transition |
| Flat | Horizontal | Expectations of weak economy and low inflation |
| Inverted | Negative slope | Heightened expectations of weak economy and low inflation; possible recession/deflation |

### Hypotheses for Yield Curve Shape

- **Market expectation** — the yield curve is influenced by market participants' views on future interest rate levels.
- **Liquidity preference** — it is riskier for lenders to commit funds for longer periods, creating a liquidity premium.
- **Money substitute** — most investors see holdings as only a substitute for cash, so there is less inclination to extend out the curve.
- **[[06-segmentation|Segmentation]]** — borrowers, lenders, and investors have differing financial needs and time frames, leading to different supply and demand along the curve (e.g. pension funds and infrastructure drive the long end; trade finance and cash surpluses influence the short end).

In practice, market participants consider a combination of these factors. One cannot assume a "parallel shift" in the yield curve. Trading book managers tend to focus on VaR limits, while banking book managers focus on annual earnings at risk (EAR) and economic value of equity (EVE).

### Yield Curve Construction

**Yield-to-maturity (YTM)** is the most commonly used method, but assumes constant reinvestment of coupons at the principal redemption rate.

**Zero-coupon yield curve** — built using zero-coupon bonds, which avoids the reinvestment rate problem. If zero-coupon bonds are unavailable, a zero-coupon curve can be derived by analysing coupons along the curve (bootstrapping).

**Par-yield curves** — use bonds trading close to par and are helpful in setting coupon rates for new issue bonds.

When data is incomplete, analysts interpolate using available information. When data is inconsistent or volatile, mathematical models and judgement are used to fit and smooth the curve. Yield curve construction is more challenging in African markets due to illiquid trading activity and underdeveloped interest rate derivatives markets.

## Interbank Benchmark Rates

### LIBOR (London Interbank Offered Rate)

LIBOR is set at 11 a.m. London time each business day by polling panels of banks as to the rate at which they can borrow from each other for a range of tenors and currencies. High and low submissions are discarded to avoid outliers and the remainder averaged. Hundreds of trillions of dollars of floating rate loans, securities, and derivatives in multiple currencies have been priced off LIBOR.

**LIBOR manipulation (2012–2013)** — certain banks were found guilty of, or admitted to, manipulating LIBOR rates. Banks had set rates lower than actual funding costs to avoid the appearance of funding difficulties, or quoted unreasonably high rates to profit from loan and swap books. Investigations found collusion and inappropriate discussions between banks when setting LIBOR. As a result, the calculation and publication of LIBOR was changed.

LIBOR has expired at the end of 2021, replaced by **alternative reference rates (ARRs)** which are overnight, backward-looking rates:

| Currency | Former LIBOR | Replacement ARR |
|---|---|---|
| GBP | GBP LIBOR | SONIA (Sterling Overnight Indexed Average) |
| USD | USD LIBOR | SOFR (Secured Overnight Finance Rate) |

The key features of ARRs are that they are overnight rates and backward-looking, unlike LIBOR which incorporated forward-looking term credit risk.

### JIBAR (Johannesburg Interbank Average Rate)

JIBAR is the key benchmark money market interest rate in South Africa. Key features:

- Published daily at 11 a.m. on the JSE website for 1, 3, 6, and 12-month tenors.
- The **3-month JIBAR** is the most widely used benchmark for floating rate transactions and interest rate swaps.
- Unlike LIBOR, JIBAR is based on interest rates at which South African banks buy and sell their own **negotiable certificates of deposit (NCDs)**. Bid and offer rates are submitted to determine mid-rates, with the two highest and two lowest removed before averaging.
- [[sarb|SARB]]-regulated banks (five local, four foreign) contribute rates.
- The JSE distributes contributor rates to ensure submissions are as close to market trading rates as possible.
- A JIBAR Code of Conduct was published in March 2014 following a [[sarb|SARB]]-initiated review.

**Basis risk note:** since derivatives such as interest rate swaps tend to reprice with reference to 3-month JIBAR, while most banking book assets are linked to the prime interest rate, hedged portfolios tend to retain prime-JIBAR basis risk.
