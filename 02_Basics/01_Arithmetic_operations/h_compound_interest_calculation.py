'''
Compound Interest Calculation

'''

def compound_interest(principal, rate, time, n=1):
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return interest


# Input values
#principal amount
principal = float(input("Enter the principal amount: "))
#annual rate in percentage
annual_rate = float(input("Enter the annual interest rate (in %): ")) / 100
#time in years
time = float(input("Enter the time period (in years): "))

# Calculations
compound_interest = compound_interest(principal, annual_rate, time)

# Display results
print("\nInterest Details:")
print("Compound Interest: ", compound_interest)
