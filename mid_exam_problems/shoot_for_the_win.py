targets = input().split()
command = input()

while command != 'End':
    command = int(command)
    if command in range(len(targets)):
        targets[command] = '-1'
    command = input()

print(f"Shot targets: {targets.count('-1')} -> {' '.join(targets)}")
