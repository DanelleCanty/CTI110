# Danelle Canty
# June 13, 2026
# P1HW2
# Calculate and display travel expenses

# Pseudocode

print("Calculate and display travel expenses")
print()

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining = budget - total_expenses

print()
print("-------Travel Expenses-------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining)

