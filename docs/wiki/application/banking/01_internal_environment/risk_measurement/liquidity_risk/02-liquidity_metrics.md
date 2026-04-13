---
tags:
  - application/banking/internal-environment/risk-measurement/liquidity-risk/liquidity-metrics
  - difficulty/unknown
  - study-status/new
aliases:
---
# Liquidity Metrics

This file covers the **quantitative liquidity risk metrics** used by bank treasury functions and Asset Liability Committees (ALCOs) to monitor and manage liquidity risk, including six baseline management information metrics, and the stock of high-quality liquid assets (HQLA) that forms the liquid asset buffer (LAB).

For the conceptual framework of liquidity risk — definitions, sources of funding, liability stability hierarchy — see [Liquidity Framework](01-liquidity_framework.md). For the balance sheet treatment of HQLA, see [Annual Financial Statements](../../02-afs.md). For the regulatory minimum [[04-lcr|LCR]] and [[05-nsfr|NSFR]] requirements that consume these metrics, see [Basel / BIS](bis.md).

## Baseline Liquidity Risk Metrics

Banks calculate and monitor six key baseline metrics as a matter of course. These measure different elements of liquidity risk and, for consolidated or group banking entities, are prepared at country level, legal entity level, and group level. Together, they provide visibility on:

- The exposure of the bank to funding rollover ("gap") risk
- The daily funding requirement and a forecast of future requirements
- The extent of self-sufficiency of a branch or subsidiary

Liquidity risk must be managed and monitored at a material currency level, as it should not be assumed that all currencies are freely convertible.

### Loan-to-Deposit Ratio (LDR)

The **loan-to-deposit ratio (LDR)** measures the relationship between net lending and customer deposits over the same period, reported monthly. It is a measure of the self-sustainability of the bank — specifically, the degree to which lending is funded by stable customer deposits rather than wholesale markets:

$$\text{LDR} = \frac{\text{Net loans}}{\text{Customer deposits}}$$

Interpretation:

- **LDR > 100%**: Can be an early warning sign of excessive asset growth or loss of customer deposits, indicating potentially risky reliance on wholesale funding. Where wholesale funding is short-dated, this risk is exacerbated.
- **LDR < 70%**: May imply excessive liquidity and potentially inadequate returns if surplus funds are deployed in low-yielding assets.
- **LDR 85%–95%**: Generally regarded as business best practice, though the appropriate range varies by [[01-business_model|business model]] and jurisdiction.

A level above 100% is not necessarily bad practice where the bank maintains a liquid asset buffer of sufficient size. However, a number significantly above 100% is an indicator of funding stress in the event of market instability.

The LDR is a useful and widely reported metric, but it is not predictive and does not account for the tenor, concentration, or volatility of funds. It must be used in conjunction with the other measures below.

### 1-Week and 1-Month Liquidity Ratios

These ratios measure **gap risk** — the net cash flows (including the cash effect of liquidating liquid securities) as a percentage of liabilities for a specific maturity bucket:

$$\text{Liquidity ratio}_{[t]} = \frac{\text{Cash inflows}_{[t]} - \text{Cash outflows}_{[t]} + \text{Liquid assets}_{[t]}}{\text{Total liabilities}}$$

They are typically measured against a regulatory limit and are an effective measure of structural liquidity, providing early warning of likely stress points. A worsening ratio approaching an internal or regulatory limit should drive a change in funding strategy or a structural change to balance sheet composition. While these metrics have been largely superseded by the [[04-lcr|LCR]] as the primary regulatory measure of short-term liquidity, they provide complementary management information that the [[04-lcr|LCR]] does not replicate exactly.

### Cumulative Liquidity Model

The **cumulative liquidity model (CLM)** extends the liquidity ratio concept into a forward-looking model over a 12-month horizon. It models cumulative cash inflows, outflows, and available liquidity across all maturity buckets, identifying forward-looking liquidity stress points on a cash basis. The CLM is typically prepared daily at legal entity and group level and is the primary tool for identifying when and where funding stress may emerge — it recognises and helps predict stress points before they crystallise.

### Liquidity Risk Factor

The **liquidity risk factor (LRF)** — also referred to as the **maturity transformation ratio** — is a static snapshot comparing the average tenor of assets to the average tenor of liabilities:

$$\text{LRF} = \frac{\text{Weighted average tenor of assets (days)}}{\text{Weighted average tenor of liabilities (days)}}$$

Tenors are calculated as weighted averages of either the behavioural or contractual tenors (or both), weighted by nominal amounts or actual drawn balances. A higher LRF indicates a larger maturity gap and hence greater liquidity risk being run by the bank.

The LRF has limited value as a one-off number. Its utility lies in **trend monitoring over time** and comparison against long-run averages, to provide early warning of the build-up of a potentially unsustainable funding structure. The limit is set judgementally by the ALCO and varies according to the risk profile and risk tolerance of the individual bank. This metric has been largely superseded by the **[[05-nsfr|net stable funding ratio (NSFR)]]** as the primary regulatory measure of structural funding risk.

### Concentration and Funding Source Report

The **concentration report** shows the extent of reliance on a single source of funds — by depositor name, sector, or country. Excessive concentration to any one lender, sector, or country is an early-warning sign of potential funding stress, since the withdrawal of a concentrated source leaves the bank with an acute structural shortfall.

Banks set a single-customer concentration limit (for example, 10% of the aggregate funding base) and monitor their largest depositors against it. The tenor of the deposits is considered alongside the concentration level: a concentrated long-dated deposit carries materially less risk than a concentrated short-dated deposit. Where the limit is breached, the bank should either reduce the concentration or increase the aggregate deposit base, or alternatively maintain sufficient liquid assets to cover the potential outflow.

### Inter-Entity Lending Report

The **inter-entity lending report** is relevant for group and consolidated banking entities. Intra-group lending is common in banking groups, and in some jurisdictions is subject to cross-border and cross-legal-entity regulatory limits. This report measures the reliance of a specific subsidiary or branch on intra-group funding and tracks proximity to regulatory limits — providing visibility on the self-sufficiency or otherwise of each legal entity within the group.

## High-Quality Liquid Assets (HQLA) and the Liquid Asset Buffer

### Liquid Asset Buffer

All banks are required to hold a buffer of **unencumbered liquid assets** — the **liquid asset buffer (LAB)** — to generate liquidity when a stress event occurs. This was always accepted as sound practice, but the [[basel_framework|Basel III]] regime codified it via regulatory minimum standards (see the [[04-lcr|LCR]] requirement). A LAB must comprise:

- Good credit quality assets
- Funded out of stable or term funding (i.e. not themselves subject to maturity rollover risk)
- Readily convertible to cash at 1-day notice if required

The stock of assets in the LAB is more commonly known, in the context of the [[basel_framework|Basel III]] [[04-lcr|LCR]], as the **stock of high-quality liquid assets (HQLA)**. Regulators expect HQLA to retain both value and market liquidity in a stressed environment — meaning they can be monetised without large discounts in sale or repo markets, even under fire-sale conditions.

Central bank eligibility of an asset is not a criterion for HQLA classification, because central bank funding should not be considered a BAU source of liquidity (see [Liquidity Framework](01-liquidity_framework.md)).

### HQLA Eligibility Tiers ([[sarb|SARB]])

The [[sarb|South African Reserve Bank]] ([[sarb|SARB]]) classifies eligible HQLA into three tiers, reflecting their credit quality and expected liquidity under stress:

**Level 1** (highest quality — no haircut applied):
- Cash (notes and coins)
- Cash reserves held with the [[sarb|SARB]]
- Marketable securities issued by the [[sarb|SARB]] or Public Sector Entities (PSEs), including:
  - Treasury bills
  - Security loans
  - Nominal and index-linked government bonds
  - Repurchase transactions / buy-sell-backs (used for temporary acquisition of HQLA, not themselves assets)

**Level 2A** (subject to a regulatory haircut):
- Corporate and SOE debt securities rated AA– or higher

**Level 2B** (subject to a larger regulatory haircut):
- Corporate and SOE debt securities rated BBB– or higher

The tiering reflects the observed behaviour of these assets in stress events: Level 1 assets (primarily government securities) retain value and liquidity even in severe market disruption, while lower-tier assets are subject to greater price discounts and liquidity impairment under stress.
