---
tags:
  - application/banking/internal-environment/capital-management
  - difficulty/unknown
  - study-status/reviewed
aliases:
---

# Capital Management

## Purpose

Liquidity and capital can easily be confused. The important distinction is that a bank’s liquidity is measured by its holding of funds in assets that are easily available to pay short-term or urgent obligations, compared to capital that is held to absorb potential losses. Both a failure to maintain adequate liquid assets or a big enough loss to the capital base can lead to the failure of a bank.

A bank’s capital position and the measurement of capital position is of utmost importance to ensure a bank remains a going concern. Bank capital can be considered as the funding set aside by the bank to cover expected and unexpected losses. The strategy of the bank is therefore closely linked to its capital position and will determine the composition of the capital base.

The need for capital arises due to credit, market, operational, and other financial and non-financial risks that could lead to financial losses. A bank with an adequate capital base will be able to absorb these losses and remain solvent. These losses are categorised as expected losses and unexpected losses. The calculations for capital to be held for expected losses and unexpected losses are set out in the [Basel regulations](..\..\regulation\international\bis\bis.md) and enforced by national regulators.

Banks’ normal course of business involves exposing themselves to risk of loss due to customer loan defaults as well as other risks. [[02-credit_losses|Credit losses]] will vary from one year to the next and are, unsurprisingly, closely correlated to the economic cycle. The extent of losses will be dictated by the amount of exposure, product type, customer credit quality, and the existence of collateral.

Obviously, it is not possible to know in advance what the exact extent of losses in the next 12 months (or any time period) will be. Banks will estimate the average level of losses they expect to incur over the next budgeting period based on historical experience, any anticipated risks that may emerge, and planned management actions. This is the bank’s expected losses. The level of expected losses dictates the nature of future business. For example, since it can be seen as part of the cost of doing business, expected loss levels will influence:

- The level of future balance sheet expansion and lending levels
- The rate of interest charged to customers.

Banks must also, however, account for unexpected losses. This should be self-evident: it would not be possible to estimate accurately what future losses will be. It is common for actual loss rates to far exceed expected loss rates, especially if historical rates were used to estimate expected losses.

It is for these unexpected losses that banks require a buffer of capital to absorb, and if the bank is to manage itself on a going concern basis, this buffer must be sufficient to absorb losses and still remain above the regulatory minimum. Otherwise, of course, it would no longer be a going concern. This is because a bank that falls even 1 basis point below the regulator’s minimum may suffer a loss of confidence and potentially a run on the bank (as well as the inevitable credit rating downgrade). In most cases, it is the unexpected losses that can lead to the failure of a bank, rather than the expected losses.

Unexpected losses are harder to estimate than expected losses and can arise due to a variety of events, including operational losses. The capital the bank holds therefore needs to cover not only expected losses, but unexpected losses as well. In fact, expected losses should be covered by the spread or profit margin of the products sold for a mature bank. For a detailed treatment of the credit loss distribution, expected losses, unexpected losses, and the Vasicek model underpinning the IRB capital formula, see [Credit Losses](credit_risk\02_airb_capital_modelling\01_introduction\02-credit_losses.md).

Different banks will have different methodologies to determine the size of their unexpected losses and consequently the required size of their capital base. The size of the bank, the risk they are exposed to, and the operating model are all factors that will determine how the bank manages their capital

## Sources

Often capital is spoken of as being “held” or “put aside” by a bank in order to support lending operations, as if it were an asset. Far from being an asset, capital is always shown on the liability side of the balance sheet alongside all the other forms of liabilities the bank has, and as such a form of funding for the bank.

However, unlike the other forms of liabilities it has no fixed interest cost; core capital is not obliged to pay out any form of coupon at any time (as such it has no explicit interest cost). Moreover, because it is perpetual and has no repayment date it is able to absorb losses. Such losses could otherwise threaten a bank’s solvency, so it is easy to see why a sufficient capital base to cover all eventualities is essential for every bank.

### Deposits

For most lending banks, the major source of funding is deposits made by retail and corporate customers.

Retail deposits are a particularly attractive source of funding because:

- Many depositors do not seem particularly sensitive to the rate of interest earned and do not typically switch to other banks to get better rates
- Retail deposits may persist for a number of years, even if they are instant access deposits
- Even in a market stress situation, retail customers do not normally withdraw their deposits due to concern over bank failure if they are protected by a deposit insurance scheme

Savings/deposits may go down during market stress situations as customers need to access excess cash to cover expenses. Institution-specific stresses (e.g. due to reputational damage) may lead to customers withdrawing savings/deposits due to concerns over the bank in question.

Under deposit insurance schemes, banks pay premiums, and in the event of a bank failure, the scheme pays out to meet claims by depositors who have lost their savings as a result of the bank failure. While such schemes reduce the risk of a "run on the bank", they can create a form of "moral hazard" — banks may pursue risky strategies without the market discipline that might be generated by the threat of customers withdrawing their deposits. This "moral hazard" issue could be addressed through risk-based insurance premiums.

### Wholesale Market Funding

Wholesale funding may be used to complement retail funding, particularly in periods when retail funding is limited, because of low interest rates or for some other reason. Wholesale funding sources include, but are not limited to, state funds, foreign deposits, and borrowing from institutional investors.

An important disadvantage of wholesale funding is that the owners of the funds are generally sensitive to changes in the risk profile of the bank. Wholesale funding is therefore vulnerable to being withdrawn in periods when banks face recessions or other stress scenarios, as was the case in 2007, when the "credit crunch" was in fact more appropriately a "liquidity crunch." Wholesale deposits tend to be less "sticky" than retail deposits and also tend to be more expensive.

### Central Bank Funding

Banks may get funding, at least on a temporary basis, through their money market operations with their central bank. It is believed that [[05-central_banks|central banks]] in various countries extended such facilities to help banks through the "liquidity crunch" of 2007, but information about such activities was not made public.

### <mark style="background: #FFF3A3A6;">Shareholder Equity (Tier 1)</mark>

Equity capital must be in the form of CET1 capital, meeting the criteria set out in [[basel_framework|Basel III]]. Given [[basel_framework|Basel III]]'s higher requirements for CET1 capital, and its introduction of capital buffers which must be in the form of CET1 capital, the percentage of funding by equity capital is much higher than it was before the banking crisis of 2007–2008.

Banks may also hold AT1 capital — contingent convertible securities with mandatory conversion to CET1 capital if the issuing bank's CET1 capital ratios fall below a stated trigger level. New entrant banks may find it not practical to issue AT1 capital, at least during their early years.

### <mark style="background: #FFF3A3A6;">Capital Obliged to Be Repaid (Tier 2)</mark>

Tier 2 capital includes debt securities that have a maturity of at least 5 years and that are subordinated to depositors and other creditors of the bank. As long as the bank is a going concern, debt capital cannot be used to absorb losses. However, in the event that a bank fails, its debt capital can be used to absorb losses. Tier 2 capital may therefore be referred to as "gone-concern" capital.

### <mark style="background: #FFF3A3A6;">Preference Shares</mark>

Banks issued preference shares historically prior to the introduction of [[bis|Basel]]. These instruments are preferred to equity on a going concern basis and were historically pari passu to equity on a liquidation basis. Preference shares are generally not recognised under the qualifying regulatory capital under [[basel_framework|Basel III]]. Many banks are phasing out these instruments.

## Classification ([[basel_framework|Basel III]])

The capital structure will consist of three types of capital and the composition will be determined by the factors discussed in this section.

### <mark style="background: #FFF3A3A6;">CET1</mark>

Common Equity Tier 1 (CET1) capital consists in principle of share capital, share premium, and retained earnings attributed as regulatory capital. Certain deductions apply.

### AT1

The features that make a long-dated liability eligible as Additional Tier 1 (AT1) and Tier 2 (T2) are as follows:

- Instruments issued by the bank that meet the criteria for inclusion in Additional Tier 1 capital (and are not included in Common Equity Tier 1)
- Stock surplus (share premium) resulting from the issue of instruments included in Additional Tier 1 capital
- Instruments issued by consolidated subsidiaries of the bank and held by third parties that meet the criteria for inclusion in Additional Tier 1 capital and are not included in Common Equity Tier 1. Note criteria being applied
- Regulatory adjustments applied in the calculation of Additional Tier 1 Capital
- <mark style="background: #FFB86CA6;">Perpetual</mark>
- Coupons are discretionary and non-cumulative
- Are subject to write-off or <mark style="background: #FFB86CA6;">conversion into equity</mark> at the Point of Non-Viability which is determined by the regulator

### T2

- Instruments issued by the bank that meet the criteria for inclusion in Tier 2 capital (and are not included in Tier 1 capital)
- Stock surplus (share premium) resulting from the issue of instruments included in Tier 2 capital
- Instruments issued by consolidated subsidiaries of the bank and held by third parties that meet the criteria for inclusion in Tier 2 capital and are not included in Tier 1 capital
- Certain <mark style="background: #FFB86CA6;">loan loss provisions</mark>
- Regulatory adjustments applied in the calculation of Tier 2 capital. Crucially, they are subject to a **20% per annum amortisation haircut** in the final 5 years before maturity, reducing their recognised capital value as they approach redemption.
- Are for a <mark style="background: #FFB86CA6;">minimum term of 5 years</mark>
- Coupons are compulsory
- Are subject to write-off or <mark style="background: #FFB86CA6;">conversion into equity</mark> at the point of non-viability which is determined by the regulator.

| | Additional Tier I | Tier II |
|---|---|---|
| Tenor | Perpetual | May be dated. Must have minimum 5 years maturity. |
| Subordination | Subordinated to depositors, general creditors and subordinated debt of the bank. | Subordinated to depositors and general creditors of the bank. |
| Distribution | Bank must have full discretion to cancel payments (non-cumulative). No dividend stoppers. Interest step-ups not allowed. | No requirement for deferral / cancellation of payments. Interest step-ups not allowed. |
| Call Features | May be callable by the Issuer only after a minimum of 5 years. With regulatory approval; Cannot create an expectation of call. Expected that early redemption for "unforseen" changes in regulator treatment, tax treatment or potential accounting treatment will be permitted. | May be callable by the issuer only after a minimum of 5 years. With regulatory approval; Cannot create an expectation of call. Expected that early redemption for "unforseen" changes in regulator treatment, tax treatment or potential accounting treatment will be permitted. |
| Going Concern Loss Absorbency | Instruments must have principal loss absorption through either conversion to shares or a write-down mechanism which allocates losses to the instrument, at a trigger point of at least 5.875% (5.125% in the UK) CET1 when the instrument is liability accounted. (Contractual write-off or conversion is also possible at higher levels of CET1). Has following effects: Reduces claim of instrument on liquidation; Reduces the amount re-paid when a call is exercised; Partially or fully reduces coupon / dividend payments on the instruments. | N/A |
| Gone Concern Loss Absorbency | Write-off or conversion to equity at the point of non-viability as determined by the local regulator, either included in contractual terms of the instrument or provided for in statutory framework. | Write-off or conversion to equity at the point of non-viability as determined by the local regulator, either included in contractual terms of the instrument or provided for in statutory framework. |

## Capital Adequacy

For a bank to ensure that it has adequate capital to support its business, it must consider the following:

- External
  - Regulatory requirements
  - Credit rating agency (for example, S&P, Moody’s, Fitch) considerations
  - Equity investor expectations
  - Accounting practices
- Internal
  - [[02-risk_appetite|Risk appetite]] and risk profile
  - Growth and business plans
  - [[02-stress_testing|Stress testing]] scenarios
  - [[01-economic_capital|Economic capital]] requirements
  - Dividend policy
  - Targeted leverage levels

Regulatory requirements will be the primary driver of the bank’s capital structure, involving the consideration of a number of metrics across the regulatory spectrum. The board sets the [[02-risk_appetite|risk appetite]] of the firm. One of the [[02-risk_appetite|risk appetite]] metrics will consider the level of friction the bank wishes to endure before breaching regulatory requirements. Capital in excess of the minimum will be held as a buffer to minimise regulatory friction.

Equity investor considerations around dividend capacity and ROC expectations would also influence the capital mix as it is important to take into account the requirements of investors.

### Regulatory Requirements

These guidelines set out what instruments can be considered as capital as well as how to calculate capital requirements. As these are only guidelines, national regulators can decide how to implement the guidelines and what additions might need to be made, determined by local conditions.

Regulators and society in general require banks to be well capitalised and profitable to reduce risk in the financial system. Well-regulated and strongly capitalised banks are fundamental components of a robust and stable financial system.

The total required capital of the bank will be the Pillar 1 requirement as well as any additions from the [[02-stress_testing|Pillar 2]] requirements. The table below shows the capital requirements of a bank as per the [[basel_framework|Basel III]] guidelines.

| Capital tiers                                             | Total capital requirement (% of RWAs) | CET1 Capital requirement | Tier 1 (CET1 + AT1) Capital requirement | Tier 2 Capital requirement |
| --------------------------------------------------------- | ------------------------------------- | ------------------------ | --------------------------------------- | -------------------------- |
| [[basel_framework\|Basel minimum Regulatory Requirement]] | 8%                                    | 4.5%                     | 6%                                      | 2%                         |
| Capital Conservation Buffer – CCoB                        | 0%–2.5%                               | 100% of CCoB             | 100% of CCoB                            | N/A                        |
| Countercyclical Capital Buffer – CCyB                     | 0%–2.5%                               | 100% of CCyB             | 100% of CCyB                            | N/A                        |
| Systemically Important Banks Add-on                       | 0%–2.5%                               | 100% of add-on           | 100% of add-on                          | N/A                        |
| Pillar 2A Add-on – P2A                                    | 0%–2%                                 | 50%+ of P2A              | 75%+ of P2A                             | Max 25% of P2A             |
| [[02-stress_testing\|Pillar 2B]]                          | Determined via Supervisory Review     | 50% of P2B               | 75% of P2B                              | Max 25% of P2B             |

The composition of the capital base for the bank is very important. The base requirement is that a minimum of 4,5% of the capital requirement needs to be held in Common Equity Tier 1 (CET1) capital. In essence, CET1/RWAs must be greater than 4,5%. An additional 1,5% of the requirement can be held in Additional Tier 1 capital (AT1). The last 2% is allowed to be held in Tier 2 capital. Combined, this is a total of 8% of RWAs and is the minimum amount of capital a bank has to hold. [[basel_framework|Basel III]] also has three capital buffers that are discussed below.

#### Pillar 1: MCR

Pillar 1 uses the risk-weighted assets (RWA) method. Each type of asset the bank holds is assigned a weight and the combined total RWAs multiplied by the [[bis|Basel]] minimum required capital percentage, leads to the minimum required Pillar 1 capital holding. Pillar 1 requirements are determined by considering the credit, market, and operational risks of the bank:

- For credit risk, a bank can apply the standardised approach, foundation internal ratings based (F-IRB) approach, or advanced IRB (A-IRB) approach. For the detailed computation of RWAs under each approach, see [Regulatory Capital](credit_risk\02_airb_capital_modelling\01_introduction\01-regulatory_capital.md). This also includes [[02-counterparty_exposures|counterparty credit risk]] as well.
- For [[05-market_risk|market risk]], the bank can apply the standardised approach or an internal [[07-var_limitations|value at risk]] (VaR) model.
- For operational risk, the basic indicator approach, standardised approach, or advanced measurement approach can be used. With the coming updates to [[basel_framework|Basel III]], the advanced measurement approach will, however, be falling away.

By applying the various [[basel_framework|Basel framework]] capital quantification principles, the total risk-weighted assets (RWA) of the bank is determined. The total required capital for the bank under Pillar 1 is then set at 8% of RWAs.

#### [[02-stress_testing|Pillar 2]]: Additional Capital Requirements

[[02-stress_testing|Pillar 2]], known as the supervisory review and evaluation process, requires the bank to complete a review of their risk profile and apply quantification principles set out in the regulation to determine their risk position and help assign a capital value to this risk position. [[02-stress_testing|Pillar 2]] strongly relates to the ICAAP (Internal Capital Adequacy Assessment Process), where the bank does an analysis of the total capital requirements based on all the identified significant risks of the bank and determines what additional capital amounts need to be held above and beyond the Pillar 1 requirement.

[[02-stress_testing|Pillar 2]] of the [[bis|Basel]] requirements requires a bank to determine their own capital requirement via a review process. This review process looks at the specific risk profile of the bank and identifies areas not necessarily captured by the Pillar 1 requirements. [[02-stress_testing|Pillar 2]] also allows national supervisors / regulators to require banks to hold capital above and beyond what was calculated in Pillar 1. Supervisors should regularly review banks’ capital positions under the guidance of [[02-stress_testing|Pillar 2]] to ensure that they are adequately capitalised. This pillar therefore goes beyond the strict definitions and methodologies of Pillar 1 to ensure banks are adequately capitalised. Many additional risks are considered when looking at [[02-stress_testing|Pillar 2]]. These include risks such as:

- [[01-business_model|Business model]] risk
- Concentration risk
- [[01-irrbb_sources|Interest rate risk in the banking book]]
- Model risk
- Reputational risk
- Legal risk
- Strategic risk
- Sustainability risk.

The above is just a small selection of possible risks. Many other risks can be identified which would constitute the additional risks to be considered under [[02-stress_testing|Pillar 2]]. In many cases, there are emerging risks that have never been present before that banks now need to consider, such as climate change risk or cyber risk.

There are two components to [[02-stress_testing|Pillar 2]] which have different meanings in the UK and South Africa.

##### Pillar 2A

The Pillar 2A requirement will determine what risks have not been identified or fully captured by Pillar 1 and what amount of capital needs to be held to cover these risks. In South Africa, this requirement is specifically set for local market concentration. The capital in Pillar 2A is expected to be met at all times and is usually disclosed publicly – similar to Pillar 1 requirements.

##### [[02-stress_testing|Pillar 2B]] ([[02-stress_testing|Stress Testing]] Buffer)

The [[02-stress_testing|Pillar 2B]] requirement (also known as the bank-specific individual capital requirement (ICR) in South Africa), looks at stressed scenarios for the bank and determines what amount of capital the bank needs to hold to absorb any losses from such scenarios. This requirement can also contain capital to cover any specific risks that might have been raised by the supervisor or other ad-hoc risks. 

Banks conduct their own [[02-stress_testing|stress testing]] to determine their additional capital requirements above and beyond the minimum. Both CCoB and CCyB serve to protect the capital base in such stressed scenarios. The CCoB and CCyB numbers are, however, only minimum requirements. If a bank’s own [[02-stress_testing|stress testing]] leads them to determine that they need to hold an amount above the sum of CCoB and CCyB, they should do so, as this would be the most prudent approach. Some banks are so prudent they simply add the stress test buffer to the CCoB and the CCyB.

In South Africa, the [[02-stress_testing|Pillar 2B]] contains both elements of the total [[02-stress_testing|Pillar 2]] requirements of the UK. [[02-stress_testing|Pillar 2B]] capital is generally not disclosed publicly. [[02-stress_testing|Pillar 2B]] does not include requirements for systemically important banks which are set separately.

#### Pillar 3: Disclosures

Pillar 3 (market discipline) requires banks to disclose more information about the way they allocate capital and the risks they take. The idea is that banks will be subjected to added pressure to make sound [[01-risk_management|risk management]] decisions if shareholders and potential shareholders have more information about those decisions.

Regulatory disclosures are likely to be different in form from accounting disclosures and need not be made in annual reports. It is largely left to the bank to choose disclosures that are material and relevant. Among the items that banks should disclose are:

1. The entities in the banking group to which [[basel_2|Basel II]] is applied and adjustments made for entities to which it is not applied
2. The terms and conditions of the main features of all capital instruments
3. A list of the instruments constituting Tier 1 capital and the amount of capital provided by each item
4. The total amount of Additional Tier 1 and Tier 2 capital
5. Capital requirements for credit, market, and operational risk
6. Other general information on the risks to which a bank is exposed and the assessment methods used by the bank for different categories of risk
7. The structure of the [[01-risk_management|risk management]] function and how it operates.

For credit risk, this means banks should adequately disclose the [[04-risk_measurement|risk measurement]] techniques used and provide detailed explanations on the entire [[01-risk_management|risk management]] process for credit risk. Disclosures of the existing credit exposures are also required, in various summarised formats (e.g. by asset class).

#### Capital Conservation Buffer (CCoB)

Under [[basel_framework|Basel III]], banks also now need to hold an additional 2,5% of RWAs in CET1 which serves as a capital conservation buffer. This brings the total minimum required CET1 of a bank to 7% (2,5% + 4,5% from Pillar 1). This buffer serves as an additional layer of protection against adverse events under a stressed scenario. In the pandemic, regulators reduced the CCoB to 0% to allow for a reduction in the capital requirements.

#### Countercyclical Capital Buffer (CCyB)

The countercyclical buffer requires a bank to hold between 0% and 2,5% of additional CET1. This number will be set by the national regulator and works to counteract any cyclical changes expected in the economy. It is generally set at 0% and increased as the economy is perceived to “overheat” when household and corporate debt to GDP increases to levels considered to be unsustainable.

#### Systemically Important Risk Buffer

The last type of capital buffer is the systemically important banks’ buffer ([[g_sibs|G-SIBs]] and D-SIBs). This requirement only applies to large banks which pose a systemic risk as determined by the regulator. The regulator can require a bank to hold up to an additional 3% of RWAs in CET1 if it is determined to be a systemically important bank. For [[g_sibs|G-SIBs]], amounts are set by the [[fsb|FSB]] in consultation with the [[bis|BCBS]] — currently at 2%, 1.5%, and 1% of total RWAs of selected banks. In the UK, amounts are set by the [[pra|PRA]] — currently at 2%, 1.5%, and 1% for ring-fenced banks within the largest UK banks.

In South Africa, a D-SIB buffer of up to 2,5% is set by the [[pa|Prudential Authority]]. The first 1% of the specified D-SIB capital requirement, up to a maximum of 1% of a bank’s risk-weighted exposures, must be fully met by CET 1 capital and reserve funds.

Any additional requirement, up to the first 1,5% of risk-weighted exposures may be met by Tier 1 capital and reserve funds. Any additional requirement to the aforementioned requirement, up to 2,5% of risk-weighted exposures, may be met with total capital and reserve funds.

#### [[tlac|TLAC]]

Over and above the capital requirements outlined in the [[basel_framework|Basel framework]], the [[fsb|Financial Stability Board]] has also introduced a term sheet containing a separate capital structure over and above [[bis|Basel]] prescribed minimums. The [[fsb|Financial Stability Board]] is an international body that makes recommendations about, and monitors, the global financial system. This structure is applicable to [[g_sibs|G-SIBS]] ([[g_sibs|Global Systemically Important Banks]]) only, but some authorities are considering its application potentially for D-SIBS (Domestic Systemically Important Banks) as well. The framework is referred to as [[tlac|TLAC]] or total loss absorbing capacity. For the full regulatory detail on [[tlac|TLAC]], see [TLAC Principles and Term Sheet](..\..\regulation\international\fsb\tlac.md).

**Purpose — the "too big to fail" problem.** The GFC exposed a brutal dilemma: when a G-SIB (Global Systemically Important Bank) neared failure, regulators faced two bad options — let it collapse in a disorderly way (systemic contagion) or bail it out with taxpayer money (moral hazard). They almost always chose the bailout. TLAC was designed to make a _third option_ viable: **orderly resolution without public funds**. The mechanism is bail-in — creditors absorb losses and are converted into equity, the bank is recapitalized, and it emerges from resolution still able to perform its critical economic functions.

**It's not just capital.** This is the key distinction. Basel III capital (CET1, AT1, Tier 2) covers loss absorption on a going-concern and gone-concern basis. TLAC goes further: it must also cover _recapitalization_ needs post-resolution. To achieve that scale, eligible instruments include not only regulatory capital but also qualifying **bail-in-able senior unsecured debt** — instruments that can be written down or converted in resolution. Calling it purely a "capital requirement" misses this debt component.

The minimum TLAC requirement is set as the _higher_ of:

- **16% of Risk-Weighted Assets** (rising to 18% from 2022), and
- **6% of the leverage ratio exposure/denominator**  (rising to 6.75% from 2022)

These sit _below_ the combined buffer requirements (capital conservation buffer + G-SIB surcharge), which must be held on top. So a G-SIB's total loss-absorbing stack is: TLAC minimum + capital buffers.

Eligible liabilities must be subordinated to operational liabilities, have a minimum remaining maturity of one year, and must not be insured or subject to netting — conditions designed to ensure they are genuinely bail-in-able without touching depositors or counterparties.

The EU parallel is **MREL** (Minimum Requirement for own funds and Eligible Liabilities) under the BRRD, which applies to all EU banks, not just G-SIBs, but with institution-specific calibration.

#### [[mrel|MREL]]

[[mrel|Minimum requirement for own funds]] and eligible liabilities ([[mrel|MREL]]) is a European standard introduced in 2016 that is conceptually similar to [[tlac|TLAC]] in that its implementation is supposed to ensure that banks have sufficient capacity to absorb losses and improve their ability to recapitalise in times of stress. While [[tlac|TLAC]] is based on percentages of RWA and leverage ratio (i.e. focusing on measures associated with Pillar 1 under [[bis|Basel]]), [[mrel|MREL]] is equal to the loss-absorption amount plus a recapitalisation amount. These components are made up of:

- **Loss-absorption amount**: The higher of the sum of Pillar 1 and Pillar 2A risk-weighted capital requirements, leverage requirement, or the [[basel_1|Basel I]] capital floor. This is intended to reflect the fact that a bank post-resolution would have to comply with these capital requirements.
- **Recapitalisation amount**: A percentage from 0%–100% which is determined by local regulators. This percentage is larger for larger banks which are more systemically important.

The intent of [[mrel|MREL]] is that it broadly aligns to [[tlac|TLAC]] for [[g_sibs|G-SIBs]] and allows for the potential for additional capital requirements (for the purpose of recapitalisation) for smaller non-SIBs.

#### Leverage Ratio

The leverage ratio limit is a [[basel_framework|Basel III]] requirement. It has been implemented as a [[02-stress_testing|Pillar 2]] measure from January 2016. The leverage ratio measures a bank’s Tier 1 capital relative to its total assets. With a higher ratio a bank is able to better withstand shocks to its balance sheet. The higher the ratio, the more coverage there is for its assets in case of emergencies. This ratio therefore serves as an additional risk measure to protect the solvency of a bank.

In South Africa, the [[pa|Prudential Authority]] has applied a minimum 4% (3% in the [[bis|Basel]] text) ratio limit, and the numerator is given by the Tier 1 capital amount.

The leverage ratio is defined as T1 capital divided by a total exposure measure. The simplest form is given by:

**Leverage ratio = Tier 1 capital / Funded assets**

The exposure measure is the sum of:

- On-balance-sheet exposures
- Derivative exposures
- Securities financing exposures (for example, repo)
- Off-balance-sheet exposures.

### Rating Agency Considerations

A rating agency will consider drivers including: business profitability, current and future levels of growth, dividend policy, access to bank financing, issuance capability in the capital markets, implicit support from government or a foreign parent, and the price the bank has to pay to raise long-term funding.

In proceeding with issuance of an AT1 or T2 hybrid capital instrument, the capital planning process will consider the treatment of the instrument by the international credit rating agencies (for example, S&P, Moody’s, Fitch), which will look at the above-mentioned factors. Ideally, the instruments issued will be eligible as capital, therefore strengthening the capital base to the benefit of the bank’s final rating from the agencies. S&P, for instance, issue guidelines for eligibility for their Risk Adjusted Capital (RAC) ratio.

### Equity Investment Analyst Considerations

Optimal capital structures are also determined by investment analyst considerations. Unlike regulatory considerations, equity analysts might identify opportunities that require a higher level of [[02-risk_appetite|risk appetite]]. As a consequence, more focus might be placed on the early payment of dividends, potential special dividends, and growth opportunities to utilise excess capital. From the bank’s point of view, it is important to always first ensure solvency both on a going concern and in stressed scenarios. The capital management team can then consider a range of options to address the growth and dividend considerations.

### Capital Need of Peers

Banks do not only ensure that their level of capital is sufficient to meet regulatory requirements; they also tend to compare their capital ratios with their peers. This ensures that they do not appear to have too little capital relative to their counterparts. For example, a bank with a low CET1 ratio relative to its peers (even well above the regulatory minimum) may be perceived to be of higher risk.

In South Africa, the four largest banks (ABG, FSR, NED, SBK) maintained total capital ratios of approximately 14–17% from 2018 to 2020, with CET1 comprising the largest portion.

### Expected [[02-credit_losses|Credit Losses]]

As changes in provisions are included in impairments in banks’ income statements, they reduce / increase banks’ retained earnings and capital resources when provisions (ECL as per [[ifrs9_standard|IFRS 9]] requirements) increase / reduce year on year.

For banks under the standardised approach for credit risk, accounting provisions are split into general (GP) and specific provisions (SP). GPs may be included in Tier 2 capital up to a maximum of 1,25% of the credit RWAs. SPs may not be included in Tier 2 capital but are used to reduce the asset exposure before applying the RWAs. The impact on CET1 capital therefore depends on the size of the accounting provisions (ECL) and the split between SP and GP. (SP and GP definitions are prescribed by local regulators.)

For banks under the IRB approach, there is no split between GP and SP. Where ECL is higher than regulatory expected losses, the difference may be added to Tier 2 capital up to a maximum of 0,6% of credit RWAs (measured under IRB). In the case where regulatory EL is higher than ECL, the difference is subtracted from the regulatory capital.

### Economic Outlook

Provisions for expected [[02-credit_losses|credit losses]] are heavily dependent on GDP forecasts. Banks tend to build forward-looking models with GDP as a key factor. When GDP growths are expected to decrease, PDs and LGDs are usually expected to increase. More loans are also expected to migrate to lower stages (from stage 1 to 2/3) with higher ECL percentages. When economies therefore go from expected growth to expected recessionary periods, as happened in 2020 due to Covid-19, there is likely to be a substantial rise in provisions leading to a reduction in capital adequacy. This may cause banks to dip into their capital buffers, but they must not go below their total capital requirements.

### National Regulator Actions

[[05-central_banks|Central banks]]’ actions and their impact on banks’ capital levels need to be considered, especially during times of recessionary periods. [[05-central_banks|Central banks]] may decrease banks’ capital requirements, for example, in South Africa the [[pa|Prudential Authority]] decreased the Pillar 2A capital requirement from 1% to 0% in 2020.

[[05-central_banks|Central banks]] may also influence the way in which banks calculate their ECLs. For example, in South Africa the [[pa|Prudential Authority]] issued a directive whereby loans with payment holidays may be held in stage 1 ([[ifrs9_standard|IFRS 9]] classification for a performing loan) even if the customer did not pay for a few months. These loans had to be in good standing before the payment holiday and expected to meet their payments after the payment holiday period.

Another example is from 2020 in the EU: To prevent a large fall in banks’ capital ratios that might have made them reluctant to support new lending, banks were allowed to phase in the impact of an increase in provisions for expected [[02-credit_losses|credit losses]]. This was, however, not the case in South Africa where the increase in ECL was recognised in full.

### Internal Capital Requirements

Another form of capital is [[01-economic_capital|economic capital]]. [[01-economic_capital|Economic capital]] is internally calculated by the bank and is a measure of the bank’s total risk as they see it, without reference to regulatory prescriptions. If a bank's [[01-economic_capital|economic capital]] was less than its regulatory capital, it still had to hold the larger amount of its regulatory capital.

## Capital Allocation

The structure of the balance sheet and the bank [[01-business_model|business model]] will thus dictate how capital is managed. A rapidly expanding balance sheet or risky strategy from a bank will require more capital to be held to ensure the bank can continue as a going concern and remains viable. When setting capital policies, strategy, and requirements it is imperative to keep these two considerations in mind.

Generally, the simplest and most transparent capital model is to consider that the complete capital base is used as part of a [[01-business_model|business model]] in which it represents equity backing for borrowed funds, which are invested in assets.

In its simplest form, the bank’s capital should not be exposed to risk. Notionally, capital could be allocated to instantly liquid low risk assets so that it is not in danger of erosion. Capital can therefore easily be retrieved if needed, either to cover losses or to fund further expansion and
investment.

The only assets that fit this category, being relatively low risk, is a deposit at the central bank or an investment in sovereign bonds of the same currency. All other investments normally carry an additional element of credit and/or liquidity risk and may be considered unsuitable assets in which to invest the bank’s capital.

### Endowment Benefit

An important aspect of the capital holdings of a bank, is how to assign any benefit that arises from it. Holding capital can lead to benefits arising that need to be accounted for. The treasury of the bank acts as the “bank to the bank”, that is, to provide funding to all assets and pay for all liabilities. From an accounting perspective, the cost of funding of capital is nil.

An endowment benefit therefore arises as no expense is incurred for this funding. To ensure that business lines in a bank group do not unduly benefit from such capital structures, the central treasury charges a funding cost on all assets and pays a funding cost to all liabilities, including capital. This means that the central treasury may accrue the endowment benefit.

The assets funded by the capital base itself should not be expected to generate a return for the business lines. Where it does, for example, the coupon return from a holding of government bonds, the benefit should accrue to a central book or ALCO book, and not to any business line. Neither is it allocated on a pro-rata basis to the business lines, otherwise the calculation of shareholder value added by the businesses will be skewed. Some banks may, however, not wish to have the endowment benefit disclosed on a central basis and therefore financial disclosure of businesses in the bank will often include an attribution of the endowment benefit as it held as a result of the business undertaken by the bank. Financial disclosures therefore provide limited insight on shareholder value generation in banks. This led to banks responding with risk adjusted performance measures to support their financial disclosures.

The business lines are assumed to utilise matched funding instruments to fund their operations. Certain banks also charge a capital risk premium which will also accrue to the ALCO book. Views vary on the treatment of this endowment benefit accrued to the ALCO book. Some banks keep the benefit in the ALCO book and implement an economic profit type of management accounting framework, while others allocate some or all of the benefit to incentivise business, hence there is no cost to allocate. It is preferable to manage costs and benefits that cannot be controlled by the business areas on a central basis.

### Business Case

Business units themselves have to submit business cases for their capital demands based on RWAs and [[01-economic_capital|economic capital]]. This is an essential part of allocating capital within a group to ensure that capital is adequately distributed. The business cases from the different business units will contain metrics such as return on capital, net generation of equity, and economic profit to justify their allocation needs. Then the balance sheet management department sets targets for risk-weighted assets and capital usage as part of the budget forecast and capital allocation, and will drill down to each business unit to estimate the optimal allocation.

The bank’s target return on equity, sets the hurdle rate for the business or the legal entities in the group. Senior management then calculates these hurdles for each of the business lines, which benefit indirectly from the existence of the capital base. This is done on a risk-adjusted basis but can include strategic objectives as well.

This hurdle rate can be a minimum for all the businesses (which is very unlikely as the returns per line of business vary greatly, for example, between asset and liability lines), or it can be modified to suit the differing requirements of each business. It is imperative to note how important it is for the bank’s return on capital (ROC) target to be set at a board level, reflecting the needs of the shareholder and other stakeholders and thereby the “cost” of that equity.

In some cases, a portion of the capital base is allocated for use as “working capital”, for example, in a start-up situation to cover cash requirements such as rental and salary expenses. In this case, the amount to be allocated should be identified in advance and once the business has declared a profit, the process will be revisited. Any excess would be returned by way ofdividend, or alternatively profit may be retained for further investment, or further capital may be injected.

The treatment of the capital base from an accounting perspective is therefore dictated by the bank’s own structure and strategy. Regardless of how capital is allocated, the allocation should not skew the financial results of the bank and artificially alter disclosed value added. Capital allocations are used as a [[01-risk_management|risk management]] and incentive tool and benefits arising from it should be managed accordingly.

### Risk-based Capital

Allocation of risk-based capital is not only about risk but must also be linked to potential rewards. In order to increase returns, the bank will need to take on additional risk, and it is necessary to optimise risk capital allocation to the portfolio in seeking higher profitability. Banker and trader pay must be linked not only to returns, but also to the amount of risk-based capital used in its generation, as higher risk positions attract higher regulatory and [[01-economic_capital|economic capital]].

Capital must be allocated with a view towards sustainability. Business plans must anticipate ongoing capital needs, costs, and availability, without which growth and continued competitiveness will not be attainable. Consideration must be given to the time value of money, tax consequences, and varying rates when assessing returns.

In allocating capital, banks can perform a comparison between the [[01-economic_capital|economic capital]] and regulatory capital charges applicable to different areas of their business. In doing so, they can identify those areas of their business which attract high amounts of regulatory capital, but low amounts of [[01-economic_capital|economic capital]] — and those which attract low amounts of regulatory capital, but high amounts of [[01-economic_capital|economic capital]]. This type of analysis will help the bank with strategic business planning and in setting growth and performance targets for the future.

### Hypothetical Example: Vanilla Commercial Bank

To illustrate the considerations involved from a first-principles basis, an assumed example of a UK commercial bank that is being set up from scratch, with an inherited portfolio, is considered. What would be the primary factors driving the capital planning process? The balance sheet risk-weighted assets (RWA) breakdown is as follows:

| Segment | RWA (£m) |
|---|---|
| Mid-corp | 2 841 |
| SME | 6 984 |
| Retail | 3 181 |

The main factors a review would consider include: profitability, asset mix (for example, whether there is a concentration in assets); advanced-versus foundation-IRB being applied; industry comparisons by asset class; [[02-stress_testing|Pillar 2]] impacts; stress buffers required; and regulatory requirements. With a total balance sheet RWA of just over GBP 13 billion, the bank is below 1% of UK GDP in size, so the countercyclical, G-SIFI, and ring-fence buffers do not apply. (The [[pa|Prudential Authority]] applies its own criteria regarding systemic importance when identifying D-SIBs. None of the South African banks are G-SIFI but an equivalent ZAR 13 billion would be a small bank with resulting high regulatory requirements.)

Under Pillar 1, a total capital amount of 10,5% has to be held before [[02-stress_testing|Pillar 2]] requirements. The bank can then complete its own supervisory review under the [[02-stress_testing|Pillar 2]] requirements and in this example, this could lead to an additional 4,5% over and above the 10,5% regulatory minimum. This would argue for a capital structure of at least 15%, which the bank now has to decide on how to achieve.

As this is a fairly small portfolio, the individual capital guidance received from the regulator will more likely impose a higher requirement. Two plausible scenarios are considered. The first is Scenario 1, the all-equity scenario, while Scenario 2 describes an equity plus other capital structure.

The all-equity scenario presents the following features:

- It is the most robust form from a regulatory perspective
- It may result in an incremental rating benefit
- As the most expensive structure, it is least efficient from a shareholder return perspective
- Compared to the equity plus other capital format, there is a substantial decrease in ROC.

The equity plus other capital liability structure has the following features:

- It is a more efficient capital structure
- Ultimately, it remains subject to national regulatory approval
- The rating agency position towards this structure may be neutral to negative
- The T2 issuance would of course be subject to investor demand for this paper
- The structure allows for further gearing / leverage of the capital base. The level of leverage is restricted under [[basel_framework|Basel III]] and, in particular, in South Africa.