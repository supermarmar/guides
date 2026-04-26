# ECL, Regulatory EL & Basel IRB Capital

## 2. The Three Loss Estimates Distinguished

This is the most commonly confused area. Three different loss estimates exist, each serving a different master.

| | **ECL (IFRS 9)** | **Regulatory EL (Basel)** | **ELBE (Basel — Defaulted Only)** |
|---|---|---|---|
| **Framework** | Accounting | Prudential | Prudential |
| **Standard** | IFRS 9 | Basel III / CRR | Basel III / CRR Art. 181 |
| **Calibration** | Point-in-time, scenario-weighted | Through-the-cycle PD, Downturn LGD | Current best estimate, loan-specific |
| **Discounting** | Yes — at original EIR | No | No (or different basis) |
| **Cyclicality** | High — moves with macro | Low — deliberately stable | Moderate — current conditions, not averaged |
| **Scope** | All stages (1, 2, 3) | All exposures | Defaulted exposures only |
| **Purpose** | Financial reporting | EL shortfall/excess vs provisions | EL input and capital floor for defaulted loans |

### ECL (IFRS 9)

- Probability-weighted across multiple economic scenarios (upside, base, downside)
- Discounts expected future cash flows at the original effective interest rate
- Responsive to current macroeconomic forecasts
- Stage 3 (defaulted): 12-month ECL = lifetime ECL (default already occurred)

### Regulatory EL (Basel IRB)
**Non-defaulted:** `EL = PD_TTC × LGD_downturn × EAD`

Uses through-the-cycle (TTC) PDs and downturn LGDs — deliberately conservative and counter-cyclical to prevent pro-cyclical capital behaviour.

**Defaulted:** `EL = ELBE × EAD`

For defaulted assets, PD collapses to 100% and the TTC LGD becomes too blunt (it's a generic average across all defaults). ELBE replaces the PD × LGD component with a loan-specific current best estimate.

### Why You Cannot Simply Use LGD_downturn in the Defaulted EL Formula
If you used downturn LGD in regulatory EL for defaulted assets, you would compare a **stressed** loss rate against **expected** ECL provisions. This would systematically overstate the EL shortfall and unfairly penalise banks' capital positions. ELBE provides the correct expected-loss anchor for the comparison.

### Why You Cannot Simply Substitute ECL LGD for ELBE
| Problem | Explanation |
|---|---|
| **Pro-cyclicality** | ECL LGDs move with economic scenarios. Low in good times → large capital gap. High in crisis → compressed gap. Exactly what Basel tries to prevent. |
| **Discounting mismatch** | IFRS 9 ECL discounts cash flows at the original EIR. ELBE is undiscounted. Subtracting them would be mathematically inconsistent. |
| **Governance** | ECL methodology varies widely across banks. ELBE must meet specific regulatory standards (CRR Art. 181), making it more comparable across institutions. |

---

## 3. ELBE — Expected Loss Best Estimate

### What It Is
ELBE is a **regulatory, point-in-time, loan-specific estimate of the expected loss rate on an already-defaulted exposure**, expressed as a percentage of EAD (like LGD).

### Where It Sits on the Spectrum

```
TTC/LRA LGD          ELBE              ECL LGD (IFRS 9)
  (generic,        (specific,           (specific,
cycle-averaged)   point-in-time,       point-in-time,
                  regulatory           scenario-weighted,
                  standards)           discounted)
←— more conservative/stable ————————— more responsive/volatile —→
```

ELBE is **not** the TTC/LRA LGD. The TTC LGD is calibrated as an average across thousands of defaults across economic cycles and does not reflect the specific recovery situation of an individual loan. Once a loan defaults, you have granular information — ELBE consumes it.

### Core Structure

A defaulted loan has two possible outcomes:

> `ELBE = P(cure) × LGD_if_cure + P(no cure) × LGD_if_no_cure`

Where:
- **P(cure)** = probability the borrower recovers and resumes payments
- **LGD_if_cure** ≈ 0 (minimal loss if borrower rehabilitates)
- **LGD_if_no_cure** = expected loss rate through workout/enforcement

### Key Segmentation Drivers

| Driver | Why It Matters |
|---|---|
| **Time in default** | Cure probability declines sharply as time in default increases |
| **Collateral type & current valuation** | Property, financial collateral, receivables carry different recovery dynamics |
| **Stage of recovery proceedings** | Pre-litigation vs active enforcement vs receivership have different timelines and recovery rates |
| **Sector and geography** | Distressed real estate vs corporate with diversified assets behave very differently |
| **Costs of recovery** | Legal fees, administration costs, and time-value of delayed recoveries all reduce net recovery |

### Regulatory Requirements (CRR Art. 181)
1. Must reflect **current economic circumstances** — not a long-run average
2. Must be grounded in the bank's **own workout experience** on comparable defaulted exposures
3. Must account for all **recovery costs** (legal, admin, time delays)
4. Must be independently **validated** within the bank and subject to regulatory review
5. Must be broadly **consistent with the ECL provisioning process** — material divergence requires justification

---

## 4. Basel IRB Capital for Defaulted Assets

### Capital Formula

> `K = max(0, LGD_downturn − ELBE) × EAD`
>
> `RWA = K × 12.5`

### The Logic of the Subtraction

Capital and provisions are **two separate loss-absorbing layers**, not interchangeable:

| Layer | What It Absorbs | When It's Used |
|---|---|---|
| **Provisions (ECL/ELBE)** | Expected losses | First line — already charged through P&L |
| **Capital** | Unexpected losses | Second line — absorbs stress beyond expected |

ELBE represents the expected loss **already earmarked through provisioning**. Capital only needs to cover the gap between expected loss (ELBE) and stressed loss (LGD_downturn). Holding capital against the full downturn LGD would double-count the protection already in provisions.

### Numerical Example

| | Rate | Amount (EAD = 1,000) |
|---|---|---|
| ELBE | 60% | 600 → already provisioned |
| LGD_downturn | 80% | 800 → stressed scenario loss |
| **Capital Required** | **20%** | **200 → the uncovered stress gap** |

Holding capital against the full 80% would give 600 in provisions + 800 in capital = 1,400 of protection against an 800 loss. The subtraction prevents this.

### Why EAD Does Not Get a Downturn Adjustment for Defaulted Assets

For non-defaulted assets, EAD is uncertain — borrowers may draw down revolving facilities before default, so downturn Credit Conversion Factors (CCFs) are applied. For defaulted assets, this uncertainty is **resolved** — the default has occurred and the outstanding balance is a known number. You use the actual current EAD. There is no future drawdown risk to stress.

---

## 5. Where Each Input Appears

| Formula            | Non-Defaulted                 | Defaulted                                   |
| ------------------ | ----------------------------- | ------------------------------------------- |
| **Regulatory EL**  | PD_TTC × LGD_downturn × EAD   | ELBE × EAD                                  |
| **Capital (K)**    | IRB formula with LGD_downturn | max(0, LGD_downturn − ELBE) × EAD           |
| **EAD adjustment** | Downturn CCF applied          | Actual outstanding — no downturn adjustment |

---

## 6. The EL Shortfall / Excess Mechanism

Basel requires banks to compare **total regulatory EL** against **total ECL provisions** across the entire portfolio:

| Outcome | Treatment |
|---|---|
| **ECL < Regulatory EL** → EL shortfall | Deducted from CET1 capital |
| **ECL > Regulatory EL** → EL excess | Eligible as Tier 2 capital up to **0.6% of RWAs** |

Because ECL uses point-in-time, scenario-weighted inputs and regulatory EL uses TTC/downturn inputs, these two numbers will almost never be equal. The gap is a live capital management lever — particularly when IFRS 9 provisions are more responsive to macroeconomic deterioration than the conservatively-calibrated regulatory EL.

### Impact of Write-Offs on This Mechanism

A full write-off eliminates:
- The ECL provision on that loan
- The ELBE-based regulatory EL on that loan
- The EAD → collapsing both RWA and capital requirement to zero
- The Tier 2 eligibility from any EL excess on that loan

Both sides of the shortfall/excess comparison reset simultaneously.

---

## 7. Summary Concept Map

```
Defaulted Loan
│
├── ACCOUNTING (IFRS 9)
│   ├── Stage 3 ECL provision → P&L hit when raised, not at write-off
│   ├── Write-off → derecognition, balance sheet neutral
│   └── Post-recovery → P&L income, cash inflow
│
└── REGULATORY (Basel IRB)
    ├── ELBE = current best estimate LGD for this specific defaulted loan
    │         (P(cure) × LGD_cure + P(no cure) × LGD_no_cure)
    │
    ├── Regulatory EL = ELBE × EAD
    │   └── Compared to ECL provision → EL shortfall (CET1 deduction)
    │                                 → EL excess (up to 0.6% RWA as Tier 2)
    │
    └── Capital = max(0, LGD_downturn − ELBE) × EAD
        ├── LGD_downturn → stressed scenario (unexpected loss ceiling)
        ├── ELBE        → expected loss already in provisions (floor)
        └── Gap         → the slice capital must protect
```

---

*These notes were compiled from active recall sessions covering IFRS 9 §5.4.4, Basel III IRB framework, and CRR Article 181.*
