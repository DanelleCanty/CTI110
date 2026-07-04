# Danelle Canty
# June 26, 2026
# P3HW2
# Salary Calculator

# Pseudocode:
# 1. Ask user for employee name, hours worked, and pay rate
# 2. Check if hours worked is greater than 40
# 3. If yes, calculate overtime hours, overtime pay, regular pay, and gross pay
# 4. If no, set overtime hours and overtime pay to 0, calculate regular pay and gross pay
# 5. Display employee name, hours, rate, overtime hours, overtime pay, regular pay, and gross pay

# Request employee info
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: ")) 
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime
if hours > 40: 
    # Calculate overtime
    overtime_hours = hours - 40
    # Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # Calculate salary for regular hours
    regular_pay = 40 * rate
    # Calculate Gross pay
    gross_pay = regular_pay + overtime_pay
else: 
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# Display results
print("----------------------")
print("Employee Name:", name)
print()
print(f'{"Hours Worked":<18}{"Pay Rate":<15}{"Overtime Hrs":<15}{"Overtime Pay":<18}{"Regular Pay":<15}{"Gross Pay":<15}')
print("---------------------------------------------------------------------------------")
print(f'{hours:<18}{rate:<15}{overtime_hours:<15.2f}{overtime_pay:<18.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}')

