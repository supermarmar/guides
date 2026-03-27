# Net Stable Funding Ratio (NSFR)

## Purpose and Formula

The **net stable funding ratio (NSFR)** is the [[basel_framework|Basel III]] long-term structural liquidity metric. Its purpose is to promote resilience over a one-year horizon by requiring banks to fund their activities with stable sources of funding on an ongoing basis. The NSFR seeks to:

- Reduce dependency on short-term wholesale markets
- Promote diversification of funding sources
- Limit rollover and maturity mismatch risks

A low NSFR indicates a concentration of funding in shorter maturities (less than one year), which creates structural rollover and mismatch risk. The NSFR complements the [[04-lcr|LCR]] (30-day horizon) by addressing the longer-term structural funding position.

```math
\text{NSFR} = \frac{\text{Available amount of stable funding (ASF)}}{\text{Required amount of stable funding (RSF)}} \geq 100\%
```

[[basel_framework|Basel III]] requires the NSFR to be maintained at or above 100% on an ongoing basis.

## Available Stable Funding (ASF)

ASF measures the relative stability of funding sources. It is calculated as the sum of weighted amounts of capital and liabilities, using prescribed **ASF factors**:

| Factor | Available stable funding components |
|---|---|
| **100%** | Total regulatory capital; other capital instruments and liabilities with residual maturity > 1 year |
| **95%** | Retail and SME "stable" demand and term deposits with residual maturity < 1 year |
| **90%** | Retail and SME "less stable" demand and term deposits with residual maturity < 1 year |
| **50%** | Non-financial corporate funding with residual maturity < 1 year; operational deposits; sovereigns and PSEs funding with residual maturity < 1 year; other funding with residual maturity > 6 months and < 1 year |
| **35%** | ZAR financial corporate funding (excluding banks) with residual maturity < 6 months — **South Africa specific** (see below) |
| **0%** | All other liabilities and equity not included above (including liabilities without a stated maturity); derivatives payable net of receivable |

## Required Stable Funding (RSF)

RSF measures the stable funding required to support the bank's assets and off-balance-sheet exposures. It is calculated as the sum of weighted amounts of assets and off-balance-sheet activity, using prescribed **RSF factors**:

| Factor | Required stable funding components |
|---|---|
| **0%** | Coins and banknotes; all central bank reserves |
| **5%** | Unencumbered Level 1 HQLA, excluding coins, banknotes, and central bank reserves |
| **15%** | Unencumbered Level 2A assets |
| **50%** | Unencumbered Level 2B assets; deposits held at other financial institutions for operational purposes; loans to non-financial corporates, sovereigns, [[05-central_banks|central banks]], and PSEs with maturity < 1 year |
| **65%** | Unencumbered residential mortgages with residual maturity > 1 year and risk weight ≤ 35%; other unencumbered loans with residual maturity > 1 year and risk weight ≤ 35% |
| **85%** | Unencumbered non-financial loans (risk weight > 35%) with residual maturity > 1 year; unencumbered listed securities not qualifying as HQLA; physical traded commodities including gold |
| **100%** | All other assets; derivatives receivable net of derivatives payable where receivables exceed payables (plus 10% of derivatives payable) |

Liabilities and equity are valued before regulatory deductions, filters, or other adjustments. Assets are valued at accounting value (net of specific provisions).

## Worked Example

| Assets | Amount (£) | RSF Factor | Liabilities | Amount (£) | ASF Factor |
|---|---|---|---|---|---|
| Loans (maturity > 1yr, RW ≤ 35%) | 500,000 | 65% | Stable retail deposits | 400,000 | 95% |
| Central bank deposits | 25,000 | 0% | Less stable SME deposits | 150,000 | 90% |
| Cash | 80,000 | 0% | Non-financial corporate funding | 60,000 | 50% |
| Other assets | 45,000 | 100% | Equity | 40,000 | 100% |
| **Total** | **650,000** | | **Total** | **650,000** | |

```math
\text{ASF} = (400{,}000 \times 0.95) + (150{,}000 \times 0.90) + (60{,}000 \times 0.50) + (40{,}000 \times 1.00) = 585{,}000
```

```math
\text{RSF} = (500{,}000 \times 0.65) + (25{,}000 \times 0) + (80{,}000 \times 0) + (45{,}000 \times 1.00) = 370{,}000
```

```math
\text{NSFR} = \frac{585{,}000}{370{,}000} = 158\%
```

## Improving NSFR Compliance

Adjusting the NSFR requires balance sheet restructuring, which is necessarily slow. Strategic decisions should always be assessed for their NSFR implications before implementation.

To **increase the NSFR**, a bank has two levers:

- **Increase ASF** (liability side): lengthen liability maturities, shift towards liabilities with higher ASF factors (e.g. retail deposits instead of short-term wholesale), raise longer-term capital instruments.
- **Decrease RSF** (asset side): shorten asset maturities, shift towards assets with lower RSF factors (e.g. reduce long-term loans or increase central bank reserves), reduce off-balance-sheet exposures.

In extreme cases, major NSFR shortfalls may require a fundamental [[01-business_model|business model]] realignment: compressing net derivatives positions, cutting credit lines, focusing on advisory rather than balance-sheet-intensive activities, or adopting an "originate and distribute" model.

## South African Structural Challenges and Dispensations

South Africa faces structural constraints that create a more challenging NSFR environment than in many international jurisdictions:

- A **low domestic savings rate**, combined with well-developed insurance, pension, and asset management (unit trust) markets, channels savings away from bank deposits.
- South African banks source a large portion of funding through **money market funds and institutional investors** — classified as financial corporates and deemed less stable by [[basel_framework|Basel III]].
- Under the standard [[basel_framework|Basel III]] framework, ZAR-denominated funding from financial corporates with residual maturity under 6 months attracts an ASF factor of **0%**, implying it provides no stable funding value.

The [[sarb|SARB]] concluded that this treatment was overly punitive given South Africa's structural features. There are regulatory and economic barriers — including exchange controls and prudential requirements on financial corporates — that prevent capital from flowing out of the domestic economy. The rand operates effectively as a **"closed rand system"**, meaning ZAR deposits cannot easily be drained by offshore currency withdrawal. Accordingly, the [[sarb|SARB]] granted a **South Africa-specific dispensation**: secured and unsecured ZAR funding from financial corporate customers (excluding banks) with residual maturity < 6 months is assigned an ASF factor of **35%** rather than 0%. This dispensation is available only to banks conducting business in South Africa.
