# N employees
N = 5

employees_work_hours = []
total_pay = 0

for i in range(N):
    employees_hour = int(input("Enter your hours: "))
    employees_work_hours.append(employees_hour)


# Final product: total pay

for i in range(N):
    total_pay += employees_work_hours[i] * 14.25

print(total_pay)