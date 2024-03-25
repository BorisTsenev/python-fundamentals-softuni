def avg(a: list):
    return sum(a) / len(a)


employees_happiness = list(map(int, input().split()))
improvement_factor = int(input())

employees_happiness = list(map(lambda a: a * improvement_factor, employees_happiness))
average_happiness = avg(employees_happiness)
happy_employees = [employee for employee in employees_happiness if employee >= average_happiness]

print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. ", end="")
if len(happy_employees) >= len(employees_happiness) / 2:
    print("Employees are happy!")
else:
    print("Employees are not happy!")
