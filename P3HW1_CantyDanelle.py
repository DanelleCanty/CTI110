# Danelle Canty
# June 26, 2026
# P3HW1
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


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / len(grades)

print()
print("----------Results----------")
print(f"{'Lowest Grade:':<18}{low:.1f}")
print(f"{'Highest Grade:':<18}{high:.1f}")
print(f"{'Sum of Grades:':<18}{total:.1f}")
print(f"{'Average:':<18}{avg:.2f}")
print("---------------------------")

# determine letter grade for average
if avg >= 90:
 print('Your grade is: A')
else:
 if avg >= 80:
  print('Your grade is: B')
 else:
  if avg >= 70:
   print('Your grade is: C')
  else:
   if avg >= 60:
    print('Your grade is: D')
   else:
    print('Your grade is: F')






