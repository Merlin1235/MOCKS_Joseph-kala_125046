# program to calculate gross salary tax amount net salary and generates a payslip for an employee

Employee_id = input("Enter employee ID: ")
Employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
deductions = float(input("Enter deductions: "))
Tax_rate = float(input("Enter tax rate: "))

# Calculate tax amount
Tax_amount = (Tax_rate / 100) * basic_salary

# Calculate net salary
Net_salary = basic_salary + allowances - deductions - Tax_amount

# Display the payslip
print("Payslip for Employee")
print("=====================")
print("Employee ID : ", Employee_id)
print("Employee Name : ", Employee_name)
print("Gross Salary : ", basic_salary)
print("Allowances : ", allowances)
print("Deductions : ", deductions)
print("Tax_Amount : ", Tax_amount)
print("Net_Salary : ", Net_salary)
