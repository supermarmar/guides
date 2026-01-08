# Data Requirements

## Loss Given Default (LGD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)||LGD is decomposed into modelled components to better reflect recovery processes and align with default lifecycle outcomes: (a) LGW, the fractional loss severity conditional on a write-off event and; (b) PWGD, A binary indicator capturing the probability that a defaulted exposure leads to a write-off. These components enable a more granular understanding and predictive power in the modelling of post-default recoveries.| |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|The LGD models rely on both pre-default and post-default information. Obligor and facility characteristics captured up to one year before default (e.g., collateral type, guarantee status, product type). Post-default information such as recovery cash flows, time to recovery, collection costs, and interest accrued. Macroeconomic factors, particularly those impacting recovery markets (e.g., property prices, insolvency trends)|  |
|Measurement Period|$[t'_0,t'_n]$|Minimum 5 years with good and bad mix years from an economic cycle perspective (e.g. March 2007 to June 2025).| |