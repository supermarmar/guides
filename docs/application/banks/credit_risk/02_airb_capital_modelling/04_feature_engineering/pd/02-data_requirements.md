# Data Requirements

Probability of default is estimated from a range of sources. The simplest and most widely used source throughout the world is rating agency ratings – primarily when using the SA under Basel. Banks also use their own historical default databases or purchase those compiled by third parties – under the IRBA.

For some asset classes, decades of default data are available and quantitative models can be built. For others, low-default portfolios, the banks may have little to no defaults or the industry itself may have experienced few defaults. In this case, more qualitative models may be suitable, where expert judgement is more relied upon. In both cases, qualitative factors should be included where possible to supplement quantitative factors.

Banks must make careful judgements as to how data is used. While default is rare in certain portfolios, consequences for debt portfolios are severe given small earnings margins and no upside as in equities. While modelling monthly or quarterly data from portfolio segments is common, defaults observed may not be a good indicator for forward-looking analysis if a portfolio is growing or the market is new. The risk of PD being understated is significant.

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)|$D^*_{i,t}(12,p)$|The dependent variable in PD models is a binary default indicator, capturing whether an obligor meets the regulatory definition of default within a defined horizon of a year. This includes a material credit obligation being past due by more than 90 days or the occurrence of unlikely-to-pay (UTP) events. This is measured as the average default rate **within** the next 12 months (worst-ever event). | §CRR Article 178(1), 180(2)(a); §Basel CRE36.68, CRE32.58 |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|Obligor characteristics such as rating, sector, and geography. Financial information, including balance sheet ratios and income metrics. Behavioural data, such as delinquency history and credit usage trends. Macroeconomic variables, including interest rates, unemployment, or sectoral GDP.|§CRR Article 180 (2)(c); §Basel CRE36.80  |
|Measurement Period|$[t'_0,t'_n]$|Minimum 5 years with good and bad mix years from an economic cycle perspective (e.g. March 2007 to June 2025).| §CRR Article 180(2)(e); §Basel CRE36.82 |