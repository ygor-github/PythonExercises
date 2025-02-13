from Employee import *

employee = Employee('Matheus', 'matheus@email.com')

employee.hours_record('Jan',300)
employee.hours_record('Feb', 200)
employee.hourly_salary_record('Jan', 30)
employee.hourly_salary_record('Feb', 30)

print(employee)
print(f'Total salary January: {employee.calculate_salary('Jan')}')
print(f'Total salary February: {employee.calculate_salary('Feb')}')