# Data Limitations

A register of known data limitations is maintained and shared with model validators and risk governance committees. These might include:

1. Exclusions due to non-representativeness (e.g. COVID). These exclusions may result in models that underestimate risk in future systemic downturns unless adjustments (e.g. MoC overlays) are applied.

2. Lack of internal data limits confidence in model stability and responsiveness across different economic shocks.

3. Segment-specific data gap (e.g., a new portfolio acquired in 2025) lacks sufficient historical performance data. This segment is excluded from model development and may rely on benchmarking or conservative assumptions.

4. Inconsistent default definition or implementation of default status (e.g., write-off logic, forbearance flagging) may have changed operationally over time, leading to inconsistencies in the target variable.

5. Data migrations and system changes may result in gaps in bureau data or truncated behavioural histories. These inconsistencies require exclusion of affected periods or imputation of missing fields.

6. Sparse observations for rare events limits statistical confidence. These segments may require pooling or regularisation, limiting model granularity.

7. Incomplete external data

8. Policy-driven shifts in portfolio composition or business rule changes (e.g., credit score cut-offs, affordability caps) have non-neutral effects on risk profiles over time.This makes it difficult to disentangle performance trends due to credit policy vs economic factors.