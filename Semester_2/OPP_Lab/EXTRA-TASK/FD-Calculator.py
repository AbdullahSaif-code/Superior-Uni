def calculate_amount(principle, interest_rate, tenure):
# Perform the calculation
    maturity_amount = principle + (principle * interest_rate * tenure) / 100
    
# Return the result
    return round(maturity_amount, 2)

principle = float(input("Enter the principle amount: "))
interest_rate = float(input("Enter the interest rate: "))
tenure = float(input("Enter the tenure in years: "))

result = calculate_amount(principle, interest_rate, tenure)
print(f"Maturity Amount: {result}")
