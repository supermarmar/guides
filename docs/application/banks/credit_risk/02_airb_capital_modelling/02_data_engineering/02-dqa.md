# Data Quality Assessment

A rigorous Data Quality Assessment (DQA) process is a critical step between transforming raw datasets into model-ready inputs and beginning any model development activity. The DQA ensures that all downstream modelling relies on data that is complete, accurate, and suitable for regulatory use—particularly under IFRS 9 and Advanced IRB (A-IRB) frameworks (BCBS 239).

| Dimension        | Description                                                                | Practical Example | Reference |
| ---------------- | -------------------------------------------------------------------------- | - | - |
| **Completeness** | Coverage of all required fields; absence of null or missing values.         | Proportion of missing values per field. | BCBS 239 §(43) |
| **Accuracy**     | Conformance to source system records; reconciliation to production systems. | Actual distirbution of a data field over a specific time should be validated against its expected distribution.  | BCBS 239 §(36)(c) |
| **Consistency**  | Logical coherence across variables and time.                                | No change in definiton of default. | |
| **Timeliness**   | Availability of data within expected processing windows.                    | Data is updated periodically. | BCBS 239 §(44) |
| **Uniqueness**   | Each record is uniquely identifiable through a primary key.                 | No duplicates of account ID and date. | |
| **Robustness**   | Data that is constructed to function in multiple settings. It's reusable and hence stable. It can be updated. | Data is auditable at every step. | BCBS 239 §(48) |

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