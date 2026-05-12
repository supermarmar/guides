---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/airb-capital/testing-results/pd/risk-differentiation
  - difficulty/unknown
  - study-status/new
aliases:
---
Got it — thanks for sharing the table and notes. I’ll now prepare a polished **Differentiation Testing Results** section that ties together the regulatory context, the table of tests, and the detailed analyses you described.

---

## **Differentiation Testing Results**

Differentiation testing assesses whether the PiT PD model provides reliable, stable, and discriminatory performance across multiple samples and conditions. The following dimensions of testing were performed, with the associated tests and sample sets summarised in **Table 11-1**.

| **Test Dimension**         | **Test Performed**                                                | **Sample Tested**     |
| -------------------------- | ----------------------------------------------------------------- | --------------------- |
| **Accuracy**               | Mean Percentage Error (MPE)                                       | OOS, OOT              |
| **Discrimination**         | Gini                                                              | OOS, OOT              |
| **Stability**              | Population Stability Index (PSI)                                  | OOT, Application      |
|                            | Characteristics Stability Index (CSI)                             | OOT, Application      |
|                            | Sensitivity of model parameters to data samples                   | OOS                   |
| **Robustness**             | Seasonality                                                       | All historical data   |
|                            | Partner resilience                                                | OOS, OOT              |
| **Stress Analysis**        | Sensitivity of input data – single factor                         | Application           |
|                            | Sensitivity of input data – multi-factor                          | Application           |
| **Benchmarking**           | Gini based on FICO score                                          | OOS, OOT              |
| **Alternative Approaches** | Accuracy and discrimination of PiT model with dynamic calibration | Development, OOS, OOT |

*Table 11-1: Summary of Tests Performed on [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/05_modelling/pd/03-risk-differentiation|Risk Differentiation]]*

---

### **Accuracy**

* Accuracy was assessed by comparing **actual default rates** to **predicted PiT PDs** across **development (DEV), out-of-sample (OOS), and out-of-time (OOT)** samples.
* Results were presented at **overall, segment, and sub-population levels**.
* Key diagnostics:

  * **Tables**: percentage error by sample and segment.
  * **Scatter plots**: actual vs predicted PDs.
  * **Line plots**: actual vs predicted defaults over time, showing stability of fit.

---

### **Discrimination**

* Measured using **Gini coefficients**, capturing the model’s ability to rank-order risk.
* Assessed at **overall, segment, and sub-population levels**.
* Key diagnostics:

  * **Tables**: Gini per segment and per sample, with comparisons across DEV, OOS, OOT.
  * **Lorenz curves**: for each sample to illustrate rank-ordering strength.
  * **Line plots**: Gini over time to confirm discriminatory power is stable.
* Findings: composite Gini values remained around **80%**, with no material degradation across samples.

---

### **Stability**

* Assessed whether the model remains valid across different populations.
* **PSI (Population Stability Index):** calculated between development and OOT/application data.

  * PSI > 0.25 indicates significant population shift.
  * At overall level, PSI was calculated for each **segment model** and for each **risk driver** individually.
* **CSI (Characteristics Stability Index):** used to track stability of risk drivers across samples.
* Results confirmed population and driver stability remained **within thresholds**, supporting transferability.

---

### **Robustness**

* **Sensitivity of Parameters:** model was re-fitted on OOS sample to check whether:

  * Coefficient **signs remained unchanged**, and
  * P-values were consistently **<0.01**, indicating robust statistical significance.
* **Seasonality:**

  * Equal number of snapshots were drawn from each quarter of the DEV sample (e.g., three from March, June, September, December).
  * This ensured no hidden seasonal bias.
  * **Unobserved Components Models (UCMs)** were also applied to further confirm absence of seasonal distortions.

---

### **Stress Analysis**

* Conducted to test model sensitivity to stressed input conditions.
* **Single-factor stresses:** raw risk drivers were shocked up and down by **±10% and ±20%** individually.
* **Multi-factor stresses:** all drivers stressed simultaneously by ±10% and ±20%.
* Results showed:

  * Some segments were more sensitive than others.
  * For **higher-risk segments**, **utilisation** was the most influential driver.
  * Stresses could lead to **population shifts** and increases in PiT PDs, highlighting areas of vulnerability.

---

### **Benchmarking**

* The model’s discriminatory power was benchmarked against the **FICO score** (an external rating commonly used in US consumer credit).
* Comparison of Gini values showed the PiT PD model performed at least as strongly, confirming competitive performance against an established benchmark.

---

### **Alternative Approaches**

* A dynamic calibration framework was tested to validate whether accuracy and discrimination improved under alternative assumptions.
* Results remained consistent across **DEV, OOS, and OOT** samples, reinforcing the robustness of the chosen calibration method.

---

✅ This structured write-up brings together the **tests, methodology, and findings** in a way that reads like a regulatory submission or model documentation.

Would you like me to also **create schematic visuals** (e.g., sample Lorenz curve, PSI bar chart, actual vs predicted line plot) so that this section can be presented more visually in a report or appendix?
