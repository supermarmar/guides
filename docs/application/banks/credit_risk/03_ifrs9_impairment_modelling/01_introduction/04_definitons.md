# Definitions

## Obligor

## Facility

## Deliquency Measure

A delinquency measure quantifies the gradual erosion of trust between bank and borrower in honouring the credit agreement. The $𝑔_0$-measure (or the unweighted number of payments in arrears) which is constructed from days past due (DPD) is used for its intuitive appeal and industry-wide ubiquity.

Banks commonly specified three payments (or 90 DPD) in arrears as a pragmatic point of ‘default’ [B5.5.37](a), long before the introduction of the Basel II Capital Accords. That said, this threshold can generally range between 30–180 days based on managerial discretion and some analysis.

## Definition of Default (DoD)

One can compare $𝑔_0(𝑡)$ at time 𝑡 against the specifiable threshold 𝑑=3. Thus the default status at time t can be denoted as:

$D_t= [g_0(t) \geq d]$ where $d=3$

Where [𝑎] are Iverson brackets that outputs 1 if the enclosed statement 𝑎 is true and 0 otherwise.

The loan’s resulting binary-valued default indicator, can now be used within a typical cross-sectional modelling setup for predicting future default-outcomes.

In preparing the modelling dataset, we observe all predictive information of loan $𝑖$ at a particular time 𝑡. Then, the loan’s future default-status at time $𝑡 + 𝑣$ is merged to the observations at 𝑡, thereby taking a snapshot between two points in time, or a cross-section. However, the chosen value for this third parameter $𝑣 ≥ 0$ (or outcome period) is what we will define as our $𝑣$-month default indicator which will then be used to determine our $𝑣$-month PD.

More formally, a process $Z_𝑡(𝑑, 𝑣) = D_{t+𝑣}$ prepares a given loan’s monthly performance history by evaluating $D_t$ at ‘future’ time $𝑡 + 𝑣$, though assigns the result to time 𝑡.

### Days Past Due (DPD)

### Return to Default

When calibrating  PDs, accounts that redefault (default after curing) and cure (recover from default) require special treatment to ensure accurate modeling of credit risk dynamics. These events introduce complexities because they alter the time-to-default patterns and can influence the term structure of PDs.

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


## SICR

§5.5.4

> *The transition to Stage 2 is not based on actual default, but rather on the bank’s forward-looking assessment of credit risk. The IFRS 9 model requires that even if a loan is still performing (i.e., no payments are yet missed), a significant increase in credit risk should trigger a shift to lifetime ECL recognition. The bank considers all available information, including industry-wide economic downturns and the borrower’s weakened financial metrics. The updated lifetime ECL of R400,000 is now booked as a loss allowance, increasing the impairment expense in the income statement.*

§5.5.9

> *At each reporting date, the bank is required to assess whether the credit risk of a loan has increased significantly compared to its risk at initial recognition. Let’s say a bank issued a 5-year loan to a mid-sized logistics company in 2022. At the time of origination, the borrower had a healthy balance sheet, steady cash flow, and an external credit rating equivalent to BBB, reflecting a low probability of default. Now, in 2025, during a new reporting cycle, the bank reassesses the risk of default over the remaining life of the loan. It notices that the borrower has experienced a significant drop in revenue, is taking longer to pay other creditors, and is on credit watch for a potential downgrade. Although the actual ECL amount hasn't changed drastically yet, the risk of default occurring over the life of the loan has materially increased when compared to 2022. Therefore, this loan would move from Stage 1 to Stage 2, and the bank would now recognise lifetime expected credit losses instead of just 12-month ECLs. This results in a higher loss allowance and an impairment loss on the income statement, even if actual cash shortfalls haven't occurred yet.*

## Cure

$5.5.7

> *In a later reporting period, suppose the borrower that had previously moved into Stage 2 due to a temporary dip in financial performance now shows signs of recovery. For example, their revenues improve, debt ratios normalize, and their credit rating is upgraded. After evaluating all available and forward-looking information, the bank concludes that the significant increase in credit risk no longer exists. As a result, the loan transitions back to Stage 1, and the loss allowance is adjusted from a lifetime ECL (e.g., R400,000) back down to a 12-month ECL (e.g., R75,000). The reduction of R325,000 is recognised in the income statement as an impairment gain, improving the bank's profitability for that period. This transition also reduces the loss allowance shown on the balance sheet, increasing the net carrying amount of the asset.*

IFRS 9 is not prescriptive in terms of defining when an account has cured [5.5.7](a). Hence, a default flag can be created under the following alternatives of cure.

- Instant Cure: An account returns to performing immediately after the cause of default is removed.
- Probabtion Period: This is used when an account needs to wait for a certain amount of time (e.g. 6m) before returning to performing. It reduces the risk of multiple defaults.

## Write Offs

§5.4.4

> *In the context of expected credit loss (ECL) modelling, paragraph 5.4.4 refers to the process of writing off a financial asset—such as a bank loan—when the bank has no reasonable expectation of full or partial recovery. This typically happens after significant default and exhaustive recovery efforts have failed. At this point, the bank derecognises the written-off portion of the loan by directly reducing the gross carrying amount of the asset. For example, suppose a bank has a loan with a gross carrying amount of R100,000. After default and collection efforts, it expects to recover only R20,000. The remaining R80,000 is written off. If the bank later recovers R5,000 through post-write-off legal action, that recovery is treated as income, but the written-off portion remains derecognised.*

## Loss

## Maximum recovery period

## PWOR

Post Write-Off Recoveries refer to the collections or repayments a bank manages to recover from borrowers after their loans have been written off as bad debts. In accounting terms, a write-off occurs when the bank deems that a loan is unlikely to be repaid and removes it from the active accounts receivable or loan book. However, even after a write-off, the bank can continue pursuing recovery actions through legal means, collection agencies, or other strategies.

A loan is written off when the bank believes there is minimal likelihood of full repayment based on its internal policies and regulations (e.g., after a certain period of nonpayment or legal default). The loan balance is removed from the bank's financial statements as an asset. Any recoveries after the write-off are recorded as recovery income in the bank’s income statement, not as a reversal of the write-off.


## Write Off Rule

If banks are recovering a significant portion of bad debts post write-off, it raises questions about the effectiveness and timing of their write-off policy. If a bank writes off loans too early (e.g., before fully exhausting all reasonable collection efforts), it might recover more post write-off. This could indicate overly conservative policies or inefficiencies in pre-write-off collection strategies. This leads to higher than expected LGWs which increases the ECL.

If post-write-off recoveries are consistently high, the bank may need to adjust its write-off criteria to better align with the actual recovery potential. 