#a program to calculate production of milk and display the result
Number_of_cows = int(input("Enter number of cows: "))
Milk_production_per_cow = float(input("Enter milk production per cow (in liters): "))
cost_of_milk_per_liter = float(input("Enter cost of milk per liter: "))

#calculating total amount of milk production
total_amount_of_milk_production_per_day = Number_of_cows * Milk_production_per_cow

#calculating total cost of milk production per day
total_cost_of_milk_production_per_day = Number_of_cows * Milk_production_per_cow * cost_of_milk_per_liter

#displaying the result
print("Number of Cows: ", Number_of_cows)
print("Milk Production per Cow: ", Milk_production_per_cow, " liters")
print("Total Milk Production per Day: ", total_amount_of_milk_production_per_day, " liters")
print("Total Cost of Milk Production per Day: ", total_cost_of_milk_production_per_day, " ksh")
