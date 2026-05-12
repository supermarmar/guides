# Sector Concentration

The IRB formula uses a single global asset correlation $\rho_m$ — the same for all corporate obligors regardless of which industry they sit in. It models every obligor as driven by one common systematic factor, with the rest being idiosyncratic risk that diversifies away.

This misses something important. Two real estate companies share not just the global economic factor but also a **sector-specific factor** — property prices, rental yields, construction costs. Two mining companies share commodity prices. In a sector stress, all obligors in that sector move together _above and beyond_ what the global factor predicts. If 40% of your portfolio is real estate, you cannot escape that sector factor no matter how many real estate names you hold.

Single-name concentration asks: _are individual exposures too large?_  
Sector concentration asks: _are exposures too clustered in sectors with high intra-sector correlation?_

Sector concentration arises when exposures are clustered in a single industry or geography, making the portfolio susceptible to sector-specific downturns. The standard model for sector concentration uses the **multi-factor extension** of the Vasicek model, replacing the single systematic factor with sector-specific factors:

$$X_i = \sqrt{\rho_s} \cdot S_{\text{sector}(i)} + \sqrt{\rho - \rho_s} \cdot S_{\text{market}} + \sqrt{1-\rho} \cdot Z_i$$
Where

$$
\rho=\rho_s+\rho_m
$$

where $\rho_s$ is the intra-sector asset correlation, $S_{\text{sector}}$ is the sector-specific systematic factor, and $S_{\text{market}}$ is the common market factor. The capital add-on captures the additional tail risk from high intra-sector correlations when a single sector is stressed. 

The capital add-on is calculated by re-running the IRB formula using the total intra-sector correlation $\rho=\rho_s+\rho_m$ for each sector, and taking the difference from the Pillar 1 baseline.
## Example

**Portfolio:** Total EAD = R2,000m across three sectors

| Sector          | EAD (Rm) | Weight | PD   | LGD | $\rho_m$ (IRB) | $\rho_s$ | $\rho$ |
| --------------- | -------- | ------ | ---- | --- | -------------- | -------- | ------ |
| Real Estate     | 800      | 40%    | 2.0% | 45% | 15%            | 10%      | 25%    |
| Retail/Consumer | 700      | 35%    | 1.5% | 40% | 15%            | 3%       | 18%    |
| Mining          | 500      | 25%    | 1.0% | 50% | 15%            | 7%       | 22%    |

The sector-specific loadings Δρ reflect the additional co-movement within each sector due to property prices, consumer spending, and commodity prices respectively. These are calibrated from historical default correlations or regulatory guidance — not assumed.

Total Pillar 1 IRB capital = R117.8m (using $\rho_m$ = 15% for all)

Now re-run the same formula using the total intra-sector $\rho$ correlation for each sector.

|Sector|IRB Capital|Sector Capital|Add-on (Rm)|% Uplift|
|---|---|---|---|---|
|Real Estate|R56.2m|R92.9m|**R36.7m**|65%|
|Retail/Consumer|R36.5m|R44.0m|**R7.5m**|21%|
|Mining|R25.1m|R37.6m|**R12.5m**|50%|
|**Total**|**R117.8m**|**R174.5m**|**R56.7m**|**48%**|

**Total sector concentration add-on = R56.7m, a 48% uplift on Pillar 1.**

The add-on pattern is instructive. Real Estate generates 65% of total Pillar 1 capital but accounts for **65% of the entire sector add-on**. This is driven by two compounding factors:

It has the largest weight (40%), which enters the capital formula directly through portfolio EAD. But more importantly, it has the largest Δρ (10 percentage points above the global IRB correlation). In the IRB formula, correlation determines how much of the 99.9th percentile tail is driven by the systematic factor — moving ρ from 15% to 25% is not a linear change, it substantially fattens the tail. In this example the real estate capital density almost doubles (7.02% → 11.61%) because the sector factor brings correlated extreme outcomes much closer to the capital threshold.

Retail, by contrast, has a meaningful exposure weight but only a 3 percentage point sector excess. The tail barely moves — hence only a 21% uplift.

## Calibrating the Sector Correlations

The $\rho_s$ values are the model's most judgement-sensitive input. Banks calibrate them using:

- **Historical default correlation data** — estimating pairwise asset correlations from equity return series (Merton-style) for obligors within each sector across full credit cycles, then decomposing into global and sector components
- **Rating agency transition data** — sector-level cohort default rates over time
- **Regulatory guidance** — the Basel Committee's empirical studies on corporate asset correlations (which underpin the IRB correlation formula) provide sector-level estimates; some regulators publish indicative $\rho_s$  ranges for ICAAP purposes
- **Stress-implied correlations** — backing out the implied correlation from the worst historical sector stress event (South African property in the early 1990s, mining sector in 2015–16)

The calibration is a Pillar 2 judgement call, and regulators will challenge it in the SREP — particularly if the bank has chosen low $\rho_s$  values for sectors where it has large concentrated exposures.