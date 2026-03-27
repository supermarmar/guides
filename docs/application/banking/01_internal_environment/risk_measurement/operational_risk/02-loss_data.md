# Operational Risk: Loss Data and Measurement Concepts

The key to developing operational [[01-risk_management|risk management]] has been the building of measurement techniques grounded in historical data. Data is gathered and organised into an **internal loss database**, making operational [[04-risk_measurement|risk measurement]] more robust, objective, and credible. Rather than relying on expert opinion alone, losses can be replicated, referred to, and compared, leading to a greater understanding of business area processes and backing hard decisions on resources, limits, and capital.

The data process must consider:

- **Automation** — for ease of access and consistency.
- **Frequency** — some data can be collected daily (e.g. transaction processing), while other data (e.g. fraud losses) is only meaningful on a monthly or quarterly basis.
- **Detail** — some types are easier to collect (e.g. legal fees, customer compensation, fines) than others (e.g. increased funding costs for failed trades).

## Loss Database Concepts

**Gross loss** is the loss from an operational risk event before recoveries, which may be recorded for [[01-risk_management|risk management]] purposes prior to its impact on financial statements. **Net loss** is the loss after recoveries, which may be amended over time. Insurance should be treated as a special recovery category; otherwise it obscures the measurement of the riskiness of the activity.

Data capture should include gross loss amounts, dates, any recoveries, and qualitative descriptions of events and causes.

### Loss Collection Thresholds

Loss collection thresholds are the minimum values above which loss amounts must be recorded in the internal loss database. Banks must ensure all material exposures are captured. Thresholds are a supervisory requirement; levels may vary across business lines, but regulators seek consistency among peer banks. In South Africa, for regulatory reporting purposes, banks must apply a minimum threshold on gross loss amounts of R10,000.

Banks generally use judgement rather than statistical evidence to set thresholds. Losses must not be disregarded only because they are relatively small — recording "near losses" can be valuable from a management and scenario analysis perspective. A simple test of the appropriateness of the current threshold is to calculate total sub-threshold losses as a percentage of all losses.

### Dates of Losses

Losses from operational risk events often build up over time and are not identified for months or years (e.g. the Daiwa unauthorised trading scandal proceeded for more than 10 years before it was exposed). Legal settlements and regulatory fines are generally incurred well after events. It should be noted that historical loss events may not necessarily be relevant in estimating future losses, especially where historic risk events can no longer occur (e.g. cheque fraud is now extremely rare in South Africa due to its limited use).

### Grouping of Loss Events

Banks sometimes group several losses into a single loss for efficiency and where they share the same root cause. If individual losses are small and unrelated, the group should be excluded in the modelling process to prevent distortion of results.

### Model Granularity, Validation and Monitoring

Limiting the number of loss groupings creates a critical mass of data and overall simplicity, but this may be unsatisfactory if risks within groups are substantially different and independent. [[bis|Basel]] text requires that measurement "must be sufficiently granular to capture the major drivers of operational risk affecting the shape of the tail of the loss estimates."

Methods and models must be monitored and validated periodically, and if necessary reviewed by specialist external parties, covering:

- Integrity of inputs, assumptions, processes, and outputs.
- Independence from business lines.
- Relevance and soundness of the model through testing.
- Consistency with policies approved by the board of directors.

The monitoring and validation process should ask whether the framework is a realistic reflection of the operational risk position and highlight any issues or deficiencies.

## Operational Risk Event Types ([[basel_2|Basel II]])

[[basel_2|Basel II]] specifies seven Level 1 categories of operational risk loss event types, each broken into Level 2 and Level 3 sub-categories.

| Level 1 Category | Definition | Level 2 Categories |
|---|---|---|
| Internal fraud | Losses due to acts intended to defraud, misappropriate property, or circumvent regulations/company policy, involving at least one internal party | Unauthorised activity; Theft and fraud |
| External fraud | Losses due to acts intended to defraud or misappropriate property by a third party | Theft and fraud; Systems security |
| Employment practices and workplace safety | Losses from acts inconsistent with employment, health or safety laws; personal injury claims; diversity/discrimination events | Employee relations; Safe environment; Diversity and discrimination |
| Clients, products, and business practices | Losses from unintentional or negligent failure to meet professional obligations to clients (including fiduciary and suitability requirements), or from the nature/design of a product | Suitability, disclosure, and fiduciary; Improper business or market practices; Product flaws; Selection, sponsorship, and exposure; Advisory activities |
| Damage to physical assets | Losses from loss or damage to physical assets from natural disaster or other events | Disasters and other events |
| Business disruption and system failures | Losses from disruption of business or system failures | Systems (hardware, software, telecommunications) |
| Execution, delivery, and process management | Losses from failed transaction processing or process management; relations with trade counterparties and vendors | Transaction capture, execution, and maintenance; Monitoring and reporting; Customer intake and documentation; Customer/client account management; Trade counterparties; Vendors and suppliers |

## Operational Risk Business Lines ([[basel_2|Basel II]])

Banks extend the grouping of loss events along eight business lines. Regulators have worked with banks to map business activities to business lines to avoid distortions and arbitrage.

| Level 1 | Level 2 | Activity Groups |
|---|---|---|
| Corporate finance | Corporate finance; Municipal/government finance; Merchant banking; Advisory services | M&A, [[00_underwriting|underwriting]], privatisations, securitisation, debt, equity, syndications, IPOs |
| Trading and sales | Sales; Market-making; Proprietary positions; Treasury | Fixed income, equity, FX, commodities, credit, funding, lending and repos, brokerage |
| Retail banking | Retail banking; Private banking; Card services | Retail/private lending and deposits, banking services, trust and estates, cards |
| Commercial banking | Commercial banking | Project finance, real estate, export finance, trade finance, factoring, leasing, guarantees |
| Payment and settlement | External clients | Payments and collections, funds transfer, clearing, and settlement |
| Agency services | Custody; Corporate agency; Corporate trust | Escrow, depository receipts, securities lending, issuer and paying agents |
| Asset management | Discretionary fund management; Non-discretionary fund management | Pooled, segregated, retail, institutional, closed, open, private equity |
| Retail brokerage | Retail brokerage | Execution and full service |

## Modelling Concepts

### Distribution Assumptions

Distribution assumptions form the basis of all operational risk models and are made for both **severity** and **frequency**.

For **severity**, banks use a range of distributions including generalised power law Pareto distributions of extreme value theory, empirical distributions, and lognormal distributions. It is important not to restrict analysis to one distribution type, but to test and parameterise several based on available data.

For **frequency**, there is consensus amongst most banks that a **Poisson distribution** should be used, though some assume a negative binomial distribution. Banks must consider how capital needs could be met if loss frequency exceeds reasonable conservative assumptions.

Banks should model expected losses (provisioning) and unexpected losses separately.

### Correlation and Dependence

Correlation is a measure of the dependency of operational risk losses across groupings. Losses may be correlated based on deterioration in economic conditions, changes in management, processes and systems, and external events. It is generally assumed that risks within a loss grouping can be 100% correlated.

Banks can use their own correlation assumptions, provided supervisors are satisfied as to the soundness of methods, integrity of implementation, allowances for uncertainty and high stress situations, and validation. Dependence assumptions must be fully supported by empirical data where possible, and biased towards conservatism (i.e. overestimating correlation).

### Data Integration

Data integration involves combining internal loss, external loss, scenario analysis, and control factor data to quantify operational risk. **Bayesian inference** can be used to update loss estimates as new data is acquired. Many banks began by relying on external loss data given limited internal data, especially at the tails. As internal loss data accumulated, **credibility models** could be used to increase its weighting, allowing a greater focus on bank-specific rather than industry-wide data.

Regardless, using data is backward-looking and is only a guide for the future.
