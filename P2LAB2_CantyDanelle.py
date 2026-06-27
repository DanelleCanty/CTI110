
#Danelle Canty
#June 18, 2026
#P2Lab2
#Using dictionaries

Cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}
keys = Cars.keys()
print(keys)

print()

#Get a car from user
car_name = input("Enter a car: ")

#Get mpg for the given car
car_mpg = Cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon. ")

#Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#Calculate 
gallons_needed = miles_driven/car_mpg 

#Display results
print(f"{gallons_needed:.2f} galllon(s) of gas are needed to drive the {car_name} {miles_driven} miles. ")

