---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/notation
  - difficulty/unknown
  - study-status/new
aliases:
---
# Notation

| Name | Mathematical Notation | Definition |
|-|-|-|
|Loan/Facility| $i$| a thing that is borrowed, especially a sum of money that is expected to be paid back with interest by an obligor|
|Obligor| $i'$| a person who owes or undertakes an obligation to another by contract|
|Loan term/age| $t$| the particular time stamp of a loan's life |
|Outcome period|$k$| the number of months added to the term of a loan which creates an observation|
|Calendar time| $t'$| the day, month and year when a loan's information is recorded |
|Loan information|$x_{i}=\{x_{1,i}$ ... $x_{n,i}\}$|information about a loan that does not change over time e.g., product type|
|Behavioural information|$x_{i,t}=\{x_{1,i,t}$ ... $x_{n,i,t}\}$|information about a loan that does change over time e.g., days past due|
|Macro-economic time series|$m_{t'}=\{m_{1,t'}$ ... $m_{n,t'}\}$|macro-economic time series that is indepedenent of all loans e.g., inflation rate, QoQ% GDP|
|Limit| $\text{Limit}_{i,t}\subset x_{i,t}$| the maximum limit on a loan at a time|
|Balance| $\text{Balance}_{i,t}\subset x_{i,t}$| the outstanding balance amount on a loan at a time|
|Days past due| $\text{DPD}_{i,t}\geq 0$| the number of days an obligor has not paid an outstanding payment at a particular time|
|Delinquency/Arrears measure| $g_{i,t}=\large\frac{\text{DPD}_{i,t}}{30}$| the unweighted number of payments in arrears constructed from DPD assuming 30 days (1 month) equals 1 missed payment |
|Stickiness measure| $s\geq 1$ | the number of consecutive months for which deliquency is tested |
|Delinquency indicator | $G_{i,t}(d,s)=[(\displaystyle \sum_{v=t-(s-1)}^t[g_{i,v} \geq d])=s]$ for $t\geq s$, where $d\geq 0$ is a specified arrears threshold and $[𝑎]$ are Iverson brackets that outputs 1 if the enclosed statement 𝑎 is true and 0 otherwise | the deliquency status of a loan defined by the number of missed payments and how long it is has missed these specified number of payments for |
|Instantaneous default indicator| $d_{i,t}=G_{i,t}(3,1)=[g_{i,t} \geq 3]$ | if a loan has 3 consecutive missed payments (i.e. 3 months in arrears), it is considered defaulted at that point|
|Probation period| $p\geq 1$ | the number of months an account remains in default after it is no longer 3-months arrears (i.e. it is no longer in instant default) |
|Probation indicator| $H_{i,t}(p)= [\displaystyle \sum_{v=t-p}^{t-1} d_{i,v}>0]$ for $t\geq p$ | the probation status of a loan defined by how long it is has to remain in default for |
|Cure indicator| $C_{i,t}(p)= \left\{\begin{array}{ll} 1 & d_{i,t}=0 \text{ and } H_{i,t}(p)=0 \\ 0 & \text{otherwise} \\ \end{array} \right.$ for $t\geq p$ | the cure status of a loan defined by whether it is not in probation and not in instant default |
|Default indicator (probabtion period)| $D_{i,t}(p)=[C_{i,t}(p) = 0]$ | if a loan has not cured, it is still considered to be "in" default |
|Write-off indicator| $W_{i,t}(w)=G_{i,t}(3,w)$ where $w\geq 1$ is a specified write-off threshold/point| if a loan has 3 or more missed payments for $w$ consecutive months it is considered written-off |
|Delinquency outcome| $G^*_{i,t}(k,d,s)=G_{i,t+k}(d,s)$ | a loan's future delinquency status for a specified outcome period |
|Default outcome| $D^*_{i,t}(k,p)=D_{i,t+k}(p)$ | a loan's future default outcome for a specified outcome period. Argument order convention: outcome horizon $k$ first, probation period $p$ second, applied throughout the rest of this file |
|Behavioural loan dataset|$I=\{i,t,t',x_{i},x_{i,t},m_{t'},g_{i,t},G_{i,t}(d,s),G^*_{i,t}(k,d,s),H_{i,t}(p),C_{i,t}(p),D_{i,t}(p),D^*_{i,t}(k,p),W_{i,t}(w)\}$|set of the behaviour of all over the entire observable period|
|Total at-risk loans| $n_0(x_{i},x_{i,t},t')=\displaystyle\sum_{i\subset I(x_{i},x_{i,t},t')} [ D_{i,t}(p)=0 ] $| total number of loans in a calendar time (point-in-time) for a cohort group|
|Total at-risk balance| $b_0(x_{i},x_{i,t},t')=\displaystyle\sum_{i\subset I(x_{i},x_{i,t},t')} [ D_{i,t}(p)=0 ]\times \text{Balance}_{i,t} $| total balance in a calendar time (point-in-time) for a cohort group|
|$k$-month forward default rate (number weighted)| $r(k,x_{i},x_{i,t},t')=\frac{1}{n_0(x_{i},x_{i,t},t')}\displaystyle \sum_{i\subset I(x_{i},x_{i,t},t')}[D^*_{i,t}(k,p) = 1]\times [D_{i,t}(p) = 0]$| $k$-month default rate in a calendar time (point-in-time) given a population of non-defaulted loans for a cohort group|
|$k$-month forward default rate (exposure weighted)| $r_\text{Bal}(k,x_{i},x_{i,t},t')=\frac{1}{b_0(x_{i},x_{i,t},t')}\displaystyle \sum_{i\subset I(x_{i},x_{i,t},t')}[D^*_{i,t}(k,p) = 1]\times [D_{i,t}(p) = 0]\times \text{Balance}_{i,t}$| $k$-month default rate in a calendar time (point-in-time) given a population of non-defaulted loans for a cohort group, weighted by balance / exposure|
|$k$-month average default rate | $\bar r(k,x_{i},[t_a',t_b'])=\frac{1}{N_\text{obs}}\displaystyle \sum_{t'\in [t_a',t_b'] } \mathbb{E}_{x_{i,t}}\!\left[r(k,x_{i},x_{i,t},t')\right]$, where $N_\text{obs}=t_b'-t_a'+1$ for monthly data| average of $k$-month forward default rates over a specified calendar window, marginalised over the behavioural information at each observation point|
|$k$-month TTC PD| $\text{PD}_{i}^\text{TTC}(k,x_{i},[t_a',t_b'])\approx\bar r(k,x_{i},[t_a',t_b'])$ | through-the-cycle $k$-month probability of default from a particular cohort group, which is approximately equal to the average of $k$-month forward default rates over a specified time period |
|$k$-month unconditional PiT marginal PD| $\text{PD}_{i,t}^\text{uPiT}(k,x_{i},x_{i,t})=P(D^*_{i,t}(k,p) = 1\|X_i=x_i,X_{i,t}=x_{i,t})$ |  $k$-month unconditional probability of default for a loan from a particular cohort group, regardless of prior default or prepayment|
|$k$-month conditional PiT marginal PD| $\text{PD}_{i,t}^\text{PiT}(k,x_{i},x_{i,t})=P(D^*_{i,t}(k,p) = 1 \| D_{i,t}(p)=0,X_i=x_i,X_{i,t}=x_{i,t})$ | $k$-month conditional probability of default for a non-defaulted loan from a particular cohort group|
|One-period survival probability|$s_{i,v}(x_i,x_{i,v})=1-\text{PD}^\text{PiT}_{i,v}(1,x_i,x_{i,v})$|probability the loan survives one more month at age $v$, conditional on having survived to $v$. Built from 1-period marginal PDs to avoid horizon confusion|
|Cumulative survival to age $t$|$\text{S}_{i,t}(x_i)=\displaystyle\prod_{v=1}^{t} s_{i,v}(x_i,x_{i,v})=\displaystyle\prod_{v=1}^{t}\!\left(1-\text{PD}^\text{PiT}_{i,v}(1,x_i,x_{i,v})\right)$|probability the loan is still performing at loan age $t$|
|Cumulative PD to age $t$|$\text{PD}_{i,t}^\text{Cum}(x_{i})=1-\text{S}_{i,t}(x_i)\;\approx\;\displaystyle\sum_{v=1}^{t}\text{PD}_{i,v}^\text{PiT}(1,x_{i},x_{i,v})$|probability the loan has defaulted by age $t$. The sum form is the small-PD linear approximation only|
|Lifetime PD| $\text{PD}_{i}^\text{Life}(x_{i})=\text{PD}^\text{Cum}_{i,T}(x_{i})$ | cumulative PD evaluated at the contractual maturity $T$ of the facility |
|PD term structure|$\text{PD}_{i}^\text{Term}(x_{i})=\{ \text{PD}^\text{PiT}_{i,t}(1,x_{i},x_{i,t}) : t \in [1,T] \}$|sequence of 1-period conditional marginal PiT PDs over the life of the exposure, typically manifest as a non-linear and right-skewed curve over the loan term|
|FLI|$\text{FLI}_{t'}=f(m_{t'-1})$|time series of a forward looking macro-economic index constructed from transformed macro economic variables (MEVs)|
|$k$-month conditional FiT PD| $\text{PD}_{i,t,t'}^\text{FiT}(k,x_{i},x_{i,t})=\text{PD}_{i,t}^\text{PiT}(k,x_{i},x_{i,t})\times\text{FLI}_{t'}$ | future or forward macro-economic adjusted $k$-month conditional probability of a non-defaulted loan from a particular cohort group |
|$k$-month systemically conditional PiT PD| $\text{PD}_{i}^\text{SysPiT}(k,x_{i}\|\text{FLI}_{t'}) = N(\large\frac{N^{-1}(\text{PD}_{i}^\text{TTC}(k,x_{i},[t_a',t_b']))+\text{FLI}_{t'}\sqrt{\rho}}{\sqrt{1-\rho}})$ | $k$-month probability of default for a non-defaulted loan conditional not necessarily on their individual non-defaulted status but instead the macro-[[03-economic_envrionment|economic environment]] |
|$k$-month EAD|$\text{EAD}_{i,t}(k)= [D^*_{i,t}(k,p)=1]\times \text{Balance}_{i,t+k}$| balance of a loan in $k$ months that is in default at that observation date |
|$k$-month EADF|$\text{EADF}_{i,t}(k)=\Large\frac{\text{EAD}_{i,t}(k)}{\text{Balance}_{i,t}}$| ratio/factor of the balance of a loan in $k$ months that is in default at that observation date, divided by its current balance |
