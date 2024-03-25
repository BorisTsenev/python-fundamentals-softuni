persons_count = int(input())
elevator_person_count = int(input())

courses_count = persons_count // elevator_person_count

if persons_count % elevator_person_count > 0:
    courses_count += 1

print(courses_count)
