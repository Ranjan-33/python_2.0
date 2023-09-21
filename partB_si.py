# Input principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the annual rate of interest (as a decimal): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate_of_interest * time_period)

# Display the simple interest
print(f"Simple Interest: {simple_interest}")
