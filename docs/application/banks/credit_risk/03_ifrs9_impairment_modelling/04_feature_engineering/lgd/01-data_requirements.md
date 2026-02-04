
# Data Requirements

## Loss Given Default (LGD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)||Same as IRB but the intention is to estimate a best estimate or forward looking LGD to reflect impact of future economic scenarios| |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|Same set of risk drivers as IRB + forecasts of future economic conditions|  |
|Collection Cost||Considers only costs directly attributable to the collection of recoveries|  |
|Discount rate||Depends on the type of instrument but is broadly based on EIR|  |
|Measurement Period|$[t'_0,t'_n]$|No requirement about historical data of either observations or collection| |

## Account & Recovery Data (Post-default)

The dataset for modeling PWGD should track the state of accounts post-default over time. This includes transitions between different states, such as in collections, write-off, and cure.

- Account ID: Unique identifier for each account.
- Snapshot Date: Date tracking status of the account.
- Default Flag: Identifies if the account is in default.
- Cure Flag: Identifies if the account has cured.
- Write-Off Flag: Identifies if the account has been written off.
- Default Date: Date when the account first entered default.
- Write-Off Date (if applicable): The date the account was written off.
- Current State:
    - In Collections: Actively managed by the recovery team.
    - Cured (Complete): Returned to performing status.
    - Write-Off (Complete): Deemed unrecoverable and written off.
- Balance: Outstanding balance during the collections process.
- Recovery Amounts: Cash recoveries (e.g., partial payments made during collections).
- Exposure at Default (EAD): Initial exposure at the time of default.
- Collection Actions: Actions taken during collections (e.g., restructuring, legal steps).
- Time in Collections: Duration spent in the collections process before cure or write-off.
- Time in Cure: Duration spent in cure
