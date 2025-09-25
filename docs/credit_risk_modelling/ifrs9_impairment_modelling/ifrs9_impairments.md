# **IFRS 9 Impairment Models**

IAS 39 and IFRS 9 are accounting standards issued by the International Accounting Standards Board (IASB) for financial instruments, particularly their recognition, measurement, and impairment. IFRS 9 replaced IAS 39 in 2018 to address the limitations and complexity of IAS 39 “incurred loss” framework, providing a more forward-looking and simplified approach. Under IAS 39, losses were recognized only when there was objective evidence of impairment (e.g., default or delinquency). Hence it was backward-looking, meaning it relied on historical data and loss events already incurred. This delayed provisioning during the 2008 financial crisis, leading to underestimation of risks.

<https://www.bis.org/fsi/fsisummaries/ifrs9.pdf>

The principle is to forfeit a portion of income today into a loss provision that ideally offsets amounts that may be written-off tomorrow. Doing so helps to smooth overall earnings volatility, which is itself a central tenet of risk management.

IFRS 9 requires that this loss provision be regularly updated based on a statistical model, i.e., the asset’s Expected Credit Loss (ECL). Given a new ECL-value, a bank adjusts its loss provision either by raising more from earnings or releasing a portion thereof back into the income statement. This ECL-model represents the probability-weighted sum of cash shortfalls that a bank expects to lose over a certain horizon, incorporating forward-looking information.

## **Impairment**

Under IFRS 9, impairment is a dynamic, forward-looking calculation that incorporates staging, probability-weighted losses, and macroeconomic scenarios. Its impact is reflected through a loss allowance on the balance sheet and impairment charges in the P&L. This ensures that the financial statements present a more accurate and timely view of credit risk. The calculated ECL is recorded as a loss allowance on the balance sheet [5.5.1](a).

### **Gross Carrying Amount**

The gross carrying amount of a financial asset under IFRS 9 represents its original or amortized cost, before any adjustments for impairment losses (i.e., loss allowances). It reflects the contractual amounts due from the borrower and excludes any deductions for expected credit losses [5.1.1](a).

The gross carrying amount includes:

- Principal Outstanding: The unpaid balance of the loan or credit facility.
- Accrued Interest: Any interest income that has been earned but not yet received.
- Transaction Costs (for amortized cost assets): Costs directly attributable to issuing or acquiring the financial asset.
- Amortization: Adjustments made due to the effective interest rate (EIR) method.

For stage 1 and stage 2 accounts, interest revenue is still calculated on the gross carrying amount.

### **Net Carrying Amount**

The financial asset is shown at its net carrying amount:

$\text{Net Carrying Amount} = \text{Gross Carrying Amount} - \text{ECL}$

Changes in the ECL (e.g., new impairments or reversals) are recognized as impairment charges in the income statement. For Stage 3 accounts, interest revenue is calculated on the net carrying amount (gross amount minus loss allowance).

>Quick check: if discount rate increases then ECL should get bigger since it is negative.

## **Staging**

IFRS 9 adopts a staged approach in §5.5.3 and §5.5.5 that is based on the extent of the perceived deterioration in the underlying risk. In principle, each of the three stages requires a progressively more severe ECL-estimate. Financial assets are categorized into three stages based on their credit risk. IFRS 9 does not explicility say in quantitative terms how to determine these stages. However, it is common in industry standard to denote it as such:

- Stage 1: No payments missed or partial arrears e.g. DO on 25th but you pay on the 10th
- Stage 2: 30 days to 89 days in arrears
- Stage 3: 90+ days in arrears. This is classified as default.

![alt text](images/ifrs9/3_stage_model.png)

### **Stage 1 (Performing Assets)**

Assets that have low credit risk or where there has been no significant increase in credit risk since initial recognition. Impairment is calculated based on 12-month ECL (expected credit losses within the next 12 months). As soon as a financial instrument is originated, 12-month ECL would be recognised in the P&L. [5.5.5](a)

#### **12-Month ECL**

$\text{ECL} =\displaystyle\sum_{t=1}^{12} \text{PD}_{t}^{FiT}\times \text{LGD}_{t}^{FiT} \times \text{EAD}_{t}^{FiT} \times (1+\text{EIR})^{-t}$

### **Stage 2 (Underperforming Assets)**

Assets that have deteriorated quite significantly in their credit quality or where there has been a significant increase in credit risk (**SICR**) but no default from the point of origination (recognition). Impairment is based on Lifetime ECL (expected credit losses over the entire remaining life of the asset). [5.5.3](a)

#### **Lifetime ECL**

$\text{ECL} =\displaystyle\sum_{t=1}^{n} \text{PD}_{t}^{FiT} \times \text{LGD}_{t}^{FiT} \times \text{EAD}_{t}^{FiT} \times (1+\text{EIR})^{-t}$

### **Stage 3 (Non-performing Assets)**

Assets that are objectively credit-impaired [Appendix A](a) or in default [B5.5.37](a) (their future cash flows are likely compromised). [5.5.3](a).

The probability of default is equal to 1 since the asset has already defaulted.

$\text{ECL} =\displaystyle\sum_{t=1}^{n} \text{LGD}_{t}^{FiT} \times \text{EAD}_{t}^{FiT} \times (1+\text{EIR})^{-t}$

![alt text](images/ifrs9/3_stage_model_2.png)

## **Financial Metrics**

### **Coverage Ratio**

A coverage ratio is a financial metric used to assess an entity's ability to meet its financial obligations, such as debt repayments, interest expenses, or other liabilities. In an IFRS 9 context it is the ECL over the total outstanding loan amounts. Investors use this to compare companies and it is used to see if the book is getting better or worse. But could be also used to see if a change in strategy has worked or will work. Usually is grouped by new business vs existing business and on the new busienss side it is used to see if any updates to an application scorecard are working.

### **NPL Ratio**

You can determine the non-performing loan ratio by taking the proportion of loans in stage 3 divded by the total loan book to see how badly your book is performing.

## **PD (Probability of Default)**

Lending poses the fundamental risk of capital loss should the borrower fail to repay their loan, which necessitates the accurate prediction of the borrower’s underlying probability of default (PD). This task usually involves finding a statistical relationship between a set of borrower-specific input variables and the binary-valued repayment outcome (i.e., defaulted or not) over some outcome period.

The literature on this particular classification task is considerable and spans various forms of supervised statistical learning, including machine learning.

### **Data**

- Typically, to calibrate your PDs the dataset has monthly loan performance (e.g. 20-year mortgage loan) observations for each loan 𝑖 = 1, ..., 𝑁.
- Each loan 𝑖 is therefore observed over discrete time $𝑡 = 1, ..., T_𝑖$ from the time of its first month-end observation up to the end of its lifetime $T_𝑖$.
- These loans are sampled between two dates, during which time new mortgages were continuously originated.
- Loans that predate the start of this sampling window, i.e., left-truncated loans, are retained along with their subsequent observations throughout this window.
- It also includes fundamental credit fields such as net cash flows (receipts), expected instalments, arrears balances, month-end balances, variable interest rates, original loan principals, the amount and timing of write-offs and early settlement.

#### **Deliquency Measure** =

A delinquency measure quantifies the gradual erosion of trust between bank and borrower in honouring the credit agreement. The $𝑔_0$-measure (or the unweighted number of payments in arrears) which is constructed from **days past due** (DPD) is used for its intuitive appeal and industry-wide ubiquity.

Banks commonly specified **three payments (or 90 DPD)** in arrears as a pragmatic point of ‘default’ [B5.5.37](a), long before the introduction of the Basel II Capital Accords. That said, this threshold can generally range between 30–180 days based on managerial discretion and some analysis.

#### **Default Indicator**

One can compare $𝑔_0(𝑡)$ at time 𝑡 against the specifiable threshold 𝑑=3. Thus the default status at time t can be denoted as:

$D_t= [g_0(t) \geq d]$ where $d=3$

Where [𝑎] are Iverson brackets that outputs 1 if the enclosed statement 𝑎 is true and 0 otherwise.

The loan’s resulting binary-valued default indicator, can now be used within a typical cross-sectional modelling setup for predicting future default-outcomes.

In preparing the modelling dataset, we observe all predictive information of loan $𝑖$ at a particular time 𝑡. Then, the loan’s future default-status at time $𝑡 + 𝑣$ is merged to the observations at 𝑡, thereby taking a snapshot between two points in time, or a cross-section. However, the chosen value for this third parameter $𝑣 ≥ 0$ (or outcome period) is what we will define as our **$𝑣$-month default indicator** which will then be used to determine our **$𝑣$-month PD**.

More formally, a process $Z_𝑡(𝑑, 𝑣) = D_{t+𝑣}$ prepares a given loan’s monthly performance history by evaluating $D_t$ at ‘future’ time $𝑡 + 𝑣$, though assigns the result to time 𝑡.

#### **Curing Rule**

IFRS 9 is not prescriptive in terms of defining when an account has cured [5.5.7](a). Hence, a default flag can be created under the following alternatives of cure.

- Instant Cure: An account returns to performing immediately after the cause of default is removed.
- Probabtion Period: This is used when an account needs to wait for a certain amount of time (e.g. 6m) before returning to performing. It reduces the risk of multiple defaults.

![alt text](images/ifrs9/hist_data.png)

### **Conditional Forward Default Rates**

Let $𝐷_{𝑖,𝑡}$ be a Bernoulli random variable that denotes the default status of loan 𝑖 at time 𝑡, i.e., 1 if in state D, and 0 otherwise. In creating a **𝑣-month forward default indicator**, we use the worst-ever aggregation type that indicates future default at present time 𝑡 whenever any of the next 𝑣 ≥ 1 statuses $𝐷_{𝑖,𝑡+1}, ..., 𝐷_{𝑖,𝑡+v}$ equals one. The worst-ever 𝑣-month conditional probability of a non-defaulted loan 𝑖 is then:  

$P(\max [𝐷_{𝑖,𝑡+1}, . . . , 𝐷_{𝑖,𝑡+v}] = 1 | 𝐷_{𝑖,𝑡} = 0)$.

Therefore a 12-month conditional default probability will be

$P(𝐷_{𝑖,𝑡+12}] = 1 | 𝐷_{𝑖,𝑡} = 0)$

Regarding its estimation, assume that a longitudinal dataset $D' = \{𝑖, 𝑡, 𝑑_{𝑖,𝑡}\}$ consists of $ 𝑑_{𝑖,𝑡} ∈  D_{𝑖,𝑡}$ default status outcomes, whereafter $D'$ can be partitioned into a series of non-overlapping subsets $D'(t')$ over calendar time $t' = t'_1 , . . . , 𝑡′_𝑛$.

The aforementioned probability can then be estimated at the portfolio-level by the 𝑣-month default rate, defined over 𝑡' for a given $D'$ as:

### **Through-the-Cycle (TTC) PDs**

Credit rating systems focus mostly on producing a conservative PD-estimate that remains **static (but stressed)** over the lifetime of each loan, often by design.

The broad goal of such systems is to facilitate the estimation of **regulatory and economic capital**, which should absorb any catastrophic **(or unexpected) losses** under the Basel framework from the BCBS. Any temporal effects that might affect the PD during loan life are therefore largely ignored, together with any macroeconomic influences; particularly since the latter is already assumed to be stressed to a recession-like level during PD-estimation. Doing so renders the resulting PD-estimates as **through-the-cycle (TTC)** in that they should at least approximate the long-run averages of 1-year (12-month) historical default rates over a full macroeconomic cycle, as required during capital estimation. While
these TTC PD-estimates are certainly stable over time by design, they are also typically inaccurate within any other setting besides capital estimation.

Put simply, a TTC PD is a measure of the likelihood that a borrower will default over a specific time horizon, calculated in a way that smooths out fluctuations caused by economic or business cycles. It reflects a borrower's **average risk of default** under both favorable and unfavorable economic conditions. The goal of TTC PD is to isolate a **borrower's intrinsic credit risk** (their ability to meet obligations independent of short-term economic changes).

PD models are traditionally based on an expectation over the next twelve months. IFRS 9 requires a forward looking – or Forward in Time (FiT) – approach. The expectation as part of the IFRS 9 requirements is that both a 12 month and lifetime FiT PD are calculated with macroeconomic factors considered.

$\text{TTC PD} = \text{PIT PD} - \text{Credit Cycle Adjustment}$

![alt text](images/ifrs9/ttc_vs_pit_pd.png)
