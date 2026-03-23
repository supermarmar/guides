# Economic Capital

Economic capital is internally calculated by the bank and is a measure of the bank's total risk as they see it, without reference to regulatory prescriptions. It is calculated as part of the Internal Capital Adequacy Assessment Process (ICAAP) and represents the amount of capital a bank believes it needs based on its own risk appetite and strategy.

For the broader treatment of the Pillar 2 capital framework (Pillar 2A/2B add-ons, buffers, capital requirements table), see [Capital — Pillar 2](..\..\04-capital.md). This file focuses on the **computation mechanics of economic capital** used in the ICAAP, including Pillar 2A risk-specific quantification and Pillar 2B stress capital.

## Economic Capital vs Regulatory Capital

While Pillar 1 regulatory capital is a rule-prescribed floor, economic capital is the bank's own best estimate of required capital. The two measures differ in several important dimensions:

| Dimension | Regulatory Capital (Pillar 1) | Economic Capital (ICAAP) |
|---|---|---|
| **Confidence level** | 99.9% (1-in-1000 year loss) | Typically 99.95%–99.97% (1-in-2000 to 1-in-3333 year loss) |
| **PD calibration** | Through-the-cycle (TTC) | Point-in-time (PIT) — reflects current conditions |
| **Diversification** | Not recognised (ASRF assumes infinite granularity and no sector correlation) | Recognised via portfolio simulation or correlation assumptions |
| **Risk coverage** | Credit, market, operational risk only | All material risks incl. IRRBB, pension, concentration, model, strategic, reputational |
| **LGD calibration** | Downturn LGD | May use PIT or DT LGD depending on modelling philosophy |
| **Formula** | Prescribed (ASRF / Vasicek) | Bank-defined (internal models) |
| **Output** | RWA × 8% | VaR at target confidence level minus EL |

Economic capital is generally lower than regulatory capital for well-diversified banks because it captures diversification benefits that the ASRF model (which assumes a single systematic risk factor and infinite granularity) cannot. However, for concentrated or small banks, EC may exceed regulatory capital.

### Credit Risk Economic Capital

Economic capital for credit risk is conceptually computed using the same Vasicek/ASRF framework as the IRB formula — a portfolio loss distribution is modelled and capital is set at VaR minus EL:

$$\text{EC}_{\text{credit}} = \text{VaR}_{q} - \text{EL}$$

where $q$ is the bank's internal confidence level (e.g., 99.95%).

Key differences from the IRB regulatory capital formula (see [Regulatory Capital](..\..\02_airb_capital_modelling\01_introduction\01-regulatory_capital.md)):

- **PIT PDs**: Economic capital typically uses PIT PDs which are higher in downturns and lower in expansions, rather than the TTC PDs used in regulatory capital.
- **Higher confidence level**: The bank's own target confidence level $q$ reflects its target credit rating and risk appetite. A bank targeting an AA rating (implied default probability ~0.03%) would use approximately $q = 99.97\%$.
- **Multi-factor models**: Unlike the single-factor ASRF, internal EC models may use multi-factor approaches (sector-specific systematic factors) to better capture concentration and diversification.
- **Diversification benefit**: Portfolio EC < sum of individual-obligor ECs. The difference — the diversification benefit — is recognised in EC but not in Pillar 1.

### Aggregation Across Risk Types

Once economic capital has been computed for each risk type, the total economic capital is not a simple sum. Risks are not perfectly correlated, so there is a diversification benefit at the firm level:

$$\text{EC}_{\text{total}} = \sqrt{\mathbf{EC}^T \boldsymbol{\Sigma} \, \mathbf{EC}}$$

where $\mathbf{EC}$ is the vector of risk-type ECs and $\boldsymbol{\Sigma}$ is the inter-risk correlation matrix. In practice, the correlation assumptions between risk types (e.g., credit risk and operational risk) are difficult to estimate and are often set conservatively based on expert judgment or regulatory guidance.

## Pillar 2: Supervisory Review Process

Pillar 2 serves as a critical bridge between a bank's internal risk management and regulatory oversight. It allows regulators in different countries some discretion in how rules are applied (so that they can take account of local conditions), but seeks to achieve overall consistency in the application of the principles. It places more emphasis on early intervention when problems arise. Supervisors are required to do far more than simply ensuring that the minimum capital required under Pillar 1 is held. Part of their role is to encourage banks to develop and use better risk management techniques and to evaluate these techniques. They should evaluate risks that are not covered by Pillar 1 and enter into an active dialogue with banks when deficiencies are identified.

Four key principles of supervisory review are specified:

1. Banks should have a **process for assessing their overall capital adequacy** in relation to their risk profile and strategy for maintaining capital levels (ICAAP).
2. **Supervisors should review** and evaluate banks' internal capital adequacy assessments and strategies, as well as their ability to monitor and ensure compliance with regulatory capital ratios. Supervisors should take appropriate supervisory action if they are not satisfied with the result of the process.
3. Supervisors should expect banks to **operate above the minimum regulatory capital** and should be able to require banks to hold capital in excess of this minimum.
4. Supervisors should seek to **intervene at an early stage** to prevent capital from falling below the minimum levels required to support the risk characteristics of a particular bank and should require rapid remedial action if capital is not maintained or restored.

In terms of credit risk, Pillar 2 requires the bank to detail and disclose to regulators the methods used to calculate capital requirements for this risk, as well as the processes involved in managing credit risk on an ongoing basis. This will form part of the "Internal Capital Adequacy Process" (ICAAP).

### ICAAP

#### Components of Capital Assessment

The ICAAP is the primary mechanism through which a bank determines its Economic Capital — the amount of capital it believes it needs based on its own risk appetite and strategy. This may require additional credit risk measurement approaches.

An important step in the process is stress testing, where the required capital is assessed under stressed conditions to determine if the amount is sufficient. These stress tests require both quantitative and qualitative elements. Quantitative elements include identifying and applying stress scenarios. Qualitative elements include assessing the ability of the bank to absorb losses under these scenarios and determining steps that should be taken to mitigate these risk scenarios. The ICAAP process also includes assessing the correlations between risk types, as when risk is being assessed on an aggregate level, certain risks will be correlated and there may be a "diversification benefit".

The key components required in an ICAAP include the following two types of capital assessment:

1. **PiT Capital Assessment**: Evaluation of capital at the current reporting date.
   - Pillar 1: 8% of RWA of credit, market, and operational risks.
   - Pillar 2A: additional capital requirements for risks not captured in Pillar 1 (e.g. Interest Rate Risk in the Banking Book (IRRBB), Pension Risk and Credit Concentration Risk).
   - MIRA: A material risk assessment (MIRA) is performed to ensure that all material risks are managed / capitalised adequately.
2. **Forward-Looking Assessment (Stress Testing)**: Evaluating capital sufficiency under adverse scenarios.
   - Quantitative: Applying specific stress scenarios.
   - Qualitative: Assessing the bank's ability to absorb losses and identifying mitigation steps.
   - Pillar 2B (Capital Planning Buffer (CPB)): A buffer set to the level of additional capital required in a downturn to ensure the bank remains in surplus. This buffer is drawn upon when there is a downturn in the economic environment and adverse circumstances appear in the economic cycle.

#### Governance & Regulatory Review

Regulators place significant emphasis on the usage of the ICAAP in practice. Banks are encouraged not to simply comply with the regulation, but to use the processes in practice.

Figure 2.1 below illustrates the governance structure of the ICAAP framework at a typical commercial bank, mapping the components of the ICAAP to the internal processes, governance, and approvals, ultimately for regulatory review (SREP).

![alt text](images/icaap_governance.png)

- **Inputs**: Includes Risk Frameworks, Risk Appetite, and Capital Planning/Budgeting.
- **Operational Execution**: Risk specialists (Credit, Operational, Liquidity, etc.) provide input, which is then reviewed by Risk Function Owners.
- **Internal Oversight**: Includes the "Models, Capital and Stress Testing Forum" (MCAST) and the Risk Management Committee.
- **Governing Bodies**: The Board of Directors and the Risk and Audit Committee provide final internal sign-off.
- **SREP and ICG**: The process culminates in the Supervisory Review and Evaluation Process (SREP) by regulators (e.g., the PRA), resulting in Individual Capital Guidance (ICG).
- **Internal Audit**: Provides an independent review of the entire ICAAP and stress testing framework.

### Pillar 2A

Pillar 2A captures risks not fully covered by Pillar 1. The bank must quantify its own capital requirement for each material risk type. The following are the main Pillar 2A risk categories, each with its typical quantification approach.

#### Credit Concentration Risk

Pillar 1 (via the ASRF model) assumes an infinitely granular, perfectly diversified portfolio — i.e., no single borrower or sector adds disproportionate risk. In practice, portfolios are concentrated. Pillar 2A requires an explicit capital add-on to compensate for this.

##### Name Concentration (Granularity Add-on)

Name concentration arises when the portfolio is not sufficiently granular, meaning a single large borrower default could cause losses materially above those predicted by the ASRF model. The standard approach uses the **Gordy-Lütkebohmert (2007) granularity adjustment**, which computes the additional capital needed relative to the infinitely granular ASRF benchmark:

$$\text{GA} = \frac{1}{2C} \sum_i w_i^2 \cdot \frac{\sigma_i^2(\text{UL}_i + \text{EL}_i)}{\text{EL}_i^2}$$

where $w_i$ is the weight of exposure $i$ in the portfolio, $\sigma_i$ is the idiosyncratic standard deviation of losses for $i$, and $C$ is total portfolio capital. A simpler proxy is the **Herfindahl-Hirschman Index (HHI)**:

$$\text{HHI} = \sum_{i=1}^N w_i^2$$

A higher HHI indicates a more concentrated portfolio. The capital add-on scales with HHI: a fully concentrated portfolio (HHI = 1) requires substantially more capital than a fully diversified portfolio (HHI → 0).

##### Sector Concentration

Sector concentration arises when exposures are clustered in a single industry or geography, making the portfolio susceptible to sector-specific downturns. The standard model for sector concentration uses the **multi-factor extension** of the Vasicek model, replacing the single systematic factor with sector-specific factors:

$$X_i = \sqrt{\rho_s} \cdot S_{\text{sector}(i)} + \sqrt{\rho - \rho_s} \cdot S_{\text{market}} + \sqrt{1-\rho} \cdot Z_i$$

where $\rho_s$ is the intra-sector asset correlation, $S_{\text{sector}}$ is the sector-specific systematic factor, and $S_{\text{market}}$ is the common market factor. The capital add-on captures the additional tail risk from high intra-sector correlations when a single sector is stressed.

#### Interest Rate Risk in the Banking Book (IRRBB)

IRRBB is the risk that changes in interest rates affect the bank's economic value or earnings. It is not captured in Pillar 1 credit or market risk RWAs (which are limited to the trading book). Under Pillar 2A, banks must quantify IRRBB using two complementary perspectives:

##### Economic Value of Equity (EVE)

The EVE perspective measures the sensitivity of the present value of all future cash flows to changes in interest rates. A shock to the yield curve changes the value of fixed-rate assets and liabilities:

$$\Delta\text{EVE} = -\sum_i \Delta \text{PV}(\text{cash flows}_i) = -\sum_i \text{MD}_i \cdot \text{PV}_i \cdot \Delta r_i$$

where $\text{MD}_i$ is the modified duration of position $i$ and $\Delta r_i$ is the interest rate shock. The Basel Committee specifies six standardised interest rate shock scenarios (parallel up/down, steepener, flattener, short-up, short-down). The Pillar 2A capital charge is based on the most adverse $\Delta\text{EVE}$ across scenarios. A bank is deemed an outlier if $|\Delta\text{EVE}| > 15\%$ of Tier 1 capital for a 200bp parallel shock.

##### Net Interest Income (NII)

The NII perspective measures the sensitivity of near-term (typically 1–2 year) interest income to rate changes. Unlike EVE, which captures the long-run economic value, NII focuses on short-term earnings volatility. Banks typically model NII sensitivity using assumptions about:

- **Repricing gaps**: The mismatch between assets and liabilities repricing at different dates.
- **Behavioural adjustments**: Non-maturity deposits (e.g., current accounts), prepayment options on mortgages, and pipeline hedges.
- **New business assumptions**: Whether modelled on a static or dynamic balance sheet basis.

$$\Delta\text{NII} = \sum_i \text{GAP}_i \cdot \Delta r_i \cdot \text{tenor}_i$$

where $\text{GAP}_i$ is the repricing gap for bucket $i$, $\Delta r_i$ is the rate shock, and $\text{tenor}_i$ is the fraction of the year the gap is open.

#### Pension Risk

Pension risk arises from defined benefit (DB) pension schemes where the bank has an obligation to fund any deficit in scheme assets relative to scheme liabilities. The liability is sensitive to the discount rate (typically a corporate bond yield), inflation assumptions, and longevity assumptions.

The Pillar 2A pension capital charge is typically computed as the **stressed deficit** under an adverse scenario, over and above the funded deficit already deducted from CET1 capital:

$$\text{EC}_{\text{pension}} = \max(0,\ \text{Pension deficit}_{\text{stressed}} - \text{Pension deficit}_{\text{base}} - \text{CET1 deduction})$$

Standard stresses applied include: a parallel shift down in risk-free rates (increasing the present value of liabilities), a fall in equity markets (reducing scheme assets), and an adverse change in inflation (increasing indexed liabilities).

#### Model Risk

Model risk is the risk of financial losses, regulatory capital miscalculation, or misstatements of financial position arising from errors or limitations in internal models. It is a Pillar 2A risk for banks using IRB and other internal models.

The Pillar 2A capital charge for model risk is typically computed as a **percentage uplift** to Pillar 1 RWAs to reflect the model uncertainty in PD, LGD, and EAD estimates:

$$\text{EC}_{\text{model}} = \alpha \cdot K_{\text{Pillar 1}}$$

where $\alpha$ is set through a model risk assessment framework, taking into account: model validation findings, back-testing results, margin of conservatism (MoC) analysis, and the relative immaturity of models. Regulators may also impose add-ons directly where specific model weaknesses are identified.

#### Business Model Risk and Strategic Risk

Business model risk captures the risk that the bank's current business model becomes unviable due to competitive dynamics, technological disruption, or macroeconomic shifts. Strategic risk relates to adverse decisions at the senior level. These risks are difficult to quantify directly and are typically assessed using:

- Scenario analysis against specific strategic failure modes.
- Earnings volatility analysis across multiple business plan scenarios.
- Peer-group comparisons of business model sustainability.

The Pillar 2A capital charge is set judgementally based on the outcome of these analyses, often expressed as a number of basis points of RWAs.

#### Other Pillar 2A Risks

Other risks assessed under Pillar 2A include:

- **Reputational risk**: Typically assessed qualitatively; capital charge set via stress scenarios (e.g., a run on funding caused by a reputational event).
- **Legal risk**: Capital held against material legal proceedings and potential regulatory fines.
- **Climate and sustainability risk**: An emerging Pillar 2A category requiring banks to assess physical risk (extreme weather events affecting collateral values) and transition risk (stranded asset risk from decarbonisation).
- **Cyber risk**: Operational risk-adjacent; quantified via loss scenario analysis or insurance-gap analysis.

### Pillar 2B

Pillar 2B is the forward-looking component of Pillar 2 capital, determined through stress testing rather than point-in-time assessment. Each jurisdiction may require additional buffers over and above Basel requirements so as to ensure that banks within the system are adequately capitalised and there is a reduced systemic risk.

#### Stress Testing Mechanics

The purpose of Pillar 2B stress testing is to quantify the capital required for the bank to remain above its Pillar 1 + Pillar 2A requirements throughout an adverse macroeconomic scenario. The capital planning buffer (CPB) is the peak shortfall observed over the stress horizon:

$$\text{CPB} = \max_{t \in [0,T]}\left(\text{Pillar 1} + \text{Pillar 2A} - \text{CET1}(t)\right)$$

where $\text{CET1}(t)$ is the CET1 ratio at time $t$ under the stress scenario, modelled as:

$$\text{CET1}(t) = \text{CET1}(0) + \sum_{s=1}^{t} \left[\text{Revenue}(s) - \text{Impairments}(s) - \text{Dividends}(s)\right] - \Delta\text{RWA}(s)$$

The key drivers modelled in a stress scenario are:

- **Impairment charges**: PD migrations and LGD increases driven by macroeconomic shocks (GDP decline, unemployment rise, property price falls). PD and LGD models feed forward-looking ECL calculations (IFRS 9 Stage 2/3 flows), which directly reduce retained earnings.
- **Revenue compression**: Net interest margin compression from lower rates or higher funding costs; non-interest income falls from lower business activity.
- **RWA inflation**: Portfolio downgrades shift borrowers to higher risk weight buckets; models may also produce higher RWAs under stressed PDs (for banks using non-modelled overlays).
- **Dividend and payout policy**: Most banks would suspend or reduce dividends in a stress scenario.

#### Scenario Design

Stress scenarios are designed to be "severe but plausible". Supervisors (e.g., PRA in the UK, PA in South Africa) may prescribe baseline stress assumptions, but banks must also design their own scenarios relevant to their specific risk profile. Standard scenario types include:

- **Macroeconomic downside**: GDP contraction, unemployment spike, property price decline, interest rate shock.
- **Idiosyncratic stress**: A scenario specific to the bank (e.g., a major operational failure, a reputational event, or a concentrated sector loss).
- **Reverse stress test**: Instead of asking "what happens to capital if X occurs?", the reverse stress test asks "what scenario would cause the business model to fail?" and then assesses its plausibility.

The Pillar 2B add-on is generally not disclosed publicly and is bank-specific. In South Africa, the Pillar 2B requirement (referred to as the Individual Capital Requirement (ICR)) combines both the stress-driven capital and any ad-hoc risks identified by the PA that are not captured in Pillar 2A.
