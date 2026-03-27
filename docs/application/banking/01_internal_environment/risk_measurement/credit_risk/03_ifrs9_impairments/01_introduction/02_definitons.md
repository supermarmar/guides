# Definitions

## Gross Carrying Amount

The gross carrying amount of a financial asset under [[ifrs9_standard|IFRS 9]] represents its original or amortized cost, before any adjustments for impairment losses (i.e., loss allowances). It reflects the contractual amounts due from the borrower and excludes any deductions for expected [[02-credit_losses|credit losses]] ([[ifrs9_standard|IFRS9]] §5.1.1).

> *Example: A bank issues a loan of £100,000 with £500 in legal fees at 10% interest. If the loan is measured at amortised cost, the bank records an initial gross carrying amount of £100,500.*

The gross carrying amount includes:

- Principal Outstanding: The unpaid balance of the loan or credit facility.
- Accrued Interest: Any interest income that has been earned but not yet received.
- Transaction Costs (for amortized cost assets): Costs directly attributable to issuing or acquiring the financial asset.
- Amortization: Adjustments made due to the effective interest rate (EIR) method.

## Net Carrying Amount

The net carrying amount (often referred to simply as amortized cost) is the value of a financial asset after adjusting for repayments, amortization of premiums/discounts, and the Expected Credit Loss (ECL) allowance ([[ifrs9_standard|IFRS9]] §5.2.2).

$\text{Net Carrying Amount} = \text{Gross Carrying Amount} - \text{ECL}$

> *Example: A retail customer borrows £100,000 from the bank, plus 500 in legal fees. After 6 months, it owes the bank £93,200. The bank plans to hold the loan to collect outstanding principal + interest, so it's measured at amortised cost. The bank applies ECL (£2,000) to reduce the net value of the loan on the balance sheet (£91,200).*

Financial assets are generally presented on the "asset side" at their net carrying amount (Amortized Cost). This means the gross carrying amount is reduced by the ECL allowance to reflect the amount the entity actually expects to collect. The allowance is not typically presented as a "provision" on the liability side for existing assets. However, for off-balance sheet exposures (such as undrawn loan commitments or financial guarantees), the estimated ECL is presented as a provision (liability) because there is no recognized asset to reduce.

Changes in the ECL (e.g., new impairments or reversals) are recognized as impairment charges in the income statement. (⬆️ECL → ⬆️Loss Provision → ⬇️Assets and ⬆️ECL → Impairment Loss → ⬇️Income → ⬇️Retained Earnings → ⬇️Equity)

## Impairments

Impairment can be described generally as when an exposure is judged by management to have deteriorated so there is no longer a reasonable expectation as to the collection of the full amount as scheduled. In other words, there has not been a default by definition, but a default is very likely or almost certain given the increased credit risk.

Impairments cannot be technically recognised as defaults yet, but should not be treated as performing owing to the increased likelihood of default. A performing asset is not assumed to be likely to default, so capital is primarily held in case of a loss, expected or unexpected, with provisions held being far less in most cases. An impaired asset, however, is very likely to default (almost certain in many cases), so an amount needs to be set aside, in the form of provisions, to prepare for this loss.

### SICR

The concept of a Significant Increase in Credit Risk (SICR) is a critical component of the impairment model. It requires financial institutions to assess whether the credit risk of a financial asset has significantly increased since its initial recognition. If there is a SICR, the asset transitions from Stage 1 to Stage 2 in the Expected Credit Loss (ECL) framework. This increases the ECL since we are now using a lifetime PD and EAD.

> *At each reporting date, the bank is required to assess whether the credit risk of a loan has increased significantly compared to its risk at initial recognition. Let’s say a bank issued a 5-year loan to a mid-sized logistics company in 2022. At the time of origination, the borrower had a healthy balance sheet, steady cash flow, and an external credit rating equivalent to BBB, reflecting a low probability of default. Now, in 2025, during a new reporting cycle, the bank reassesses the risk of default over the remaining life of the loan. It notices that the borrower has experienced a significant drop in revenue, is taking longer to pay other creditors, and is on credit watch for a potential downgrade. Although the actual ECL amount hasn't changed drastically yet, the risk of default occurring over the life of the loan has materially increased when compared to 2022. Therefore, this loan would move from Stage 1 to Stage 2, and the bank would now recognise lifetime expected [[02-credit_losses|credit losses]] instead of just 12-month ECLs. This results in a higher loss allowance and an impairment loss on the income statement, even if actual cash shortfalls haven't occurred yet.*

### SICR Triggers

Banks should disclose impairment triggers to supervisors. Banks can analyse several triggers for borrower deterioration to determine whether an asset is impaired:

- Macro-economic deterioration
  - Deterioration of national or local economic conditions relevant to the asset class
  - Reduction in GDP
  - Increased unemployment rate
  - Reduced property prices for mortgages
  - Industry (or sector) declines.
- Company deterioration
  - Borrower requests for forbearance
  - Breach of contract or covenants
  - Decline in credit rating
  - Debt service capacity reduction
  - Reduced financial performance
  - Issues with cashflow
  - Reduced net worth
  - Decrease in turnover
  - Loss of customers or market share
  - Diversion of cashflows from earning assets to support non-earning assets
  - Poor prospects of the guarantors
  - Poor collateral quality or reduced value thereof
  - Increased country risks.
- Mortgage portfolio deterioration
  - Decrease in rents received
  - Absence of refinancing options
- Retail portfolio deterioration
  - Early delinquency (e.g. one payment in arrears)
  - Continual high utilisation of facilities
  - Steady increase in total debt for the client
  - Income less than total debt repayments
  - Occurrence of risk events, such as a deceased estate, fraud, abscondence, insurance shortfall, or some total loss event experienced (e.g. vehicle theft for a motor vehicle loan).

## Definition of Default (DoD)

[[ifrs9_standard|IFRS 9]] statest that when definining default for the purposes of determining the risk of a defualt occuring, an entity shall apply a default defintion that is consistent with the definition used for internal credit [[01-risk_management|risk management]] purposes. However there is a rebuttable presumption that default does not occur later than when a financial assete is 90 daas past due unless an entity has reasonable and supportable information to demonstrate that a more lagging default criterion is more appropriate.

The DoD for impairment models should therefore be aligned to the IRB model DoD where such models exist.

### Days Past Due (DPD)

Banks commonly specified three payments (or 90 DPD) in arrears as a pragmatic point of ‘default’ [B5.5.37](a), long before the introduction of the [[basel_2|Basel II]] Capital Accords. That said, this threshold can generally range between 30–180 days based on managerial discretion and some analysis.

### Return to Default

When calibrating PDs, accounts that redefault (default after curing) and cure (recover from default) require special treatment to ensure accurate modeling of credit risk dynamics. These events introduce complexities because they alter the time-to-default patterns and can influence the term structure of PDs.

Ignoring redefaults may underestimate the default probabilities for certain risk segments. Overlooking cures may lead to overestimation of default probabilities.

Include key states in the credit lifecycle.

- Performing: Accounts with no arrears.
- Curing: Accounts that have recovered from default.
- Defaulted: Accounts in default.
- Redefaulting: Cured accounts that default again.

When preparing the training dataset for PIT PD calibration:

- Separate Redefault Events: Treat redefault events as distinct observations to reflect the elevated risk of these accounts.
- Include Cure Behavior: Incorporate cured accounts into the dataset, showing their risk of redefault or returning to performing status.
- Track Time Since Cure: Include "time since cure" as a feature, as the likelihood of redefault often decreases the longer an account remains cured.

## Cure

[[ifrs9_standard|IFRS 9]] is not prescriptive in terms of defining when an account has cured [5.5.7](a). Hence, a default flag can be created under the following alternatives of cure.

- Instant Cure: An account returns to performing immediately after the cause of default is removed.
- Probabtion Period: This is used when an account needs to wait for a certain amount of time (e.g. 6m) before returning to performing. It reduces the risk of multiple defaults.

## Write Offs


### PWOR

Post Write-Off Recoveries refer to the collections or repayments a bank manages to recover from borrowers after their loans have been written off as bad debts. In accounting terms, a write-off occurs when the bank deems that a loan is unlikely to be repaid and removes it from the active accounts receivable or loan book. However, even after a write-off, the bank can continue pursuing recovery actions through legal means, collection agencies, or other strategies.

A loan is written off when the bank believes there is minimal likelihood of full repayment based on its internal policies and regulations (e.g., after a certain period of nonpayment or legal default). The loan balance is removed from the bank's financial statements as an asset. Any recoveries after the write-off are recorded as recovery income in the bank’s income statement, not as a reversal of the write-off.

### Write Off Rule

If banks are recovering a significant portion of bad debts post write-off, it raises questions about the effectiveness and timing of their write-off policy. If a bank writes off loans too early (e.g., before fully exhausting all reasonable collection efforts), it might recover more post write-off. This could indicate overly conservative policies or inefficiencies in pre-write-off collection strategies. This leads to higher than expected LGWs which increases the ECL.

If post-write-off recoveries are consistently high, the bank may need to adjust its write-off criteria to better align with the actual recovery potential. 

## EIR

A component of the ECL is the effective interest rate (EIR), which is the rate that will discount all expected future cashflows over an account’s life to the gross carrying amount of that account. The calculation of EIR is done to ensure that banks recognise interest revenue / expenses and fees on an account in a similar consistent manner. The EIR is the rate that should be used when discounting in the ECL calculation. The EIR is the internal rate of return (IRR) on the expected future cash flows of a financial instrument over its life, accounting for:

- **Contractual Interest Rate**: The nominal interest rate stated in the loan agreement.
- **Transaction Costs**: Fees directly attributable to the acquisition or issuance of the financial instrument (e.g., initiation fees).
- **Other Adjustments**: Any premiums, discounts, or deferred fees.

The EIR is derived by solving the following equation:

$\text{Initial Loan Amount} = \Large\Sigma_{t=1}^n\frac{\text{CF}_t}{(1+\text{EIR})^t}$
$\text{CF}_t$ The expected cash inflows/outflows (e.g., interest payments, principal repayments, fees).
$\text{Initial Loan Amount}$ The net amount disbursed to the borrower after fees and costs.

Use numerical methods (e.g., Newton-Raphson method or financial software) to find the discount rate (EIR) that equates the present value of future cash flows to the initial loan amount. The EIR is found to be approximately higher than the contractual rate due to the initiation fee.

Reflects the true cost of borrowing or yield on lending. Allows borrowers or investors to compare financial instruments with different fee structures or terms.

## Interest Revenue

The distinction between gross and net carrying amounts is critical for calculating interest income (§5.4.1):

- Stage 1 & 2 Assets: Interest income is calculated using the gross carrying amount (only depreciation is accounted for).
- Stage 3 Assets (Credit-Impaired): Interest income must be calculated using the net carrying amount (gross minus ECL). If the asset is very likely to default, the losses will affect the interest revenue. This interest revenue is considered impaired and is termed “interest in suspense” (ISP). This ensures the entity only recognizes interest on the portion of the loan it actually expects to recover.

> *Let’s say a bank lends R1,000,000 (no transaction costs) to a corporate client at 10% interest over 5 years. Here’s how the rules apply at different stages of credit quality. At initial recognition, the loan is performing. Use the effective interest rate (EIR) — say 10% — to calculate interest on the gross carrying amount (i.e., full R1,000,000). (Paragraph 5.4.1 (b)) Suppose after 2 years, the original loan defaults or moves to Stage 3 under ECL. From that point, interest must be calculated using EIR (still 10%) but on the amortised cost — i.e., gross amount minus lifetime ECL.*

## Financial Metrics

### Coverage Ratio

A coverage ratio is a financial metric used to assess an entity's ability to meet its financial obligations, such as debt repayments, interest expenses, or other liabilities. In an [[ifrs9_standard|IFRS 9]] context it is the ECL over the total outstanding loan amounts.

$\Large\frac{\text{ECL}_{i,t,t'}}{\text{Balance}_{i,t}}$ where $\text{ECL}_{i,t,t'} = \displaystyle\sum_{s=1}^{3}\text{ECL Stage } s_{i,t,t'}$

Investors use this to compare companies and it is used to see if the book is getting better or worse. But could be also used to see if a change in strategy has worked or will work. Usually is grouped by new business vs existing business and on the new busienss side it is used to see if any updates to an application scorecard are working.

### NPL Ratio

You can determine the non-performing loan ratio by taking the proportion of loans in stage 3 divded by the total loan book to see how badly your book is performing.

$\Large\frac{\text{ECL Stage 3}_{i,t,t'}}{\text{Balance}_{i,t}}$
