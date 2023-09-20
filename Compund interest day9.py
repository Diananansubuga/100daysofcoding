# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.
# Prompt the user to enter the amount deposited into the account
principal = float(input("Enter the amount deposited into the account: "))

# Calculate the amount in the savings account after 1 year
interest_rate = 0.04
amount_1_year = principal * (1 + interest_rate)

# Calculate the amount in the savings account after 2 years
amount_2_years = amount_1_year * (1 + interest_rate)

# Calculate the amount in the savings account after 3 years
amount_3_years = amount_2_years * (1 + interest_rate)

# Display the amounts after each year, rounded to 2 decimal places
print(f"The amount after 1 year is: {round(amount_1_year, 2)}")
print(f"The amount after 2 years is: {round(amount_2_years, 2)}")
print(f"The amount after 3 years is: {round(amount_3_years, 2)}")

