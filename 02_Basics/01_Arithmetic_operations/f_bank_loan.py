'''
    Simple Interest Calculation
'''

def simple_interest(principal, rate, time):
    simple_interest= principal * rate * time
    return simple_interest



# Input values
#principal
principal = float(input("Enter the principal amount: "))
#annual rate of interest
annual_rate = float(input("Enter the annual interest rate (in %): ")) / 100
#time period
time = float(input("Enter the time period (in years): "))

# Calculating simple Interest
simple_interest = simple_interest(principal, annual_rate, time)


# Displaying simple interest
print("\nInterest Details:")
print("Simple Interest: ", simple_interest )

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
