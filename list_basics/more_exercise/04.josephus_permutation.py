victims = input().split()
counting = int(input())
current_count = 0
output = list()

while len(victims) > 0:
    current_count += counting - 1
    if current_count > len(victims) - 1:
        current_count = current_count % len(victims)

    output.append(victims.pop(current_count))

print(f"[{','.join(output)}]")
