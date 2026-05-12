# Economic Capital

Economic capital is the amount of capital a bank estimates it needs to remain solvent over a one-year horizon at a confidence level linked to its **target credit rating**, covering **all material risks**, using the bank's own models and **current (PIT) inputs**, and recognizing **portfolio diversification** across risk types.

The key words in that definition:

- **Target credit rating** — this is what determines the confidence level. A bank targeting an A rating (implied 1-year PD ~0.1%) uses 99.9%; one targeting AA (implied PD ~0.03%) uses 99.97%. The confidence level is a _strategic choice_, not a regulatory prescription.
- **All material risks** — not just the Pillar 1 trio. EC covers IRRBB, concentration, pension, business risk, model risk, and anything else the bank deems material.
- **PIT inputs** — EC is a _current_ view of risk, not a through-cycle average. It answers "how much capital do we need today?" rather than "how much do we need on average across a cycle?"
- **Diversification** — EC recognises that credit losses, market losses, and operational losses do not all peak simultaneously. P1 ignores this; EC does not.

## Link to Pillar 1

Pillar 1 sets the **minimum regulatory floor**, covering three prescribed risk types:

- **Credit risk** — default losses on loans and exposures
- **Market risk** — losses from trading book positions (rates, FX, equities)
- **Operational risk** — losses from failed processes, systems, or external events

| Risk Type          | RWA       | Capital @ 8% |
| ------------------ | --------- | ------------ |
| Credit risk        | R10bn     | R800m        |
| Market risk        | R2bn      | R160m        |
| Operational risk   | R1bn      | R80m         |
| **Total Pillar 1** | **R13bn** | **R1,040m**  |

This is the regulatory minimum. It is necessary but **not sufficient** — it deliberately excludes several material risks.

Economic capital is the bank's **own internal estimate** of the capital it needs to cover _all_ material risks at a chosen confidence level (typically 99.9%). It is a management tool, not a regulatory requirement, but it drives the ICAAP submission.

| Additional Risk                 | EC Estimate |
| ------------------------------- | ----------- |
| Credit risk                     | R900m       |
| Market risk                     | R200m       |
| Operational risk                | R80m        |
| IRRBB                           | R200m       |
| Credit concentration risk       | R150m       |
| Pension risk                    | R50m        |
| Business / strategic risk       | R100m       |

So economic capital ≈ **R1,680m** — materially above the R1,040m Pillar 1 floor. This gap is not an accident; it represents genuine risk the bank carries that Basel's prescribed formulae were not designed to capture.

The 99.95% confidence level is not arbitrary — it reflects the bank's **target credit rating**. A bank targeting an AA rating implies a 1-year survival probability of roughly 99.97%; an A rating implies ~99.9%. This is higher than Basel's prescribed 99.9%, which means the bank is modelling a more extreme tail.

### Credit Risk

The Pillar 1 IRB formula is hardcoded to 99.9% — the Vasicek quantile G(0.999) is baked into the capital formula. For EC at 99.95%, the bank substitutes G(0.9995) instead, producing a higher conditional PD and therefore higher capital per exposure.

Beyond just the confidence level, EC credit risk models typically also differ in:

- Using **point-in-time PDs** rather than TTC PDs, since EC is a forward-looking management tool rather than a through-cycle regulatory floor.
- Using **full portfolio simulation** (Monte Carlo) rather than the analytical ASRF formula, which allows the bank to model actual name concentrations and sector correlations rather than assuming a single systematic factor.
- Capturing **diversification within the credit portfolio** — something the portfolio-invariant ASRF formula explicitly ignores.

### Market Risk

Under FRTB, regulatory market risk uses 97.5% ES over liquidity-adjusted horizons ranging from 10 to 250 days. For EC, the bank recalculates using its chosen confidence level (99.95%) and typically a **1-year time horizon** to match the EC framework's common horizon. This usually produces a materially larger capital figure than the regulatory number, particularly for illiquid positions where the 1-year horizon captures far more potential loss.

### Operational Risk

Regulatory op risk under the SMA is formula-driven and does not use an explicit VaR confidence level. For EC, banks often use a **Loss Distribution Approach** — fitting severity and frequency distributions to internal and external loss data — and then read off the 99.95th percentile loss directly. This gives a more tailored estimate than the regulatory formula, though it is highly sensitive to tail assumptions.

### Cross-Risk Diversification

This is where EC diverges most fundamentally from regulatory capital. Pillar 1 simply **adds** credit RWA + market RWA + op risk RWA with no recognition that these risk types are imperfectly correlated. In a recession, credit losses spike — but market risk losses may partially offset gains elsewhere, or operational losses may not peak simultaneously.

EC frameworks model the **correlation structure across risk types** and apply a diversification benefit. In practice this can reduce total EC by 10–25% relative to a simple sum of the parts, depending on the bank's business mix. This diversification benefit is one reason EC can sometimes sit _below_ regulatory capital even at a higher confidence level, for well-diversified universal banks.

|Risk|Regulatory Capital Basis|EC Basis (99.95%)|
|---|---|---|
|Credit|99.9% ASRF, TTC PD, downturn LGD|99.95% Monte Carlo, PIT PD, full correlation|
|Market|97.5% ES, liquidity-adjusted horizon|99.95% VaR/ES, 1-year horizon|
|Op Risk|SMA formula|99.95% LDA|
|IRRBB|Not in P1|EVE sensitivity at 99.95% shock|
|**Diversification**|**None**|**Correlation benefit applied**|

The EC number that emerges is the bank's own best estimate of its true capital need — more granular, more forward-looking, and more portfolio-specific than Pillar 1, but also less conservative in its treatment of cross-risk offsets.

## Link to P2A

Pillar 2A is the **regulator's formalisation of that gap**. After reviewing the ICAAP, the supervisor agrees the additional risks are material and sets binding add-ons:

| Risk                 | P2A Add-On |
| -------------------- | ---------- |
| IRRBB                | R200m      |
| Credit concentration | R150m      |
| Pension risk         | R50m       |
| **Total P2A**        | **R200m**  |

Note: the supervisor may not simply rubber-stamp the bank's own EC estimates — they will challenge assumptions, apply their own benchmarks, and may set a different number. But the _source_ of P2A is the economic capital analysis.

**At this point: P1 + P2A = R1,040m + R400m = R1,440m**, which corresponds closely to the bank's own economic capital view of R1,680m (the difference being business risk, which regulators may not require explicit capital for but the bank models internally).

## Link to P2B

P2A captures risks at a _going-concern, baseline_ level. P2B asks a different question: **"If a severe stress materialises, how much extra capital does BankBSM need to absorb losses and still remain above its P1+P2A floor?"**

BankBSM runs a severe recession scenario: unemployment rises to 12%, property values fall 30%, interest rates spike 200bp. Under this scenario:

- Credit losses on retail mortgages surge (PDs rise from TTC levels to stressed point-in-time levels)
- IRRBB losses hit as the EVE of the banking book falls
- Wholesale exposures suffer rating migrations and defaults

The stressed capital position falls R300m below the P1+P2A minimum. Therefore: **P2B = R300m**.

Economic capital (R1,540m) sits roughly between P1+P2A and P1+P2A+P2B — it represents the bank's own view of _going-concern_ capital need, while the full stack including P2B represents the _stress-resilient_ position the regulator requires.