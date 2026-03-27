# Interest Rate Risk in the Banking Book ([[04-irrbb_measurement|IRRBB]]): Sources

A bank can be extremely effective at managing its credit portfolio but still perform poorly if it fails to manage its interest rate and [[05-market_risk|market risk]]. While credit risk remains the main type of risk exposure for most retail banks, interest rate risk in the banking book ([[04-irrbb_measurement|IRRBB]]) represents a significant and pervasive structural risk for all deposit-taking institutions.

## Banking Book vs Trading Book

**Interest rate risk in the banking book ([[04-irrbb_measurement|IRRBB]])** refers to the current or potential risk to the bank's capital and earnings arising from adverse movements in interest rates that affect the bank's banking book positions. [[basel_framework|Basel III]] defines [[04-irrbb_measurement|IRRBB]] as "the current or prospective risk to the bank's capital and earnings arising from adverse movements in interest rates that affect the bank's banking book positions."

**Trading book** — a portfolio of financial instruments held by a bank that are actively traded to facilitate trading for the institution's customers, profit from trading spreads, or hedge risk. Trading books are marked to market daily and use [[07-var_limitations|value at risk]] (VaR) as a key risk metric.

An instrument must be designated as a trading book instrument (at first recognition) if it is held for one or more of the following purposes: short-term resale; profiting from short-term price movements; locking in arbitrage profits; or hedging risks arising from the above. Any instrument not held for these purposes at inception must be assigned to the banking book.

## How Interest Rate Changes Affect a Bank

When interest rates change, two key effects arise:

1. **Earnings effect** — changes in interest rate-sensitive income and expenses alter the bank's [[03-nii_nim|net interest income]] ([[03-nii_nim|NII]]).
2. **Economic value effect** — the present value of future cashflows changes, altering the underlying value of assets, liabilities, and off-balance sheet items, and hence the bank's economic value of equity (EVE).

Mismatches between assets and liabilities mean these changes are not symmetrical, leaving banks exposed to adverse interest rate movements.

## Four Sources of [[04-irrbb_measurement|IRRBB]] Mismatch

The sources of structural mismatch that give rise to [[04-irrbb_measurement|IRRBB]] are:

- **Term** — short-term liabilities funding long-term assets (e.g. non-maturity deposits funding 20-year mortgages).
- **Volume** — many smaller deposits funding large loans.
- **Interest rate type** — offering fixed and floating rate products on both sides of the balance sheet.
- **Product features** — early termination of deposits and prepayment/redraw of loan facilities.

## Forms of Interest Rate Risk

### Gap Risk

Gap risk arises from the term structure (maturity mismatch) of banking book instruments. A gap analysis report is used to measure potential gap risk. To manage gap risks:

- **Cash hedges** — the bank writes assets or liabilities at specific repricing maturities to reduce gap exposures (e.g. offering 5-year fixed rate deposits to offset 5-year fixed rate mortgages).
- **Derivative hedges** — forward rate agreements (FRAs), futures, and interest rate swaps. More flexible than cash hedges but more complex to manage.

### Option Risk

Option risk arises when customers have the ability to alter the level and timing of cashflows. It is categorised as:

**Automatic option risk** — explicitly embedded in contractual terms, where the customer will most likely exercise the option. Examples:

- **Cap risk** — loans with a maximum rate; in a rising rate environment, liabilities reprice upwards but assets cannot, squeezing the margin.
- **Floor risk** — deposit products where the rate cannot be repriced downwards; in a decreasing rate environment, loan rates may fall but deposit rates cannot (particularly relevant near the zero bound). Management may include effective product design (minimum rates on loans built into contracts) or purchasing interest rate caps and floors in the financial markets.

**Behavioural option risk** — arises where customer behaviour is influenced by interest rates within the flexibility allowed in the product terms. Examples:

- **Prepayment risk** — the risk that a customer repays their loan faster than contractually anticipated. Since this is largely driven by socio-economic factors, it is difficult to mitigate through hedges. A bank should diversify its funding profile and construct a dynamic hedging/funding profile based on the anticipated behavioural run-off, periodically re-evaluated as actual loan experience occurs.
- **Early redemption risk** — the opposite side to prepayment; the risk that depositors withdraw money earlier than contractually expected (e.g. fixed deposits). Early redemption charges may discourage this, but regulators may cap penalties for retail customers. Careful monitoring of the behavioural lifetime of customers is key.

### Basis Risk

Basis risk arises when assets and liabilities are priced off different benchmark rates at the same tenor, or off the same benchmark rate at different tenors. Note that basis risk is **not** captured by the gap report.

In a typical South African retail bank, assets are linked to the prime rate while funding references JIBAR 3-months. These rates are correlated but not perfectly so. Management techniques include:

- Entering a pay-fixed-receive-floating interest rate swap referencing JIBAR 3-months (offsetting the funding cashflows).
- Effective product design (developing products on both sides that reference the same underlying rate for a natural hedge).
- Adjusting product pricing.

### Yield Curve Risk

Interest rates may not change across the entire yield curve uniformly. In a borrow short-term / lend long-term strategy, profitability could be reduced if only short-term rates increase.

## Asset-Sensitive vs Liability-Sensitive Banks

Banks are often described by their relative responsiveness to short-term rate changes:

- **Asset-sensitive** — interest-earning assets (loans and investments) tend to reprice more quickly than interest-bearing deposits and borrowed funds. These banks tend to benefit when rates rise but face margin compression when rates fall.
- **Liability-sensitive** — liabilities reprice more quickly than assets (e.g. funded long-term fixed rate assets with short-term deposits). These banks face [[03-nii_nim|NII]] pressure when rates rise, and their EVE declines as the discount rate applied to long-duration assets increases.

South African banks tend to have floating rate assets (linked to the prime rate) and a mix of fixed-rate liabilities (cheque accounts, fixed deposits) and floating-rate wholesale funding (JIBAR-linked). If left unhedged, this structure leads to widening margins when rates increase and narrowing margins when rates decrease.

## [[04-irrbb_measurement|IRRBB]] Hedging (Behavioural)

Interest rate risk in the banking book may be hedged to mitigate rate risk and lock in [[03-nii_nim|NII]]. However, hedging instruments come at a cost, reducing earnings. Furthermore, **behavioural risks** arise from hedging: early redemptions or prepayments can result in "naked" hedges that no longer have underlying offsetting exposures, incurring a cost to unwind.

For [[05-market_risk|market risk]] hedging instruments (FRAs, futures, swaps, options) see [Hedging Instruments](05-market_risk.md).
