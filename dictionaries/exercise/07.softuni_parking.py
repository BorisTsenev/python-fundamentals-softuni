def register(reg_dict: dict, name, reg_num):
    if reg_num in reg_dict.values():
        print(f"ERROR: already registered with plate number {reg_num}")
        return reg_dict
    reg_dict[name] = reg_num
    print(f"{name} registered {reg_num} successfully")
    return reg_dict


def unregister(reg_dict: dict, name):
    if name not in reg_dict.keys():
        print(f"ERROR: user {name} not found")
        return reg_dict

    reg_dict.pop(name)
    print(f"{name} unregistered successfully")
    return reg_dict


actions_count = int(input())
registrations = {}
for _ in range(actions_count):
    action = input().split()
    if action[0] == "register":
        registrations = register(registrations, action[1], action[2])
    else:
        registrations = unregister(registrations, action[1])

for (person, registration_num) in registrations.items():
    print(f"{person} => {registration_num}")
