company_users = {}
while True:
    command = input()
    if command == "End":
        break

    company, user = command.split(" -> ")
    if company not in company_users.keys():
        company_users[company] = []

    if user not in company_users[company]:
        company_users[company].append(user)

for (company, members) in company_users.items():
    output = company
    for member in members:
        output += f"\n-- {member}"
    print(output)
