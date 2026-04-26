---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/ifrs9-impairments/modelling/pd/data-representativeness
  - difficulty/unknown
  - study-status/new
aliases:
---
# [[04-data-representativeness|Data Representativeness]]

We measure the representativeness of the sets $\{D_𝑆,D_𝑇, D_𝑉\}$ by comparing the **𝑣-month forward default rate** across these sets. Regarding its estimation, assume that a longitudinal dataset $D' = \{𝑖, 𝑡, 𝑑_{𝑖,𝑡}\}$ consists of $ 𝑑_{𝑖,𝑡} ∈  D_{𝑖,𝑡}$ default status outcomes, whereafter $D'$ can be partitioned into a series of non-overlapping subsets $D'(t')$ over calendar time $t' = t'_1 , . . . , 𝑡′_𝑛$.

## Forward Default Rate

The [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/04_feature_engineering/pd/01-target_variable|target variable]] can then be estimated at the portfolio-level by the 𝑣-month default rate, defined over 𝑡' for a given $D'$ as:

$r(k,x_{i},x_{i,t},t')=\frac{1}{n_0(x_{i},x_{i,t},t')}\displaystyle \sum_{i\subset I(x_{i},x_{i,t},t')}[D^*_{i,t}(p,k) = 1]\times [D_{i,t}(p) = 0]$

where $𝑛_𝑡'$ denotes the size of the at-risk population within each subset $D'(t')$. Finally, and in verifying sampling representativeness using the equation above, we graph and compare the $v$-month default rate over time and across the various datasets. We furthermore calculate the mean absolute error (MAE) between $D$ and each respective sample, $D_𝑇$ and $D_𝑉$. If these values are low then the sample is representative of the population.

The method above calculates default rates by considering the number of accounts, treating all defaults equally, regardless of exposure size. This is used when the focus is on account-level performance, customer [[08-segmentation|segmentation]], or building behavioral scorecards. Useful for corporate business banking when there is low number of accounts.

### Exposure Weighted

In this method, default rates are calculated by weighting each default event by the corresponding exposure (e.g., balance or loan amount).

$r_\text{Bal}(k,x_{i},x_{i,t},t')=\frac{1}{b_0(x_{i},x_{i,t},t')}\displaystyle \sum_{i\subset I(x_{i},x_{i,t},t')}[D^*_{i,t}(p,k) = 1]\times [D_{i,t}(p) = 0]\times \text{Balance}_{i,t}$

Typically used when capital allocation, loss estimation, or regulatory compliance (e.g., [[bis|Basel]] standards) is the focus. Emphasizes large exposures since their defaults have a more significant financial impact.

