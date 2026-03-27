# Data Sourcing & Collection

## Internal

These sources provide information on the bank's own portfolio and operations. Robust data quality assessments, controls and governance processes are essential to ensure data quality.

1. **Month-End Financial Data**: This forms the foundation of most models. It includes:

    - Delinquency Data: Days past due (DPD), number of days delinquent, and delinquency status (e.g., 30-day delinquent, 90-day delinquent). This is crucial for estimating Probability of Default (PD).
    - Balances: Outstanding loan balances, credit card balances, and other relevant financial exposures. This is used to calculate Exposure at Default (EAD).
    - Limits: Credit limits, exposure limits, and other relevant risk limits applied to borrowers. This is used in EAD calculations and for [[02-stress_testing|stress testing]].

2. **Transactional Data**: Individual transaction details, including payment amounts, dates, and types of transactions. This provides insights into borrower behaviour and can be used to refine PD and EAD estimations.
3. **Collection Data**: Details on collection efforts, including contact attempts, recovery amounts, and write-off information. This is crucial for refining PD and Loss Given Default (LGD) estimations.

## External

These sources provide information from outside the bank, offering a broader perspective on borrower risk. Careful consideration of data quality, licensing, and privacy regulations is essential.

1. **Application Data**: Information provided by customers during the loan application process. This includes income, employment history, assets, liabilities, and other financial information. This is used to assess creditworthiness and estimate PD.
2. **Credit Bureau Data**: Information from credit bureaus, including credit scores, credit history, payment behaviour, and other relevant credit information (inquiries). This is a critical input for PD estimation and can help to validate internal data.
3. **[[04-ratings_agencies|Ratings Agencies]]**: The simplest and most widely used source throughout the world is rating agency ratings – primarily when using the SA under [[bis|Basel]].
