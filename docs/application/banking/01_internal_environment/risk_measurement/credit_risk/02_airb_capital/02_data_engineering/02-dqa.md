# Data Quality Assessment

A rigorous Data Quality Assessment (DQA) process is a critical step between transforming raw datasets into model-ready inputs and beginning any model development activity. The DQA ensures that all downstream modelling relies on data that is complete, accurate, and suitable for regulatory use—particularly under IFRS 9 and Advanced IRB (A-IRB) frameworks.

## BCBS 239 Principles

The ability to aggregate risk data in a holistic and timely manner is important for banks. The
ability to do so assists banks with risk reporting, risk management, and the ability to make
decisions. The “Principles for effective risk data aggregation and risk reporting” Standard
published in BCBS 239 aims to codify this risk data aggregation ability for banks.

The Standard has 14 principles, summarised
below:

1. Governance: A bank’s governance structure should be in control of the capabilities and reporting of risk aggregation
2. Technology infrastructure: IT and data infrastructure should allow for a bank to aggregate and report on risk
3. Accuracy and integrity: The output from risk aggregation activities should be reliable and accurate
4. Completeness: Risk aggregation should consider all material risks that a bank is exposed to. Additionally, it should consider all business lines, geographic regions, industries, and assets that a bank is involved in
5. Timeliness: Banks should be able to generate and report on the aggregation of risk in a timely manner so that the results are up to date
6. Adaptability: The risk aggregation capabilities of a bank should be flexible enough to meet a wide range of needs for various stakeholders, levels of granularity, and forms of business
7. Accuracy: Results from risk aggregation exercises should be reconciled and verified
8. Comprehensiveness: A bank’s risk aggregation should be consistent with its size and complexity
9. Clarity: Risk aggregation reports should facilitate easy decision making
10. Frequency: The frequency of reporting should be determined by senior stakeholders and the frequency selected should reflect the needs of the report recipients, nature of underlying risks and the speed at which they change, and the importance of the given report
11. Distribution: Risk aggregation reports should be distributed only to those that need it.

The three remaining principles below relate to how local regulatory bodies (“supervisors”),
monitor and enforce the Standard:

12. Review: Supervisors should periodically review the bank’s compliance with the
principles
13. Remedial actions and supervisory measures: Supervisors should have the capabilities
to ensure adherence to the Standard and the ability to require effective and timely
remedial action where deficiencies in a bank arise
14. Home / host co-operation: There should be inter-jurisdiction co-operation and
communication between supervisors.

## DQA Checks

| Dimension | Description | Practical Example | Reference |
| ---------------- | -------------------------------------------------------------------------- | - | - |
| **Completeness** | Coverage of all required fields; absence of null or missing values. | Proportion of missing values per field. | BCBS 239 §(43) |
| **Accuracy** | Conformance to source system records; reconciliation to production systems. | Actual distirbution of a data field over a specific time should be validated against its expected distribution. | BCBS 239 §(36)(c) |
| **Consistency** | Logical coherence across variables and time. | No change in definiton of default. | |
| **Timeliness** | Availability of data within expected processing windows. | Data is updated periodically. | BCBS 239 §(44) |
| **Uniqueness** | Each record is uniquely identifiable through a primary key. | No duplicates of account ID and date. | |
| **Robustness** | Data that is constructed to function in multiple settings. It's reusable and hence stable. It can be updated. | Data is auditable at every step. | BCBS 239 §(48) |

This process is led by the Risk & Finance Technology (RFT) team in collaboration with model developers and data governance specialists. The RFT team performs the following steps to assess and document data quality.

## Data Lineage

Data lineage diagrams track variables from source system through staging and transformation to final model-ready format. Each field includes:

- Business and technical definition
- Source table and field
- Data type and permissible values

## Data Dictionaries

A full data dictionary is created for all variables used in modelling.

## Summary Statistics and Data Profiling

Summary statistics are produced for all key model variables, segmented by:

- Product type (e.g., Classic, Gold, Platinum cards)
- Time (vintages, calendar years)
- Customer segment (e.g., salaried vs self-employed)

These include:

- Missing rates
- Mean/median/min/max
- Standard deviation
- Distribution plots

## Transformation Rules and Source Merging Logic

All rules for merging internal and external data sources are documented. Hierarchical overrides (e.g., selecting between bureau and internal income) and transformation logic (e.g., truncating, winsorising) are tested for reproducibility.

## Reconciliation Graphs Over Time

Line graphs compare the number of accounts and balances in the model-ready dataset with the source system totals on a monthly basis. These highlight breaks or anomalies in data loads and give assurance of consistency over time. Discrepancies are flagged and investigated jointly with IT and data control functions.