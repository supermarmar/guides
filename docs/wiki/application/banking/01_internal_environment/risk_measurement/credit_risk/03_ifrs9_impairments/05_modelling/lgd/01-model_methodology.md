---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/ifrs9-impairments/modelling/lgd/model-methodology
  - difficulty/unknown
  - study-status/new
aliases:
---
# **LGD (Loss Given Default)**

The proportion of the exposure that is expected to be lost if a default occurs. Typically considers collateral and recovery rates. Here's how LGD is modeled, considering Probability of Write-Off Given Default (PWGD) and Loss Given Write-Off (LGW) as well as Loss-Given Cure (LGC) which is mostly the costs associated with debt-collection and counselling.

$\text{LGD} = \text{PWGD} \times \text{LGW} + (1-\text{PWGD}) \times \text{LGC}$

The LGC describes the severity of a loss given that a default cures.

- LGC is typically dependent on the duration of the default
- LGC is typically small and mainly due to costs and delays in the payment

The LGW describes the severity of a loss given that a default does not cure.

- LGW is typically highly dependent on value of collateral
- Borrower characteristics can be used to further discriminate (e.g. industry type)
- LGW can still be zero if collateral coverage is sufficient

## **Lifetime PWGD**

The probability that a defaulted borrower will enter a write-off phase given they have defaulted, **eventually**. Unlike PDs, where we look at 12m and lifetime. The in-collections state is a critical phase where accounts are actively managed to either **cure**, **remain in collections**, or move to a **full write-off**.

$\text{Write Off Rate} = \frac{\text{Written Off Accounts}}{\text{Total Completed Accounts}}= 1 - \text{Cure Rate}$

Often modelled similarly to PD using risk drivers that reflect the borrower's repayment capacity and the cure rate tends to decline with increasing time in-default. It is usually modelled by means of a logistic regression (similar to PD).

### **Completion Threshold**

A completion threshold defines the minimum proportion of accounts in a default cohort that have transitioned to a final state (e.g., cured or written off). For example, an 80% threshold means the bank will only analyze cohorts where at least 80% of accounts have reached one of these final states cure or write off (not in collections). Ensures that sufficient transitions have been observed, reducing uncertainty in the model.  Avoids including cohorts with a high percentage of unresolved accounts, which could distort default recovery rates. Provides more reliable and stable transition probabilities for PWGD and LGD modeling.

This is not prescribed by IFRS.

$\text{Completion Rate} = \Large\frac{\text{Written Off or Cured Accounts}}{\text{Total Accounts}}$

### **Stage 1 & 2 Accounts**

Stage 1 and Stage 2 accounts are typically not in the dataset used for modeling PWGD, as they are still performing or in early stages of credit deterioration. However, they can be modeled using an average lifetime PWGD (an overall write-off rate given default) based on historical patterns of cure and write off for accounts that eventually default (Stage 3).

Calculate the historical write off rate for each deafult date cohort. Then take an average of the historical write-off rates and set it equal to the PWGD assumption for Stage 1 and Stage 2 accounts (fixed probability).

### **Stage 3 Accounts**

For Stage 3 accounts (which are the defaulted accounts in collections, written off, or cured), the PWGD model needs to account for the time these accounts spend in collections and the likelihood of write-off or recovery over that time. To calibrate PWGD for Stage 3 accounts, build a model (typically a survival analysis model, such as Cox Proportional Hazards or a Logistic Regression model) that predicts the probability of recovery based on the time an account spends in collections **(TIC)**.

### **Curing Rule**

The curing rule refers to the process by which an account that was previously in default (Stage 3) returns to performing (Stage 1), typically because the borrower has made a **number of sufficient payments** or **resolved the outstanding debt for some time**.

For Stage 3 accounts, you would track the time spent in collections. This is crucial because the longer an account is in collections, the less likely it is to recover (i.e., the PWGD tends to increase over time). However, what you might notice is that there will be an inital decrease in the PWGD by TIC up until a certain point.

In terms of PWGD, curing affects the likelihood of a defaulted account recovering. This recovery process can be visually represented on a graph showing PWGD by Time in Collection. During the early months of being in collections, the PWGD is often relatively low and possibly decreasing. This is because accounts that defaulted may still have a chance to recover, either through cure or partial payment.

As time in collections increases, the PWGD begins to increase. The likelihood of curing decreases because more time spent in default often indicates more severe financial distress or neglect.

The longer the account stays in collections without curing, the higher the PWGD becomes. This reflects the higher probability of the account being written off or becoming irrecoverable. Accounts that have been in collections for 12+ months often have very low chances of curing, so their PWGD is typically near 100.

The curing rule can be inferred from the point where accounts stop recovering or where a lower PWGD is observed.

## **Lifetime LGW**

The percentage of the exposure lost during the write-off phase, accounting for recovery efforts. It is is usually calibrated as a function of present value of recoveries (which includes collection costs):

$\text{Loss Rate}=1-\text{Recovery Rate}$

This can be balance weighted (EAD) or number weighted.

### **Recovery Curves**

A **recovery rate** is the proportion of the exposure that is expected to be recovered after the default. Longer recovery periods (TIC) can decrease the overall recovery rate. A recovery curve plots (rate vs TIC) are often used to estimate how much of the exposure will be recovered over time. For example, some recovery may occur immediately upon default, and additional recovery might take place through legal actions over a few years.

#### **Secured Loans**

The recovery for secured loans tends to be higher since the bank can sell the collateral (e.g., a house, car, or business asset) to recover part of the defaulted amount. Therefore, the LGW for secured loans will be calibrated based on the expected recovery from the collateral.

This is also usually modelled in two components: 

- Loss for secured part: mostly driven by value of the collateral
- Loss for unsecured part: mostly driven by recoveries

#### **Unsecured Loans**

For unsecured loans (e.g., credit cards), the recovery is typically lower because there is no collateral to recover the outstanding balance. LGWs for unsecured loans are usually modeled based on historical recovery rates from similar loans.

### **Stage 1 & 2 Accounts**

Similar to the PWGDs, LGWs can be modeled using an average lifetime LGW (an overall loss rate given write-off). Calculate the historical recovery rate for each deafult date cohort. Then take an average of the historical one minus the recovery rates and set it equal to LGW assumption for Stage 1 and Stage 2 accounts.

### **Stage 3 Accounts**

Similar to the PWGDs, machine learning models or statistical techniques (e.g., regression analysis, survival models) are often used to model the recovery rates for stage 3 loans. Unlike the PWGD term structure you will most likely see a monotonically increasing graph that slows down the furhter in collections it goes.

If you plot the LGW against the write-off date you should get an average rate that should be the average of your LGW curve by TIC.
