first_row = input().split()
second_row = input().split()
third_row = input().split()
winner = ''

for i in range(3):
    if first_row[i] == second_row[i] == third_row[i]:
        winner = first_row[i]

    if i != 0 and first_row.count(str(i)) == 3 \
            or second_row.count(str(i)) == 3 \
            or third_row.count(str(i)) == 3:
        winner = str(i)

if first_row[0] == second_row[1] == third_row[2]:
    winner = first_row[0]

if first_row[2] == second_row[1] == third_row[0]:
    winner = first_row[2]

if winner == "1":
    print("First player won")
elif winner == "2":
    print("Second player won")
else:
    print("Draw!")
