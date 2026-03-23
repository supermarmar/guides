# Overview

## Purpose & Use Tests

The primary purpose of the Advanced Internal Ratings-Based (AIRB) LGD, EAD, and PD models is to estimate expected loss (EL), regulatory capital (RWA), and economic capital for the credit card portfolio. These models form part of an integrated suite designed to ensure consistent risk ranking across all components of credit risk estimation.

When used without long-run average (LRA) adjustments, margin of conservatism (MoC), or downturn adjustments, the models serve as direct feeders to the IFRS 9 Expected Credit Loss (ECL) framework to maintain consistent rank-ordering between accounting and regulatory purposes.

## Scope

The models should cover specified exposures and other portoflios are out of scope dependent on factors such as:

- Product types
- Size of portoflio (materiality)

## Data

Several key design decisions are made to ensure data accuracy, completeness, and representativeness throughout model development.

1. Data Sources: Internal data is used as the main input, given its higher relevance, accuracy, and alignment with the bank’s portfolio and performance trends. External sources are used only where internal data was unavailable or insufficient.

2. Data Quality and Reconciliation: Extensive data reconciliation and quality checks are performed to ensure accuracy and consistency. Missing accounts and data gaps are addressed through validation and enrichment processes.

3. Data Representativeness: To ensure the development data reflected the entire portfolio, an analysis of variable distributions is conducted across time. This assessment tries to confirm that the development data adequately represents both the current and historical portfolio composition.

## Portfolio Description

High level descriptive statistics such as current total portoflio balance, product segmentation, target customers and strategy.

## Modelling

1. Conceptual Soundness: Model development and calibration should follow conceptually sound statistical and regulatory principles.

2. Risk Differentiation: Point-in-Time (PiT) models should demonstrate sufficient accuracy, discriminatory power, and stability across development, out-of-sample (OOS), and out-of-time (OOT) datasets.

3. Risk Quantification: Risk grades should exhibit sufficient concentration, homogeneity within grades, and heterogeneity between grades. Migration analysis should confirm stable grade movements over time. Realised default and exposure rates are compared with LRA and downturn-calibrated estimates. MoC adjustments should appropriately addressed any deficiencies, ensuring conservatism across risk grades and key subpopulations.

4. Margin of Conservatism (MoC): The MoC framework applies targeted uplifts to account for known data limitations, model uncertainty, and representativeness gaps. The overall MoC should ensure that regulatory risk parameters are conservative relative to PiT estimates and observed target variables for PD, EAD and LGD respectively.

## Performance & Results

- Risk Differentiation: Range of PiT accuracy (measured via relative prediction error), should indicatie strong alignment between actual and predicted outcomes per segment.
- Risk Quantification: Regulatory risk parameters should be higher than PiT estimates, demonstrating adequate conservatism for capital purposes.

## Key Assumptions

- Performance Consistency: Past performance is indicative of future outcomes; variable–default relationships remain stable over time.
- Behavioural Drivers: Macroeconomic factors are excluded; changes in risk parameters are explained through customer behaviour and credit utilisation metrics.
- Portfolio Representativeness: The development sample represents the current and foreseeable portfolio composition.
- Downturn Definition: The downturn period is defined and should exhibit the most conservative historical rates.

## Limitations

- Some internal data were excluded from modelling.
- Results may be influenced by policy changes, particularly in collections.
- Data availability remains limited.
- Lack of variables historically.
- Poor performance of certain cohorts in recent periods.

## Validation

- Model owners should be involved throughout development, overseeing readiness for the independent validation team reviews and documentation through each tollgate.
- Indepedent validation teams should perform independent challenge testing at each tollgate, maintaining a challenge log and ensuring all issues are tracked to resolution.
- Model design decisions should be reviewed via peer reviews by quants and feedback from leadership ensuring alignment across all risk differentiation and quantification steps.

## Materiality and Complexity

1. Materiality: These models are highly material due to their direct impact on capital requirements, ECL estimation, and risk management processes.
2. Complexity: These models are usually highly complex due to their:

- Multi-source data integration
- Advanced statistical and machine learning techniques
- Dual compliance with IFRS 9 and IRB regulatory frameworks

## Compliance

- These models should be fully aligned with PRA and IFRS 9 requirements.
- Material gaps are addressed through data reconciliation, enhanced quality checks, and model monitoring.
- Immaterial gaps (with negligible impact on performance) are documented, with mitigating controls in place.
