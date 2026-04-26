---
epoch: 1776237833602
modelKey: "claude-sonnet-4-6|anthropic"
topic: "Delta-Gamma Option Risk Management"



tags:
  - copilot-conversation
---

**user**: Explain the delta-gamma approximation for option portfolio risk, state when gamma becomes critical, and describe how a derivatives desk manages gamma exposure.
[Timestamp: 2026/04/15 08:23:53]

**ai**: 
<think>The user is asking about the delta-gamma approximation for option portfolio risk, when gamma becomes critical, and how a derivatives desk manages gamma exposure. This is a finance/derivatives question that I can answer from my knowledge.</think># Delta-Gamma Approximation for Option Portfolio Risk

---

## 1. The Approximation

Option prices are nonlinear functions of the underlying asset price $S$. A Taylor expansion of the portfolio value $V(S)$ around the current price $S_0$ gives:

$$\Delta V \approx \delta \cdot \Delta S + \frac{1}{2} \gamma \cdot (\Delta S)^2$$

Where:

| Term | Symbol | Meaning |
| --- | --- | --- |
| First-order sensitivity | $\delta$ | Rate of change of $V$ w.r.t. $S$ |
| Second-order sensitivity | $\gamma$ | Rate of change of $\delta$ w.r.t. $S$ |
| Underlying move | $\Delta S$ | Change in asset price |

For a **full portfolio** of $n$ positions with weights $w_i$:

$$\Delta V_{portfolio} \approx \left(\sum_i w_i \delta_i\right) \Delta S + \frac{1}{2}\left(\sum_i w_i \gamma_i\right)(\Delta S)^2$$

The delta term is **linear** in the move; the gamma term introduces **curvature** — this is the correction that delta-only (delta-neutral) hedging misses.

---

## 2. Geometric Intuition

$$V(S) \approx V(S_0) + \delta(S - S_0) + \frac{1}{2}\gamma(S-S_0)^2$$

- **Long gamma** portfolio (net $\gamma > 0$): the $P\&L$ curve is **convex** — you benefit from large moves in *either* direction.
- **Short gamma** portfolio (net $\gamma < 0$): the $P\&L$ curve is **concave** — large moves hurt you symmetrically.

This asymmetry is the core of gamma risk.

---

## 3. When Gamma Becomes Critical

Gamma is **not constant** — it varies significantly with moneyness, time, and volatility.

### 3.1 At-the-Money (ATM) Options

$$\gamma_{ATM} \approx \frac{e^{-d_1^2/2}}{S \sigma \sqrt{2\pi T}}$$

Gamma **peaks at ATM** and decays rapidly as the option moves in- or out-of-the-money:

$$\gamma_{ATM} \uparrow \quad \text{as} \quad T \downarrow$$

### 3.2 Near Expiry — "Gamma Trap"

As $T \to 0$, ATM gamma spikes toward $+\infty$. The delta flips discontinuously around the strike:

- Just above strike: $\delta \approx +1$
- Just below strike: $\delta \approx 0$

This means **delta hedges break down** — a small move in $S$ demands a massive rehedge.

### 3.3 Summary: When Gamma Is Most Dangerous

| Scenario | Why Gamma Is Critical |
| --- | --- |
| Options near expiry (days to go) | Gamma spikes, delta becomes unstable |
| Options ATM | Maximum curvature, hedges drift fastest |
| Large $\Delta S$ moves (gap risk) | $({\Delta S})^2$ term dominates |
| High short-gamma inventory | P&L concavity amplifies losses |
| Low realized vol vs implied vol | Short gamma bleeds slowly, then crashes |

---

## 4. Managing Gamma Exposure on a Derivatives Desk

### 4.1 Delta-Gamma Neutral Hedging

A pure delta hedge sets:

$$\sum_i w_i \delta_i = 0$$

But to also neutralize gamma, the desk adds an **option hedge** (since delta-only instruments like futures have $\gamma = 0$):

$$\sum_i w_i \gamma_i = 0$$

This requires solving a **two-instrument system** simultaneously — one option to zero gamma, then a linear instrument to re-zero delta.

---

### 4.2 The Gamma P&L Identity

The desk's realized gamma P&L over a rehedging interval is approximately:

$$P\&L_\gamma \approx \frac{1}{2}\gamma \left[(\Delta S)^2 - \sigma_{imp}^2 S^2 \Delta t\right]$$

This is the **realized vs. implied variance** trade:
- If realized vol $>$ implied vol → **long gamma** profits
- If realized vol $<$ implied vol → **short gamma** profits

This is the foundation of **volatility trading**.

---

### 4.3 Practical Desk Tools

**Gamma bucketing** — gamma is reported by expiry and strike:

$$\Gamma_{bucket}(K_i, T_j) = \sum_{options} w \cdot \gamma \cdot \mathbf{1}[strike = K_i, expiry = T_j]$$

This lets the desk see *where* the risk concentrates.

**Key management strategies:**

- **Dynamic delta rehedging** — rehedge at fixed time intervals or when $|\Delta S| > $ threshold; frequency trades off transaction costs vs. hedge slippage
- **Gamma scalping** — intentionally hold long gamma, rehedge frequently to capture realized moves
- **Spread trades** — buy near-dated ATM options, sell far-dated to flatten the gamma term structure
- **Vanna/volga hedging** — extend to third-order Greeks when smile dynamics matter significantly
- **Stress testing** — run $\pm 1\sigma, \pm 2\sigma, \pm 3\sigma$ gap scenarios on the $({\Delta S})^2$ term explicitly

---

### 4.4 Risk Limits

| Limit Type | What It Controls |
| --- | --- |
| Gross gamma limit | Total curvature exposure in dollar terms |
| Gamma concentration limit | Max gamma in a single expiry bucket |
| Overnight gamma limit | Tighter limits during non-trading hours (gap risk) |
| Theta/gamma ratio | Ensures premium decay is fair compensation for gamma risk |

---

## 5. Key Relationship: Gamma and Theta

For a standard BSM option:

$$\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$$

This means **gamma and theta are inextricably linked** — a desk that is long gamma is paying theta (time decay) as the "insurance premium." Managing gamma therefore always involves a **carry vs. convexity** tradeoff.

> **Bottom line:** Delta gets you close; gamma tells you how fast you're drifting away. A well-run derivatives desk monitors gamma by bucket, stress-tests gap moves, and actively trades the spread between realized and implied volatility to monetize or hedge curvature risk.
[Timestamp: 2026/04/15 08:24:28]

**user**: Can you explain this (a) Define the repricing gap and explain how it determines a bank's EVE exposure to a parallel rate shock. (b) A bank has RSA = R500m (average repricing in 2 years) and RSL = R600m (average repricing in 1 year). Estimate the approximate ΔEVE for a +200 bps parallel rate shock, using the duration approximation. (c) What SARB reporting obligations arise if this bank is an IRRBB outlier?
[Timestamp: 2026/04/15 08:29:24]

**ai**: 
<think>The user is asking about Interest Rate Risk in the Banking Book (IRRBB) concepts, specifically about repricing gap, EVE (Economic Value of Equity) exposure, and SARB (South African Reserve Bank) reporting obligations. Let me provide a comprehensive answer.</think># IRRBB: Repricing Gap, EVE Sensitivity & SARB Obligations

---

## Part (a): The Repricing Gap & EVE Exposure

### What Is the Repricing Gap?

The **repricing gap** measures the mismatch between **Rate-Sensitive Assets (RSA)** and **Rate-Sensitive Liabilities (RSL)** within a defined time bucket:

$$\text{Repricing Gap}_t = RSA_t - RSL_t$$

It captures the **timing difference** in when assets vs. liabilities have their cash flows repriced (either because they mature, reset, or are contractually re-struck) within horizon $t$.

---

### How It Determines EVE Exposure

**Economic Value of Equity (EVE)** is the present value of all asset cash flows minus the present value of all liability cash flows:

$$EVE = PV(\text{Assets}) - PV(\text{Liabilities})$$

A rate shock $\Delta r$ changes the present value of every cash flow. The sensitivity of EVE to a rate change is driven by the **duration-weighted gap**:

$$\Delta EVE \approx -\left(D_A \cdot RSA - D_L \cdot RSL\right) \cdot \frac{\Delta r}{1 + r}$$

Where:

| Symbol | Meaning |
| --- | --- |
| $D_A$ | Duration (average repricing) of RSA |
| $D_L$ | Duration (average repricing) of RSL |
| $RSA$ | Rate-sensitive assets |
| $RSL$ | Rate-sensitive liabilities |
| $\Delta r$ | Parallel rate shock |

The **key insight** is:

- A **positive gap** ($RSA > RSL$) → bank is **asset-sensitive** → EVE *falls* when rates rise (long-duration assets lose more value than short-duration liabilities)
- A **negative gap** ($RSA < RSL$) → bank is **liability-sensitive** → EVE *rises* when rates rise (liabilities reprice sooner, losing PV faster than assets)

> The repricing gap thus acts as the **transmission mechanism** between a rate shock and the change in the net present value of the bank's balance sheet.

---

## Part (b): Estimating ΔEVE

### Given Information

| Item | Value |
| --- | --- |
| RSA | R500m |
| Average repricing of RSA ($D_A$) | 2 years |
| RSL | R600m |
| Average repricing of RSL ($D_L$) | 1 year |
| Rate shock ($\Delta r$) | +200 bps = +0.02 |

---

### Duration Approximation Formula

Using the simplified duration approximation (assuming a base rate $r \approx 0$ for the $(1+r)$ denominator, which is standard in regulatory EVE approximations):

$$\Delta EVE \approx -\left(D_A \cdot RSA - D_L \cdot RSL\right) \cdot \Delta r$$

---

### Step-by-Step Calculation

**Step 1: Duration-weighted asset sensitivity**

$$D_A \cdot RSA = 2 \times R500m = R1{,}000m$$

**Step 2: Duration-weighted liability sensitivity**

$$D_L \cdot RSL = 1 \times R600m = R600m$$

**Step 3: Net duration-weighted gap**

$$D_A \cdot RSA - D_L \cdot RSL = R1{,}000m - R600m = R400m$$

**Step 4: Apply the rate shock**

$$\Delta EVE \approx -R400m \times 0.02 = \boxed{-R8m}$$

---

### Interpretation

$$\Delta EVE = -R8\text{m for a } +200\text{ bps shock}$$

- The bank is **net long duration** — assets reprice slower than liabilities
- A rate *rise* reduces EVE because the long-duration assets lose more present value than the shorter-duration liabilities
- The **negative gap in value terms** (R400m exposure) is the source of the loss
- This is a **liability-heavy but duration-long** position — the R600m RSL reprices quickly (less PV loss), while R500m RSA are locked in for 2 years (more PV loss)

---

## Part (c): SARB IRRBB Outlier Reporting Obligations

### The Outlier Test Threshold

Under **SARB's Directive 12/2018** and the **BA 330 return** framework (aligned with Basel IRRBB Standards, April 2016), a bank is classified as an **IRRBB outlier** if:

$$\frac{|\Delta EVE|}{Tier\ 1\ Capital + Tier\ 2\ Capital} > 15\%$$

Or under the **NII (Net Interest Income)** outlier test:

$$\frac{|\Delta NII|}{Tier\ 1\ Capital} > 5\%$$

for any of the **6 prescribed rate shock scenarios**.

---

### The 6 SARB/Basel Prescribed Scenarios

- Parallel up / parallel down
- Short rate up / short rate down
- Steepener shock (short down, long up)
- Flattener shock (short up, long down)

---

### Reporting & Supervisory Obligations

If classified as an outlier, the bank faces the following obligations:

**1. Immediate Notification**
- The bank must **notify SARB promptly** upon identifying outlier status during internal IRRBB measurement
- Notification must be directed to the **Prudential Authority (PA)**, the South African prudential regulator housed within SARB

**2. Enhanced Regulatory Reporting**
- Submission of the **BA 330 return** (IRRBB return) with **increased frequency** or supplementary detail as directed
- Full disclosure of EVE and NII sensitivities across **all 6 shock scenarios** and all material currencies

**3. Internal Capital Adequacy Assessment Process (ICAAP)**
- The outlier finding must be **explicitly addressed in the IRRBB pillar** of the bank's ICAAP
- The bank must demonstrate it holds **adequate Pillar 2 capital** against the identified EVE risk

**4. Remediation Plan**
- Submission of a **written remediation or risk management plan** to the PA explaining:
    - Root cause of the outlier position
    - Hedging strategy or balance sheet restructuring planned
    - Timeline for returning within limits

**5. Possible Supervisory Capital Add-on**
- SARB/PA may impose a **Pillar 2A capital add-on** under Regulation 28 / BA regulations to cover the excess IRRBB exposure until remediated

**6. Enhanced Governance Requirements**
- Board and ALCO must formally acknowledge the outlier status
- Minutes of **ALCO and Board Risk Committee** addressing IRRBB must be made available to the PA on request

---

### Summary Table

| Obligation | Trigger | Regulator |
| --- | --- | --- |
| Outlier notification | $\Delta EVE / Capital > 15\%$ | Prudential Authority (SARB) |
| Enhanced BA 330 reporting | Outlier classification | Prudential Authority (SARB) |
| ICAAP IRRBB capital buffer | Outlier classification | Internal + PA review |
| Remediation plan | Outlier classification | Prudential Authority (SARB) |
| Pillar 2A capital surcharge | PA discretion | Prudential Authority (SARB) |
| Board/ALCO escalation | Outlier classification | Internal governance |

---

> **Key Takeaway:** The repricing gap is the structural source of EVE risk. In this bank's case, the R8m EVE loss on a +200bps shock is modest in absolute terms, but its materiality depends entirely on the bank's capital base — if Tier 1 + Tier 2 capital is below ~R53m, this bank would already be an IRRBB outlier and face the full suite of SARB supervisory obligations.
[Timestamp: 2026/04/15 08:30:03]