## 4. Sampling Strategy

### 4.2 Exposure at Default (EAD)

The sampling methodology for EAD is tailored to reflect accurate utilisation behaviour at the point of default and adheres to both regulatory and technical requirements. This section describes the selection logic for development, calibration, testing, and application samples.

---

### 4.2.1 Source Data and Snapshot Availability

* EAD modelling uses the same **Model-Ready Data (MRD)** as PD, with **monthly snapshots from March 2007 to March 2024**.
* The **most recent performance window** ends in **March 2024**, allowing a full **12-month observation horizon**.
* The EAD target (e.g. EADF) requires both the **account’s limit at observation** and the **realised exposure at default** 12 months later.

---

### 4.2.2 Development Sample (Risk Differentiation)

For model development, a **Point-in-Time (PiT)** approach was used with data drawn from the **2023 portfolio**:

* **12 fixed observation dates**: Each month from **January 2023 to December 2023** was used as a snapshot.
* For each snapshot:

  * All **active accounts** were identified (denoted as set ( x )).
  * From this, a subset of accounts that **defaulted exactly 12 months later** (set ( y )) was selected.
  * For each defaulted account in ( y ):

    * The **default balance in month ( t+12 )** was extracted (used as **EAD**).
    * The **credit limit at month ( t )** was used to calculate **EADF = EAD / Limit**.
  * Each month’s defaulted cohort formed its own segment (e.g., the "Jan23" cohort), ensuring clean fixed-horizon behaviour tracking.
* This results in a **fixed 12-month window approach**, which:

  * Aligns with **Basel III requirements** for EAD modelling (Art. 182(1)(g)),
  * Meets the **CRR representativeness requirement** (Art. 174(c)),
  * Differs from the **cohort-based approach** used for PD where accounts defaulting at *any* point over the horizon are included.
* **Full dataset usage**:

  * Due to the relatively smaller size of defaulted samples, **no downsampling** or random sampling was applied.
  * The entire constructed dataset was used for modelling, and performance metrics were based on account-level observations across all 12 cohorts.

Defining calibration sample.
The calibration sample is composed of 37 quarterly snapshots taken over the LRA period. Unlike PD models, the choices around observation month and overlapping cohorts do not apply for EAD because a 12-month fixed horizon is used. This means that any given default will only appear in one snapshot, avoiding double-counting across periods and ensuring consistency in the calibration data.

---

### 4.2.3 Calibration Sample (Risk Quantification)

* Long-Run Average (LRA) and Downturn (DT) periods were selected from historical data for **EAD calibration**.
* These periods reflect:

  * **Adverse credit conditions**,
  * Observed behavioural shifts in exposure pre-default (e.g., limit increases, utilisation patterns),
  * Required for LRA and downturn adjustment factors applied to the model outputs post-modelling.

---

### 4.2.4 Model Testing Samples

* **Out-of-Sample (OOS) validation**:

  * For model testing during development, a simple **80/20 split** was applied to the development data.
  * 80% of the full sample was used for training and 20% retained for OOS testing.
* **Out-of-Time (OOT) testing**:

  * The snapshot from **March 2024** was reserved as a clean OOT sample.
  * This dataset was not used in development or calibration and provides a **final test of model generalisability** and **performance stability** across time.

---

### 4.2.5 Application Sample (Monitoring and RWA Impact)

* The **application sample** consists of the **most recent snapshots from June 2024 to December 2024**.
* This sample supports:

  * **Stability testing** across current portfolios,
  * **Impact analysis** on capital metrics (e.g. RWA),
  * **Representativeness testing** between the application population and the development sample.

---