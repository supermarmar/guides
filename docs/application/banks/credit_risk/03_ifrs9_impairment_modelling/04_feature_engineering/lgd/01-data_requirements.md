# mlAccount & Recovery Data (Post-default)ml

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
