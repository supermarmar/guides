# Data Requirements

## Exposure at Default (EAD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)|$\text{EAD}_{i,t}(12)$ or $\text{EADF}_{i,t}(12)$ |Intention is to model a downturn EAD to reflect what would be expected ruing a period economic downturn. EAD is modelled either directly or through related components: EADF (Exposure at Default Factor) ratio of EAD to current balance; CCF (Credit Conversion Factor) or UCF (Undrawn Conversion Factor) representing the portion of unused commitments expected to be drawn down by the time of default. It is also modeled as a 12-month fixed-horizon approach.|§CRR Article 182(1)(f,g); §Basel CRE36.93, CRE36.95 |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|Customer and product-level data available at origination, one year prior, and at the point of default. Utilisation trends, historical drawdown behaviour, account activity, and limit management. Potential inclusion of macroeconomic factors affecting utilisation patterns.| §CRR Article 181A, 181AB, 181AC; §Basel CRE36.90 |
|Measurement Period|$[t'_0,t'_n]$|Minimum 5 years with good and bad mix years from an economic cycle perspective for retial exposures and 7 years for sovereign, corproate and bank exposures (e.g. March 2007 to June 2025).|§CRR Article 182(3); §Basel CRE36.99 |
