# Overview

## Purpose & Use Tests

The primary purpose of the impairment models requrieed to calculate the expected credit losses (ECL), as described in the IFRS9 impairment requirements.

The ECL is calculated using the banks's own estimates of PD, LGD and EAD, subejct to minimum requirements. 

## Scope

The models should cover specified exposures and other portoflios are out of scope dependent on factors such as:

- Product types
- Size of portoflio (materiality)

## Data

<!-- Several key design decisions are made to ensure data accuracy, completeness, and representativeness throughout model development.

1. Data Sources: Internal data is used as the main input, given its higher relevance, accuracy, and alignment with the bank’s portfolio and performance trends. External sources are used only where internal data was unavailable or insufficient.

2. Data Quality and Reconciliation: Extensive data reconciliation and quality checks are performed to ensure accuracy and consistency. Missing accounts and data gaps are addressed through validation and enrichment processes.

3. Data Representativeness: To ensure the development data reflected the entire portfolio, an analysis of variable distributions is conducted across time. This assessment tries to confirm that the development data adequately represents both the current and historical portfolio composition. -->

## Portfolio Description

<!-- High level descriptive statistics such as current total portoflio balance, product segmentation, target customers and strategy. -->

## Modelling

IFRS 9 states that an entity should measure ECL in a way that reflects:

- an unbiased and probabiltiy weighted amount that is determiend by ecaluating a range of possible outcomes
- time value of money
- reasonable and supporatable information that is available without undue cost or effort at the reporting date about past events, current conditions and forecasts of future economic conditions

The key models are:

- PD
- Attrition
- LGD
- EAD

The MEV scenario generation, scenario weights and EIR Inputs are sometimes inputs generated from outputs from other set of models.

## Performance & Results

<!-- Range of PiT accuracy (measured via relative prediction error), should indicatie strong alignment between actual and predicted outcomes per segment. -->

## Key Assumptions

<!-- - Performance Consistency: Past performance is indicative of future outcomes; variable–default relationships remain stable over time.
- Behavioural Drivers: Macroeconomic factors are excluded; changes in risk parameters are explained through customer behaviour and credit utilisation metrics.
- Portfolio Representativeness: The development sample represents the current and foreseeable portfolio composition. -->

## Limitations

<!-- - Some internal data were excluded from modelling.
- Results may be influenced by policy changes, particularly in collections.
- Data availability remains limited.
- Lack of variables historically.
- Poor performance of certain cohorts in recent periods. -->

## Validation

<!-- - Model owners should be involved throughout development, overseeing readiness for the independent validation team reviews and documentation through each tollgate.
- Indepedent validation teams should perform independent challenge testing at each tollgate, maintaining a challenge log and ensuring all issues are tracked to resolution.
- Model design decisions should be reviewed via peer reviews by quants and feedback from leadership ensuring alignment across all risk differentiation and quantification steps. -->

## Materiality and Complexity

<!-- 1. Materiality: These models are highly material due to their direct impact on capital requirements, ECL estimation, and risk management processes.
2. Complexity: These models are usually highly complex due to their:

- Multi-source data integration
- Advanced statistical and machine learning techniques
- Dual compliance with IFRS 9 and IRB regulatory frameworks -->

## Compliance

<!-- - These models should be fully aligned with PRA and IFRS 9 requirements.
- Material gaps are addressed through data reconciliation, enhanced quality checks, and model monitoring.
- Immaterial gaps (with negligible impact on performance) are documented, with mitigating controls in place. -->
