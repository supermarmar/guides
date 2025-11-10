import pandera.pandas as pa
import pandas as pd
from typing import Optional
from pandera.typing import Series

from src.const import PRIMARY_KEY


# Define schema for credit card balance data
class CreditCardBalanceSchema(pa.DataFrameModel):
    """
    Schema for credit_card_balance data validation
    Focus on transactional data quality
    """

    SK_ID_PREV: Series[int] = pa.Field(ge=1, description="Previous loan identifier")
    SK_ID_CURR: Series[int] = pa.Field(
        ge=1, description="Current application identifier (foreign key)"
    )
    MONTHS_BALANCE: Series[int] = pa.Field(
        le=0,
        description="Month of balance relative to application date",
    )
    AMT_BALANCE: Optional[Series[float]] = pa.Field(
        nullable=True, description="Balance amount"
    )
    AMT_CREDIT_LIMIT_ACTUAL: Optional[Series[float]] = pa.Field(
        ge=0, nullable=True, description="Credit limit"
    )
    AMT_DRAWINGS_ATM_CURRENT: Optional[Series[float]] = pa.Field(
        nullable=True, description="ATM drawings for current period"
    )
    AMT_DRAWINGS_CURRENT: Optional[Series[float]] = pa.Field(
        nullable=True, description="Total drawings for current period"
    )
    AMT_DRAWINGS_POS_CURRENT: Optional[Series[float]] = pa.Field(
        nullable=True, description="POS drawings for current period"
    )
    AMT_DRAWINGS_OTHER_CURRENT: Optional[Series[float]] = pa.Field(
        nullable=True, description="Other drawings for current period"
    )
    AMT_PAYMENT_CURRENT: Optional[Series[float]] = pa.Field(
        ge=0, nullable=True, description="Payment amount for current period"
    )
    AMT_PAYMENT_TOTAL_CURRENT: Optional[Series[float]] = pa.Field(
        ge=0, nullable=True, description="Total payment amount for current period"
    )
    AMT_RECIVABLE: Optional[Series[float]] = pa.Field(
        nullable=True, description="Amount receivable on the previous credit"
    )
    AMT_RECEIVABLE_PRINCIPAL: Optional[Series[float]] = pa.Field(
        nullable=True,
        description="Amount receivable for principal on the previous credit",
    )
    AMT_TOTAL_RECEIVABLE: Optional[Series[float]] = pa.Field(
        nullable=True,
        description="Amount receivable for principal on the previous credit",
    )
    AMT_INST_MIN_REGULARITY: Optional[Series[float]] = pa.Field(
        ge=0, nullable=True, description="Minimum regular installment amount"
    )
    CNT_DRAWINGS_ATM_CURRENT: Optional[Series[int]] = pa.Field(
        ge=0,
        le=100,
        nullable=True,  # Reasonable limit on number of ATM transactions
        description="Number of ATM drawings",
    )
    CNT_DRAWINGS_CURRENT: Optional[Series[int]] = pa.Field(
        ge=0,
        le=1000,
        nullable=True,  # Reasonable limit on total transactions
        description="Number of drawings current",
    )
    CNT_DRAWINGS_POS_CURRENT: Optional[Series[int]] = pa.Field(
        ge=0, le=500, nullable=True, description="Number of POS drawings"
    )
    CNT_DRAWINGS_OTHER_CURRENT: Optional[Series[int]] = pa.Field(
        ge=0, le=500, nullable=True, description="Number of other drawings"
    )
    CNT_INSTALMENT_MATURE_CUM: Optional[Series[int]] = pa.Field(
        ge=0,
        le=500,
        nullable=True,
        description="Number of paid installments on the previous credit",
    )
    SK_DPD: Optional[Series[int]] = pa.Field(
        ge=0, nullable=True, description="Days past due"
    )
    SK_DPD_DEF: Optional[Series[int]] = pa.Field(
        ge=0, nullable=True, description="Days past due with tolerance"
    )
    NAME_CONTRACT_STATUS: Optional[Series[str]] = pa.Field(
        nullable=True,
        description="Contract status (active signed,...) on the previous credit",
    )

    class Config:
        name = "CreditCardBalanceSchema"
        strict = True  # No additional columns allowed
        coerce = True

    @pa.dataframe_check
    def validate_primary_key_uniqueness(cls, df: pd.DataFrame) -> bool:
        """Check if combination of SK_ID_PREV, SK_ID_CURR, MONTHS_BALANCE is unique"""
        return df[PRIMARY_KEY].duplicated().sum() == 0

    # @pa.dataframe_check
    # def validate_balance_credit_limit(cls, df: pd.DataFrame) -> bool:
    #     """Balance should not exceed credit limit"""
    #     valid_data = df[
    #         df["AMT_BALANCE"].notna() & df["AMT_CREDIT_LIMIT_ACTUAL"].notna()
    #     ]
    #     if valid_data.empty:
    #         return True
    #     return (
    #         valid_data["AMT_BALANCE"] <= valid_data["AMT_CREDIT_LIMIT_ACTUAL"] * 1.1
    #     ).all()  # Allow 10% tolerance

    # @pa.dataframe_check
    # def validate_drawings_consistency(cls, df: pd.DataFrame) -> bool:
    #     """Total drawings should be sum of ATM and POS drawings"""
    #     valid_data = df[
    #         df["AMT_DRAWINGS_CURRENT"].notna()
    #         & df["AMT_DRAWINGS_ATM_CURRENT"].notna()
    #         & df["AMT_DRAWINGS_POS_CURRENT"].notna()
    #     ]
    #     if valid_data.empty:
    #         return True
    #     calculated_total = (
    #         valid_data["AMT_DRAWINGS_ATM_CURRENT"]
    #         + valid_data["AMT_DRAWINGS_POS_CURRENT"]
    #     )
    #     # Allow small tolerance for rounding differences
    #     return abs(valid_data["AMT_DRAWINGS_CURRENT"] - calculated_total).max() < 1.0


# # Define Home Credit specific data quality schemas
# class ApplicationDataSchema(pa.DataFrameModel):
#     """
#     Schema for application_train/application_test data validation
#     Implements BCBS 239 data quality requirements
#     """

#     SK_ID_CURR: Series[int] = pa.Field(
#         ge=1, unique=True, description="Unique application identifier - primary key"
#     )
#     TARGET: Optional[Series[int]] = pa.Field(
#         isin=[0, 1],
#         nullable=True,
#         description="Target variable (1 = default, 0 = no default)",
#     )
#     NAME_CONTRACT_TYPE: Series[str] = pa.Field(
#         isin=["Cash loans", "Revolving loans"], description="Contract type"
#     )
#     CODE_GENDER: Series[str] = pa.Field(
#         isin=["F", "M"], description="Gender of the client"
#     )
#     FLAG_OWN_CAR: Series[str] = pa.Field(
#         isin=["Y", "N"], description="Flag if client owns a car"
#     )
#     FLAG_OWN_REALTY: Series[str] = pa.Field(
#         isin=["Y", "N"], description="Flag if client owns real estate"
#     )
#     CNT_CHILDREN: Series[int] = pa.Field(
#         ge=0,
#         le=20,  # Reasonable range for number of children
#         description="Number of children",
#     )
#     AMT_INCOME_TOTAL: Series[float] = pa.Field(
#         gt=0,
#         le=1e9,  # Income should be positive and reasonable
#         description="Total income of the client",
#     )
#     AMT_CREDIT: Series[float] = pa.Field(
#         gt=0,
#         le=1e9,  # Credit amount should be positive
#         description="Credit amount of the loan",
#     )
#     AMT_ANNUITY: Optional[Series[float]] = pa.Field(
#         gt=0, nullable=True, description="Loan annuity"
#     )
#     DAYS_BIRTH: Series[int] = pa.Field(
#         le=-6570,
#         ge=-25550,  # Age between 18-70 years (negative days)
#         description="Client's age in days (negative)",
#     )
#     DAYS_EMPLOYED: Series[int] = pa.Field(
#         le=0,  # Should be negative or 0 (unemployed)
#         description="Days employed (negative or 0)",
#     )

#     class Config:
#         name = "ApplicationDataSchema"
#         strict = False  # Allow additional columns for now
#         coerce = True

#     @pa.check("AMT_CREDIT")
#     def validate_credit_amount_precision(cls, series: pd.Series) -> bool:
#         """Credit amounts should be reasonable precision (e.g., multiples of 100)"""
#         return ((series % 100) == 0).sum() / len(
#             series
#         ) > 0.8  # 80% should be round hundreds

#     @pa.dataframe_check
#     def validate_income_credit_ratio(cls, df: pd.DataFrame) -> bool:
#         """Income to credit ratio should be reasonable (credit not > 10x income)"""
#         return (df["AMT_CREDIT"] <= df["AMT_INCOME_TOTAL"] * 10).all()

#     @pa.dataframe_check
#     def validate_age_employment_consistency(cls, df: pd.DataFrame) -> bool:
#         """Employment days should not exceed age (accounting for negative values)"""
#         age_days = abs(df["DAYS_BIRTH"])
#         employment_days = abs(df["DAYS_EMPLOYED"])
#         # Handle unemployed (365243 is special value for unemployed)
#         valid_employed = employment_days < 365243
#         return (employment_days[valid_employed] <= age_days[valid_employed]).all()
