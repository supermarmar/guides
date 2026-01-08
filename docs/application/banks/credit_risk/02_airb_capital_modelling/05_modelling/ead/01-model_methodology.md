
# **Model Methodology – EAD**

## **Rating Philosophy**

* The model follows a **Point-in-Time (PiT)** rating philosophy.
* PiT EAD estimates are designed to be **sensitive to the economic cycle** and provide an accurate forecast of exposure usage over a **12-month horizon**.
* This approach is consistent with IFRS9, where **PiT EADs** are required to calculate expected credit losses (ECL).
* In addition, in accordance with **CRR Articles 182.1(a) and 182.1(b)**, the following measures are calculated and maintained:

  * **PiT EADF** (Exposure at Default Factor)
  * **Long-Run Average (LRA) EADF**
  * **Downturn (DT) EASF**
  * **Regulatory EADF** (incorporating MoC)

---

## **End-to-End Design**

The model is structured to estimate **EAD** at the account level as:

[
EAD = EADF \times \text{Limit at Observation}
]

Where:

* **EADF** = expected credit conversion factor at the time of default.
* **Limit at Observation** = committed credit line (e.g., credit card limit) at T=0.

The estimation framework mirrors the PD approach:

1. **PiT EADF** is estimated directly from observed data.
2. **LRA EADF** is calibrated using historical averages over the defined long-run period.
3. **DT EADF** is calculated per grade over the downturn period.
4. **Regulatory EADF** is derived by applying **Margin of Conservatism (MoC)** to the LRA and DT estimates.

---

## **Downturn EADF**

* In line with regulatory guidance, a **Downturn EADF (DT EADF)** is calculated to reflect stressed conditions.
* Methodology:

  * The downturn period is defined as **2008M01 to 2008M12**, aligning with the global financial crisis.
  * For each **risk grade**, the **average observed EADF** during this downturn period is computed.
  * This provides a stressed calibration that can be compared against both PiT and LRA levels.

---

## **Margin of Conservatism (MoC)**

* Consistent with the PD methodology, **MoC adjustments** are applied to both **LRA EADF** and **DT EADF** to account for model limitations, data uncertainty, and sampling biases.
* Separate MoCs are calculated per grade and aggregated at the portfolio level.
* The final **Regulatory EADF** is defined as:

[
\text{Regulatory EADF} = \max \big( \text{LRA EADF} + MoC_{LRA}, ; \text{DT EADF} + MoC_{DT} \big)
]
