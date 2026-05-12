---
tags:
  - application/banking/internal-environment/risk-management/risk-mitigation
  - difficulty/unknown
  - study-status/new
aliases:
---
# Risk Mitigation

Before focusing on technical and complicated [[01-risk_management|risk management]] matters, management should always know and be thinking about a few basic questions: What are the bank's largest individual, sector, product, and regional exposures? In what circumstances should these exposures be reduced or grown? And, very importantly, what are the means and options for reducing these exposures under a range of circumstances? The bank would also want to understand how to grow certain exposures to meet their strategic and business objectives, without taking on excessive risk.

## Risk Avoidance

This proactive approach involves changing plans to eliminate a specific threat entirely, such as deciding not to launch a product in a volatile market or cancelling a project.

## Risk Acceptance

Acknowledging a risk exists but deciding not to take action because the cost of mitigation is higher than the potential loss. This is often used for low-impact risks, though the risks should still be monitored

## Risk Transfer

Shifting the consequence and responsibility of a risk to a third party. Common examples include purchasing insurance, using service contracts, or outsourcing a risky activity.

### Hedging

Hedging of various other risks via financial derivatives can be used to protect against interest rate and exchange rate risk. Banks mitigate risk when exposure to a counterparty or risk factor becomes large. The instruments below are used to manage credit risk, interest rate risk, foreign exchange risk, and market risk in both the trading and banking books.

#### Basis Challenge

The "basis" is a key challenge in hedging: there is no certainty that rates on the bank's exposure will move in tandem with the instrument used to hedge. If a bank earns prime on its assets but pays JIBAR 3-months on liabilities, entering a pay-fixed-receive-JIBAR swap eliminates the JIBAR liability exposure, leaving only the fixed leg and the prime-JIBAR basis as residual risks.

[[01-risk_management|Risk management]] reports must identify hedging so that basis risk can be analysed separately. Aggregating long and short positions could show little net risk while basis risk is substantial.

#### Forward Rate Agreements (FRAs)

FRAs are over-the-counter (OTC) trades between two parties. Both parties agree to buy or sell an instrument in the future with a predefined amount, maturity, and rate fixed. At maturity, funds are exchanged to reflect the change in value from interest rate movements. FRAs can be tailored to specific needs.

#### Futures

Futures are exchange-traded with standard terms (e.g. Eurodollar futures are $1 million for 90-day periods settling quarterly). Banks can sell consecutive futures contracts ("strips") to create long-dated hedges. Futures positions are **margined** — the exchange requires an initial margin to cover potential losses and variation margin (adjusted daily) to mitigate credit risk. The standard terms and strict margining rules allow for liquid trading. Both FRAs and futures are priced off the yield curve.

#### Swaps

**Overnight Index Swaps (OIS)** are a popular form of interest rate hedging. One party pays a fixed rate for a fixed period on a nominal amount; the other pays the average floating overnight rate based on a benchmark index. Nominal amounts are not exchanged; settlement involves paying the difference between fixed and floating leg cashflows. OIS allows a treasury function to separate interest rate and liquidity positions.

Interest rate swaps are one of the main methods used by banks to hedge floating rate debt. A **pay-fixed-receive-floating** swap receiving JIBAR 3-months, for example, offsets liabilities referencing JIBAR 3-months — the only remaining exposure is the fixed leg payment.

#### Options

Options provide protection against adverse market movements without the firm commitment of FRAs, futures, or OIS. Buying an option is like buying an insurance policy.

- **Swaption (swap option)** — an option on an interest rate. A **payer swaption** gives the holder the right but not the obligation to enter a pay-fixed-receive-floating swap at the expiry date; useful for a bank with floating rate debt exposed to rising rates.
- **FX option** — gives the holder the right but not the obligation to fix the price at which two currencies are exchanged in the future; used to hedge FX exposure.

#### Credit Default Swaps

Credit risk is, for practical purposes, difficult to hedge. The optimum approach to credit risk for most banks involves diversification of the loan book, avoiding concentration with one borrower or sector, and the operation of conservative origination principles.

For a more proactive approach, historically the means of hedging credit risk was to short the bonds of the borrower or similar borrowers. However, it is not always possible to borrow the bonds in sufficient size, and the repo rate can be prohibitively expensive. Basis risk can again be a challenge.

Since the early 1990s, the management and transfer of credit risk has been transformed by the emergence of **credit derivatives**, which are contracts and instruments that separate and transfer credit or default risk from the lender / noteholder to another party.

**Credit Default Swaps (CDS)** spreads are watched closely by issuers, investors, and banks, and are key to issuance, investment, and pricing decisions. CDSs allow credit protection to be bought and sold between bilateral counterparties, with premiums paid as in traditional insurance. Key characteristics:

- Specify the nominal amount of reference asset (e.g. bond, entity, index, or tailored basket) against which a payment amount will be made if a specified credit event is triggered
- Credit events include: default on a payment, rating downgrade, or bankruptcy
- Are considered "unfunded" — the nominal amount is never transferred
- Under the International Swaps and Derivatives Association (ISDA) master agreement provisions, margining and collateral are made

In the early years of credit derivatives, there were controversies in agreeing exactly when credit events were triggered (e.g. no payout on Greece because default was accepted "voluntarily"). Many call for greater market transparency and better statistics to build confidence and liquidity to maximise opportunities for active credit portfolio management.

### Debt Sale

A more direct approach is the outright sale of loan and bond positions. Selling has the advantage of immediacy and avoids the risk that a hedging instrument does not perform as expected (basis risk). Liquidity varies based on factors including market size and standardisation, complexity and terms of the debt instrument, and borrower credit rating. In stressed markets, liquidity can be expected to diminish when it is needed most.

### Securitisation

At its simplest, securitisation involves transforming assets into securities. Assets are sold to a bankruptcy-remote special purpose vehicle (SPV), which issues securities backed by the assets. Benefits include enhanced liquidity, balance sheet management, diversification, and [[01-risk_management|risk management]].

Banks have securitised — with varying success — most types of assets. These range from straightforward government bonds to trade, auto, and credit card receivables; mortgages; auto leases; and loans to the more exotic future streams of rock star royalties, football gate receipts, pharmaceutical patents, and funeral home burials.

**Common forms of securitisation:**

- Asset backed securities (ABS)
- Mortgage backed securities (MBS)
- Collateralised debt obligations (CDOs) — generally bonds, which can take synthetic exposure through derivatives including credit default swaps
- Collateralised loan obligations (CLOs) — consist of loans
- Asset backed commercial paper (ABCP)

**Credit enhancement** is required depending on the perceived risk and liquidity of the underlying assets. Enhancement can take forms including overcollateralisation, reserves (established upfront or through retained earnings), guarantees, letters of credit, credit default swaps, and first loss provisions. Securities can be "tranched," with junior, mezzanine, and senior issuance having different risk and return profiles. Regardless, investors must be largely confident that the assets can service the repayment of interest and principal, without looking to the bank / originator for payment.

**Issues with securitisation — the "originate to distribute" model**: Securitisation ran into trouble in the financial crisis. Because each participant in the "chain" of creating a securitisation is responsible for only their function (asset generation, securitisation structuring, sales), none had the responsibility for knowing the borrower fully and verifying and understanding that the entire deal makes sense. Each earned a fee upfront and none had a direct ongoing economic stake in the performance of the borrower.

**Post-crisis regulation (EU)** — Changes have been introduced to revive the securitisation market on a sound basis:

- Enforce and standardise risk retention requirements on banks offering securitisations
- Enforce due diligence requirements on investors both before investing and while holding a securitisation position
- Increase transparency requirements for originators and sponsors to ensure investors and supervisors have access to all relevant information in a standardised format
- Capital requirements on securitised assets can be calculated using: the internal ratings-based approach (SEC-IRBA), external ratings-based approach (SEC-ERBA), or the Standardised Approach (SEC-SA)

**STS / STC securitisation** (Simple, Transparent, Standardised / Comparable) — A new kind of securitisation introduced in Europe with specific requirements:

- Restrictions on the types of underlying exposures that may be incorporated into the securitisation
- Limits on the risk-weighting of underlying exposure to ensure high-risk assets are not bundled into these securitisations
- Rules regarding granularity of the underlying pool of assets — no exposure can account for more than 1% of the total exposure
- At origination, the underlying exposures should not be in default nor represent loans to credit-impaired borrowers

## Risk Reduction

This involves taking steps to lower the probability or impact of a risk. Examples include implementing new security controls, training employees to prevent phishing, or diversifying suppliers to prevent shortages.
### Loan [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/application_scoring/01_introduction/01-context|Underwriting]] Criteria

Best-practice credit [[01-risk_management|risk management]] discipline dictates that banks apply a sound credit policy at origination — prevention is better than cure.  New loans must be sanctioned only within the context of the [[02-risk_appetite|risk appetite]] statement and risk-weighted capital criteria:

- **Corporate and wholesale banking**: A request to provide credit should involve the completion of a form to be submitted to a separate entity from the relationship bankers, whether it be a credit committee or (in the case of smaller banks) executive management and ALCO. The request will contain all the information needed for the committee to discuss the risk and return of the loan, terms, and the customer, so a determination can be made as to whether it fits into the broader strategy.
- **Retail banking**: New loans can be granted via automated applications, which will be approved or referred to by loan origination officers.

Beyond the credit risk of the borrower and the rate charged, the bank must also evaluate the specifics of the loan:

- Legal framework and jurisdiction risks
- Collateral: acceptable forms and enforceability
- Disclosure requirements
- Ability to terminate: material adverse change clauses and covenants
- Transferability: can the loan be sold?
- Currencies
- Fixed or floating rate
- Prepayment options

Within the bank, many of the items should align with credit risk policies and procedures as laid out in the bank's [[02-risk_appetite|risk appetite]] framework. Some specifics will require legal consultation and others may require input from various committees and levels of staff.
#### [[05-aml_kyc|KYC]]

"[[05-aml_kyc|Know Your Customer]]" ([[05-aml_kyc|KYC]]) is a key element of the loan origination process. For corporate and wholesale banking, relationship bankers should have an extensive dialogue with customers to have a thorough understanding of their business, strategy, and risks. For retail banking, the bank will maintain behavioural scorecards and delinquency information to monitor loan performance and take action should the loan be at risk of defaulting.

### Management Actions

The risk portfolio of a bank can be adjusted by monitoring maturing business and adjusting policy for assets accordingly. New business for sectors can be frozen, reduced, or subjected to stricter standards (e.g. increased spread and fees, more collateral, tighter covenants). Emphasis can be placed on booking business in sectors that can be expected to perform counter to the concentration risk — sectors that outperform in different phases of the economic cycle (e.g. consumer staples are usually relatively strong in a downturn).
