import sys

snowball_count = int(input())
output = ""
max_result = -sys.maxsize

for snowball in range(snowball_count):
    snowball_weight = int(input())
    time_needed = int(input())
    snowball_quality = int(input())

    current_result = (snowball_weight / time_needed) ** snowball_quality

    if current_result > max_result:
        output = f"{snowball_weight} : {time_needed} = {int(current_result)} ({snowball_quality})"
        max_result = current_result

print(output)
