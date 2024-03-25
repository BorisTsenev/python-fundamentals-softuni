actions_count = int(input())
student_book = {}
for _ in range(actions_count):
    name = input()
    grade = float(input())
    if name in student_book.keys():
        student_book[name].append(grade)
    else:
        student_book[name] = [grade]

for (student, grades) in student_book.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade:.2f}")
