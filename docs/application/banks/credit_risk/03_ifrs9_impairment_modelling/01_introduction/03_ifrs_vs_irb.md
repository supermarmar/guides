# IFRS 9 vs IRB

Banks around the globe leverage their well-established IRB models as starting point to satisfy the IFRS 9 modelling needs. The IRB PD, LGD and EAD parameters are typically TTC with some flooring and Margin of Conservatism (MoC) added. IFRS 9 requires the use of forward looking PIT parameters or conditional FiT parameters. The outcome of the IRB models is adjusted for IFRS 9 purposes to reflect forward looking and macro-economic information.

## PD

### Through-the-Cycle (TTC) PDs

Credit rating systems focus mostly on producing a conservative PD-estimate that remains static (but stressed) over the lifetime of each loan, often by design.

The broad goal of such systems is to facilitate the estimation of regulatory and economic capital, which should absorb any catastrophic (or unexpected) losses under the Basel framework from the BCBS. Any temporal effects that might affect the PD during loan life are therefore largely ignored, together with any macroeconomic influences; particularly since the latter is already assumed to be stressed to a recession-like level during PD-estimation. Doing so renders the resulting PD-estimates as through-the-cycle (TTC) in that they should at least approximate the long-run averages of 1-year (12-month) historical default rates over a full macroeconomic cycle, as required during capital estimation. While these TTC PD-estimates are certainly stable over time by design, they are also typically inaccurate within any other setting besides capital estimation.

Put simply, a TTC PD is a measure of the likelihood that a borrower will default over a specific time horizon, calculated in a way that smooths out fluctuations caused by economic or business cycles. It reflects a borrower's average risk of default under both favorable and unfavorable economic conditions. The goal of TTC PD is to isolate a borrower's intrinsic credit risk (their ability to meet obligations independent of short-term economic changes).

![alt text](images/ttc_vs_pit_pd.png)

In this case, the TTC population PD  seen in the graph above (population being segmented by risk grades) is also the same TTC for the borrower (i.e. this is the LRA PD calibrated at the end of the risk quantification step per risk grade):

$\text{PD}_{i}^\text{TTC}(12,x_{i},[t_a',t_b'])$

And it is this TTC PD that is used to aquire the systemically conditional PD (denoted as the PIT for population) used in the RWA calculation:

$\text{PD}_{i}^\text{SysPiT}(12,x_{i}|\text{S}_{99.9^{th}}=N^{-1}(0.999)) = N(\large\frac{N^{-1}(p^*)+\sqrt{\rho}N^{-1}(0.999)}{\sqrt{1-\rho}})$

where $p^* = \text{PD}_{i}^\text{TTC}(12,x_{i},[t_a',t_b'])$

For IFRS 9 models, we are interested in the PiT PD for the borrower (which is modeled during the risk differentiation phase) since we require not only a 12-month PD, but a lifetime one as well, or even a term-structure of PDs.

### Point-in-Time (PiT) PD

IRB PiT PD models are traditionally based on an expectation over the next twelve months. IFRS 9 requires a forward looking – or Forward in Time (FiT) – approach. The expectation as part of the IFRS 9 requirements is that both a 12 month and lifetime FiT PD are calculated with macroeconomic factors considered.

|Feature|IFRS 9|IRB|
|-|-|-|
|PD Types|PIT or FIT|TTC|
|Macroeconomic Sensitivity|High|Low|
|Update Frequency|Monthly|Annual or Longer|
|Data Time Horizon|Borrower specific time|Full economic cycle (at least 5 years)|
|Horizon|12m and lifetime|12m|
|Level of Granularity|Contract level|Counterparty level|
|Flooring|No floor|0.03% floor|
|Data Inputs|Model includes all reasonable and supportable information about past events, current conditions and forecasts of future macroeconomic conditions (forward looking perspective)|Model includes only variables representing the intrinsic quality to the counterparty.|

### Converting 12m TTC PD to 12m PiT PD

Conditional PiT PD and LGD values can be obtained by adjusting the pre-MoC and pre-floored IRB TTC PD (i.e. LRA PDs) for the macroeconomic impact using a Vasicek model (at a risk grade level not an individual borrower level). The Vasicek model links the impact of systematic risk to a single (unobservable) factor. Macro-economic factors can be used to approximate the single factor in the Vasicek model.

$\text{PD}_{i}^\text{SysPiT}(12,x_{i}|\text{S}_{1-\alpha^{th}}=N^{-1}(1-\alpha))$ for a given $\alpha$ that corresponds to the current PiT.

### Converting 12m PiT PiT to 12m Lifetime PD

Likewise, IRB PDs need to be extended from a 12-month horizon to a remaining lifetime. As rating is a key identifier for classifying assets between the three stages, it is necessary to extend the 12-month PD on a rating level. However, migrations between different ratings can occur over time.

The impact of migrations between ratings is considered by using migration matrices:

- Two migration matrices are multiplied with each other to obtain the 2-year migration matrix, The last column of the resulting matrix now represents a 2-year cumulative PD.
- The 12-month PD for the second year is obtained by subtracting the 1-year PD from the 2-year cumulative PD.
- Going forward, the n-th year cumulative PD is obtained from multiplying n migration matrices, and the n-th year 12-month PD is obtained by subtracting the (n - 1)th year cumulative PD from the n-th year cumulative PD.
- In order for the lifetime PD to represent current and future macro-economic conditions, the migration matrices used in this calculation are made PiT by linking it to the “state of the economy” per year in the future.

## LGD

|Feature|IFRS 9|IRB|
|-|-|-|
|LGD Types|PIT (Point-in-Time) view with forward looking adjustment (no downturn required)|TTC (Through-the-Cycle) view with Downturn adjustment|
|Flooring|No Floor|Floor on certain types of assets|
|Defaulted Loans|LGD on lifetime default for Stage 2 assets|LGD on 1-year default|

## EAD

|Feature|IFRS 9|IRB|
|-|-|-|
|Amortisation|Model includes expected lifetime changes in the balance outstanding that are permitted by the contractual terms: amortization, repayments and (partial) prepayments.|Amortization not included.|
