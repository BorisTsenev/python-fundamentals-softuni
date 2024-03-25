time_input = input().split()
time_list = [int(x) for x in time_input]
total_left_time = 0
total_right_time = 0

steps_count = len(time_list) // 2

for i in range(steps_count):
    current_left_time = time_list[i]
    current_right_time = time_list[-1 - i]

    if current_right_time == 0:
        total_right_time *= 0.8
    else:
        total_right_time += current_right_time
    if current_left_time == 0:
        total_left_time *= 0.8
    else:
        total_left_time += current_left_time

if total_left_time > total_right_time:
    winner = "right"
    win_time = total_right_time
else:
    winner = "left"
    win_time = total_left_time

print(f"The winner is {winner} with total time: {win_time:.1f}")
