# Danelle Canty
# June 20, 2026
# P2HW2
# Display student's test grades

print()

# Pseudocode:
# Create an empty list to store grades
# Ask user to enter grade for each of the 6 modules
# Add each grade to the list
# Find the lowest grade using min()
# Find the highest grade using max()
# Calculate the sum of all grades using sum()
# Calculate the average by dividing sum by number of grades
# Display the results formatted in a table

grades = []

grade1 = float(input("Enter grade for Module 1: "))
grades.append(grade1)

grade2 = float(input("Enter grade for Module 2: "))
grades.append(grade2)

grade3 = float(input("Enter grade for Module 3: "))
grades.append(grade3)

grade4 = float(input("Enter grade for Module 4: "))
grades.append(grade4)

grade5 = float(input("Enter grade for Module 5: "))
grades.append(grade5)

grade6 = float(input("Enter grade for Module 6: "))
grades.append(grade6)

print()

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = sum(grades) / len(grades)

print()
print("----------Results----------")
print(f"{'Lowest Grade:':<18}{lowest:.1f}")
print(f"{'Highest Grade:':<18}{highest:.1f}")
print(f"{'Sum of Grades:':<18}{total:.1f}")
print(f"{'Average:':<18}{average:.2f}")
print("---------------------------")
