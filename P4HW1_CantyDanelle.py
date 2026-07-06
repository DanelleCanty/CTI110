# Danelle Canty
# 07-03-2026
# P4HW1
# Display student's scores

print()

# Pseudocode:
# 1.Ask user how many scores they want to enter
# 2.Create an empty list to store scores
# 3.Use a loop to collect each score
# 4.Check each score to make sure it is between 0 and 100
# 5.If score is invalid, keep asking until a valid score is entered
# 6.Add each valid score to the list
# 7.Find the lowest score
# 8.Create a modified list by removing the lowest score
# 9.Calculate the average of the modified list
# 10.Determine the letter grade
# 11.Display the results

score_list = []

num_scores = int(input("How many scores do you want to enter? "))

count = 1
while count <= num_scores:
    score = float(input(f"Enter score #{count}: "))

    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{count} again: "))

    score_list.append(score)
    count += 1

print()

lowest_score = min(score_list)

modified_list = score_list.copy()
modified_list.remove(lowest_score)

average = sum(modified_list) / len(modified_list)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print()
print("------------Results------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {modified_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("-------------------------------")