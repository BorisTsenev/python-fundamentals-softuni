courses = {}

while True:
    command = input()
    if command == "end":
        break
    course, name = command.split(" : ")

    if course in courses.keys():
        courses[course].append(name)
    else:
        courses[course] = [name]

for (course, names) in courses.items():
    print(f"{course}: {len(courses[course])}")
    for name in names:
        print(f"-- {name}")