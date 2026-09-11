print("enter number of cows: ")
num_cows = int(input())

print("enter the average milk production per cow (in liters): ")
average_milk = float(input())

print("enter the price of milk per liter(ksh): ")
milk_price = float(input())

total_milk_production_per_day = num_cows * average_milk
total_milk_cost_production_per_day = total_milk_production_per_day * milk_price
print("Total milk production (in liters):", total_milk_production_per_day)
print("Total cost of milk production (in ksh):", total_milk_cost_production_per_day)
