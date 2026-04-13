---
tags:
  - application/banking/internal-environment/risk-measurement/operational-risk/capital-basel2
  - difficulty/unknown
  - study-status/new
aliases:
---
# Operational Risk Capital: [[basel_2|Basel II]] Approaches

The [[basel_2|Basel II]] Accord outlined three approaches to measuring operational risk and the minimum capital required against it. These range from simple approaches used by smaller banks with limited international operations, to more complex internal model approaches. Banks approved for more sophisticated approaches cannot revert to simpler ones without supervisory approval. Risk-weighted assets (RWA) for operational risk under all approaches are calculated as the capital requirement multiplied by 12.5.

## 3.1 Basic Indicator Approach (BIA)

The BIA is the default approach and uses a single indicator — **gross income** — as the proxy for overall operational risk exposure. Gross income is net interest and non-interest income before deduction of operational losses.

```math
K_{\text{BIA}} = \frac{\sum_{n=1}^{3} (GI_n \times \alpha)}{3}
```

where $\alpha = 15\%$ and any year showing a negative or zero annual gross income is excluded from both the numerator and denominator.

The BIA is most often used by smaller banks with limited international operations. It does not help measure, monitor, and respond to risks, so larger banks are expected to use more advanced approaches.

## 3.2 Standardised Approach (TSA)

The TSA differs from the BIA in that the percentage of gross income varies by business line. Standard **betas** serve as a proxy for the relationship between industry-wide business line operational risk losses and aggregate business line gross income.

```math
K_{\text{TSA}} = \frac{\sum_{n=1}^{3} \max\left(\sum_{i=1}^{8} (GI_i \times \beta_i),\ 0\right)}{3}
```

The total capital charge is the 3-year average of the summation of the capital charges for each business line. In any year, at national discretion, negative capital charges in a business line may offset positive charges in others — but where the aggregate across all business lines is negative in a given year, the input to the numerator for that year is zero. In South Africa, netting of negative capital charges across business lines is not permitted.

### Beta Coefficients by Business Line

| Business Line | Beta (β) |
|---|---|
| Corporate finance | 18% |
| Trading and sales | 18% |
| Payment and settlement | 18% |
| Commercial banking | 15% |
| Agency services | 15% |
| Retail banking | 12% |
| Asset management | 12% |
| Retail brokerage | 12% |

Banks must apply to the national supervisor for approval before using the TSA and must implement a sound framework backed by adequate resources that is actively supervised by the board and senior management.

### Alternative Standardised Approach (ASA)

The ASA allows some large, diversified banks to use **outstanding loans and advances (LA)** multiplied by a constant factor $m$ as the operational risk proxy rather than gross income, for retail and commercial banking business lines only:

```math
K_{\text{RB}} = \beta_{\text{RB}} \times m \times LA_{\text{RB}}
\\
K_{\text{CB}} = \beta_{\text{CB}} \times m \times LA_{\text{CB}}
```

where $m = 0.035$ and the betas are as defined in the table above.

## 3.3 Advanced Measurement Approach (AMA)

The AMA allows banks to use their **internal [[04-risk_measurement|risk measurement]] systems** to generate the regulatory capital requirement. There is no prescribed methodology; banks must be able to demonstrate that potentially severe "tail" loss events are captured. VaR must capture aggregate losses (expected and unexpected) over 1 year at a 99.9% confidence level — comparable to the IRB approach for credit risk.

### Four Required Data Types

| Data Type | Description |
|---|---|
| Internal loss | Database with at least 5 years of history (minimum 3 years when first moving to AMA) |
| External loss | Competitor experience purchased from vendors or built from public information; most important for measuring severity of infrequent, high-severity events |
| Scenario analysis | Expert opinion on the most severe loss events (e.g. 1-in-1,000-year events); extends loss distributions beyond actual experience or adjusts correlations for multiple simultaneous events |
| Business environment control factors | Objective KRIs, KPIs, and KCIs expressed in counts, values, percentages, and ratios (e.g. unmatched trades, failed trades, disputed collateral calls); intended to make the risk assessment more forward-looking |

Correlation and diversification may be recognised but banks must justify calculations. Insurance can be used to hedge and reduce up to a maximum of **20% of total VaR**, subject to criteria relating to the insurance provider and the specific nature of the policy.

### Loss Distribution Approach (LDA)

One permissible AMA method is the LDA, which models **loss severity** and **loss frequency** distributions separately and combines them using Monte Carlo simulation or other statistical techniques to produce an aggregate loss distribution.

The Monte Carlo process draws a random sample from the frequency distribution for a business unit/loss type combination, then draws that number of events from the severity distribution to plot a point on the aggregate loss distribution curve. Standard goodness-of-fit tests used include Kolmogorov-Smirnov, Anderson-Darling, Chi-Square, and Shapiro-Wilk.

The biggest challenge is selecting the distribution that best fits the **tail** of the observed data, as this is essential to setting the capital requirement. Some banks use **extreme value theory** by separating the body and tail of the distribution and applying different statistical methods to each. This complicates modelling as the frequency distribution must also be split and truncated severity distributions must be parameterised.

The minimum operational risk capital requirement under the LDA is:

```math
K_{\text{LDA}} = \text{VaR}_{99.9\%}\left(\sum_{i,j} \text{AggLoss}_{i,j}\right)
```

where the summation is across all combinations of business lines ($i$) and risk event types ($j$).

The LDA is easy to use for non-technical stakeholders as every type of business activity can be evaluated using VaR and parameters (time horizon, confidence level) already familiar from credit and [[05-market_risk|market risk]]. The challenges are complexity, less transparent assumptions, and substantial resource requirements.

### Qualitative Input and Model Validation

Even after extensive quantitative modelling, qualitative analysis is important in evaluating results. Quantitative methods are most straightforward for high-frequency, low-severity areas like transaction processing, and less useful for assessing risks related to governance, organisation, and incentives.

Banks organise regular internal workshops where managers complete **risk scorecards** by business line and event, scoring not only frequency and financial severity but also reputational impact and employee retention.

Qualitative inputs must be assessed for quality — [[01-risk_management|risk management]] must ask the right people and the right questions without creating bias or anchoring. Qualitative inputs should be converted into metrics for scenario analysis and be forward-looking, clearly defined, and repeatable.

### Key Risk Indicators

Business environment control factors are risk metrics and statistics used to monitor drivers of risk exposure:

- **Key performance indicators (KPIs)** — monitor operational efficiency (e.g. system downtime, staff turnover).
- **Key control indicators (KCIs)** — monitor effectiveness of controls (e.g. outstanding confirmations, audit exceptions).
- **Key risk indicators (KRIs)** — a selection of KPIs and KCIs aligned to key risks, used to warn of escalating risk and trigger management attention and action. Composite KRIs can be rolled up to top management.

Indicators must be measurable, not complicated, and representative of the business line and its risk. The [[bis|Basel]] Committee regards risk indicators as subjective in nature and cautions against overweighting them.
