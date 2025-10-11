# Economic Capital

<https://www.bankofengland.co.uk/-/media/boe/files/ccbs/resources/modelling-credit-risk>

Credit is money provided by a creditor to a borrower (also referred to as an **obligor** as he or she has an obligation).  Credit risk refers to the risk that a contracted payment will not be made. Markets are assumed to put a price on this risk. This is then included in the market’s purchase price for the contracted payment. The part of the price that is due to credit risk is the credit spread. The role of a typical credit risk model is to take as input the conditions of the general economy and those of the specific firm in question, and generate as output a credit spread.  

The motivation to develop credit risk models stemmed from the need to develop quantitative estimates of the amount of economic capital needed to support a bank’s risk taking activities. Minimum capital requirements have been coordinated internationally since the Basel Accord of 1998. Under Basel 1, a bank’s assets were allotted via a simple rule of thumb to one of four broad risk categories, each with a ‘risk weighting’ that ranged from 0%-100%. A portfolio of corporate loans, for instance, received a risk weight of 100%, while retail mortgages – perceived to be safer – received a more favourable risk weighting of 50%. Minimum capital was then set in proportion to the weighted sum of these asset.

$K = 8\% \times \text{RWA}$

Over time, this approach was criticised for being insufficiently granular to capture the cross sectional distribution of risk. All mortgage loans, for instance, received the same capital requirement without regard to the underlying risk profile of the borrower (such as the loan to value or debt to income ratio). This led to concerns that the framework incentivised ‘risk shifting’. To the extent that risk was not being properly priced, it was argued that banks had an incentive to retain only the highest risk exposures on their balance sheets as these were also likely to offer the highest expected return.

In response, Basel II had a much more granular approach to risk weighting. Under Basel II, the credit risk management techniques under can be classified under:

- Standardised approach: this involves a simple categorisation of obligors, without considering their actual
credit risks. It includes reliance on external credit ratings.
- Internal ratings-based (IRB) approach: here banks are allowed to use their ‘internal models’ to calculate the regulatory capital requirement for credit risk.

These frameworks are designed to arrive at the risk-weighted assets (RWA), the denominator of four key capitalisation ratios (Total capital, Tier 1, Core Tier 1, Common Equity Tier 1). Under Basel II, banks following the IRB approach may compute capital requirements based on a formula approximating the Vasicek model of portfolio credit risk. The Vasicek framework is described in the following section.

Under Basel III the minimum capital requirement was not changed, but stricter rules were introduced to ensure capital was of sufficient quality. There is now a 4.5% minimum CET1 requirement (§RBC20.1). It also increased levels of capital by introducing usable capital buffers rather than capital minima. See BCBS (2010). Basel III cleaned up the definition of capital, i.e., the numerator of the capital ratio. But it did not seek to materially alter the Basel II risk based framework for measuring risk-weighted assets, i.e., the denominator of the capital ratio; therefore, the architecture of the risk weighted capital regime was left largely unchanged. Basel III seeks to improve the standardised approach for credit risk in a number of ways. This includes strengthening the link between the standardised approach the internal ratings-based (IRB) approach.

When estimating the amount of economic capital needed to support their credit risk activities, banks employ an analytical framework that relates the overall required economic capital for credit risk to their portfolio’s probability density function (PDF) of credit losses, also known as loss distribution of a credit portfolio. Figure below shows this relationship. Although the various modelling approaches would differ, all of them would consider estimating such a PDF.

![image_1.png](images/credit_losses.png)

<https://www.bis.org/bcbs/irbriskweight.pdf>

Mechanisms for allocating economic capital against credit risk typically assume that the shape of the PDF can be approximated by distributions that could be parameterised by the mean and standard deviation of portfolio losses. Figure below shows that credit risk has two components. First, the expected loss (EL) is the amount of credit loss the bank would expect to experience on its credit portfolio over the chosen time horizon. This could be viewed as the normal cost of doing business covered by provisioning and pricing policies. Second, banks express the risk of the portfolio with a measure of unexpected loss (UL). Capital is held to offset UL and within the IRB methodology, the regulatory capital charge depends only on UL. The standard deviation, which shows the average deviation of expected losses, is a commonly used measure of unexpected loss.

Figure below illustrates how variation in realised losses over time leads to a distribution of losses for a bank:

![image_1.png](images/losses_over_time.png)

The worst case one could imagine would be that banks lose their entire credit portfolio in a given year. This event, though, is highly unlikely, and holding capital against it would be economically inefficient. Banks have an incentive to minimise the capital they hold, because reducing capital frees up economic resources that can be directed to profitable investments. On the other hand, the less capital a bank holds, the greater is the likelihood that it will not be able to meet its own debt obligations, i.e. that losses in a given year will not be covered by profit plus available capital, and that the bank will become insolvent. Thus, banks and their supervisors must carefully balance the risks and rewards of holding capital.

## Value-at-Risk

The area under the curve in the PDF is equal to 100%. The curve shows that small losses around or slightly below the EL occur more frequently than large losses. The likelihood that losses will exceed the sum of EL and UL – that is, the likelihood that the bank will not be able to meet its credit obligations by profits and capital – equals the shaded area on the RHS of the curve and depicted as stress loss. 100% minus this likelihood is called the Value-at- Risk (VaR) at this confidence level. If capital is set according to the gap between the EL and VaR, and if EL is covered by provisions or revenues, then the likelihood that the bank will remain solvent over a one-year horizon is equal to the confidence level.

Under Basel II, capital is set to maintain a supervisory fixed confidence level. The confidence level is fixed at 99.9% i.e. an institution is expected to suffer losses that exceed its capital once in a 1000 years. Lessons learned from the 2007-2009 global financial crisis, would suggest that stress loss is the potential unexpected loss against which it is judged to be too expensive to hold capital. Regulators have particular concerns about the tail of the loss distribution and about where banks would set the boundary for unexpected loss and stress loss. For further discussion on loss distributions under stress scenarios see Haldane et al (2007).

This confidence level might seem rather high. However, Tier 2 does not have the loss absorbing capacity of Tier 1. The high confidence level was also chosen to protect against estimation errors, that might inevitably occur from banks’ internal PD, LGD and EAD estimation, as well as other model uncertainties.

## Expected Losses

So far the Expected Loss has been regarded from a top-down perspective, i.e. from a portfolio view. It can also be viewed bottom-up, namely from its components.

A bank has to take a decision on the time horizon over which it assesses credit risk. In the Basel context there is a one-year time horizon across all asset classes. The expected loss of a portfolio is assumed to be equal to the proportion of obligors that might default within a given time frame, multiplied by the outstanding exposure at default, and once more by the loss given default, which represents the proportion of the exposure that will not be recovered after default.

Under the Basel II IRB framework the probability of default (PD) per rating grade is the average percentage of obligors that will default over a one-year period. Exposure at default (EAD) gives an estimate of the amount outstanding if the borrower defaults. Loss given default (LGD) represents the proportion of the exposure (EAD) that will not be recovered after default. Assuming a uniform value of LGD for a given portfolio, EL can be calculated as the sum of individual ELs in the portfolio.

$\text{EL} = \displaystyle \sum_{i=1}^N{\text{PD}_{i}^\text{TTC}(12,x_{i},[t_a',t_b'])\times\text{EAD}_{i,t}(12)\times\text{LGD}_i}$ where $i$ denotes an obligor

## Unexpected Losses

Unlike EL, total UL is not an aggregate of individual ULs but rather depends on loss correlations between all loans in the portfolio. The deviation of losses from the EL is usually measured by the standard deviation of the loss variable. The UL, or the portfolio’s standard deviation of credit losses can be decomposed into the contribution from each of the individual credit facilities:

$\text{UL} = \displaystyle\sum_{i=1}^N\sigma_i\rho_i$

where $\sigma_i$ denotes the stand-alone standard deviation of credit losses for the $i$th facility, and $\rho_i$ denotes the correlation between credit losses on the ith facility and those on the overall portfolio. The parameter captures the ith facility’s correlation/diversification effects with other instruments in the bank’s credit portfolio. Other things being equal, higher correlations among credit instruments – represented by higher $\rho_i$ lead to a higher standard deviation of credit losses for the portfolio as a whole.

## Conditional Expected Losses

Another way of looking at it is through the following:

$\text{UL}=\text{Conditional Expected Losses}-\text{EL}$

$\text{Conditional Expected Losses}=\text{UL}+\text{EL}$

The formula sets the minimum capital requirement such that unexpected losses will not exceed the bank’s capital up to a 99.9% confidence level.

The implementation of this model (ASFR), developed for Basel II, makes use of average PDs that reflect expected default rates under normal business conditions. These average PDs are estimated by banks. To calculate the conditional expected loss, **bank-reported average PDs are transformed into systemically conditional PDs** using a supervisory mapping function (described below). The conditional PDs reflect default rates **given an appropriately conservative value of the systematic risk factor**. The same value of the systematic risk factor is used for all instruments in the portfolio. Diversification or concentration aspects of an actual portfolio are not specifically treated within an ASRF model.

In contrast to the treatment of PDs, Basel II does not contain an explicit function that transforms average LGDs expected to occur under normal business conditions into conditional LGDs consistent with an appropriately conservative value of the systematic risk factor. Instead, banks are asked to report **LGDs that reflect economic-downturn conditions** in circumstances where loss severities are expected to be higher during cyclical downturns than during typical business conditions.

The conditional expected loss for an exposure is estimated as the product of the conditional PD and the “downturn” LGD for that exposure. Under the ASRF model the total economic resources (capital plus provisions and write-offs) that a bank must hold to cover the sum of UL and EL for an exposure is equal to that exposure’s conditional expected loss. Adding up these resources across all exposures yields sufficient resources to meet a portfolio-wide Value-at-Risk target.

This can be illustrated below. Ideally, ELs should be covered by provisions. However, if there is a shortfall between EL and provisions (EL> provisions), then this shortfall is deducted from Tier 1 capital. Likewise, if there is an excess, Basel describes how much you are allowed to include in your Tier 2 capital.

![image](images/el_vs_ul.png)

## Downturn LGDs

The Basel Committee considered two approaches for deriving economic-downturn LGDs. One approach would be to apply a mapping function similar to that used for PDs that would extrapolate downturn LGDs from bank-reported average LGDs. Alternatively, banks could be asked to provide downturn LGD figures based on their internal assessments of LGDs during adverse conditions (subject to supervisory standards).

In principle, a function that transforms average LGDs into downturn LGDs could depend on many different factors including the overall state of the economy, the magnitude of the average LGD itself, the exposure class and the type and amount of collateral assigned to the exposure. The Basel Committee determined that given the evolving nature of bank practices in the area of LGD quantification, it would be inappropriate to apply a single supervisory LGD mapping function. Rather, Advanced IRB banks are required to estimate their own downturn LGDs that, where necessary, reflect the tendency for LGDs during economic downturn conditions to exceed those that arise during typical business conditions. Supervisors will continue to monitor and encourage the development of appropriate approaches to quantifying downturn LGDs.

The downturn LGD enters the Basel II capital function in two ways. The downturn LGD is multiplied by the conditional PD to produce an estimate of the conditional expected loss associated with an exposure. It is also multiplied by the average PD to produce an estimate of the EL associated with the exposure.
