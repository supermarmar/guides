# Data Requirements

## Probability of Default (PD)

|Metadata|Notation|Description|Reference|
|-|-|-|-|
|Dependent Variable (Target)|$D^*_{i,t}(12,p)$|Indicator of defualt in line with IRB (regulatory) DoD. However, depending on the asset the PD measuers either for the next 12 months (Stage 1) or for the remainign life of the financial instrument (Stage 2 and 3).  | |
|Independent Variables (Features)|$I(x_{i},x_{i,t},m_{t'})$|Same set of risk drivers as IRB + forecasts of future economic conditions| |
|Measurement Period|$[t'_0,t'_n]$|No requirement on historical data but current and expectedfuture conditions. | |

- Typically, to calibrate your PDs the dataset has monthly loan performance (e.g. 20-year mortgage loan) observations for each loan 𝑖 = 1, ..., 𝑁.
- Each loan 𝑖 is therefore observed over discrete time $𝑡 = 1, ..., T_𝑖$ from the time of its first month-end observation up to the end of its lifetime $T_𝑖$.
- These loans are sampled between two dates, during which time new mortgages were continuously originated.
- Loans that predate the start of this sampling window, i.e., left-truncated loans, are retained along with their subsequent observations throughout this window.
- It also includes fundamental credit fields such as net cash flows (receipts), expected instalments, arrears balances, month-end balances, variable interest rates, original loan principals, the amount and timing of write-offs and early settlement.

Let $𝐷_{𝑖,𝑡}$ be a Bernoulli random variable that denotes the default status of loan 𝑖 at time 𝑡, i.e., 1 if in state D, and 0 otherwise. In creating a 𝑣-month forward default indicator, we use the worst-ever aggregation type that indicates future default at present time 𝑡 whenever any of the next 𝑣 ≥ 1 statuses $𝐷_{𝑖,𝑡+1}, ..., 𝐷_{𝑖,𝑡+v}$ equals one. The worst-ever 𝑣-month conditional probability of a non-defaulted loan 𝑖 is then:  

$P(\max [𝐷_{𝑖,𝑡+1}, . . . , 𝐷_{𝑖,𝑡+v}] = 1 | 𝐷_{𝑖,𝑡} = 0)$.

Therefore a 12-month conditional default probability will be

$P(𝐷_{𝑖,𝑡+12}] = 1 | 𝐷_{𝑖,𝑡} = 0)$