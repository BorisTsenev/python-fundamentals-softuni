import math

total_students_per_hour = 0
for current_employee in range(3):
    total_students_per_hour += int(input())

students_count = int(input())
work_hours = math.ceil(students_count / total_students_per_hour)
rest_hours = int(work_hours // 3)
total_hours = work_hours + rest_hours
print(f"Time needed: {total_hours}h.")
