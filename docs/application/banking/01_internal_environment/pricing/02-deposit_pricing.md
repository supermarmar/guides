# Deposit Pricing

This file covers the pricing of bank deposit products — product types and their value to the bank, price elasticity theory, cannibalisation, strategies for reducing the marginal cost of deposits, and the role of the term liquidity premium. For the structural liquidity management implications of deposit behaviour see [Liquidity Framework](../liquidity_risk/01_introduction/01-liquidity_framework.md) and [LCR](../liquidity_risk/01_introduction/04-lcr.md). For the pricing framework overview and NIM management see [Pricing Framework](01-pricing_framework.md).

## Deposit Product Types

Deposit products sit on a spectrum from fully flexible to fully locked-in. The more flexibility the product offers, the lower the rate; the less flexibility, the higher the rate. For product descriptions see [Products](../06-products.md).

**Instant access deposits** (call accounts, savings accounts) — customers may withdraw at any time. Banks can still use these funds for term lending because aggregate inflows and outflows tend to net off, leaving a stable funding core. However, banks must hold HQLA against these deposits to cover stress outflows (governed by Basel III LCR rules — see [LCR](../liquidity_risk/01_introduction/04-lcr.md)), which reduces the net return from holding them as funding.

**Notice accounts** — withdrawals require advance notice (common periods: 32, 60, 90 days). No HQLA required, making them more valuable to the bank as a stable funding source. Regulations typically permit an early breakage fee that covers the bank's lost interest.

**Fixed-term deposits / savings bonds** — both deposits and withdrawals are locked in for an agreed term (1–60 months), usually at a fixed rate. Most valuable to the bank: no HQLA required, allows term-matched funding of loans. Banks can use pricing ladders (adjusting rates on specific tenors based on upcoming maturities) to optimise rollover costs. Saving a few basis points on the rollover of a large maturing tranche can materially affect profitability.

**Current accounts (MTAs)** — payment-focused accounts with debit cards, direct debits, overdraft facilities, and low or zero credit interest rates. Despite low/zero deposit rates, current accounts are expensive to operate (IT, fraud, branch infrastructure). Their value lies in customer relationships and cross-sell opportunity, not in low funding cost alone.

## Price Elasticity

**Price elasticity of deposits** is defined as:

```math
\text{Price elasticity} = \frac{\% \text{ change in volume}}{\% \text{ change in price}}
```

For example, if elasticity = 25%, a 1% rise in the deposit rate produces only a 0.25% increase in deposit volumes. To attract a 5% volume increase, the rate must rise 20% (e.g. from 0.5% to 0.6%).

### Marginal Cost of Deposits

Increasing the rate on all existing deposits to attract new money is costly. The **marginal cost** of the additional deposits is:

```math
\text{Marginal cost} = \frac{\Delta \text{Interest paid}}{\Delta \text{Volume of deposits}}
```

In the example above, raising the rate from 0.5% to 0.6% on £100bn to attract £5bn new deposits: the extra interest paid = £100bn × 0.1% + £5bn × 0.6% = £130m on £5bn extra deposits = marginal cost of **2.6%**, far exceeding the 0.5% average deposit cost. If lending earns only 3%, the true cost of growing the book by repricing the entire back book may erode almost all the lending margin.

This explains why banks manage deposit books carefully: the goal is to minimise the marginal cost of additional deposits, not just the average cost.

### Cannibalisation

When banks introduce a new higher-rate product to raise incremental deposits, existing depositors transfer to the new product. **Cannibalisation** means the effective new money raised is less than total inflows into the new product. If £15bn flows into a new 1%-rate product but £10bn transfers from the existing 0.5%-rate product (with only £5bn being genuinely new money):

```
Extra interest = £10bn × (1% − 0.5%) + £5bn × 1% = £100m
Marginal cost = £100m / £5bn = 2.0%
```

This is better than repricing the entire back book but still far above the average cost. Cannibalisation must be modelled carefully when designing new products or promotional campaigns.

## Strategies to Reduce Marginal Deposit Cost

**Multiple products for different segments:** Offering instant-access, notice, and term products allows price-sensitive customers who are willing to lock funds away to self-select into higher-rate term products, while transactional customers remain on low-rate current accounts. This limits the rate the bank pays on the bulk of its stable deposit base.

**Preferential rates for specific segments:** The senior/retired market has a higher savings propensity; competition for this segment is intense, and banks frequently offer preferential rates targeted at them. This attracts incremental stable deposits with lower cannibalisation risk from the general population.

**Differentiated distribution channels:** Online deposit accounts historically attract price-sensitive, financially active customers. A bank can offer higher rates on online-only products while maintaining lower rates in branches, reducing cannibalisation from less price-sensitive customers who prefer branch access. However, online depositors may be "rate chasers" who switch more readily to competitors, so retention risk must be assessed.

**Regulatory constraint (TCF):** Product design must avoid discriminating against customers who can only access banking through one channel (particularly relevant in South Africa). Rate structures must be defensible under TCF principles.

## Term Liquidity Premium in Deposit Pricing

Banks can treat the deposit book as a pure funding vehicle (assigning all profit to lending) or use **funds transfer pricing (FTP)** to intermediate between deposits and loans via treasury. Under FTP, treasury creates a bank-specific yield curve reflecting the internal cost of raising money for different tenors. Deposits are "rewarded" based on their behavioural tenor — a longer-dated deposit receives a higher internal FTP rate, turning the deposit book into a profit centre.

The **term liquidity premium (TLP)** adds a term-dependent cost above the short-term funding rate to reflect maturity transformation risk. For deposits:

- For **corporate and investment banking**, the TLP methodology directly reflects the wholesale funding curve and is applied strictly: the deposit is valued at its behavioural tenor's TLP-inclusive rate.
- For **retail banking**, applying the wholesale TLP methodology rigidly can misprice deposits relative to competitors, because retail banks fund primarily from retail deposits rather than wholesale markets. The retail TLP should be calibrated to reflect the actual retail deposit funding mix, not the pure wholesale curve.

A bank that fails to apply TLP concepts risks subsidising long-term loans with cheap short-term funding in a way that appears profitable but embeds unpriced maturity transformation risk. When rates rise, the cost of rolling short-term deposits increases while fixed-rate loans remain locked at original spreads, destroying NIM.
