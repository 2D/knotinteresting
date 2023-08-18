def future_value_of_investment(principal, rate, years):
    return principal * (1 + rate)**years

def future_value_of_annuity(payment, rate, years):
    return payment * (((1 + rate)**years - 1) / rate)

def main():
    # Constants
    INITIAL_INVESTMENT = 100000
    ANNUITY_PAYMENT = 20000
    TARGET = 10000000
    YEARS = 10
    
    scenarios = {
        "5% Return (Conservative)": 0.05,
        "10% Return (Moderate)": 0.10,
        "20% Return (Aggressive)": 0.20
    }
    
    for name, rate in scenarios.items():
        fv_initial = future_value_of_investment(INITIAL_INVESTMENT, rate, YEARS)
        fv_annuity = future_value_of_annuity(ANNUITY_PAYMENT, rate, YEARS)
        
        total_fv = fv_initial + fv_annuity
        amount_needed = TARGET - total_fv
        
        print(f"{name}:")
        print(f"Future Value of Initial Investment: €{fv_initial:,.2f}")
        print(f"Future Value of Annuity: €{fv_annuity:,.2f}")
        print(f"Total Future Value: €{total_fv:,.2f}")
        print(f"Additional Amount Needed to Reach €10 Million: €{amount_needed:,.2f}\n")

if __name__ == "__main__":
    main()
