# Data Controls

The bank maintains a comprehensive data control framework designed to ensure the accuracy, completeness, and integrity of all data used for credit risk modelling, reporting, and decision-making. The data controls framework is aligned with regulatory expectations under [[bcbs_239|BCBS 239]] (Principles for Effective Risk Data Aggregation and Risk Reporting), [[pra|PRA]] Supervisory Statement SS11/13 (Internal Ratings-Based Approaches), and PA Directive D5/2017 (Framework for Data Management in Banks). Collectively, these frameworks require firms to establish robust governance processes and control mechanisms to ensure that data used for [[04-risk_measurement|risk measurement]] and regulatory reporting is accurate, complete, timely, and appropriate for its intended use.

In practice, this control environment operates through a series of automated and manual checks embedded throughout the MDS creation process. Each step—from data ingestion to transformation and model input generation—is governed by specific validation and reconciliation controls.

- **File Transfer Controls**: The daily ingestion of source data (e.g., bureau or transactional data) is monitored through automated record count validations to ensure completeness. Any discrepancies between expected and received volumes trigger exception reporting and investigation.
- **Error Handling**: Data load processes include embedded error-handling routines that identify, log, and escalate data anomalies or processing errors for resolution prior to model input or reporting.
- **Data Accuracy Checks**: On a quarterly basis, a sample of approximately 200 customer accounts is manually validated against the original data source to confirm the ongoing accuracy and consistency of key fields.
- **Business Logic Validation**: All transformation rules, business filters, and derivations (e.g. delinquency flags, transactor indicators) undergo periodic validation to ensure they remain aligned with approved definitions and regulatory expectations.
- **Change Control**: Any change to data mappings, business rules, or source systems is subject to formal approval and testing before deployment, following the model risk and [[04-data_governance|data governance]] framework.

These controls collectively provide assurance that data used for model development and monitoring remains reliable, traceable, and compliant with internal and regulatory standards.

## Examples

- **Daily bureau data ingestion**: record count validations, file format checks, and automated exception handling to ensure completeness and integrity of source data transfers.
- **Business logic validation**: reconciliation of transformation outputs against business rules (e.g., product hierarchies, exposure classifications) to confirm that derivations and calculations are applied consistently and accurately.
- **Error handling and remediation**: automated alerts and workflow escalation when data quality thresholds are breached, ensuring timely investigation and correction.
- **Periodic data accuracy testing**: quarterly sample reviews (e.g., 200 accounts) comparing model input data to source systems to confirm end-to-end consistency.
- **Change management controls**: versioning and peer review of data processing scripts to maintain reproducibility and traceability of all transformations.
