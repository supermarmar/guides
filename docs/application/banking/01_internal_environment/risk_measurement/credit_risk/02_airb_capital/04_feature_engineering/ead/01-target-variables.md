## Exposure at Default (EAD)

Exposure at default (EAD) is the gross total of extended credit plus estimated additional drawings for 1 year or until maturity. EAD modelling is relatively simpler than PD and LGD modelling, as for many products the EAD may simply be estimated as the exposure to the obligor, or client.

Where EAD modelling becomes more complex is where this exposure is not fixed and can fluctuate over time. Off-balance-sheet exposures, for example, that incur [[02-counterparty_exposures|counterparty credit risk]] (derivatives, etc.) are required to be treated separately from other exposures, as detailed by [[bis|Basel]].

The greatest analytical challenge is setting credit conversion factors (CCFs) (or loan equivalents). This involves estimating additional drawings. Globally, unused commitments are huge, and it is logical that a corporation would seek to draw down in stress scenarios. Products where CCF modelling is needed include committed loan, liquidity facilities, and credit cards. Once the CCF is calculated as a percentage of the undrawn exposure, an EAD estimate can be calculated as follows:

```math
\text{EAD} = \text{Drawn Balance} + \text{CCF} \times \text{Undrawn Balance}
```

Strong information management systems are vital in assessing EAD, as the bank must ensure that troubled entities draw only under the terms permitted by the facility and up to the limit. Collateral must be monitored, priced, and margined. The bank must act efficiently and quickly in default situations to reduce losses and limit additional drawings where possible.

Whilst EAD is commonly positioned or understood as account balance at the point of default, there exists a number of nuances that can lead to a misalignment between account balance, IFRS accounting value, accounting value gross of specific credit risk adjustments and the adjustments required by [[ss4-24|SS4/24]] to derive a compliant "outstanding amount" that serves as both the LGD denominator and EAD untransformed dependent variable. Additionally, there are motivations to model a transformation of EAD. The sections below cover:

- Deriving a compliant outstanding amount and demonstrating equivalence to account balance and IFRS accouniting value; and
- Applying a transformation to help improve overall holdout goodness-of-fit as well as consistency of goodness-of-fit across key strata of the live portfolio.

### Outstanding Amount

The definition of EAD for AIRB model estimation must comply with rules set out in the [[crr|CRR]] and [[ss4-24|SS4/24]]. This section discusses the EAD definition and introduces the concept of "outstanding amount" per [[ss4-24|SS4/24]] Paragraph 13.1, which reflects the accounting value gross of impairment, plus some specific adjustments menitioned in regulation.

#### Accounting Value Equivalence to Customer Balance

In its purest form, [[crr|CRR]] Article 166A(2) defines exposure value as the accounting value without considering Specific Credit Risk Adjustments (SCRA). SRCA are [[ifrs9_standard|IFRS 9]] impairments on assets measured at Amortised Cost (AC), or the credit component of Fair Value (FV) discounted to par value for assets measured at Fair Value. At present there are no credit card exposures measured at FV and none are anticipated.

- For exposures measured at AC in the IFRS accounts: Although interest accrues daily. it is allocated to accounts as a monthly debit. Thus, month-end balance snapshots are equivalent to the AC Cost accounting value at month-end. Impairment liabilities are held separately and do not need to be removed from balances that are already gross of SCRA. Therefore, a customer account with a $100 balance has an outstanding amount for EAD purposes of $100.
- A special case with features of both AC and FV assets is acquired portfolios. These are typically measured at FV (i.e. the transaction price) at day zero, with a day-one transfer to AC.
  - In this scenario the AC gross accounting value would in theory be set to $95 and unwound via a credit-adjusted Effective Interest Rate (EIR), up to $100 at the facility's behavioural life.
  - The [[ifrs9_standard|IFRS 9]] impairment liability is measured with respect to the $95 and set to $0 at initial recognition. (If the credit risk increases to $6 from an initial estimate of $4 factored into the FV, then an impairment liability of $2 is recognised and the gross accounting value remains $95). Being a gross amount, in line with AC as described above, no further adjustment for SCRA is needed
  - Technically, the outstanding amount is $95. The operational challenges associated with allocating the FV adjustment to individual facilities would result in exposure values that float because of accounting policy and not due to credit-related action or behaviour. As a general principle, Basel seeks estimates that are agnostic to accounting policy (e.g. the economic loss calculation can include cash flows that occur after the point of accounting derecognition and looks through restructures onto new accounts). To maintain RWA consistency with exposures originated within USCB and to develop an intuitive model that is agnostic to accounting treatment, the outstanding amount has been set to the customer balance (in this example $100) in line with [[crr|CRR]] Article 3.

#### Outstanding Amount for Performing Facilities

[[crr|CRR]] Article 182(1)(ca)(i) and [[ss4-24|SS4/24]] Paragraph 13.11 require that additional drawings between observation and default are reflected in Conversion Factors (CFs). Such drawings are reflected in both the customer balance and accounting value, therefore, no adjustments are required to incorporate this requirement. Thus, the outstanding amount for performing facilities is the customer balance at default, which includes all principal, interest and fees.

#### Outstanding Amount for Defaulted Facilities

For facilities in default, the LGD rules within [[ss4-24|SS4/24]] also require the following of the outstanding amount:

- Adding back previous partial write-offs ([[ss4-24|SS4/24]] Paragraph 13.5).
- Late fees not capitalised per [[crr|CRR]] Article 181(1)(i) and [[ss4-24|SS4/24]] Paragraph 13.9
- Interest not capitalised ([[ss4-24|SS4/24]] Paragraph 13.10)

Thus, the outstanding amount for defaulted facilities is the customer balance (which includes all principal, interest and fees), with no further adjustments.

#### Treatment of Related Facilities

The concept of a "related facility" is not explicitly defined in the [[crr|CRR]]. However, for the purposes of unbiased estimation, firms are required to look through restructures and account number changes to connect post-default drawings and cash flows with facilities at-observation ([[ss4-24|SS4/24]] Paragraph 13.8). As an example, a related facility may arise if an account is restricted to a new facility number or transferred to a fixed term loan to clear the debt.

The EAD target is more complex due to the variety of ways in which utilisation and credit availability can change over time, especially for revolving products like credit cards or overdrafts.

#### 3.2.1 Raw Outstanding Amount (Untransformed)

* This refers to the **total outstanding amount** at default (`EAD_tD`), which serves as the basis for calculating transformed targets.

* It can differ from:

  * **IFRS carrying values** (due to inclusion of off-balance sheet items or accrued interest),
  * **Internal account balances** (which may or may not include fees, interest, or accrued charges), and
  * **Post-default drawings** (depending on the bank’s recovery or workout policy).

* This amount is used:

  * As a **numerator** in LGD calculations (Loss = EAD - Recoveries),
  * To define the transformed EAD modelling targets described below.

#### 3.2.2 Transformed EAD Targets

This section describes the choice of [[01-target_variable|target variable]] for EAD modelling, It discusses the merlts of
direct EAD estimation and transformations of EAD. The concept of a transformation is attractive,
because it allows the application of a broader set of standard modelling techniques to find and
select modelled assumptions with an appropriate goodness-of-fit, holdout performance/stability,
and alignment to business requirements such as intuitiveness.
[[ss4-24|SS4/24]] Paragraph 17.1 states, in part, "Firms may choose to provide own estimates of EAD in
place of the own estimates of CF in accordance with Article 166D(3) of the Credit Rlsk: Internal
Ratings Based Approach ([[crr|CRR]]) Part." Paragraph 17.2 reads, "The [[pra|PRA]] considers that there are a
number of potentially complant approaches to estimate EAD and that an acceptable approach is
to estimate EAD as a percentage of total limit (Limit Factor estimation)."

Table 7.2-1 lists the candidate target variables considered for EAD modelling with their
associated strengths, weaknesses, ranges, and limits.

Different [[01-target_variable|target variable]] transformations are applied to better align with model performance, business use, and interpretability. Each has distinct pros and cons:

| Target   | Formula                                                                   | Description                         | Strengths                                                                           | Weaknesses                                                                                               | Typical Range               |
| -------- | ------------------------------------------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------- |
| **EAD**  | EAD<sub>tD</sub>                                                          | Dollar value of exposure at default | Simple, easy to understand                                                          | Scale-sensitive, hard to model across balances, doesn’t use limit or available credit                    | ≥ 0                         |
| **LEQ**  | EAD<sub>tD</sub> / Total Balance<sub>t0</sub>                             | Loan Equivalent                     | Good for high-utilisation, closed accounts                                          | Unstable with low balances, undefined for 0 balance                                                      | 0–2 (but can spike)         |
| **EADF** | EAD<sub>tD</sub> / Credit Limit<sub>t0</sub>                              | Exposure as % of credit limit       | Smooths volatility, stable trends, combines drawn & undrawn, intuitive for business | Omits current balance, can crowd out impact of other drivers, >1 possible if limit increases pre-default | Typically 0–1, can exceed 1 |
| **CCF**  | (EAD<sub>tD</sub> – Balance<sub>t0</sub>) / Available Credit<sub>t0</sub> | Credit Conversion Factor            | Focuses on undrawn portion, precise tracking of conversion                          | Can be volatile, undefined for 0 avail credit                                                            | -∞ to ∞ (often > 0)         |
| **UCF**  | (EAD<sub>tD</sub> – Balance<sub>t0</sub>) / Credit Limit<sub>t0</sub>     | Utilisation Conversion Factor       | Normalised undrawn draw                                                             | Ignores full drawn usage                                                                                 | 0–1+                        |

#### 3.2.3 Selection Considerations

* **EADF** is often preferred due to:

  * Its **stability across credit cycles**,
  * Strong correlation with utilisation at t0,
  * Intuitive interpretation for business users and regulators.

* However, banks may choose **EAD** or **LEQ** where:

  * Business decisions rely on absolute amounts,
  * Balance volatility is low, or
  * Simplified interpretation is needed.

* Model developers should evaluate:

  * **Goodness-of-Fit** (Gini, RMSE, AIC),
  * **Holdout performance** (on out-of-time sample),
  * **Predictor interpretability**, and
  * **Business and regulatory alignment**.

Here is a write-up for **Section 3.2: EAD [[01-target_variable|Target Variable]] Analysis**, based on your notes:

---

## 3.2 Selection of EAD [[01-target_variable|Target Variable]]

To determine the most appropriate [[01-target_variable|target variable]] for **Exposure at Default (EAD)** modelling, we undertook a structured comparative analysis between two candidate target transformations: **EADF** (EAD as a proportion of credit limit) and **CCF** (Credit Conversion Factor).

### 3.2.1 Candidate Target Definitions

* **EADF** = EAD at default / Credit limit at observation
* **CCF** = (EAD at default – Balance at observation) / Available credit at observation

These were chosen due to their interpretability and use in industry, and their alignment with both internal practice and regulatory expectations.

---

### 3.2.2 Segmented Preliminary Modelling

A toy model was developed using four intuitive portfolio segments to test performance under each target transformation:

* **EMOB** buckets (Early Months on Book)
* **Inactive accounts** (no activity >4 months)
* **Utilisation <10%**
* **Utilisation between 10–95%**

This [[06-segmentation|segmentation]] allowed early identification of structural biases or volatility in target variables across key behavioural clusters.

---

### 3.2.3 Volatility Analysis

Results showed:

* **CCF exhibited significantly higher variance**, especially in:

  * High utilisation accounts (where balance ≈ credit limit)
  * Low utilisation or inactive accounts (where available credit is high)
* **EADF showed more stable distributions** across all segments, with lower susceptibility to extreme values.

---

### 3.2.4 Predictive Performance Evaluation

We compared actual vs predicted EAD values on both candidate models using the following diagnostics:

* **Relative Error** (|Predicted EAD – Actual EAD| / Actual EAD)
* **Visual comparison** of predicted vs actual EAD

This was conducted:

* Across full portfolio (excluding accounts with utilisation >95% where **CCF becomes unstable**)
* On **Good Book** vs **Bad Book** (accounts that defaulted vs didn’t)
* By **FICO band**, **credit limit band**, and **utilisation band**

**EADF consistently showed lower error volatility**, better central tendency alignment, and smoother trends across [[06-segmentation|segmentation]] variables.

---

### 3.2.5 Considerations on CCF Definition Complexity

**CCF introduces practical modelling complications** due to its conditional nature:

* When balance ≈ limit → **available credit ≈ 0** → CCF explodes or is undefined.
* To resolve:

  * If balance = limit → define CF = 1
  * If balance = 0 → define CF = EAD / limit
  * Else → define CF = EAD / balance
    Each approach introduces an **assumption** that must be **justified and tested**. Sensitivity analysis is required to confirm robustness across these edge cases, making deployment more complex.

---

### 3.2.6 Final Selection and Justification

**EADF was selected** as the final EAD target transformation for the following reasons:

* **Industry standard** — commonly used in IRB portfolios
* **Simpler modelling assumptions** and better model interpretability
* **Lower volatility** in outcome variable, supporting better generalisation
* **Consistency** with other Business Units and past validation work

---

### 3.2.7 Supporting Diagnostics

We plotted historical trends of **EADF** across the portfolio, including:

* **Median and mean EADF** over time
* **Account volume** supporting each monthly or quarterly view
* Stability of EADF distributions in different portfolio segments

These showed strong and stable behaviour over time, adding to the robustness of this choice.
