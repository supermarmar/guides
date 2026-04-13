---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/ifrs9-impairments/modelling/pd/model-methodology
  - difficulty/unknown
  - study-status/new
aliases:
---
# Model Methodology (PD)

Several PD modelling approaches exist that may be considered as possible methodologies to derive the PD component for [[ifrs9_standard|IFRS 9]] purposes, although very few [[ifrs9_standard|IFRS 9]] PD methodologies exist in published academic literature. In spite of the expansion of research in respect to [[ifrs9_standard|IFRS 9]] in the past few years, it is still in its infancy in developing countries (Dib and Feghali 2021).The focus of the literature overview will be on retail portfolios and not wholesale portfolios, because some methodologies for wholesale portfolios are not applicable for retail portfolios (see e.g., (Gubareva 2021)).

Some of these possible approaches will now be discussed in the literature overview. How risk drivers are incorporated in each of these approaches will be mentioned, since it is crucial to derive sufficiently granular PD estimates to assess significant increases in credit risk as required by [[ifrs9_standard|IFRS 9]]. Some advantages and disadvantages of each approach will be discussed with specific consideration of the requirements of [[ifrs9_standard|IFRS 9]] (McPhail and McPhail 2014). Țurlea (2021) highlights various rating methods and systems applicable under the [[ifrs9_standard|IFRS 9]] framework with some advantages and disadvantages.

The calibration process differs for new business (typically informed by application scorecards) and existing business (typically informed by behavioral scorecards). Behavioural scorecard methodologies will be described below.

## Binary Logistic Regression

Logistic regression (Țurlea 2021) can be used in a scorecard to predict PDs (Thomas 2009). Typically risk drivers will be included as independent variables (Anderson 2007). The literature on using binary logistic regression (LR) as a generic supervised classifier is quite extensive and its use within banking is ubiquitous, particularly in the field of application credit scoring, as was first demonstrated in Wiginton (1980). The technique is considered by many authors to be the **most successful modelling technique** thus far in quantitative finance.

Beyond application credit scoring, this technique is also typically used in pre-screening loan offers, detecting fraud cases, scoring collection success, informing direct marketing offers, and in risk-based pricing. At the very least, this technique and its results can serve as a benchmark when using more advanced classification techniques in future.

For each $m$-month PD for each loan $i$ the logit function can be defined as

$g(\mu _{j})=\log\Large(\frac{𝑝(𝒙_{i})}{1-𝑝(𝒙_{i})})$ $ = \beta_{0} + \beta_{1}x_{i1} + ... + \beta_{1n}x_{in}$

The advantages of logistic regression include: it is simple to use, well known in the industry (Siddiqi 2006), it produces account-level estimates, and it can regress multiple variables without the need for [[07-segmentation|segmentation]] (Siddiqi 2017). The key disadvantage from an [[ifrs9_standard|IFRS 9]] perspective is that logistic regression is not designed for varying time horizons and, if used, may result in unnecessary complexity.

## Empirical Term Structures

https://mpra.ub.uni-muenchen.de/76271/1/MPRA_paper_76271.pdf

Cumulative default curves can be estimated from empirical default and closure data which is sometimes referred to as segmented empirical term structures (Schutte et al. 2020). The PD term structures will often be segmented for different risk drivers. This method is generally intuitive and well understood (Yang 2017) and directly includes re-defaults and attrition effects. The one disadvantage is that the resulting estimates’ quality depends significantly on how the term structures are segmented and granular segmentations are often not possible due to [[05-data_limitations|data limitations]] such as a sufficient number of observations and defaults for stable estimates per segment.

This section describes how marginal PDs (referred to as ‘PD term structures’ in future) are derived by using empirical information. The method creates PD term structures based on the most recent default information and accounts’ risk characteristics prior to default. The approach accounts for attrition effects (i.e., accounts closing from a performing status and can thus no longer default in subsequent months) such that no separate adjustment will be required in the calculation of ECL. The proposed methodology also includes re-default events in the PD term structures (i.e., scenarios where an account defaulted more than once during its lifetime) such that lifetime PDs can theoretically exceed 100% for high risk accounts, particular for portfolios with long lifetime assumptions. This approach was chosen to capture the portfolio’s actual default behaviour more accurately and reduce complexities compared to a ‘worst ever’ modelling approach, typically used in regulatory models. The same approach must also be applied in the LGD model, e.g., by assigning a zero loss assumption to cure events to avoid double counting effects. Different PiT PD term structures are developed to capture the structurally different default risk patterns for different pools of accounts using [[07-segmentation|segmentation]].

To define the PD term structure, we define the cumulative and marginal PD’s similarly as in (Yang 2017). Let $p_{k,t}^c$ be the cumulative PD for the period (0,𝑡] with respect to observation month 𝑘 i.e., the probability of defaulting in the total period (0,𝑡]. We define the marginal PD in the period (𝑡−1,𝑡] with respect to observation month 𝑘 is then defined as $p_{k,t}^m=p_{k,t}^c-p_{k,t-1}^c$. Note that by definition, for the period (0, 1] we have $p_{k,t}^m=p_{k,t}^c$.

To estimate the empirical marginal PD’s we construct a defaults table containing the number of defaults and performing accounts. Each row in the defaults table represents an observation month, where ${𝑀_1,𝑀_2,…,𝑀_𝐾}$ is the set of observation months e.g., ${201501, 201502, …, 201507}.$ Let $𝑑_{𝑘,𝑡}$ be the number of accounts that were performing as at the observation month $𝑀_𝑘$, and then defaulted in the period (𝑡−1,𝑡] months after the observation month and $𝑛_{𝑘,𝑡}$ the number of performing accounts that survived in the period (0,𝑡−1], where $𝑡 ={0,1,…,𝑇_𝑘}$ is the number of months since the observation month 𝑘, i.e., $𝑛_{𝑘,0}$ will be the number of performing accounts as at the observation month.

Table 1 is an illustrative example of the defaults table. The number of performing accounts at the start of the observation month 201501 (i.e., $𝑀_1 =201501$) was 500 accounts (i.e., $𝑛_{1,0}$ =500). Of these 500 accounts 10 accounts defaulted in 201502, during the period (0,1] (i.e., $𝑑_{1,1} =10$), and 5 accounts defaulted in 201503, during the period (1,2] (i.e., $𝑑_1,2 =5$). Note that no forecasting is required.

![alt text](wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/03_ifrs9_impairments/05_modelling/pd/image.png)

From the defaults table, the empirical PD’s, per observation month 𝑀𝑘 can be calculated as follow:

$p_{k,t}^m = \frac{d_{k,t}}{n_{k,0}}$ and $p_{k,t}^c = \displaystyle \sum_{i=0}^t \frac{d_{k,i}}{n_{k,0}}$

After having derived the empirical marginal PD estimates 𝑝𝑚
𝑘,𝑡 for the different observation months 𝑀𝑘 and outcome horizons 𝑡 ={1,2,…,𝑇𝑘}, it needs to be decided which of these estimates should contribute to the final PD term structure and how these contributions should be weighted. As mentioned earlier, the model’s objective is to yield PiT PD estimates such that only defaults from the most recent 𝑅 outcome months are used in the final PD estimates. 𝑅 is referred to as the ‘reference period’ and is a key parameter for estimating the PD term structure. A shorter reference period will make the resulting estimates more PiT but could result in unwanted volatility (and vice versa for longer reference periods). If one uses a very long reference period over an entire economic cycle, the resulting PD term structures can be considered to provide through-the-cycle (TTC) estimates. It may sometimes also be required not to use the most recent data, e.g., if models are refreshed in August but should only account for information until June. Hence, a reference month 𝑀 ∈{𝑀1,𝑀2,…,𝑀𝐾} is used in order to denote the last observation month from the set of observations months that is used in the derivation of 𝑝𝑚
𝑘,𝑡. Therefore only defaults from the outcome months {𝑀−(𝑅−2),…,𝑀,𝑀+1} are used for modelling purposes.
We estimated the marginal PD, 
̃
𝑝
𝑚
𝑡, from the defaults table, as the weighted average of marginal PDs across the most recent 𝑅 observation months with available outcome horizons of at least 𝑡 months. A weighting by the number of observations is performed to smooth the impact of outlier months for segments with small and volatile population sizes.
Thus given 𝑅 and a reference month 𝑀 (note that the term structure is generally calculated taking the reference month to be the most recent observation month, i.e., 𝑀 =𝑀𝐾

e estimate the marginal PD for time horizon 𝑡 as
̃
𝑝
𝑚
𝑡⁡(𝑅,𝑀)=
∑𝑀−(𝑡−1)
𝑖=𝑀−(𝑡−1)−(𝑅−1)𝑑𝑖,𝑡
∑𝑀−(𝑡−1)
𝑖=𝑀−(𝑡−1)−(𝑅−1)𝑛𝑖,0
 
.
(4)
For example, if a reference period of 3 months is chosen (𝑅 =3), and the reference month is 201507 (𝑀 =201507), then Table 2 illustrates the resulting marginal PDs.

![alt text](wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/03_ifrs9_impairments/05_modelling/pd/image-1.png)

To summarise, the approach will create PD term structures based on the most recent default information and initial performing accounts as at observation month. It does not require the explicit modelling of future cures or closures, as no survival analysis is required. Below we discuss how the PD term structure is segmented.

We have a single PD term structure at this stage, and typically, a revolving retail credit portfolio is not a homogeneous set of exposures. Hence, it is unlikely that a single PD term structure would adequately fit across different pools of accounts. If the portfolio is left unsegmented, then the resulting PD term structure will represent a combination of low risk PD term structures and high risk PD term structures. Such an unsegmented PD term structure will understate the default risk of high risk customers and overstate the default risk of low risk customers. Typical examples of effects that cause PD term structures to be materially different from a portfolio average are ageing effects and irregular payment behaviours. Young accounts tend to carry significant default risk in the first year or two after origination, but this improves significantly over time.
In contrast, more matured accounts do not show this significant further improvement in later time periods. Customers with irregular payment behaviour in the recent past have a higher risk of defaulting shortly after observation than in later periods, while very low risk customers often show a more constant (or even increasing) default risk over time. Therefore, a steep increasing cumulative PD term structure is needed for the high risk customers, whereas a more linear-shaped cumulative PD term structure would be needed for the low risk customers.
Therefore, it is necessary to identify segments for which the PD term structure shape is structurally different from the shape of the unsegmented PD term structure to ensure an appropriate [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]]. Banks commonly segment their portfolios along business lines, product types and risk characteristics to model more homogeneous loans groups (McPhail and McPhail 2014). To identify these segments, detailed data analysis based on typical dimensions like delinquency cycle, account age or product type is used and often supported by additional insights from business areas.
It is also important to quantify what a materially different term structure constitutes. To assess whether segmented PD term structures are materially different from the corresponding unsegmented PD term structure, the following tests are proposed:
Visual comparison of the segmented PD term structures vs the unsegmented PD term structure: The segmented PD term structures should ideally show no crossings and provide clear [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/02_airb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]].
Comparing the ratio of cumulative segmented PDs over different horizons to the 12 month cumulative segmented PD: Define 𝑅⁢𝑎⁢𝑡⁢𝑖⁢𝑜𝑇⁡(𝑅,𝑀) =
̃
𝑝
𝑐
𝑇⁡(𝑅,𝑀)
̃
𝑝
𝑐
12⁡(𝑅,𝑀)
 
 =
∑𝑇
𝑡=1
̃
𝑝
𝑚
𝑡⁡(𝑅,𝑀)
∑12
𝑡=1
̃
𝑝
𝑚
𝑡⁡(𝑅,𝑀)
 
  for 𝑇 =24, 36, 48 months. These ratios assess the segmented PD term structure’s steepness. The ratios will also show potential levels of over- or underestimations if only the unsegmented PD term structure is used. The ratios can be analysed over time by varying the reference month 𝑀.
Comparison of the cumulative segmented PDs to cumulative unsegmented PDs over time for different horizons: This test will confirm whether the difference between the segmented PD term structures and the unsegmented one remains consistent over different horizons 𝑇 =12, 24, 36, 48 months. The PDs can be analysed over time by varying the reference month 𝑀.
The validity of the suggested segments will be evaluated using these three tests. These three tests are another contribution to this paper and will be illustrated in the case study.

## Run-off Triangles

Run-off triangles (Braun 2004) use the most recent default and closure information to predict the term structure for the performing portfolio. These run-off triangles are often segmented for different risk drivers. The most significant advantage of this approach is that it is easy to design and implement, easy to automate, and generates PiT estimates that are often predictive for the near future. The disadvantages are that the derivation of account specific PD term structures typically requires techniques like the simple linear scaling of segment level PD term structures which may not result in a good fit. Structural changes in the portfolio in the recent past might distort PD term structures (but can be corrected).

The chain ladder method (England and Verrall 2002) is a popular method that insurance companies use to estimate their required claim reserves and can also be used to determine PDs. The chain ladder method utilises run-off triangles and has similar advantages and disadvantages as the run-off triangles provided above.

## Markov Chains

<https://arxiv.org/pdf/2502.14479>

Markov chains (Aalen and Johansen 1978) can also be used to derive PD term structures by multiplication of empirically derived migration matrices that describe the transition between risk states (Cziraky and Zink 2017). To account for different risk drivers, one can either use segmented migration matrices or incorporate these as specific risk states into the migration matrix (e.g., delinquency). The advantages include that one can produce PD estimates for any time horizon. They are easy to design and implement and provide forecasts of future portfolio risk profiles (e.g., what % of today’s portfolio is expected to be delinquent in 12 months) that can be used for budgeting/[[02-stress_testing|stress testing]]. However, the disadvantages are that the standard time-invariant Markov chain assumption typically does not result in a good fit for actual multi-period default behaviour. Additional time-specific (e.g., two months after observation) migration matrices are, in these cases, required to achieve acceptable fits, making the model very complex with limited benefit compared to direct estimation of PD term structures. Furthermore, minor deviations in monthly migrations may lead to significant over- or underestimation for multi-year PDs.

A loan may reside in any one of the following five states at any point 𝑡 of its lifetime: Stage 1 (P), Stage 2 (U), Stage 3 (D), Settled (S) and Written Off (WO); the last of which serves as an absorbing state that signifies debt write-off. Together with a paid-up/settled state, these delinquency states (or arrears categories) constitute the state space within the $k$-month transition matrix 𝑇, thereby incorporating all competing risk events.

A performing loan is typically up-to-date on its payments, though it may accrue payments in arrears until reaching the default threshold, at which point the loan transits to state D. From either of these two transient (and communicating) states {P,D}, a loan may also move into one of the two absorbing states, {S,W}, whereupon observation of the loan ceases thereafter. Practically, and aside from behavioural profiles, the only difference between S and W is a non-zero outstanding balance for W that will need to be written-off as a credit loss.

We will assume that accounts instantly cure and their are no redefaults.

Let $𝑌_𝑡$ ∈ S denote a random variable that can assume one of these five states at time 𝑡 in our state space $S$ ∈ {P,U,D,S,W}. The sequence $𝑌_{1} , . . . ,𝑌_{T}$ then forms a discrete-time first-order Markov chain. Assuming stationarity, the transition matrix $T$ that governs this Markov chain will have as entries the transition probabilities $𝑝_{𝑘𝑙}$ from state $m$ to 𝑙, i.e., $𝑝_{m𝑙} = P (𝑌_𝑡 = 𝑙 | 𝑌_{𝑡−1} = $m$)$ between any two points in time $𝑡-1$ and $𝑡$.

The maximum likelihood estimates (MLEs) of each $𝑝_{m𝑙}$ is $𝑛_{m𝑙}/𝑛_{m}$, where $𝑛_{m𝑙}$ is the number of observed transitions from $m$ to 𝑙 across the sampling window, while $𝑛_{m}$ denotes the number of total transitions starting in $m$. The resulting 𝑇 (Transition Probability Matrix) is therefore expressed as

$T=\begin{bmatrix}
p_{\text{P,P}} & p_{\text{P,U}} & p_{\text{P,D}} & p_{\text{P,WO}} & p_{\text{P,S}}\\
p_{\text{U,P}} & p_{\text{U,U}} & p_{\text{U,D}} & p_{\text{U,WO}} & p_{\text{U,S}}\\
p_{\text{D,P}} & p_{\text{D,U}} & p_{\text{D,D}} & p_{\text{D,WO}} & p_{\text{D,S}}\\
0 & 0 & 0 & 1 & 0\\
0 & 0 & 0 & 0 & 1
\end{bmatrix}$

### Initial State Vector

The ininial state vector $v$ represents the distribution of accounts across states at time $t=1$. For $n$ states, the vector $v_1$ has elements $v_{1,i}$ where it is the proportion of accounts in state $i$ at $t=1$.

### PD Term Structure

Use $T$ to project the distribution of accounts across states over multiple time steps. At time $t$ the state vector $v_t$ is given by:

$v_t = v_1 T^t$

After 12 time steps $t=12$, the probability of an account being in the Default state $D$ is given by the corresponding element in $v_{12}$. This is the equivalent of calculating your 12-month conditional marignal PiT PD. Likewise for a lifetime PiT PD this would be the element in $v_n$

### Soujourn Times

The mean sojourn time for an object in a dynamical system is the amount of time an object is expected to spend in a system before leaving the system. It is the time spent in state $m$ before moving to state 𝑙. The various histograms are all heavily right-skewed, which is to be expected, though the degree thereof differs markedly; e.g., the distribution of P → D vs that of P → S. By inspecting these distributions graphically, it is clear that they are surely not exponentially distributed. This result serves as further proof that the Markov-property is indeed violated, given its requirement for sojourn times to be exponentially distributed.

### Limitations

Despite the acclaim of Markov chains, there are two critical assumptions when modelling default risk:

1. That the transition matrix is largely **stationary over time**.
2. That the **population is homogenous** regarding payment behaviour.

#### Beta Regression

>That the transition matrix is largely stationary over time.

A non-stationary Markov chain implies a time-dependent transition matrix $T(t')$, where each matrix cell  $T_{ml}(t') = p_{ml}(t')$, itself denoting the estimated transition probability from state $m$ to $l$ between calendar dates $t'_2$ and $t'_1$, represents an element of a broader time series. When modelling such percentage-valued panel data, one can use a class of techniques known as beta regression (BR) models which can incorporate any set of input variables.

The time-homogeneous transition matrix 𝑇 can be easily re-estimated as a time-dependent quantity $𝑇(𝑡')$ over calendar time 𝑡' = $𝑡'_1, . . . , 𝑡'_n$, e.g., Jan-2007 to Dec-2022. Having partitioned the data by monthly cohort 𝑡′, each matrix element in $𝑇(𝑡')$ is the time-dependent transition probability $𝑝_{m𝑙}(𝑡')$ from state 𝑘 to 𝑙, estimated simply using MLE as:

$𝑝_{m𝑙}(𝑡') = \large\frac{n_{m𝑙}(𝑡')}{n_{m}(𝑡')}$

In particular, $n_{m𝑙}(𝑡')$ denotes the number of transitions from $m$ to 𝑙 during the interval $(𝑡' − 1, 𝑡']$, while $n_{m}(𝑡')$ similarly represents the total volume of transitions starting in $m$ during the same interval.

For each $(m,l)$, you then get a time series of specific transition probabilities:

$𝑇(𝑡')^{ml} = 𝑇(𝑡_1')^{ml}, ..., 𝑇(𝑡'_m)^{ml}$

This time series may then be modelled using a beta regression (BR) model.

Consider the dataset $D = \{𝑡', $m$, 𝑙, 𝑇(𝑡')^{ml} ,X_1(𝑡')^{ml} , X_2(𝑡')^{ml}\}$ over calendar reporting time $𝑡' = 𝑡'_1 , . . . , 𝑡'_𝑛$. We shall construct a set of BR-models with variable dispersion (VDBR), one for each transition type of interest, from state $m$ to 𝑙. In so doing, we relate the transition rate $𝑇(𝑡')^{ml}$ over 𝑡' with two sets of input variables, denoted by $X_1(𝑡')^{ml}$ and $X_2(𝑡')^{ml}$, which contain predictive information that are specific to the transition type $m$ → 𝑙; thereby embedding heterogeneity at the portfolio-level e.g. proportion of loans in arrears, prevailing inflation rate. Each BR-model is then constructed by modelling both its mean $\mu(𝑡')^{ml}$ and precision $\sigma(𝑡')^{ml}$ parameters for state $m$ to 𝑙.

#### Multinomial Logistic Regression

>That the population is homogenous regarding payment behaviour.

In fully catering for any degree of heterogeneity during PD-modelling, the modus operandi should clearly veer away from directly predicting the portfolio’s aggregate behaviour, and rather towards predicting that of its constituent loans; i.e., loan-level modelling. Within each cell of $T(t')$, either model predicts the corresponding transition probability $p_{ml}(t', x_i)$ given the characteristics $x_i$ of each loan $i$.

In statistics and probability, "multinomial" refers to a generalization of the binomial distribution, used to model scenarios where each trial can result in one of several possible outcomes, rather than just two (like success or failure).

The probabilities $\{𝑝_1, ..., 𝑝_𝑗, ... , 𝑝_J\}$ of assuming any particular outcome 𝑗 can be written in terms of the category counts $𝑛_1, ..., 𝑛_𝑗, ..., 𝑛_𝐽$. These category counts follow a
multinomial distribution, which yields the joint probability of assuming any particular combination of category counts. An MLR-model then relates the conditional probability $𝑝_𝑗(𝒙_𝑗) = P(𝑌=𝑗|𝒙)$ to a set of input variables $𝒙_𝑗$ for category 𝑗 using a logit link function 𝑔(·). In particular, and with reference to some baseline-category $J' ∈ [1, J]$, the conditional mean $\mu _{𝑗𝑖}$ for the 𝑗th outcome and for loan 𝑖 = 1, . . . , 𝑛 is modelled as:

$g(\mu _{ij})=\log\Large\frac{𝑝_𝑗(𝒙_{ji})}{𝑝_𝑗(𝒙_{J'i})}$ $ = \beta_{j0} + \beta_{j1}x_{ji1} + ... + \beta_{j1n}x_{jin}$ for $j\neq J'$

The formulation above implies that an MLR-model will have 𝐽 − 1 logit functions, where each model 𝑗 has a separate coefficient vector $𝜷_𝑗$ from the next model. In turn, one will have to estimate (𝐽 − 1)(𝑝 + 1) coefficients in total.

Now when we consider the time component, let $y_{it}$ denote the observed value from $Y_t$ for loan $i$ over its lifetime $T$ at each discrete time point $t = t_1, . . . , T$ . These $y_{it}$ ∈ {P, D, S, W} values are nominal in nature and are encoded accordingly for the ending state 𝑙 = 1, . . . , 4 as:

$
y_{it} =
  \begin{cases}
    1 & \text{if loan } i \text{ ends in state } l=P \text{ at time }t \\
    2 & \text{if loan } i \text{ ends in state } l=U \text{ at time }t \\
    3 & \text{if loan } i \text{ ends in state } l=D \text{ at time }t \\
    4 & \text{if loan } i \text{ ends in state } l=S \text{ at time }t \\
    5 & \text{if loan } i \text{ ends in state } l=W \text{ at time }t \\
  \end{cases}
$

The various transition probabilities $𝑝_{𝑘𝑙}$ can be written as a linear function of input variables $X_i^{𝑘𝑙}$ , i.e., $𝑝_{𝑘𝑙}(X_i^{𝑘𝑙}) = P(Y_t=l | Y_{t-1}=k, X_i^{𝑘𝑙})$ for loan $i$ with a with a vector of $n$ characteristics.

We shall fit two MLR-models respective to the starting states 𝑘 ∈ {P, D}, since the other states are absorbing.

Lastly, the input variables $X^{𝑘𝑙}$ of the MLR-models reprise those from the beta regression model  denoted as $X(𝑡',[q])^{kl}$ and $X(𝑡',[p])^{kl}$ for the $q^{th}$ time period of the $p$ observations, but also incorporate the following loan account-level $[a]$ idiosyncratic variables:

1. time-fixed variables specific to loan 𝑖, denoted by $X(𝑡',[a])^{kl}$, e.g., the chosen payment method;
2. time-dependent variables specific to loan 𝑖 and period 𝑡, denoted by $X(𝑡',t,[a])^{kl}$, e.g., the delinquency level.

## Hazard Models

https://www.researchgate.net/publication/391443830_Towards_modelling_lifetime_default_risk_Exploring_different_subtypes_of_recurrent_event_Cox-regression_models

https://www.researchgate.net/publication/393890374_Approaches_for_modelling_the_term-structure_of_default_risk_under_IFRS_9_A_tutorial_using_discrete-time_survival_analysis

Hazard models (Țurlea 2021) can be used to assess the riskiness of the obligor by computing a score that indicates whether the obligor defaults within the specified horizon. However, the models can be quite complex, and the model does not determine when the obligor defaults will occur (Crook and Bellotti 2013). More generally, survival analysis can also be used (Chimezda and Marimo 2017).

## ARIMA Models

Autoregressive models (Glen 2015) can also be used where future default rates are modelled as a function of previous default rates. Additional risk drivers can be included in the modelling process as separate covariates in the regression. One of the most significant advantages of autoregressive models is that they can incorporate macroeconomic forecasts in the regression. However, disadvantages include that very granular [[07-segmentation|segmentation]] is often not possible, which leads to top-down approaches being required. Autoregressive models are sometimes sensitive to recent changes (e.g., driven by credit policy changes).

## Lorenz Curve Calibration

https://www.mdpi.com/2227-9091/9/11/208

## Machine Learning Models

Using machine learning models like XGBoost to calibrate m-month PDs is a practical alternative to traditional models such as the Cox Proportional Hazards (CPH) model or Markov Chains, particularly when handling large datasets with complex non-linear relationships. The goal is to train a machine learning model (e.g., XGBoost) to predict the m-month Probability of Default (PD) directly or infer it through intermediate predictions (e.g., month-by-month PDs).

Use account-level data to determine whether an account defaults within m months **(TTD)**. Optionally, create intermediate targets for shorter time horizons (e.g., 1-month PDs). For each account i, create a binary target (1 if account defaults within m months, 0 otherwise).
