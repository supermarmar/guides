# Data Requirements

## Probability of Default (PD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)|$D^*_{i,t}(12,p)$|The dependent variable in PD models is a binary default indicator, capturing whether an obligor meets the regulatory definition of default within a defined horizon of a year. This includes a material credit obligation being past due by more than 90 days or the occurrence of unlikely-to-pay (UTP) events. | §CRR Article 178(1), 180(2)(a); §Basel CRE36.68, CRE32.58 |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|Obligor characteristics such as rating, sector, and geography. Financial information, including balance sheet ratios and income metrics. Behavioural data, such as delinquency history and credit usage trends. Macroeconomic variables, including interest rates, unemployment, or sectoral GDP.|§CRR Article 180 (2)(c); §Basel CRE36.80  |
|Measurement Period|$[t'_0,t'_n]$|Minimum 5 years with good and bad mix years from an economic cycle perspective (e.g. March 2007 to June 2025).| §CRR Article 180(2)(e); §Basel CRE36.82 |

<!-- ## Loss Given Default (LGD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)||LGD is decomposed into modelled components to better reflect recovery processes and align with default lifecycle outcomes: (a) LGW, the fractional loss severity conditional on a write-off event and; (b) PWGD, A binary indicator capturing the probability that a defaulted exposure leads to a write-off. These components enable a more granular understanding and predictive power in the modelling of post-default recoveries.| |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|The LGD models rely on both pre-default and post-default information. Obligor and facility characteristics captured up to one year before default (e.g., collateral type, guarantee status, product type). Post-default information such as recovery cash flows, time to recovery, collection costs, and interest accrued. Macroeconomic factors, particularly those impacting recovery markets (e.g., property prices, insolvency trends)|  |
|Measurement Period|$[t'_0,t'_n]$|Minimum 5 years with good and bad mix years from an economic cycle perspective (e.g. March 2007 to June 2025).| | -->

## Exposure at Default (EAD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)|$\text{EAD}_{i,t}(12)$ or $\text{EADF}_{i,t}(12)$ |EAD is modelled either directly or through related components: EADF (Exposure at Default Factor) ratio of EAD to current balance; CCF (Credit Conversion Factor) or UCF (Undrawn Conversion Factor) representing the portion of unused commitments expected to be drawn down by the time of default. It is also modeled as a 12-month fixed-horizon approach.|§CRR Article 182(1)(f,g); §Basel CRE36.93, CRE36.95 |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|Customer and product-level data available at origination, one year prior, and at the point of default. Utilisation trends, historical drawdown behaviour, account activity, and limit management. Potential inclusion of macroeconomic factors affecting utilisation patterns.| §CRR Article 181A, 181AB, 181AC; §Basel CRE36.90 |
|Measurement Period|$[t'_0,t'_n]$|Minimum 5 years with good and bad mix years from an economic cycle perspective (e.g. March 2007 to June 2025).|§CRR Article 182(3); §Basel CRE36.99 |
