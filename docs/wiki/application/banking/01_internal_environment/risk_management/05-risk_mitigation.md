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

#### Hedge Accounting

The accounting treatment of hedges is a separate test from economic effectiveness or capital recognition. Hedge accounting under [[../../../../regulation/international/ifrs/ifrs9_standard|IFRS 9]] requires documented hedge designation, prospective and retrospective effectiveness assessment, and falls into three categories: fair value hedge, cash flow hedge, and net investment hedge. A trade that hedges economically but does not qualify for hedge accounting will still introduce P&L volatility through the income statement, which is one reason why the front office, the risk function, and the finance function must agree on hedge design before the trade is booked.

### Central Clearing through CCPs

Following the 2009 G20 Pittsburgh agreement, standardised over-the-counter (OTC) derivatives must be cleared through a **central counterparty** (CCP). The CCP novates each bilateral contract into two contracts with itself, becoming the buyer to every seller and the seller to every buyer.

The mitigation effect is twofold. Counterparty credit risk is transferred from the original bilateral counterparty (whose default in 2008 was the systemic threat) to the CCP, which is mutualised, regulated, and in practice implicitly backstopped by the central bank. The CCP also performs **multilateral netting** across all members, compressing gross exposures to a single net exposure per member.

CCPs require members to post **initial margin** (covering potential future exposure under stressed market moves), **variation margin** (settled daily to reflect mark-to-market moves), and **default fund contributions** (a mutualised cushion that absorbs losses if a defaulting member's margin proves insufficient). The default waterfall consumes the defaulter's margin first, then the defaulter's default-fund contribution, then a "skin in the game" tranche from the CCP, then non-defaulting members' default-fund contributions, then assessment rights on surviving members.

The trade-off is concentration: the CCP becomes too important to fail in its own right. Recovery and resolution planning for CCPs is an active supervisory topic (CPMI-IOSCO has issued specific guidance). For products that are not standardised enough to clear, bilateral margining rules apply (see Margining for Non-Cleared Derivatives below).

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

### Insurance and Guarantees

Beyond financial derivatives, the most established transfer mechanism is **traditional insurance**. The bank pays a premium to an insurer that agrees to indemnify a defined loss. The varieties most relevant to a bank are operational-risk policies (bankers blanket bond covering employee dishonesty, robbery, and forgery; professional indemnity for advisory negligence; directors and officers; cyber; crime), credit insurance (covering trade credit, single-name corporate exposure, or sovereign-political risk, common at export credit agencies and trade finance desks), title and surety bonds, and reinsurance for banks with insurance subsidiaries.

A **guarantee** is a contractual undertaking by a third party to pay a defined obligation if the primary obligor fails to do so. In capital terms, an eligible guarantee is **unfunded credit protection** under the CRR and qualifies for credit risk mitigation by substituting the guarantor's risk weight for the borrower's. Parent-company guarantees, government export-credit guarantees, and standby letters of credit are common forms. The same recognition tests apply (legal certainty, no escape clauses, no material residual basis); a "comfort letter" without legal force delivers economic comfort but no capital relief, however reassuring it sounds.

The recurring failure mode of insurance-based transfer is insurer concentration and credit. AIG in 2008 was the canonical example: a single counterparty had written so much protection that, when called on it, it could not pay, and the public sector absorbed the loss. The grandmaster's heuristic applies again: an insured exposure is at least three risks (the original, the basis, and the insurer's credit).

## Risk Reduction

This involves taking steps to lower the probability or impact of a risk. Examples include implementing new security controls, training employees to prevent phishing, or diversifying suppliers to prevent shortages. In a bank context, the most important reduction tools are the limit framework, underwriting discipline, covenants, collateral, netting, and bilateral margining.

### Diversification and Concentration Limits

The oldest banking-risk mitigation is **don't put all your eggs in one basket**. Diversification reduces the impact of any single default, sector downturn, or country shock by spreading exposure widely. The framework that operationalises diversification is the **limit structure**, set by the board through the [[02-risk_appetite|risk appetite]] statement and enforced by the credit committee and front-office limit system:

- **Single-name limits** capping exposure to any one borrower or borrower group, denominated in absolute value or as a percentage of CET1
- **Sector limits** capping exposure by industry (commercial property, leveraged finance, oil and gas) to reflect the bank's view on correlated stress
- **Country and sovereign limits** capping exposure to any one jurisdiction, including its government, banks, and corporates
- **Counterparty and trading limits** for derivative and securities-financing exposures, often combined with potential-future-exposure (PFE) measures
- **Large-exposure limits** under CRR Article 395: no exposure above 25% of Tier 1 capital to any single counterparty, with tighter limits for G-SIB-to-G-SIB exposures

Limit breach is a hard control: a transaction that would exceed an applicable limit cannot be booked without escalation. Diversification has a known failure mode: in a systemic event, correlations rise toward one and apparently diversified portfolios concentrate. This is exactly what credit concentration stress testing exists to surface (see [[../risk_measurement/credit_risk/credit_concentration_risk/01-context|credit concentration risk]]).

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

### Loan Covenants

**Covenants** are contractual undertakings by the borrower that travel with the loan. They give the bank a right to act before a default occurs, which is precisely why they are the second-most-important mitigation lever after underwriting itself. Five families of covenant appear in a typical loan agreement:

- **Financial covenants** require the borrower to maintain specified ratios. Common examples are debt service coverage (DSCR), interest coverage (ICR), leverage (net debt to EBITDA), loan-to-value (LTV), and minimum net worth. Tested periodically, usually quarterly
- **Affirmative covenants** require the borrower to do specified things: deliver audited accounts on time, maintain insurance, pay taxes, comply with laws, allow inspection
- **Negative covenants** prohibit specified actions: granting security to other creditors (the **negative pledge**), incurring further debt above a cap, paying dividends above a cap, disposing of material assets, changing the business
- **Information covenants** require periodic disclosure of management accounts, compliance certificates, and any material adverse event
- **Material adverse change (MAC) clauses** give the bank the right to call default on a qualitative basis, though most banks use them rarely because the legal threshold is high and exercising the clause can crystallise the loss

A covenant breach triggers a right to act, not an automatic default. The bank can demand cure, renegotiate terms, charge a waiver fee, increase pricing, demand additional collateral, or, in the most serious cases, accelerate the loan. The discipline lies in using covenant breaches as **early warning signals** of credit deterioration rather than waiting for missed payments. The mid-2010s saw a strong trend toward **covenant-lite** structures in leveraged finance, eliminating maintenance covenants in favour of incurrence-only tests; this is widely viewed as a weakening of mitigation in exchange for issuer flexibility.

### Collateral and Credit Risk Mitigation

Beyond the underwriting decision, a bank's main risk-reduction lever is taking **collateral**. Collateral does not reduce the probability of default; it reduces the loss given default by giving the bank a claim on a specific asset.

The CRR (Articles 192 to 241, mirrored in the UK PRA rulebook) distinguishes two forms of recognised **credit risk mitigation** (CRM):

- **Funded credit protection**: the bank has direct control of a tangible asset. The eligible forms include cash deposits with the bank, government and corporate debt securities, gold, equities in main indices, certain UCITS funds, residential and commercial real estate, and trade receivables. Each carries its own eligibility tests and supervisory haircuts
- **Unfunded credit protection**: a third party stands behind the obligation. The eligible forms are guarantees and credit derivatives. The protection provider must itself be a "good" counterparty (sovereign, public-sector entity, regulated institution, or rated corporate above a threshold)

Two methods translate eligible CRM into capital relief. The **financial collateral simple method** substitutes the collateral's risk weight for the unsecured exposure's risk weight (subject to a 20% floor for most collateral). The **financial collateral comprehensive method** adjusts the exposure for the collateral's market value after applying supervisory or own-estimate haircuts, recognising volatility of both exposure and collateral and any currency or maturity mismatch.

CRM is recognised only if the legal and operational conditions hold. The collateral arrangement must be legally enforceable in all relevant jurisdictions, the bank must have the right to liquidate or retain the collateral on default, and (for financial collateral under the comprehensive method) the bank must mark to market the collateral at least every six months. A pledged asset whose enforcement is uncertain (a foreign-jurisdiction asset under unclear local law, an equity stake subject to political restriction) delivers economic comfort but no capital relief.

### Netting

**Netting** compresses gross exposures into a smaller net exposure by offsetting amounts owed in both directions between the same parties. It does not transfer risk; it eliminates the gross exposure that should never have counted in the first place. The forms most relevant to a bank are:

- **Payment netting**: multiple payments between two parties on the same day in the same currency are combined into a single net payment. Reduces settlement risk
- **Close-out netting**: on a counterparty default, all outstanding transactions under the master agreement are terminated and replaced by a single net obligation in one direction. This is the central function of the **ISDA Master Agreement** for derivatives, the GMRA for repo, and the GMSLA for securities lending
- **Cross-product netting**: extends close-out netting across product types under cross-product master agreements where supported by legal opinion
- **On-balance-sheet netting**: limited recognition under CRR for the netting of loans and deposits with the same counterparty where a legally enforceable netting agreement exists

The economic effect is large. A bank with $10bn gross derivative exposure to a counterparty might have $200m net after enforceable close-out netting. Basel rules permit netting in exposure measurement (and therefore capital) only where the netting agreement is supported by a clean legal opinion in every relevant jurisdiction; see [[../risk_measurement/credit_risk/counterparty_credit_risk/02-counterparty_exposures|counterparty exposures]] for the capital mechanics. The single largest legal-risk exposure for a derivatives desk is a netting opinion that turns out to be wrong in a particular jurisdiction during a default.

### Margining for Non-Cleared Derivatives

For OTC derivatives that are not cleared through a CCP, the post-2008 reforms introduced bilateral margining as a parallel mitigation layer.

The contractual home is the **ISDA Credit Support Annex (CSA)**, which sits under the ISDA Master Agreement. Under the CSA, parties post **variation margin** (VM) daily, reflecting mark-to-market moves, so that the exposure between margin calls is the move over a single day. Since 2017, **initial margin** (IM) has also been required between in-scope counterparties under the global **uncleared margin rules** (UMR), reflecting potential future exposure under a stressed move. IM must be segregated at a third-party custodian; VM transfers title to the receiving party.

In-scope counterparties are determined by aggregate average notional amount of non-cleared derivatives. The thresholds were phased in (Phase 1 captured firms above $3tn in 2016, down to Phase 6 capturing firms above $8bn in 2022), now covering all major financial counterparties and many corporate hedgers. UMR is one of the largest operational changes the derivatives industry has absorbed in the past decade.

The mitigation effect is to constrain the residual exposure on a non-cleared trade to a few days of mark-to-market move, comparable to the position with a CCP. Margining complements but does not replace the basis-risk discipline of the hedging desk: an effective hedge that drifts in basis still loses value, regardless of who is posting collateral.

### Management Actions

The risk portfolio of a bank can be adjusted by monitoring maturing business and adjusting policy for assets accordingly. New business for sectors can be frozen, reduced, or subjected to stricter standards (e.g. increased spread and fees, more collateral, tighter covenants). Emphasis can be placed on booking business in sectors that can be expected to perform counter to the concentration risk — sectors that outperform in different phases of the economic cycle (e.g. consumer staples are usually relatively strong in a downturn).
