# SICR Performance Metrics

An important component of [[ifrs9_standard|IFRS 9]] modelling is the set of staging criteria. The evaluation of the staging criteria can be performed with quantitative indicators on stage transfers.

These types of metrics should be used to adequately assess the SICR criteria, including the calibration of quantitative SICR criteria.

- Proportion of transfers to stage 2 due to change in PD
- Proportion of transfers to stage 2 due solely to qualitative criteria
- Proportion of transfers to stage 2 due solely to backstop indicators
- Difference in PD for stage 2 and stage 1
- Stage 2 outflow to stage 1 (3-month average)
- Proportion of stage 3 that spent less than 12 months in stage 2
- Proportion of stage 3 that spent less than 6 months in stage 2
- Assessment of transition matrix among stages
- Comparison between transfer rate from stage 1 to 3 and from stage 2 to 3
- Proportion of stage 3 exposures moved directly from stage 1
- Comparison between default rates of stage 1 and Stage 2
- Average time in stage 2 before moving to stage 3

Some of these measures focus on SICR-predictions at the loan account-level (as summarised over time), while others are defined at the portfolio-level; both aggregation levels provide useful perspectives. These performance measures can also be applied more generally on the predictions and/or decisions of any binary SICR-classification system under [[ifrs9_standard|IFRS 9]]. Doing so can foster comparability with our results, as well promote standardisation across the industry when evaluating or auditing SICR-decisions.

 Prevalance

Assume a sample $D = \{𝑖, 𝑡, 𝑦_{𝑖𝑡}\}$ of binary-valued SICR-outcomes $𝑦_{𝑖𝑡}$ that are observed for accounts 𝑖 = 1, ... ,𝑁 at each period $𝑡 = 𝑡_1, . . . , 𝑇_𝑖 − 𝑘$ over each account’s lifetime $𝑇_𝑖$ from its time of initial recognition $𝑡_1$.

Given D of size $𝑛 = |D|$, we estimate the prevalence using Iverson brackets [·] as:

```math
𝜙_{d,s,k}=\frac{1}{n}\displaystyle\sum_{i,t \element D} [y_{i,t}=1]
```

Put differently, 𝜙 is the proportion of rare events in D, which also measures the degree of class imbalance. Longer outcome periods also result in fewer observed SICR-outcomes, which explains the decreasing 𝜙-values, thereby signifying increased rarity.

 SICR-rates

Denoted as $𝐴_𝑡$ , the SICR-rate estimates at reporting/calendar time 𝑡 the portfolio-level transition probability of moving from Stage 1 to Stage 2 impairment over a 𝑘-month period. More formally, $𝐴_𝑡$ estimates at 𝑡 the conditional probability $P(𝑌_{𝑡+𝑘} = 1| 𝑌_𝑡 = 0)$ of becoming SICR-flagged later at 𝑡 + 𝑘, where $𝑌𝑡 ,𝑌_{𝑡+1}, . . .$ are Bernoulli random variables that represent the SICR-status over 𝑡, as given by $G(𝑑, 𝑠, 𝑡)$.

```math
A_t = \frac{1}{n_t}\displaystyle\sum_{i,t \subset S_1(t)} [y_{i,t}=1]
```

While the eqaution above yields the actual SICR-rate over time, the account-level predictions from an underlying SICR model can be similarly aggregated into an expected SICR-rate $B_𝑡$ , which can be duly compared to $𝐴_𝑡$ . This $B_𝑡$ -quantity similarly estimates at 𝑡 the conditional probability $P(𝑌_{𝑡+𝑘} = 1| 𝑌_𝑡 = 0, 𝑿)$ of becoming SICR-flagged later at 𝑡 + 𝑘, given the random input vector 𝑿.

Estimating this probability implies developing a SICR-model from
data, which can then be used to render predictions on new data.

```math
B_t = \frac{1}{n_t}\displaystyle\sum_{i,t \subset S_1(t)} p_1(x_{i,t})
```

We formulate another variety of $B_t$ called the discretised expected SICR-rate $𝐶_𝑡$, wherein the underlying SICR-model (itself a discriminative/probabilistic classifier) is first dichotomised into a discrete classifier. This dichotomisation requires evaluating each SICR-prediction against a static cut-off 𝑐 ∈ [0, 1], thereby producing a
discrete SICR-prediction.

```math
C_t = \frac{1}{n_t}\displaystyle\sum_{i,t \subset S_1(t)}[ p_1(x_{i,t})>c_{d,s,k}]
```

 Mean Rate

This quantity is simply the sample mean of portfolio-level SICR-rates over time. Given the actual SICR-rates $𝐴_𝑡$ we estimate the SICR-mean over reporting time $𝑡 = 1, . . . , 𝑡_𝑛$ as:

$\bar A = \frac{1}{t_n} \sum_t A_t$

 Instability

Denoted as 𝜎, the instability refers to the degree to which a series of portfolio-level SICR-rates varies over time.

 Prediction Dynamicity

Denoted as 𝜔, the dynamicity represents the extent to which the SICR-predictions (or probability scores) vary over the lifetime of an average loan account.

More formally, we first estimate each $𝜔_𝑖$ by calculating the account-level standard deviation of scores for each account 𝑖 in a given sample D, expressed as:

where $𝑛_𝑖 = 𝑇_𝑖 − 𝑘 > 0$ denotes the number of probability scores that are available for account 𝑖 in D. We finally estimate 𝜔 as:

Smaller outcome periods clearly yield more accurate SICR-models that also produce more dynamic account level SICR-predictions. However, this dynamicity may not necessarily translate to the portfolio-level, especially since smaller 𝑘-values also produce more stable SICR-rates. At the account-level, extremely dynamic SICR-predictions (e.g., $𝑘 ≤ 3$) can lead to rapid oscillations in moving an account between Stages 1 and 2 over time. This oscillatory effect dampens the overall transition into Stage 2 when aggregating across accounts, hence the less responsive SICR-rate.

 AUC & ROC & Gini

Secondly, the area under the curve (AUC) summarises a classical ROC-analysis (receiver operating characteristic) in measuring a model’s discriminatory power.

AUC-values suggest that smaller outcome periods yield more accurate SICR-models than longer periods. This result corroborates the work of Kennedy et al. (2013) and Mushava and Murray (2018) wherein the outcome period was similarly varied in PD-modelling – an older ‘cousin’ of SICR-modelling. The plateauing effect in AUC-values suggest yet again that examining smaller 𝑘 ≤ 18 values is a more worthwhile endeavour.

This trend is mirrored in the discrete AUC-values, having dichotomised the SICR-predictions using 𝑐 as thresholds. Fewer SICR-outcomes can generally exacerbate the modelling task, which is why AUC decreases as 𝑘 increases.

The midpoint 𝑘 = 9 therefore seems ‘optimal’ when considering the various trade-offs.

 MAE

Most mean absolute error (MAE) between $𝐴_𝑡$ and $𝐵_𝑡$ ($𝑚_1$), are fairly similar with a mean error of 0.44% across 𝑘, barring 𝑘 ≥ 36. This result corroborates the relatively high AUC-values in the table above and visually suggests greater agreement as 𝑘 increases. Having dichotomised the SICR-models, a discretised expected SICR-rate ($C_𝑡$) emerges, which is similarly compared to 𝐴𝑡 and summarised again with the MAE ($𝑚_2$). Clearly, there is more disagreement between either rates, particularly during the 2008-GFC, with a mean $𝑚_2$-value of 1.11% across 𝑘; almost three times larger that of $𝑚_1$. Nonetheless, the smallest $𝑚_2$-value still occurred at 𝑘 = 9, which further supports its selection as the prudential choice.

## Modelling vs Comparison

Our SICR-modelling framework aims to provide a new and flexible way of conducting SICR-classification that is more proactive, focused, accurate, and dynamic than that of the classical PD-comparison approach. It is only natural then to compare the old to the new in identifying a superior approach.

We therefore examine a few different choices of 𝑢 ∈ {100%, 120%, 150%, 180%, 200%, 300%} using discretion, though which deliberately includes the candidate 𝑢 = 200% from the [[eba|European Banking Authority]] (2018), or [[eba|EBA]]. Accordingly, the actual and discretised expected 1-month SICR-rates can be estimated respectively from the resulting sample of $𝑦_{𝑖𝑡}$ and $ℎ(𝒙_{𝑖𝑡})$ values. The prediction accuracy of the resulting SICR-classification is similarly gauged using ROC-analysis.

In summarising the ROC-analysis, the AUC-values clearly indicate that the prediction accuracy of $H$ is substantially inferior to that of any SICR-model, regardless of 𝑢.

Moreover, the AUC-values appear to be a monotonically decreasing function of 𝑢, where the AUC seems to deteriorate rapidly for 𝑢 ≥ 150%. The
[[eba|EBA]]-recommended threshold of 𝑢 = 200% produced some of the most inaccurate SICR-predictions.

In comparing approaches, we select SICR-definition 1b(iii) and consider the resulting SICR model, which was previously motivated in subsection 4.3 as one of the best-performing SICR-models. Using the corresponding $𝑐_{129}$-value from Table 4 for this definition (𝑑 = 1, 𝑠 = 2, 𝑘 = 9), we dichotomise this SICR-model and similarly evaluate its discrete predictions within the validation set using ROC-analysis.

The resulting AUC-value of 76.8% indicates a decent level of accuracy, which compares favourably to that of the $H$-classifier. While its account-level prediction accuracy is clearly atrocious, the $H$-classifier may perform more admirably on the portfolio-level.

We therefore compare the time graphs of actual vs discretised expected SICR-rates, respective to both approaches and shown below. All of the expected rates across both approaches seemingly exceed their actual counterpart for most periods, which is certainly risk-prudent under [[ifrs9_standard|IFRS 9]]. However, the degree of such over-prediction amounts to misallocated funds and wasted provisions, which can again be measured using the MAE
between two SICR-rates. The [[eba|EBA]]-threshold (𝑢 = 200%) achieves a respectable MAE-value, which is reasonably close to that of the SICR-model, albeit still worse. More importantly, the MAE-value of the [[eba|EBA]]-threshold is more than 7 times lower than that of the best-AUC threshold (𝑢 = 100%). Despite its improved prediction accuracy at the account-level, the best-AUC threshold clearly results in an overly conservative SICR-rate at the portfolio-level, which surely poses an immense opportunity cost.

It also demonstrates different volatility patterns in the underlying SICR-rates across both approaches. In particular, the actual SICR-rate (in green) from the PD-comparison approach reacted rather mildly to the onset of the 2008-GFC, relative to its counterpart (in pink) from the SICR-modelling approach. We largely ascribe this result to the former’s use of 𝑘 = 1, which usually causes volatility in PD-modelling due to risk immaturity in the outcomes;

On the other hand, the two expected SICR-rates from the PD-comparison approach either under-predict their actual counterpart during the 2008-GFC (shown in orange: [[eba|EBA]]-threshold), or massively over-predict it (shown in purple: best-AUC threshold). Both of these results are unsatisfactory and highlight the main drawbacks of the PD-comparison approach: 1) its tacit reliance on an appropriately accurate PD-model; and 2) its extraordinary sensitivity to the 𝑢-threshold. In contrast, both rates (in yellow and pink) from the SICR-modelling approach react more flexibly and intuitively as the 2008-GFC unfolds, having achieved a more pronounced peak at the height of the crisis without becoming excessive. Although decent, the dichotomisation of the SICR-model can surely be improved in future studies by tweaking the $𝑐_{129}$-threshold, which should result in even better performance. However, and in finalising the approach comparison, the evidence suggests that the SICR-modelling approach is objectively the superior approach.

Our approach is more parsimonious than PD-comparisons since
the inputs of a SICR-model can relate more directly to the change in delinquency risk, instead of just default risk alone. As one of these inputs, the PD-ratio already signifies the change in risk since initial recognition, thereby rendering the predictions from a SICR-model as compliant with §5.5.9 of [[ifrs9_standard|IFRS 9]]. Moreover, a SICR-modelling approach allows drawing statistical inference on the drivers of the overall SICR-process as a stochastic phenomenon, which can certainly help in portfolio management. Lastly, our approach prevents any pre-existing issues within a PD-model from bleeding into staged impairment classification under [[ifrs9_standard|IFRS 9]], which can be another practical benefit.

The 𝑠-parameter has a stabilising yet costly effect on SICR-classification, wherein SICR-events become scarcer as 𝑠 increases. Greater stickiness yield account-level SICR-predictions that are more accurate but also less dynamic over loan life. From these stickier SICR-definitions, the resulting portfolio-level SICR-rates become less dynamic over time, have lower means, and are increasingly insensitive to the 2008-GFC. Furthermore, both 𝑘 and 𝑠 parameters interact with each other in that SICR-predictions become more accurate as 𝑘 decreases and 𝑠 increases. However, the dynamicity of account-level predictions decreases for larger 𝑠 but increases again for smaller 𝑘. Lastly, choosing 𝑑 = 2 yields extremely scarce SICR-events across all values of 𝑠 and 𝑘, which would compromise the resulting Stage 2 provision-levels if used; a result that supports the ‘backstop’ (𝑑 = 1) of [[ifrs9_standard|IFRS 9]]. These trends form a reusable analytical framework in which any SICR-definition can be examined on the following four factors: the accuracy and dynamicity of the resulting SICR-predictions, the instability of implied SICR-rates, and its responsiveness to economic distress. A reasonable trade-off exists amongst these factors when choosing 𝑘 = 9 across any 𝑠-value, as well as when selecting 𝑠 = 2 across 𝑘 ∈ {6, 9}.
