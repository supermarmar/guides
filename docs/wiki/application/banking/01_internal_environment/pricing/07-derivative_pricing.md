---
tags:
  - application/banking/internal-environment/pricing/derivative-pricing
  - difficulty/unknown
  - study-status/new
aliases:
---
# Derivative Pricing

This file covers investment banking pricing — the pricing of transactional and advisory services, and the mathematical foundations of derivative pricing including risk-neutral pricing, Black-Scholes, dynamic hedging, swaps, and the breakdown of these models under stress. For interest rate and FX derivatives used in asset-liability management see [Market Risk](../market_risk/05-market_risk.md) and [IRRBB Measurement](../market_risk/04-irrbb_measurement.md). For [[08-proprietary_trading_xva_pension|xVA]] adjustments to derivative fair values see [Proprietary Trading and xVA](../market_risk/08-proprietary_trading_xva_pension.md).

## Investment Banking Services and Pricing Regimes

### Transactional Services

Securities trading and standardised derivative contracts are highly commoditised and competitive. Prices are effectively set by the market — competition drives fees to the marginal cost of the least efficient provider. Investment banks must achieve economies of scale to remain profitable. Example: equity commissions on the NYSE fell from ~$0.40 (mid-1980s) to ~$0.05 (2005) while volumes grew. Investment banks competing on transaction services focus entirely on cost reduction.

### Advisory Services

Advisory services (M&A advice, debt/equity capital raising, IPOs) are far less commoditised. Reputation and track record are the primary differentiators. A small number of large banks dominate. Fees are set by the banks, not the market, and reflect deal size and complexity:
- Large IPOs: ~3% of funds raised
- Smaller IPOs: ~7% of funds raised

Advisory pricing reflects the bank's role in **price discovery** — establishing a fair price acceptable to both issuers and investors — and ensuring the deal succeeds. Fees in advisory have been relatively stable for decades.

### Overall Profitability of Customer Relationships

Universal banks offering both corporate banking and investment banking to the same customer may price some services at or below cost (e.g. payment services) to maintain the relationship and access to more profitable mandates (bond issuance, hedging, advisory). Inter-business tensions arise when remuneration is tied to individual business unit profitability.

## Risk-Neutral Pricing

Traditional finance values assets by projecting future cashflows and discounting at a risk-adjusted rate (e.g. using CAPM). **Financial economics — and derivative pricing — takes a fundamentally different approach**: it removes the need to estimate probabilities or risk preferences by constructing a **risk-neutral (hedged) portfolio**.

**The bookmaker analogy:** A bookmaker does not need to know the true probability of each horse winning. Instead, they set odds based on the money bet, creating a book where their payout is the same regardless of the outcome (with a bid-offer spread locking in profit). Investment banks price derivatives the same way: they set the price such that any existing book position can be perfectly hedged, eliminating directional risk. The fair price is the one that makes the hedged portfolio earn exactly the risk-free rate — no more, no less.

## Pricing a Forward Contract

A forward contract obligates the buyer to purchase an asset at time $T$ for a price $K$ agreed today. Payoff at maturity: $S(T) - K$.

To price fairly (eliminating arbitrage), an investor who sells the forward can hedge by borrowing $S(0)$ today at the risk-free rate $i$ and buying the asset. At maturity, the loan has grown to $S(0)(1+i)^T$. The proceeds from the forward ($K$) must repay the loan exactly, or the investor would have locked in either a riskless profit or loss:

```math
K = S(0) \times (1 + i)^T
```

The forward price depends only on the **current spot price** and the **risk-free rate** — not on the investor's view of future price movements. This no-arbitrage result holds for all derivatives: the fair price is always the cost of a self-financing hedging strategy.

## Black-Scholes Option Pricing

### Key Assumptions

Fisher Black and Myron Scholes (1973 Nobel Prize) derived their option pricing formula under five assumptions:

1. Both the derivative and underlying asset markets are highly liquid and continuously tradeable.
2. Trading is frictionless — no dealing costs.
3. A risk-free asset exists and can be borrowed or lent in any quantity.
4. Asset prices are "well-behaved" — no step changes (continuous paths).
5. It is impossible to create a risk-free portfolio that earns more than the risk-free rate (no arbitrage).

An additional distributional assumption: **stock prices follow a lognormal distribution** (i.e. log returns are normally distributed).

### The Black-Scholes Formula

The price of a **European call option** on stock $S$, exercisable at time $T$, with strike price $K$ and risk-free rate $r$, where volatility is $\sigma$:

```math
c(S,T) = S \cdot N(d_1) - K e^{-rT} N(d_2)
```

where:

```math
d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
```

$N(\cdot)$ is the cumulative standard normal distribution. This formula allows investment banks to price options and establish trading desks that dynamically hedge portfolios of securities and derivatives — the trading desk functions as a bookmaker, hedging out risk as trades are placed.

## Option Greeks and Dynamic Hedging

**Delta ($\Delta$)** is the first-order sensitivity of the option price $V$ to the underlying asset price $S$:

```math
\Delta = \frac{\partial V}{\partial S}
```

A delta-hedged portfolio holds $\Delta$ units of the underlying for each option written, so that small moves in $S$ produce offsetting gains and losses. **Delta hedging** must be continuously rebalanced as the underlying price moves.

**Vega ($\nu$)** is the sensitivity of the option price to the volatility $\sigma$ of the underlying:

```math
\nu = \frac{\partial V}{\partial \sigma}
```

A vega-hedged portfolio offsets exposure to changes in implied volatility by holding or being short of appropriate amounts of the underlying. In practice, vega is hedged with other options.

**Dynamic hedging** works continuously in theory. In practice, it entails dealing costs at every rebalance and locks in small incremental losses because a convex option payoff is hedged with a linear instrument — hedging is never perfect. These operational costs must be priced into the derivative bid-offer spread. Additionally, **gap risk** (sudden overnight or intraday price dislocations) can make dynamic hedging prohibitively expensive or impossible to execute.

## Swaps

### Interest Rate Swaps (IRS)

An IRS is a contract exchanging interest payments on a notional principal for an agreed period. Example: Party A pays 3m LIBOR + 0.25% and receives 2% fixed for 2 years on a notional of £1m.

This allows a bank to safely fund a fixed-rate loan (earning 4%) with variable-rate deposits (paying 3m LIBOR). Without the swap, rising LIBOR compresses [[03-nii_nim|NIM]]; with the swap, the bank locks in a fixed net margin regardless of LIBOR:

```
Net margin = 4% (fixed rate on loan) − 2% (fixed paid on swap) = 2% fixed
```

Most LIBOR rates were phased out from end-2021 following the 2012–13 manipulation scandal. Replacements include **SONIA** (Sterling Overnight Index Average, [[bank_of_england|Bank of England]]) and **SOFR** (Secured Overnight Financing Rate, Federal Reserve). See [Yield Curves and Benchmarks](../market_risk/02-yield_curves_benchmarks.md) for further detail.

### Currency Swaps

A currency swap exchanges principal and/or interest payments denominated in different currencies at agreed exchange rates. Example: £100m swapped for $135m in 2 years at an implied rate of 1.35, regardless of how the spot rate moves over the period.

Interest payments on currency swaps can be structured as fixed-fixed, floating-floating, or fixed-floating in each currency. Banks use currency swaps both to manage their own FX and interest rate mismatches and to offer customers hedging solutions.

### Derivative Costs of Manufacture

The total price of a derivative includes the theoretical Black-Scholes price plus **costs of manufacture**:
- **Collateral costs** — cash or securities posted to counterparties under CSA arrangements (see [Behavioural Modelling](../liquidity_risk/01_introduction/03-behavioural_modelling.md))
- **Capital for credit risk and CVA risk** — holding regulatory capital against the risk of counterparty deterioration (not just default)
- **For options:** costs of borrowing cash to buy the underlying, or borrowing the underlying to sell short
- **Delta and vega hedging rebalancing costs** — dealing costs and locked-in losses from convex-vs-linear hedging
- **Infrastructure and trading desk costs** — computational power and personnel

Post-2008, [[basel_framework|Basel III]] encouraged moving OTC derivatives onto exchanges or central counterparties (CCPs) to reduce systemic risk from open bilateral positions — highlighted by the 2008 Lehman Brothers failure.

## When Black-Scholes Assumptions Break Down

### Fat Tails (Non-Lognormal Returns)

The lognormal distribution describes typical daily price movements well, but dramatically underestimates the probability of large moves. Actual returns have **very fat tails**. One illustration: the S&P 500's average annual return between 1978 and 2007 was 9.5%, but excluding the worst 50 days increased it to 18.2%, while excluding the best 50 days reduced it to 0.6%. The Black-Scholes formula ignores this tail asymmetry, causing it to systematically underprice out-of-the-money options.

### Stochastic Volatility and the Volatility Smile

If the Black-Scholes assumptions held exactly, **implied volatility** (back-solved from observed option prices) would be flat across all strike prices. In reality, a plot of implied volatility vs. strike price forms a **volatility smile** — higher implied volatility at both out-of-the-money and in-the-money strikes. After the October 1987 crash, the smile became a **volatility skew**: implied volatility is higher for out-of-the-money put options (downside protection demand) than for out-of-the-money calls. This reflects:

- Market demand asymmetry (more buyers of downside protection than sellers)
- Heightened awareness of crash risk and the non-lognormality of returns
- The fact that volatility is itself stochastic — rising when prices fall (fear) and falling when prices rise (complacency)

Volatility that clusters (periods of high vol followed by high vol; low vol by low vol) is modelled using **GARCH** (General Autoregressive Conditional Heteroscedasticity) models.

### Negative Feedback Mechanisms — LTCM and the Forced Seller Problem

Hedge funds amplify Black-Scholes-based strategies through leverage: they identify mispriced assets, set up delta-hedged portfolios, and earn small risk-adjusted returns — then leverage these positions to make them meaningful. This works while markets are rational. When a highly-leveraged fund suffers losses, it may face margin calls that force it to unwind positions at losses:

**Long-Term [[04-capital_management|Capital Management]] (LTCM), August 1998:** Founded by Black-Scholes Nobel laureates, LTCM bet that spreads between safe assets (US Treasuries) and riskier assets (corporate bonds, emerging market debt) would narrow. Russia's government default triggered a massive flight to safety — the opposite of LTCM's position. LTCM was forced to unwind at massive losses. As one forced seller became multiple forced sellers, spreads widened further, triggering more losses in a self-reinforcing cycle.

The key insight: **Keynes's dictum applies directly** — "The market can remain irrational longer than you can remain solvent." Derivatives-based strategies that appear risk-free under lognormal assumptions can produce catastrophic losses when markets behave irrationally and when too many funds have made similar leveraged bets. The 2007–2008 crisis repeated this dynamic at scale: when one fund became a forced seller, the strategy that had attracted many imitators simultaneously unwound, creating the "deleveraging of historical proportions" described by hedge fund manager Cliff Asness.
