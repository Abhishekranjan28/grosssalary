# Function to calculate gross salary
def calculate_gross_salary(basic, grade):
    # Calculate HRA, DA, and Allowance based on the provided information
    hra = 0.20 * basic
    da = 0.50 * basic
    if grade == 'A':
        allowance = 1700
    elif grade == 'B':
        allowance = 1500
    else:
        allowance = 1300
    
    # Calculate PF
    pf = 0.11 * basic
    
    # Calculate gross salary
    gross_salary = basic + hra + da + allowance - pf
    return gross_salary

# Input data for employees
employees = [
    {'basic': 10000, 'grade': 'A'},
    {'basic': 4567, 'grade': 'B'}
]

# Calculate and print gross salary for each employee
for emp in employees:
    gross_salary = calculate_gross_salary(emp['basic'], emp['grade'])
    print(f"Gross Salary for grade {emp['grade']} with basic {emp['basic']} = {gross_salary}")

# Save the code to a file
code = '''
# Function to calculate gross salary
def calculate_gross_salary(basic, grade):
    hra = 0.20 * basic
    da = 0.50 * basic
    if grade == 'A':
        allowance = 1700
    elif grade == 'B':
        allowance = 1500
    else:
        allowance = 1300
    pf = 0.11 * basic
    gross_salary = basic + hra + da + allowance - pf
    return gross_salary

# Input data for employees
employees = [
    {'basic': 10000, 'grade': 'A'},
    {'basic': 4567, 'grade': 'B'}
]

# Calculate and print gross salary for each employee
for emp in employees:
    gross_salary = calculate_gross_salary(emp['basic'], emp['grade'])
    print(f"Gross Salary for grade {emp['grade']} with basic {emp['basic']} = {gross_salary}")
'''

# Save the code to a file named 'calculate_salary.py'
with open('calculate_salary.py', 'w') as file:
    file.write(code)

print("Code saved to 'calculate_salary.py'")
