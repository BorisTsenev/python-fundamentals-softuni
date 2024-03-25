resources = {}
while True:
    command = input()
    if command == "stop":
        break

    resource = command
    quantity = int(input())

    if resource in resources.keys():
        resources[resource] += quantity
    else:
        resources[resource] = quantity

for (resource, quantity) in resources.items():
    print(f"{resource} -> {quantity}")
