# Operational Risk Capital: [[basel_framework|Basel III]] New Standardised Approach (NSA)

[[basel_framework|Basel III]] introduces a **New Standardised Approach (NSA)** to measuring operational risk capital in response to well-documented weaknesses identified in the [[basel_2|Basel II]] approaches. The NSA is effective from 1 January 2023 and replaces the BIA, TSA/ASA, and AMA.

## Shortfalls with the [[basel_2|Basel II]] Approaches

Post-crisis, the [[bis|Basel]] Committee found that despite an increase in the frequency and severity of operational risk loss events, operational risk capital remained steady or in some cases declined. Where banks experienced events that caused revenue (gross income) to decline, the capital assessed under the standardised approaches decreased — when in fact capital should have increased or held steady.

Other key findings:

- Using gross income as a proxy for risk implicitly assumes a linear relationship between operational risk losses and revenue, which was found to be invalid.
- The size of a bank and its operational risk losses do not increase in a linear manner.
- Changing operational risk profiles may render a calibration based on past behaviour of variables unfit for the future.
- Business lines do not differ significantly in terms of their operational risk profiles (undermining the rationale for differentiated betas in TSA).

For the AMA, the original framework allowed for flexibility in internal modelling practices in the hope that this would converge to best practice over time. This did not materialise, resulting in a lack of comparability between banks and extreme variability in calculated RWAs.

## NSA Capital Calculation

The NSA replaces gross income with a **Business Indicator (BI)** as the proxy for risk — a financial statement-based measure better able to capture a bank's exposure to operational risk inherent in its business mix. The key concepts are:

| Concept | Description |
|---|---|
| Business Indicator (BI) | Financial statement-based proxy for operational risk |
| Business Indicator Component (BIC) | BI multiplied by regulator-determined marginal coefficients ("alphas") |
| Internal Loss Multiplier (ILM) | Scaling factor determined using the bank's average internal [[02-loss_data|loss data]] and the BIC |

### Step 1: Business Indicator (BI)

The BI is the sum of three components, where a bar above a term denotes the average over the most recent 3-year period and "abs" denotes absolute value:

**Interest, Leases and Dividend Component (ILDC):**

```math
\text{ILDC} = \min\left(\overline{|II - IE|},\ 0.035 \times \overline{IEA}\right) + \overline{DI}
```

where $II$ = interest income, $IE$ = interest expense, $IEA$ = interest earning assets, $DI$ = dividend income.

**Services Component (SC):**

```math
\text{SC} = \max\left(\overline{OOI},\ \overline{OOE}\right) + \max\left(\overline{FI},\ \overline{FE}\right)
```

where $OOI$ = other operating income, $OOE$ = other operating expense, $FI$ = fee income, $FE$ = fee expense.

**Financial Component (FC):**

```math
\text{FC} = \overline{|NPLT|} + \overline{|NPLB|}
```

where $NPLT$ = net P&L in the trading book, $NPLB$ = net P&L in the banking book.

```math
\text{BI} = \text{ILDC} + \text{SC} + \text{FC}
```

### Step 2: Business Indicator Component (BIC)

The BIC applies marginal coefficients to the BI according to the bank's size bucket:

| Bucket | BI Range (€bn) | BI Marginal Coefficient |
|---|---|---|
| 1 | ≤ 1 | 12% |
| 2 | 1 < BI ≤ 30 | 15% |
| 3 | > 30 | 18% |

Coefficients are applied in a **marginal manner**. For example, a bank with a BI of €35bn would have a BIC of:

```math
\text{BIC} = 1 \times 0.12 + (30-1) \times 0.15 + (35-30) \times 0.18 = €5.37\text{bn}
```

### Step 3: Internal Loss Multiplier (ILM)

The ILM scales the BIC up or down based on the bank's actual loss experience.

The **Loss Component (LC)** is defined as 15 times the average annual internal operational risk losses over the last 10 years:

```math
\text{LC} = 15 \times \overline{\text{Annual Internal Losses (10yr)}}
```

The ILM is then:

```math
\text{ILM} = \ln\left(\exp(1) - 1 + \left(\frac{\text{LC}}{\text{BIC}}\right)^{0.8}\right)
```

| Condition | ILM | Interpretation |
|---|---|---|
| LC > BIC | ILM > 1 | Actual experience was worse than BI suggests; capital exceeds BIC |
| LC = BIC | ILM = 1 | Capital equals BIC |
| LC < BIC | ILM < 1 | Actual experience was better than BI suggests; capital is below BIC |

### Step 4: Capital Requirement

```math
K_{\text{NSA}} = \text{BIC} \times \text{ILM}
```

```math
\text{RWA} = K_{\text{NSA}} \times 12.5
```

### Data Requirements for ILM

- Banks with **≥ 10 years** of data use the full 10-year average.
- Banks with **5 to 9 years** of quality data may use the available data.
- Banks with **< 5 years** of data must base capital requirements solely on the BIC (i.e. ILM = 1), unless the computed ILM from available data exceeds 1 and the supervisor believes the loss experience is representative of the bank's actual risk exposure.
- For **Bucket 1** banks (BI ≤ €1bn), internal [[02-loss_data|loss data]] does not affect the capital calculation; the ILM is set equal to 1. Supervisors may permit Bucket 1 banks to incorporate internal [[02-loss_data|loss data]] if it meets the necessary collection requirements.
