print("Please enter your employee id:")
employee_id = input()

print("Please enter your employee name:")
employee_name = input()

print("Please enter your basic salary:")
basic_salary = float(input())

print("Please enter your allowances:")
allowances = float(input())

print("Please enter your deductions:")
deductions = float(input())
print("basic salary entered:", basic_salary)

print("Please enter your tax rate:")
tax_rate = float(input())
print("tax rate entered:", tax_rate)

gross_salary = basic_salary + allowances - deductions
print("Please enter your gross salary:")
print("gross salary:", gross_salary)

tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount
print("tax amount:", tax_amount)
print("net salary:", net_salary)
