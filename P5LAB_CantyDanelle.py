# Danelle Canty
# July 15, 2026
# P5LAB
# Calculating money part 2

import random


def disperse_change(change):
    # Displays the number of dollars and coins needed for the change.

    # Convert the change amount to cents
    change = round(change * 100)

    # Determine how many dollars and coins are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    # Display only the dollars and coins that are needed
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")


def main():
    # Generate a random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${amount_owed:.2f}")

    # Ask the customer how much cash they are entering
    cash = float(input("How much cash will you put in the self-checkout? $"))

    # Continue asking if the customer did not enter enough cash
    while cash < amount_owed:
        print("That is not enough cash.")
        cash = float(input("How much cash will you put in the self-checkout? $"))

    # Calculate and display the change
    change_owed = round(cash - amount_owed, 2)

    print(f"Change is: ${change_owed:.2f}")
    print()

    # Pass the change amount to the function
    disperse_change(change_owed)


main()