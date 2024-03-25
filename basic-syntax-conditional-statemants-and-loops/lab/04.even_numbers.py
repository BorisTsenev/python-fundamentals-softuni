num_count = int(input())

for numbers in range(num_count):
    current_num = int(input())
    if current_num % 2 == 0:
        pass
    else:
        print(f"{current_num} is odd!")
        break
else:
    print("All numbers are even.")