# Data Requirements

## Probability of Default (PD)

- Typically, to calibrate your PDs the dataset has monthly loan performance (e.g. 20-year mortgage loan) observations for each loan 𝑖 = 1, ..., 𝑁.
- Each loan 𝑖 is therefore observed over discrete time $𝑡 = 1, ..., T_𝑖$ from the time of its first month-end observation up to the end of its lifetime $T_𝑖$.
- These loans are sampled between two dates, during which time new mortgages were continuously originated.
- Loans that predate the start of this sampling window, i.e., left-truncated loans, are retained along with their subsequent observations throughout this window.
- It also includes fundamental credit fields such as net cash flows (receipts), expected instalments, arrears balances, month-end balances, variable interest rates, original loan principals, the amount and timing of write-offs and early settlement.

Let $𝐷_{𝑖,𝑡}$ be a Bernoulli random variable that denotes the default status of loan 𝑖 at time 𝑡, i.e., 1 if in state D, and 0 otherwise. In creating a 𝑣-month forward default indicator, we use the worst-ever aggregation type that indicates future default at present time 𝑡 whenever any of the next 𝑣 ≥ 1 statuses $𝐷_{𝑖,𝑡+1}, ..., 𝐷_{𝑖,𝑡+v}$ equals one. The worst-ever 𝑣-month conditional probability of a non-defaulted loan 𝑖 is then:  

$P(\max [𝐷_{𝑖,𝑡+1}, . . . , 𝐷_{𝑖,𝑡+v}] = 1 | 𝐷_{𝑖,𝑡} = 0)$.

Therefore a 12-month conditional default probability will be

$P(𝐷_{𝑖,𝑡+12}] = 1 | 𝐷_{𝑖,𝑡} = 0)$