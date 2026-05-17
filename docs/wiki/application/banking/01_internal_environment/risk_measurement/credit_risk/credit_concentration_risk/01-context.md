---
tags:
  - application/banking/internal-environment/risk-management/pillar-2-modelling/economic-capital
  - difficulty/unknown
  - study-status/new
aliases:
---
# Economic Capital (Banking Book)

Economic capital is internally calculated by the bank and is a measure of the bank's total risk as they see it, without reference to regulatory prescriptions. It is calculated as part of the Internal Capital Adequacy Assessment Process (ICAAP) and represents the amount of capital a bank believes it needs based on its own [[02-risk_appetite|risk appetite]] and strategy.

For the broader treatment of the [[01-pillar_2b|Pillar 2]] capital framework (Pillar 2A/2B add-ons, buffers, capital requirements table), see [Capital — Pillar 2](../../../03-capital_management.md). This file focuses on the **computation mechanics of economic capital** used in the ICAAP, including Pillar 2A risk-specific quantification and [[01-pillar_2b|Pillar 2B]] stress capital.

While Pillar 1 regulatory capital is a rule-prescribed floor, economic capital is the bank's own best estimate of required capital. The two measures differ in several important dimensions:

| Dimension            | Regulatory Capital (Pillar 1)                                                | Economic Capital (ICAAP)                                       |
| -------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Confidence level** | 99.9% (1-in-1000 year loss)                                                  | Typically 99.95%–99.97% (1-in-2000 to 1-in-3333 year loss)     |
| **Diversification**  | Not recognised (ASRF assumes infinite granularity and no sector correlation) | Recognised via portfolio simulation or correlation assumptions |
| **Formula**          | Prescribed (ASRF / Vasicek)                                                  | Bank-defined (internal models)                                 |

## Pillar 2A

Pillar 2A captures risks not fully covered by Pillar 1. The bank must quantify its own capital requirement for each material risk type. 
### Credit Risk

The IRB model operates under Basel constraints: PD floors (0.03% for retail), supervisory LGD floors, fixed correlation formulae. This means the EC model is a more honest reflection of _current_ risk, whereas IRB capital has a degree of conservatism baked in by regulation.

Economic capital for credit risk is conceptually computed using the same Vasicek/ASRF framework as the IRB formula — a portfolio loss distribution is modelled and capital is set at VaR minus EL:
$$\text{EC}_{\text{credit}} = \text{VaR}_{q} - \text{EL}$$
where $q$ is the bank's internal confidence level (e.g., 99.95%).

Key differences from the IRB regulatory capital formula (see [Regulatory Capital](../a-irb_capital/01_introduction/01-context.md)):

- **PIT PDs**: Economic capital typically uses PIT PDs which are higher in downturns and lower in expansions, rather than the TTC PDs used in regulatory capital.
- **Higher confidence level**: The bank's own target confidence level $q$ reflects its target credit rating and [[02-risk_appetite|risk appetite]]. A bank targeting an AA rating (implied default probability ~0.03%) would use approximately $q = 99.97\%$.
- **Multi-factor models**: Unlike the single-factor ASRF, internal EC models may use multi-factor approaches (sector-specific systematic factors) to better capture concentration and diversification.
- **Diversification benefit**: Portfolio EC < sum of individual-obligor ECs. The difference — the diversification benefit — is recognised in EC but not in Pillar 1.

Your A-IRB and IFRS 9 modelling work sits directly at the input layer of this whole process. The PDs, LGDs, and EADs you model flow into the EC model, which flows into the ICAAP credit capital number, which the PA reviews in the SREP to set the P2R. The regulatory capital framework and the internal economic capital framework are two different lenses on the same underlying risk — the ICAAP is the mechanism by which the bank reconciles the two and explains the gap to the supervisor.

### Credit Concentration Risk

The internal EC model produces a higher capital number than IRB Pillar 1 for most real portfolios, primarily because it captures what IRB ignores:

- **Single-name concentration** — large exposures to individual obligors. The granularity assumption in Basel breaks down completely when you have a few dominant counterparties.
- **Sector / industry concentration** — correlated default risk within a sector (e.g., property, mining). IRB uses a fixed asset correlation; your internal model can use empirically estimated sector correlations.
- **Geographic concentration** — systemic risk tied to a single economy or region.

The difference between internal EC and Pillar 1 IRB capital becomes the **credit concentration Pillar 2A add-on** in the ICAAP. The regulator looks at this gap and uses it to set the P2R.

Pillar 1 (via the ASRF model) assumes an infinitely granular, perfectly diversified portfolio — i.e., no single borrower or sector adds disproportionate risk. In practice, portfolios are concentrated. Pillar 2A requires an explicit capital add-on to compensate for this.