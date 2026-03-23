# DCF Loan Pricing Model

This file covers the mechanics of discounted cashflow (DCF) models used to assess the pricing and profitability of loan products — model structure, assumptions, and uses. For the loan products themselves see [Loan Pricing](03-loan_pricing.md). For credit risk parameters (PD, LGD, EAD) see the credit risk modelling files.

## Model Overview and Purpose

A DCF model helps a bank derive the loan interest rate and fees for a given customer segment such that the net present value (NPV) of the loan is positive under a specified return criterion. The model:

- Represents a single notional account, scaled to portfolio level
- Must be validated and back-tested against actual portfolio experience (balance run-down, default volumes, interest revenue)
- Aims to be simple enough for senior management to trust, while capturing the most relevant cashflows

Product complexity scales with behaviour: a fixed-rate term loan is the simplest to price; mortgages with introductory periods require a three-state Markov multiple-decrement model (introductory rate → SVR → withdrawal); credit cards require assumptions on utilisation rates, repayment behaviour, and competitor campaign effects.

## Model Structure

### In-Force Population Dynamics

Not all borrowers follow the contractual repayment schedule. The bank must model the rate at which loans leave the portfolio due to **default** (d) or **early settlement** (s), using historically observed cumulative curves (fitted per application scorecard decile or risk segment):

```math
n_{t+1} = n_t - d_t - s_t
```

where $n_t$ is the in-force count at time $t$, $d_t$ is defaults at $t$, and $s_t$ is settlements at $t$. All customers remain accounted for across three states: in-force, default, and settled. When the curves are scaled (e.g. to a specific starting cohort), the scaling must interact with the remaining in-force population, not the original cohort size.

### Default Balance and Loss Calculation

The default balance at time $t$ can be expressed as a ratio of:
- The original loan amount
- The contractual balance outstanding (adjusted for term and amortisation)
- The behavioural run-down balance

The **contractual balance ratio** is generally preferred. The default loss at each duration is then:

```math
\text{Default Loss}_t = d_t \times \text{Balance at default}_t \times \text{LGD}_t
```

LGD parameters are sourced from the IFRS 9 or IRB rating system (see credit risk modelling). Default losses are calculated across all model durations.

### Balance Run-Down

The remaining in-force balance at each duration is expressed as a ratio of observed outstanding balances to contractual balances. This allows the model to respond dynamically when interest rates are updated: the balance run-down curve captures past repayment behaviour at historical rates, so care is needed when new pricing diverges significantly from historical rates.

## Assumptions

### Income

Income has two components: **interest income** and **non-interest (fee) income**. Both decline over the loan life as the in-force population shrinks.

- Interest income may be fixed or variable rate. Fixed-rate income should be hedged using interest rate swaps based on the **behavioural term** (not the contractual term), unless the customer contractually bears the cost of breaking the hedge. Hedging costs appear as negative income.
- Introductory rate periods (e.g. 0% credit cards) require hedging only to the re-pricing date.
- Fee income may be initial (e.g. mortgage arrangement fee), ongoing (transaction fees), or final (early repayment charges). Some fees must be spread over the product life under **EIR (Effective Interest Rate) accounting**. Regulatory caps on fees and early repayment charges may apply.

### Expected Credit Losses (ECL)

ECL is typically low at origination, rises over the loan life, then levels off or declines. Banks use through-the-cycle expected loss assumptions for fundamental pricing; point-in-time losses are too volatile (too low in booms, too high in recessions). Stress scenarios consistent with ICAAP stress testing may be evaluated alongside the base case.

Under **IFRS 9**, provisions reduce profits and capital immediately. The DCF model must account for both the amount and timing of ECL impacts on capital. Note that **IFRS 9 ECL ≠ Basel expected loss** — the Basel expected loss definition differs methodologically and a capital gap adjustment may be necessary (see figure below: Basel methodology creates a gap between provisions held and the capital required to cover losses at the 0.1% confidence level).

### Operational Costs

Operational costs are split into: **direct variable costs** (credit bureau fees, intermediary fees — vary per transaction), **semi-fixed direct costs** (product design and marketing teams — increase with volume but benefit from economies of scale), and **shared/indirect costs** (head office, IT, treasury, branch network — fixed, allocated across products).

For the credit cut-off decision and marginal pricing, only **marginal costs** (variable + incremental semi-fixed) should be used. Fully-loaded costs (including allocated fixed costs) are used for overall profitability monitoring. A bank that applies fully-loaded costs to the cut-off decision will reject loans that would have contributed to fixed cost recovery, potentially ending up with insufficient volume.

### Capital Requirements and Cost of Capital

CET1 capital is the primary loss-absorbing capital and the denominator for ROE/RORAC calculations. The capital profile (amount of capital required at each loan duration) must be explicitly modelled, using either:

- The **Basel Standardised Approach** (prescribed risk weights — generally higher, putting standardised banks at a disadvantage vs IRB banks, particularly for mortgages)
- **Internal models (IRB)** — subject to regulatory approval, generally produce lower capital requirements

Capital buffers (CCB, countercyclical, etc.) should be allocated to loan categories in proportion to the stress losses identified in the ICAAP.

**Approach 1 — Capital as deferred expense:**
Treat capital as an upfront charge; as balances repay, capital is progressively released back into P&L. Total of initial charge and releases = zero. The discount rate used is the bank's targeted return on capital (ROE hurdle rate).

**Approach 2 — Opportunity cost of capital:**
Recognise capital required at each duration; charge the **opportunity cost of capital** (targeted ROC − actual return on assets in which capital is invested) as an explicit expense at each period. The discount rate is set to the risk-free rate, since the required return is already charged explicitly as a cost.

### Funding Costs (FTP)

Loans are funded by a mix of CET1 capital, debt capital, and deposits. The FTP rate (from treasury's term liquidity premium yield curve) is applied to the balance run-down and in-force volumes at each duration. Interest on debt capital is charged at actual rates paid. See [Deposit Pricing](02-deposit_pricing.md) for FTP and TLP mechanics.

## Profit Calculation and NPV

At each duration, the profit is:

```
Profit_t = NII_t + Non-interest income_t − FTP cost_t − Operating costs_t − ECL_t − Capital cost_t
```

The **NPV** is the sum of discounted profits across all durations:
- Under Approach 1: discount at the targeted ROC (ROE hurdle)
- Under Approach 2: discount at the risk-free rate

**For pricing to be satisfactory, NPV ≥ 0.** The model is iterated to find the rate at which NPV = 0 (the break-even rate), and the business sets pricing above this level to achieve a positive target return.

## Uses of the DCF Model

### Credit Cut-Off Score

As credit risk increases, the NPV of a fixed-rate loan (say at 6%) declines and eventually turns negative. The **credit cut-off score** is the minimum acceptable borrower score — the point where NPV = 0. For cut-off decisions, only marginal costs should be included (not allocated fixed costs), to avoid over-restricting lending. The bank should also ensure it writes enough volume to cover fixed costs, requiring a balance between cut-off stringency and volume.

### Risk-Based Pricing

To lend to higher-risk borrowers while maintaining positive NPV, the rate charged must increase. At 15% on a higher-risk segment, the NPV turns positive again. This is **risk-based pricing**: offering 6% to low-risk borrowers and 15% to high-risk borrowers. The practical requirement: the bank must offer rates differentially based on individual credit assessment, not a blanket high rate to everyone, because a single high rate (15%) would fail to attract low-risk customers (who get 6% elsewhere) and attract only high-risk borrowers — pure **adverse selection**.

Risk-based pricing uses: consumer credit bureau scores for retail loans; LTV bands for mortgages; financial statement analysis for corporate loans. Regulatory constraints apply (e.g. UK's 51% at headline rate rule).

### Marginal Pricing and Contribution to Fixed Costs

A bank may extend loans at prices covering only marginal costs (variable + incremental semi-fixed), to generate volume that contributes to fixed cost recovery. However, pricing too many loans at marginal cost risks not covering the total fixed cost base. If a bank cannot cover fixed costs, the correct response is typically to reduce fixed costs (e.g. branch closures) rather than raise prices, because raising prices in a competitive market reduces volume, further increasing per-unit fixed costs.

### Lifetime ROE / RORAC

A simpler, widely used summary metric for loan profitability. The **lifetime (undiscounted) ROE** for new loans:

```math
\text{Lifetime ROE} = \frac{\text{Lifetime profit (undiscounted)}}{\text{Lifetime average capital}}
```

where lifetime average capital = (sum of capital required at each month) ÷ number of months. This represents the ROE the bank would earn if the loan reaches steady state (i.e. held to maturity). **RORAC** uses risk-adjusted capital (CET1 per Basel) in the denominator — equivalent to ROE when CET1 is the relevant capital measure. This metric is useful for rapid profitability comparison across products and banks using Basel-standardised capital requirements.
