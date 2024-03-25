def avg(a: list):
    return int(sum(a) / len(a))


nums = list(map(int, input().split()))
better_than_average = list()
better_than_average = [better_than_average.append(nums) for num in nums if num > avg(nums)
                       and len(better_than_average) <= 5]

better_than_average.sort(reverse=True)
if len(better_than_average) == 0:
    print("No")
else:
    print(better_than_average)
