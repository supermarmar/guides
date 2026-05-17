---
tags:
  - application/banking/internal-environment/risk-measurement/liquidity-risk/lcr
  - difficulty/unknown
  - study-status/new
aliases:
---
# Loan-to-Deposit Ratio (LDR)

The **loan-to-deposit ratio (LDR)** measures the relationship between net lending and customer deposits over the same period, reported monthly. It is a measure of the self-sustainability of the bank — specifically, the degree to which lending is funded by stable customer deposits rather than wholesale markets:

$$\text{LDR} = \frac{\text{Net carrying amount for loans}}{\text{Retail deposits}}$$
**Why net, not gross?** The LDR is a funding sustainability metric — it asks whether deposits are sufficient to fund the loan book as it actually stands on the balance sheet. Gross loans would overstate the asset being funded, since the provision represents a portion of the asset that is expected to be unrecoverable and has already been expensed through the P&L.

**Practical implication:** A bank with a rapidly deteriorating loan book will see its ECL provisions increase, which _reduces_ net loans and thus _mechanically improves_ the LDR — even though credit quality is worsening. This is one of the reasons the LDR must always be read alongside credit quality metrics (Stage 2 ratio, NPL ratio, cost of credit) rather than in isolation.

Interpretation:

- **LDR > 100%**: Can be an early warning sign of excessive asset growth or loss of customer deposits, indicating potentially risky reliance on wholesale funding. Where wholesale funding is short-dated, this risk is exacerbated.
- **LDR < 70%**: May imply excessive liquidity and potentially inadequate returns if surplus funds are deployed in low-yielding assets.
- **LDR 85%–95%**: Generally regarded as business best practice, though the appropriate range varies by [[01-business_model|business model]] and jurisdiction.

A level above 100% is not necessarily bad practice where the bank maintains a liquid asset buffer of sufficient size. However, a number significantly above 100% is an indicator of funding stress in the event of market instability.

The LDR is a useful and widely reported metric, but it is not predictive and does not account for the tenor, concentration, or volatility of funds. It must be used in conjunction with the other measures below.

# 1-Week and 1-Month Liquidity Ratios (LR)

These ratios measure **gap risk** — the net cash flows (including the cash effect of liquidating liquid securities) as a percentage of liabilities for a specific maturity bucket:

$$\text{Liquidity ratio}_{[t]} = \frac{\text{Cash inflows}_{[t]} - \text{Cash outflows}_{[t]} + \text{Liquid assets}_{[t]}}{\text{Total liabilities}}$$

They are typically measured against a regulatory limit and are an effective measure of structural liquidity, providing early warning of likely stress points. A worsening ratio approaching an internal or regulatory limit should drive a change in funding strategy or a structural change to balance sheet composition. While these metrics have been largely superseded by the [[01-short_term_metrics|LCR]] as the primary regulatory measure of short-term liquidity, they provide complementary management information that the [[01-short_term_metrics|LCR]] does not replicate exactly.

# Cumulative Liquidity Model (CLM)

The **cumulative liquidity model (CLM)** extends the liquidity ratio concept into a forward-looking model over a 12-month horizon. It models cumulative cash inflows, outflows, and available liquidity across all maturity buckets, identifying forward-looking liquidity stress points on a cash basis. The CLM is typically prepared daily at legal entity and group level and is the primary tool for identifying when and where funding stress may emerge — it recognises and helps predict stress points before they crystallise.

# Liquid Asset Buffer (LAB)

All banks are required to hold a buffer of **unencumbered liquid assets** — the **liquid asset buffer (LAB)** — to generate liquidity when a stress event occurs. This was always accepted as sound practice, but the [[basel_framework|Basel III]] regime codified it via regulatory minimum standards (see the [[01-short_term_metrics|LCR]] requirement). A LAB must comprise:

- Good credit quality assets
- Funded out of stable or term funding (i.e. not themselves subject to maturity rollover risk)
- Readily convertible to cash at 1-day notice if required

The stock of assets in the LAB is more commonly known, in the context of the [[basel_framework|Basel III]] [[01-short_term_metrics|LCR]], as the **stock of high-quality liquid assets (HQLA)**. Regulators expect HQLA to retain both value and market liquidity in a stressed environment — meaning they can be monetised without large discounts in sale or repo markets, even under fire-sale conditions.

Central bank eligibility of an asset is not a criterion for HQLA classification, because central bank funding should not be considered a BAU source of liquidity (see [Liquidity Framework](../../04-liquidity_management.md)).