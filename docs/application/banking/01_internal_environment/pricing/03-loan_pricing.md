# Loan Pricing

This file covers the pricing of bank loan products by product type (retail, corporate, investment bank), including key credit risk drivers, structural risks, and the challenge of managing fixed-rate loan margins through interest rate cycles. For the DCF modelling framework used to derive loan prices see [DCF Model](04-dcf_model.md). For general pricing principles see [Pricing Framework](01-pricing_framework.md).

## Retail Loan Products

### Personal Loans (Unsecured Term Loans)

Personal loans are offered without any security; recoverability depends entirely on the borrower's income. In the event of default (e.g. due to unemployment), the **loss given default (LGD) is typically 70% or higher**. Typical product characteristics: small principal (c. £1,000–£15,000 in the UK), terms of 3–7 years, with risk-based pricing applied to reflect individual borrower risk. In South Africa, maximum interest rates are regulated by the NCA (e.g. repo rate + 21% for unsecured credit). In the UK, at least 51% of loans issued must be at the marketed headline rate even if risk-based pricing is used.

### Mortgages (Residential and Buy-to-Let)

A mortgage is secured on real property, allowing the bank to repossess and sell the property on default. The key risk driver is the **loan-to-value (LTV) ratio**:

```math
\text{LTV} = \frac{\text{Loan outstanding}}{\text{Market value of property}}
```

The loss given default on a mortgage is directly proportional to LTV: at 95% LTV, a property price fall of more than 5% (net of repossession costs) produces a loss. At 70% LTV, prices would have to fall by over 30% to produce a loss. LTV is therefore the primary variable in mortgage pricing models. Higher LTV bands attract both higher pricing and higher capital requirements.

**Fixed vs variable rate mortgages — the margin management problem:** When banks fund long-term fixed-rate mortgages with short-term variable-rate deposits, rising interest rates compress NIM. Additionally, fixed-rate mortgages embed an asymmetric option: if rates fall, borrowers prepay (reducing the bank's fixed-rate asset duration); if rates rise, borrowers stay (extending duration at a below-market rate). UK banks resolve this through **deal periods** (fixed rates applying for 2 or 5 years) that revert to the bank's **standard variable rate (SVR)**. SVR is a bank-controlled rate that can be reset with adequate notice, creating a repricing point that restores margin management capability. See the S&L crisis example below.

**US S&L crisis:** US regulations historically required banks to offer 15-year fixed-rate mortgages. During the 1970s–1980s, rising inflation and short-term rates caused savings and loan (S&L) institutions to pay escalating deposit rates while earning fixed low rates on their mortgage books — creating negative margins. Approximately one-third of US S&Ls failed. US banks now securitise mortgages (selling to Freddie Mac, Fannie Mae, or ABS investors) to transfer this duration and margin risk off-balance-sheet.

### Vehicle and Asset Finance

Secured on the underlying asset (vehicle, machinery, boat, etc.). On default, the bank repossesses and sells the asset. Loan risk depends on the age and marketability of the asset, the loan tenor, the initial deposit paid, and the residual value (if applicable). Factors specific to the contract type (hire purchase vs PCP) affect risk profile. **Personal contract purchase (PCP)** loans are structured as leases with balloon payments: the residual value of the car at end of term settles the remaining loan balance, exposing the lender to **residual value risk** if the car is worth less than expected.

### Credit Cards (Revolving Credit)

Unsecured revolving credit up to a customer-set limit. High LGD on default (comparable to personal loans). Key additional risks:

- **Credit utilisation risk:** Most cardholders borrow well below their limit in normal times. In recession, newly unemployed borrowers may rapidly "max out" their card before defaulting, causing a sharp spike in defaulted balances. Banks must hold capital against unutilised limits (at a lower rate than utilised balances) as well as drawn balances.
- **Revolving structure:** Because the limit can be drawn, repaid, and redrawn repeatedly, prepayment and drawdown assumptions are more complex than for term loans. Default and early settlement curves must account for the revolving pattern.

### Leasing

Under a lease, the bank funds purchase of an asset that reverts to the lender at lease expiry. Monthly payments for the borrower are lower than hire purchase (which includes full repayment of principal) because they cover only usage, not ownership. For business customers, lease payments may be tax-deductible. The residual value of the asset at lease end remains the bank's risk, as does the credit quality of the lessee.

## Corporate Loan Pricing

Corporate loans are individually structured to the borrower's needs. They may be fixed or variable rate, domestic or foreign currency, secured or unsecured, with repayment structures tailored to the corporate's cash flow profile. Pricing reflects the **borrowing hierarchy** within the group (parent vs subsidiary guarantees).

Credit assessment uses borrower-specific financial statement analysis rather than consumer bureau scorecard data. Factors affecting price include the financial strength of the borrower, the nature and extent of security, the ranking of debt in default (senior secured vs subordinated), and the overall value of the banking relationship (payment services, hedging income, advisory fees).

Loans above certain thresholds require credit committee and board approval. Banks must monitor and manage **concentration risk** — excessive exposure to a single name, industry sector, or country — to avoid portfolio losses correlated with a single adverse event.

**Covenants:** Corporate loan agreements typically include financial covenants (e.g. requiring EBITDA to remain above 125% of annual debt service). Covenant breaches trigger the bank's right to demand repayment or renegotiate terms, providing earlier intervention than simply waiting for default.

**Specialised corporate products** include large-ticket leasing (trains, aircraft, ships), and trade finance (import/export credit facilities, letters of credit, documentary collections).

## Investment Bank Loans

Investment banks generally prefer not to lend from their own balance sheet, instead intermediating between issuers and capital markets. However, investment banks **underwrite bond and equity issues** — committing to purchase any unsold portion — which creates temporary credit risk if an issue is not successfully placed with investors. This underwriting risk is priced into the fees and underwriting spread.

## Managing NIM Over the Rate Cycle

The ability to reprice products as interest rates change is a critical design feature. Key considerations:

- **Variable-rate lending** (overdrafts, credit cards, corporate floating-rate loans linked to repo/LIBOR/JIBAR) can be repriced rapidly when base rates change, protecting NIM.
- **Fixed-rate personal loans** — shorter behavioural lives and higher spreads mean NIM exposure to rate changes is limited.
- **Fixed-rate mortgages** — the most problematic: the asymmetric prepayment option combined with long maturities creates substantial NIM and duration risk if not managed through deal periods and SVR reversion.
- **Negative rate environments** — in some EU countries, Switzerland, and Japan, policy rates turned negative. Banks compressed lending rates (as intended by policy) but were reluctant to impose negative rates on retail deposits, squeezing NIM from both sides.

Banks must price and design loan products with the full repricing cycle in mind, not just at origination — a lesson emphasised by the S&L crisis and more recently by the post-2020 rate normalisation cycle.
