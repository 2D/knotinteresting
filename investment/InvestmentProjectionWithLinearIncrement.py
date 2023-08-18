def total_value(initial, rate, years, start_addition, increment):
    """Calculate the total value of the investment after a given number of years."""
    total = initial
    for year in range(years):
        # Add the annual addition which increases linearly every year
        total += start_addition + year * increment
        # Compound the total with the annual rate
        total *= 1 + rate
    return total

def find_increment_to_reach_target(initial, rate, years, target, start_addition):
    """Determine the required annual increment to reach a target amount in a given number of years."""
    increment = 0
    while total_value(initial, rate, years, start_addition, increment) < target:
        increment += 1000  # Increase by 1000 each iteration for demonstration purposes
    return increment

def print_annual_additions_for_rate(rate):
    """Print the annual additions for each year given a specific rate."""
    required_increment = find_increment_to_reach_target(initial_amount, rate, years, target_amount, start_annual_addition)
    
    print(f"\nFor an annual return rate of {rate*100}%, the annual investment additions are:")
    for year in range(1, years + 1):
        current_addition = start_annual_addition + (year - 1) * required_increment
        print(f"Year {year}: €{current_addition}")

# Set the investment parameters
initial_amount = 100000         # Initial investment
start_annual_addition = 20000   # Starting annual addition
years = 10                      # Investment period
target_amount = 10000000        # Desired final amount

# Display the annual additions for each rate
for rate in [0.05, 0.10, 0.20]:
    print_annual_additions_for_rate(rate)
