# Danelle Canty
# June 19, 2026
# P2HW1
# Calculate and display travel expenses 2

# Pseudocode

print("Calculate and display travel expenses")
print()

budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining = budget - total_expenses

print()
print("----------Travel Expenses----------")
print(f"{'Location:':<20s}{destination}")
print(f"{'Initial Budget:':<20s}${budget:.2f}")
print(f"{'Fuel:':<20s}${gas:.2f}")
print(f"{'Accommodation:':<20s}${accommodation:.2f}")
print(f"{'Food:':<20s}${food:.2f}")
print("------------------------------------")
print()
print(f"{'Remaining Balance:':<20s}${remaining:.2f}")
