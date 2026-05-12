# Behavioral Scorecards

A behavioural scorecard is a PD/risk-ranking model applied to existing accounts on a recurring (typically monthly, increasingly nightly or real-time) cycle, using account-level performance and transactional data accumulated since origination. The structural differences from application scorecards are deep: behavioural data is internal-dominant rather than bureau-dominant, refresh is dynamic rather than one-shot, the sample is panel rather than cross-sectional, and **discriminatory power is materially higher** — typical behavioural Ginis run 70–85% versus 40–60% for application scorecards, because revealed payment behaviour on the account itself dominates inferential signals from demographics. Each additional month of observed repayment behaviour adds material lift; by month 12, application-score variables are stale or dominated.
## Application to Behaviour

The classical blending pattern interpolates between application and behavioural scores as on-book history accumulates:

| MOB   | Primary score                                               | Rationale                                                           |
| ----- | ----------------------------------------------------------- | ------------------------------------------------------------------- |
| 0–3   | Application only                                            | No internal performance                                             |
| 3–6   | Application primary; emerging-behaviour overlays            | Limited but informative behaviour                                   |
| 6–12  | **Hybrid blend** w(t)·B + (1−w(t))·A, w ramping ~0.3 → ~0.8 | Smooths transition; controls overweighting of noisy early behaviour |
| 12–18 | Behavioural primary; application as backstop                | Behaviour dominates                                                 |
| 18+   | Behavioural only                                            | Application variables fully stale                                   |

## Use Cases

A large retail bank will typically run **four to six distinct behavioural scorecard variants** on the same portfolio simultaneously, each with a different definition of default, outcome window, and rating philosophy. They share the same raw input data but diverge fundamentally in how they're built and what they're used for.
### Account Management and Strategy Decisions

This is the "workhorse" scorecard driving day-to-day decisions:

- automated **credit-line increases** for top deciles and **decreases** triggered by score deterioration; 
- real-time **transaction authorisations** at sub-second latency; 
- cross-sell and retention scoring; 
- **risk-based re-pricing** on revolving products; 
- automatic credit-line renewal that obviates fresh application scoring;

It typically uses a **90 DPD definition**, a **12-month outcome window**, and a **Point-in-Time (PIT) philosophy** because you want it to reflect _current_ risk conditions. Discrimination (Gini/KS) is the primary objective; absolute PD calibration matters less because the output is used ordinally for ranking rather than as an absolute probability.

### IRB PD Risk Grade Segmentation

This is built to satisfy Basel/CRR IRB requirements. The definition of default follows **EBA GL/2016/07 precisely** — 90 DPD _plus_ the unlikeness-to-pay (UTP) triggers (distressed restructuring, write-off, specific credit adjustment, bankruptcy). That UTP component is often missing from pure 90 DPD scorecards, which is why a separate IRB build is needed. 

The outcome window is typically **12 months for retail**. The model is re-calibrated annually to the long-run average default rate and goes through full MRM validation and regulatory sign-off before any change goes live. It feeds directly into RWA and the capital stack.

### IFRS 9 PiT PD Calibration

This requires **Point-in-Time PDs projected forward over the remaining lifetime** of the instrument, conditioned on multiple macro scenarios. The definition of default aligns with IRB (EBA GL/2016/07) for consistency, but the philosophy is the opposite of IRB — you _want_ it to be sensitive to the current economic environment. 

Banks often build this as a **macro-conditional overlay** on top of the TTC IRB PD rather than a fully separate scorecard: take the IRB PD, apply a Z-shift derived from a macro-economic model (GDP growth, unemployment, HPI), and produce a PIT PD per scenario. 

The outcome window is not fixed at 12 months — it stretches to remaining lifetime for Stage 2 accounts, which requires a separate **survival model or marginal PD term structure**. This is typically the most technically complex of the variants.

### SICR Classifier

Some banks build a dedicated model just for the Stage 1 → Stage 2 migration decision, separate from the PD models used to size the ECL. Its target is not "will this account default" but "has credit risk increased significantly since origination." It might use a **relative PD comparison** (current PIT PD vs origination PD), a **score notch downgrade rule**, or a bespoke classifier trained directly on behavioural attributes that precede significant deterioration. The outcome window here is short — often 3–6 months — because you want early warning, not a full-cycle default prediction.

### Collections Scorecard

Once an account is delinquent, the target inverts entirely. The  definition becomes something like **"fails to cure within 90 days"** or **"rolls to charge-off."** The outcome window shortens dramatically — often 3–6 months — because collections decisions are tactical and time-sensitive. The feature space shifts heavily toward post-delinquency signals: broken promise-to-pay, partial payment counts, contact responsiveness, hardship flag. This model typically sits in the Collections system (e.g. Experian Collections Advantage, FICO Debt Manager) rather than the originations/account management engine.

### Recovery Scorecard

At charge-off and beyond, the scorecard predicts **probability of recovery** and shapes placement strategy — in-house workout, first-placement agency, legal action, or debt sale. This is the smallest, most specialist variant, and at smaller banks is often replaced by a vendor model or a simple rules-based placement matrix.
## Sampling

**Panel sampling** (also called longitudinal sampling) tracks the _same accounts over time_, producing multiple observations per account at different points. Think of it like a film rather than a photograph — you see each account's trajectory.

For a behavioural scorecard, a single account might contribute 12 rows to your training dataset — one snapshot per month. Each row captures that account's attributes _as of that month_ (utilisation, payment behaviour, delinquency status, etc.) and its outcome over the following 12 months. So an account opened in January 2021 might generate observations for January, February, March… all the way through December 2021, each with a different feature set.