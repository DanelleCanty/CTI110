#Danelle Canty
#07-01-2026
#P4Lab2
#Write a program that asks the user to enter an integer using a while loop and a for loop

#Pseudocode
# 1.Get integer from user
# 2.Determine if the integer is positive or negative
# 3.If number is positive, display multiplication table
# 4.If number is negative, tell user program cannot accept it
# 5.Ask user to run again
# 6.If yes, run the program
# 7.If no, end the program

run_again = 'yes'

while run_again != "no" :

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")
    
    run_again = input("Would you like to run the program again? ").lower()

#Loop has broken. User entered 'no'
print("Program is ending....")

