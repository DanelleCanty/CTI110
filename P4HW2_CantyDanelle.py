# Danelle Canty
# 07-03-2026
# P4HW2
# Calculate pay for multiple employees

# Pseudocode:
# 1. Ask user for employee name, hours worked, and pay rate; repeat until name is 'done'
# 2. Check if hours worked is greater than 40
# 3. If yes, calculate overtime hours, overtime pay, regular pay, and gross pay
# 4. If no, set overtime hours and overtime pay to 0, calculate regular pay and gross pay
# 5. Display employee name, hours, rate, overtime hours, overtime pay, regular pay, and gross pay
# 6. Add totals to accumulator variables and display final totals when done

# Request employee info
name = input("Enter employee name or 'done' to finish: ")

# Create accumulator variables for overtime pay, regular pay, gross pay, and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name.lower() != 'done':
    # Add employee count plus one
    employee_count += 1
    # Ask for employee info
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ " 's hourly pay rate? "))



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
    
    # Add to accumulator variables
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay




    # Display results
    print("------------------------------")
    print("Employee Name:", name)
    print()
    print(f'{"Hours Worked":<18}{"Pay Rate":<15}{"Overtime Hrs":<15}{"Overtime Pay":<18}{"Regular Pay":<15}{"Gross Pay":<15}')
    print("-------------------------------------------------------------------------------------------")
    print(f'{hours:<18}{rate:<15}{overtime_hours:<15.2f}{overtime_pay:<18.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}')

    name = input("Enter employee name or 'done' to finish: ")

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total,',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total,',.2f'))
print("Total amount paid in gross: $", format(grosspay_total,',.2f'))

