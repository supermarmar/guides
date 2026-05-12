# <mark style="background: #FFF3A3A6;">Probability of Default</mark>

The important considerations when calculating PD are:

- Definition of default (DoD)
- Time Horizon: 1m, 2m, ... 12m .... Lifetime
- Rating philosophy: point-in-time (PIT) versus through-the-cycle (TTC)

In terms of the element of the philosophy, banks will likely calculate both the PIT and TTC PD estimates for various differing purposes.
## <mark style="background: #FFF3A3A6;">Point-in-Time</mark>

PIT PDs assess the probability of an entity defaulting over a specific period given available information at a point in time in the economic cycle. Even though it is only focused on one point in time, it should include an assessment of the entity’s ability to withstand adverse economic events. PiT PD is a **model-driven, forward-looking, and conditioned on current economic information**. **PiT PD** conditions on the current state of the economy and the obligor's current financial position. It rises in downturns and falls in expansions.

IRB PiT PD models are traditionally based on an expectation over the next twelve months. [[ifrs9_standard|IFRS 9]] requires a forward looking – or Forward in Time (FiT) – approach. The expectation as part of the [[ifrs9_standard|IFRS 9]] requirements is that both a 12 month and lifetime FiT PD are calculated with macroeconomic factors considered.

| Feature                   | IFRS 9                                                                                                                                                                         | IRB                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| PD Types                  | FIT                                                                                                                                                                            | TTC (Output from Vasicek-Merton Model)                                                |
| Rating Philosophy         | Dynamic PiT                                                                                                                                                                    | TTC, PiT or Dynamic PiT                                                               |
| Macroeconomic Sensitivity | High                                                                                                                                                                           | Low                                                                                   |
| Update Frequency          | Monthly                                                                                                                                                                        | Annual or Longer                                                                      |
| Data Period               | Borrower specific time                                                                                                                                                         | Full economic cycle (at least 5 years)                                                |
| Horizon                   | 12m and lifetime                                                                                                                                                               | 12m                                                                                   |
| Level of Granularity      | Contract level                                                                                                                                                                 | Counterparty level                                                                    |
| Flooring                  | No floor                                                                                                                                                                       | 0.03% floor                                                                           |
| Data Inputs               | Model includes all reasonable and supportable information about past events, current conditions and forecasts of future macroeconomic conditions (forward looking perspective) | Model includes only variables representing the intrinsic quality to the counterparty. |
PIT PDs are more useful in the case of a bank needing accurate and timely information on likely defaults – i.e. it is closer to the default rate and used updated information throughout time. This will allow the bank to manage its risk and the related capital more efficiently, as well as being useful for provisioning and [[ifrs9_standard|IFRS9]] purposes. However, it does require fluctuating PDs and continuous reviewing of the bank’s clients, as well as regular changes in the bank’s capital. This can be costly.
## <mark style="background: #FFF3A3A6;">Through-the-Cycle</mark>

**TTC PD** is estimated by averaging observed default rates across a full credit cycle (expansion and contraction). Because it smooths out the cycle, it is relatively stable over time. This stability is exactly why Basel IRB uses it for Pillar 1 RWA — regulators do not want capital requirements swinging dramatically with the economy (procyclicality concern). A bank's internal rating system under IRB is designed to assign obligors to grades whose TTC PD is stable, meaning ratings don't migrate simply because the macro environment has deteriorated.

TTC PDs assess the probability of an entity defaulting throughout a long-term economic cycle. TTC PDs will inherently include this ability to withstand adverse economic events, as it will most often be the average PD over an economic cycle. The structure of these PDs over time is illustrated in the figure below.

![alt text](pit_vs_ttc.png)

TTC PDs are smoother and can be used for a longer-term view; thus, they reduce the aforementioned costs. However, a shortfall of these PDs is that they are not as successful at identifying defaults and may cause losses in this area.

## <mark style="background: #FFF3A3A6;">Transformations</mark>

### 12m PiT to 12m TTC

TTC PDs can often be calculated using PIT PDs, albeit removing the credit cycle effects.

A bank often builds a PiT scorecard/model, maps scores to risk grades, then derives TTC PDs for those grades by averaging PiT PDs across historical cycles. This satisfies both IFRS 9 (PiT for ECL) and IRB (TTC for RWA) from a common modelling framework.

### 12m TTC to WCDR

Credit rating systems focus mostly on producing a conservative PD-estimate that remains static (but stressed) over the lifetime of each loan, often by design.

The broad goal of such systems is to facilitate the estimation of regulatory and [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/credit_concentration_risk/01-context|economic capital]], which should absorb any catastrophic (or unexpected) losses under the [[basel_framework|Basel framework]] from the [[bis|BCBS]]. Any temporal effects that might affect the PD during loan life are therefore largely ignored, together with any macroeconomic influences; particularly since the latter is already assumed to be stressed to a recession-like level during PD-estimation. Doing so renders the resulting PD-estimates as through-the-cycle (TTC) in that they should at least approximate the long-run averages of 1-year (12-month) historical default rates over a full macroeconomic cycle, as required during capital estimation. While these TTC PD-estimates are certainly stable over time by design, they are also typically inaccurate within any other setting besides capital estimation.

Put simply, a TTC PD is a measure of the likelihood that a borrower will default over a specific time horizon, calculated in a way that smooths out fluctuations caused by economic or business cycles. It reflects a borrower's average risk of default under both favorable and unfavorable economic conditions. The goal of TTC PD is to isolate a borrower's intrinsic credit risk (their ability to meet obligations independent of short-term economic changes).

![alt text](ttc_vs_pit_pd.png)

In this case, the TTC population PD  seen in the graph above (population being segmented by risk grades) is also the same TTC for the borrower (i.e. this is the LRA PD calibrated at the end of the [[07-risk_quantification|risk quantification]] step per risk grade):

$\text{PD}_{i}^\text{TTC}(12,x_{i},[t_a',t_b'])$

And it is this TTC PD that is used to aquire the systemically conditional PD (denoted as the PIT for population) used in the RWA calculation:

$\text{WCDR}=\text{PD}_{i}^\text{SysPiT}(12,x_{i}|\text{S}_{99.9^{th}}=N^{-1}(0.999)) = N(\large\frac{N^{-1}(p^*)+\sqrt{\rho}N^{-1}(0.999)}{\sqrt{1-\rho}})$

where $p^* = \text{PD}_{i}^\text{TTC}(12,x_{i},[t_a',t_b'])$

For [[ifrs9_standard|IFRS 9]] models, we are interested in the PiT PD for the borrower (which is modeled during the [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/05_modelling/pd/03-risk-differentiation|risk differentiation]] phase) since we require not only a 12-month PD, but a lifetime one as well, or even a term-structure of PDs.

### 12m TTC to 12m Systemic PiT

Conditional PiT PD and LGD values can be obtained by adjusting the pre-MoC and pre-floored IRB TTC PD (i.e. LRA PDs) for the macroeconomic impact using a Vasicek model (at a risk grade level not an individual borrower level). The Vasicek model links the impact of systematic risk to a single (unobservable) factor. Macro-economic factors can be used to approximate the single factor in the Vasicek model.

$\text{PD}_{i}^\text{SysPiT}(12,x_{i}|\text{S}_{1-\alpha^{th}}=N^{-1}(1-\alpha)) = N(\large\frac{N^{-1}(p^*)+\sqrt{\rho}N^{-1}(1-\alpha)}{\sqrt{1-\rho}})$ for a given $\alpha$ that corresponds to the current PiT.

### 12m Systemic PiT to Lifetime PD

Likewise, IRB PDs need to be extended from a 12-month horizon to a remaining lifetime. As rating is a key identifier for classifying assets between the three stages, it is necessary to extend the 12-month PD on a rating level. However, migrations between different ratings can occur over time.

The impact of migrations between ratings is considered by using migration matrices:

- Two migration matrices are multiplied with each other to obtain the 2-year migration matrix, The last column of the resulting matrix now represents a 2-year cumulative PD.
- The 12-month marginal PD for the second year is obtained by subtracting the 1-year PD from the 2-year cumulative PD.
- Going forward, the n-th year cumulative PD is obtained from multiplying n migration matrices, and the n-th year 12-month PD is obtained by subtracting the (n - 1)th year cumulative PD from the n-th year cumulative PD.
- In order for the lifetime PD to represent current and future macro-economic conditions, the migration matrices used in this calculation are made PiT by linking it to the “state of the economy” per year in the future.