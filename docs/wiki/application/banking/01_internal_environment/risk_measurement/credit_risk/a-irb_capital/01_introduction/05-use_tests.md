---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/introduction/use-tests
  - difficulty/unknown
  - study-status/new
aliases:
---
# Use Tests

The [[bis|Basel]] Use Test ([[crr|CRR]] Article 144.1(b)) requires that internal models are primarily built and deployed for [[01-risk_management|risk management]] and decision-making purposes, not solely for the calculation of Risk-Weighted Assets (RWAs).

"*Internal ratings and default and loss estimates used in the calculation of own funds requirements and associated systems and processes shail play an essential role in the [[01-risk_management|risk management]] and decision-making process, and in the credit approval. Internal capital allocation and corporate governance functions of the institution;*"

This means they must serve as the basis of decisions made concerning, for example, risk, limits, pricing, provisioning, and [[03-capital_management|capital management]], i.e. they must not be simply for regulatory risk capital calculations.

While no prescriptive list of applications exists—since these depend on each institution’s [[01-business_model|business model]] and context—the IRB model’s risk parameters (PD, LGD, and EAD) are widely used and well-embedded across the Bank’s core [[01-risk_management|risk management]], capital allocation, and governance processes.

## Minimum Usage Requirements

To use the IRB approach, a bank must:

- Define a risk grading methodology based on an assessment horizon reflected in the bank’s rating philosophy (shorter or longer term).
- Maintain at least seven borrower grades for non-defaulted exposures, and one for those in default.
- Assign ratings to all borrowers.
- Review ratings annually.
- Review the model annually.
- Stress test the rating system under adverse economic and market conditions.
- Document the rating system with clear definitions and criteria to enable the replication of ratings by auditors or other independent parties.
- Provide adequate disclosure and data and demonstrate the model’s use over 3 years.
- Obtain approval from national supervisors

### National Usage Requirements

As mentioned, [[bis|Basel]] offers requirements that must be met in order for banks to use the IRBA. One of these requirements is supervisory approval. Supervisors may, in addition to the [[bis|Basel]] requirements, outline further requirements to be met by banks in their jurisdiction.

The [[pa|Prudential Authority]], under the [[sarb|South African Reserve Bank]] ([[sarb|SARB]]), requires additional governance requirements when the IRBA is used, such as:

- The board of directors and senior management must approve the bank’s rating and [[04-risk_measurement|risk measurement]] processes.
- Governance processes and models’ compliance to regulatory requirements must be selfassessed annually by the board.
- Completion of self-assessment templates where banks must qualitatively and quantitatively assess their models.

The [[fca|FCA]], in the United Kingdom, also applies further restrictions. For example:

- The credit risk control unit that manages the IRB models and related processes should be independent and unbiased.
- Internal outsourcing (within a group) of the above is allowed only under specific circumstances.
- Accuracy of the rating systems must be tested, with respect to specific guidelines.
- The “use test” is expanded and more detailed requirements are provided.

Supervisors often seek to provide more clarity and detail on the [[bis|Basel]] requirements when outlining their own requirements, and generally provide more measurable requirements. These requirements will also align more closely with the [[03-economic_envrionment|economic environment]] and structure within the jurisdiction.

## Applications

| Area of Application | Description of Use |
|-|-|
|Allocation of Credit Decisioning Authority | Not applicable to retail portfolios.|
|Profitability and Performance Management | Return on RWA (RoRWA) and Return on Tangible Equity (ROTE) are reported and targeted. IRB model outputs support acquisition strategy, planning, investment valuation, marketing, and credit strategies. Inputs such as RWA and ECL feed into economic value and return on equity analyses. Existing customer management strategies (Balance Transfer, Proactive Credit Line Increase/Decrease, Account Closure) leverage RWA movements from prior year test/control populations for cost-benefit analysis.|
|Acquisitions and Divestments|Used in the for potential partnership renewals, portfolio acquisitions, and new partnership assessments. ROTE inputs include RWA and ECL forecasts.|
|Credit [[00_underwriting|Underwriting]] and Limit Setting|Modern ML-based [[00_underwriting|underwriting]] and ECM strategies are used; however, alignment with IRB default definitions and key risk drivers is maintained and will continue going forward.|
|Accounting ([[ifrs9_standard|IFRS 9]] Impairment)|Point-in-Time (PiT) models can feed [[ifrs9_standard|IFRS 9]] models, ensuring alignment between regulatory and accounting measures.|
|Credit Risk Reporting|Risk profiles for front-book and back-book exposures include balance-weighted PiT PDs derived from IRB models.|
|Risk Appetite Framework|IRB-derived PD, LGD, and EAD parameters are integral to the Bank’s [[02-risk_appetite|risk appetite]] and capital planning processes. RWAs, derived from these parameters, act as proxies for portfolio risk intensity and are embedded in key business metrics such as RoRWA and ROTE. These inform strategic decisions across acquisitions, investment, and credit line management.|
|Collections, Recoveries, and Restructuring|PiT LGD models are being evaluated for use in recovery strategies, including forward-flow debt sale decisions.|
|Pillar 2 Capital and [[02-stress_testing|Stress Testing]] |IRB parameter values feed Pillar 2A capital approaches (e.g., [[06-economic_capital|Economic Capital]]). [[02-stress_testing|Stress testing]] incorporates granular RWA movements and their PD/EAD/LGD drivers under adverse scenarios.|
|Internal Audit Planning |Model outputs may inform prioritization of audit focus areas based on portfolio risk intensity.|
|Risk-Adjusted Remuneration | Bonuses and salaries can be informed by the level of capital available and possible future performance |
