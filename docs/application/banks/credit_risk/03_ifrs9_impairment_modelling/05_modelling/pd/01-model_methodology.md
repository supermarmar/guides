# Model Methodology (PD)

The calibration process differs for new business (typically informed by application scorecards) and existing business (typically informed by behavioral scorecards). Behavioural scorecard methodologies will be described below.

## Markov Chains

One class of portfolio-level modelling techniques that can overcome the challenges stated before is that of Markov models, wherein a dynamic phenomenon (e.g., delinquency) is modelled as a stochastic process that depends only on the current state.

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

## Binary Logistic Regression

Instead of MLR-models, future work can pursue fitting a binary logistic regression model for each transition type. The literature on using binary logistic regression (LR) as a generic supervised classifier is quite extensive and its use within banking is ubiquitous, particularly in the field of application credit scoring, as was first demonstrated in Wiginton (1980). The technique is considered by many authors to be the **most successful modelling technique** thus far in quantitative finance.

Beyond application credit scoring, this technique is also typically used in pre-screening loan offers, detecting fraud cases, scoring collection success, informing direct marketing offers, and in risk-based pricing.

At the very least, this technique and its results can serve as a benchmark when using more advanced classification techniques in future.

For each $m$-month PD for each loan $i$ the logit function can be defined as

$g(\mu _{j})=\log\Large(\frac{𝑝(𝒙_{i})}{1-𝑝(𝒙_{i})})$ $ = \beta_{0} + \beta_{1}x_{i1} + ... + \beta_{1n}x_{in}$ 

## XGBoost

Using machine learning models like XGBoost to calibrate m-month PDs is a practical alternative to traditional models such as the Cox Proportional Hazards (CPH) model or Markov Chains, particularly when handling large datasets with complex non-linear relationships. The goal is to train a machine learning model (e.g., XGBoost) to predict the m-month Probability of Default (PD) directly or infer it through intermediate predictions (e.g., month-by-month PDs).

Use account-level data to determine whether an account defaults within m months **(TTD)**. Optionally, create intermediate targets for shorter time horizons (e.g., 1-month PDs). For each account i, create a binary target (1 if account defaults within m months, 0 otherwise).
