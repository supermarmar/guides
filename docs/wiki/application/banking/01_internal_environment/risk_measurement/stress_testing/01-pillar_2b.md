---
tags:
  - application/banking/internal-environment/risk-management/pillar-2-modelling/stress-testing
  - difficulty/unknown
  - study-status/new
aliases:
---
# Pillar 2B

Pillar 2B is the forward-looking component of Pillar 2 capital, determined through stress testing rather than point-in-time assessment. Each jurisdiction may require additional buffers over and above [[bis|Basel]] requirements so as to ensure that banks within the system are adequately capitalized and there is a reduced systemic risk.

## Stress Testing Mechanics

The purpose of Pillar 2B stress testing is to quantify the capital required for the bank to remain above its Pillar 1 + Pillar 2A requirements throughout an adverse macroeconomic scenario. The capital planning buffer (CPB) is the peak shortfall observed over the stress horizon:

$$\text{CPB} = \max_{t \in [0,T]}\left(\text{Pillar 1} + \text{Pillar 2A} - \text{CET1}(t)\right)$$

where $\text{CET1}(t)$ is the CET1 ratio at time $t$ under the stress scenario, modelled as:

$$\text{CET1}(t) = \text{CET1}(0) + \sum_{s=1}^{t} \left[\text{Revenue}(s) - \text{Impairments}(s) - \text{Dividends}(s)\right] - \Delta\text{RWA}(s)$$

The key drivers modelled in a stress scenario are:

- **Impairment charges**: PD migrations and LGD increases driven by macroeconomic shocks (GDP decline, unemployment rise, property price falls). PD and LGD models feed forward-looking ECL calculations ([[ifrs9_standard|IFRS 9]] Stage 2/3 flows), which directly reduce retained earnings.
- **Revenue compression**: [[04-nii_nim|Net interest margin]] compression from lower rates or higher funding costs; non-interest income falls from lower business activity.
- **RWA inflation**: Portfolio downgrades shift borrowers to higher risk weight buckets; models may also produce higher RWAs under stressed PDs (for banks using non-modelled overlays).
- **Dividend and payout policy**: Most banks would suspend or reduce dividends in a stress scenario.

## Scenario Design

Stress scenarios are designed to be "severe but plausible". Supervisors (e.g., [[pra|PRA]] in the UK, PA in South Africa) may prescribe baseline stress assumptions, but banks must also design their own scenarios relevant to their specific risk profile. Standard scenario types include:

- **Macroeconomic downside**: GDP contraction, unemployment spike, property price decline, interest rate shock.
- **Idiosyncratic stress**: A scenario specific to the bank (e.g., a major operational failure, a reputational event, or a concentrated sector loss).
- **Reverse stress test**: Instead of asking "what happens to capital if X occurs?", the reverse stress test asks "what scenario would cause the [[01-business_model|business model]] to fail?" and then assesses its plausibility.

The Pillar 2B add-on is generally not disclosed publicly and is bank-specific. In South Africa, the Pillar 2B requirement (referred to as the Individual Capital Requirement (ICR)) combines both the stress-driven capital and any ad-hoc risks identified by the PA that are not captured in Pillar 2A.
