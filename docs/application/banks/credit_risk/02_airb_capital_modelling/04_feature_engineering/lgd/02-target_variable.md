## Loss Given Default (LGD)


LGD is modelled using a **component-based approach** to capture the complex nature of post-default outcomes. The target is not a single value but built from two or more sub-models:

#### 3.3.1 Component Targets

1. **Loss Rate (LGW)**

   * Formula: `(EAD_tD – Total Recoveries) / EAD_tD`
   * This continuous variable captures the **loss severity** as a proportion of exposure.

2. **Probability of Loss / Recovery (PWGD or PR)**

   * Binary flag indicating whether **any recovery occurs** post-default.
   * Enhances model granularity by predicting whether the account will experience full, partial, or no recovery.

#### 3.3.2 Considerations

* Losses and recoveries are tracked over a **maximum resolution period**, typically **5 years**, in accordance with **Basel and PRA** expectations.
* LGD estimates should reflect **long-run average (LRA)** and **downturn (DT)** conditions, with proper segmentation by:

  * Security type (secured vs. unsecured),
  * Product type,
  * Recovery channels (e.g., internal collection, legal, third-party),
  * Default and recovery vintage.

The LCD1 (non-default book) and LGD2 (default book) models were designed to predict the economic loss realised on an exposure following default, expressed as a percentage of exposure at default.

The LGD model was developed based on a component-based design, where the overall LGD prediction has been decomposed into a sequence of probability and recovery components. The composite LGD model was then calibrated and back-tested based on realised LGD. Details of the LCD model design are provided in Model Methodology.

The table below summarises the target variable and outcome periods for each model component:

| Model Component | Target Variable | Formula | Outcome Period |
| - | - | - | - |
| Probability of Zero Payment | Binary - Zero Payer | P(Undiscounted Cum Rec= 0% \ Default) | 24 months |
| Probability of Full Repayment | Binary - Full Payer | P(Undiscounted Cum Rec= 100% \ Recoveries > 0% and Default) | 24 months |
| Recovery Rate | Continouos - Recovery Rate | E(Discounted Cumulative \ 0% <2 4m Cum Rec < 100% and Default) | 60 months |

It is important to note that while PDs are generally associated with the borrower, or client, LGDs are associated with the facility, and the asset being financed, as the loss depends on the characteristics of the product in question.

### Probability of Zero Payer and Full Repayment

The target variables for probability model components are binary indicators:

- For the probability of Zero Payer model component, the target variable is the zero-payer flag ("segment_24m_zp" in the MRD) which is an indicator that an account has made no payments during a 24-month outcome period after the point of default.
- For the probability of Full Payer model component, the target variable is the fuil payer flag ("segment_24m_fp" in the MRD) which is an indicator that an account has repaid all outstanding debt during e 24-month outcome period after the point of default.

The same outcome period is used for the probability component models to ensure consistency. To determine an appropriate outcome performance window, three different time horizons were assessed: 12-months, 24- months and 36-months.

Given the model design, the probabilities of whether an account is a Zero Payer or full payer are not necessarily independent. The probability of full repayment may be conditional on certain factors that also influence the probability of zero repayment. For example, higher balances may increase the probability of zero repayment while also decrease the probability of full repayment. Therefore, the hierarchy of which of these probabilities are predicted first is important and may impact the accuracy of the overall estimated LGD. The hierarchy of predictions was also assessed using the same performance windows for the following architectures:

- Full Payer (FP) first: This approach models the full payer population first and subsequent population is conditional on full payment.
- Zero Payer (ZP) first: This approach models the zero-payer population first and subsequent population is conditional on zero payment.

Toy models for the probability components were built using the development sample (detailed in Section 7.4) to compare their results with different outcome periods. The first step in building the toy models was running the variable reduction analysis (details in Section 9.4) and identifying the strongest 35 variables for each model. Thereafter, the model was fit using these variables to better understand the implications of the model hierarchy. Figure 7.3-1 presents the accuracy (error rates) and discriminatory power (Gini) of each probability component calculated based on different outcome periods and hierarchies.

### Recovery Rate

The target variable for the partial payer recovery rate model component is the observed discounted recovery rate ("discounted_cum_recovery_rate_60m" in the MRD) during a 60-month outcome period after the point of default. This is calculated as the present value at default of repayments over the 60-month outcome period (gross of cost) divided by the exposure at default. All recoveries and additional post-default drawings have been discounted using the discount rates described above.

The outcome period was determined by assessing the incremental cumulative recovery rates of partial payers as the performance window is extended.

<!--  

An “economic” loss (unlike an accounting loss) considers all relevant factors including material discount effects, and material direct and indirect costs associated with holding and collecting the defaulted facilities, i.e. direct and indirect costs discounted back to the point of default. Indirect costs are only considered when calculating the LGD used for capital calculations, but not included within the LGD used in the IFRS9 impairment calculations (discussed in a later section).

It is important to note that while PDs are generally associated with the borrower, or client, LGDs are associated with the facility, and the asset being financed, as the loss depends on the characteristics of the product in question.

Methods used to estimate the LGD for credit facilities fall into one of two categories.

- Subjective methods are primarily driven by expert judgement and used mainly on portfolios with few defaults and/or by banks in the early stage of internal model development.
- Objective methods largely rely on formal mathematical procedures and can be further divided into two methods. The decision to select one of these objective methods is largely driven by the nature of portfolio, exposure type (e.g. loan vs bond), and the availability of data.
  - Explicit methods, i.e. the market LGD approach and workout LGD approach
  - Implicit methods, i.e. the implied market LGD approach.

Unlike PD estimates, where Basel has provided more detailed guidelines, LGD estimates follow a principles-based approach where Basel describes what the resulting LGD should include and account for but does not necessarily provide guidelines on how it should be estimated. For example, Basel requires banks to “reflect economic downturn conditions where necessary to capture the relevant risks” in their LGD estimates; i.e. “downturn” (DT) LGDs. Regulatory bodies, however, may provide further guidance. -->

### Downturn LGD

<!-- DT LGD estimates are based on historical recoveries (including collateral) in economic downturn conditions and used in calculating regulatory capital. Interpretations of key parameters differ by bank and are not always comparable, given the less specific guidelines provided by international bodies. Definitions of downturn vary, with some banks using two consecutive quarters of negative GDP growth, while others emphasise product downturn rather than overall economic conditions. While PD is largely the same across all types of exposures to a borrower, LGD is likely to vary significantly by product. Banks are expected to be conservative, and auditors and external supervisors must be able to validate the model. -->

### LGD Reference Value

SS4/24 Paragraph 15.7 requires that firms calculate a "reference value" as the simple average of the realised LGDs in the two years with the highest total economic loss divided by total outstanding amount (i.e. the average of the two years with highest balance-weighted LCD). The reference value should be compared against the downturn LGD at least at the level of calibration segments.

### Observed Average LGD

In line with SS4/24 Paragraph 14.6, the observed average LGD represents the arithmetic (default-weighted) average realised LGD, on resolved facilities.
