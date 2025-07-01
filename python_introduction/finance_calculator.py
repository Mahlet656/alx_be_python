# Prompt the user for their monthly financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project the annual savings with 5% interest
# Formula: (Monthly Savings * 12) + (Interest on annual savings)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results to the user
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
