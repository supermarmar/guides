# Data Requirements

## Probability of Default (PD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)|$D^*_{i,t}(12,p)$|The dependent variable in PD models is a binary default indicator, capturing whether an obligor meets the regulatory definition of default within a defined horizon of a year. This includes a material credit obligation being past due by more than 90 days or the occurrence of unlikely-to-pay (UTP) events. | §CRR Article 178(1), 180(2)(a); §Basel CRE36.68, CRE32.58 |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|Obligor characteristics such as rating, sector, and geography. Financial information, including balance sheet ratios and income metrics. Behavioural data, such as delinquency history and credit usage trends. Macroeconomic variables, including interest rates, unemployment, or sectoral GDP.|§CRR Article 180 (2)(c); §Basel CRE36.80  |
|Measurement Period|$[t'_0,t'_n]$|Minimum 5 years with good and bad mix years from an economic cycle perspective (e.g. March 2007 to June 2025).| §CRR Article 180(2)(e); §Basel CRE36.82 |