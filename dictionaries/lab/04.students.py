searched_course = str()
student_with_program = dict()
while True:
    command = input()
    if ":" not in command:
        searched_course = command
        break
    name, identi, course = command.split(":")
    name_course = [name, course]
    student_with_program[identi] = name_course

searched_course = searched_course.split("_")
searched_course = " ".join(searched_course)

for (identi, name_course) in student_with_program.items():
    if searched_course in name_course:
        print(f"{name_course[0]} - {identi}")
