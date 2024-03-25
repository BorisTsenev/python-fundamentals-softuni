def main():
    nums = list(map(int, input().split()))
    command = input()
    while command != 'end':
        if command != 'decrease':
            command = command.split()
            code = f"{command[0]}(nums, {command[1]}, {command[2]})"
        else:
            code = "decrease(nums)"
        nums = eval(code)
        command = input()
    nums = [str(num) for num in nums]
    print(', '.join(nums))


def swap(nums, index1, index2):
    if index2 == 0:
        index1, index2 = index2, index1
    index1_element = nums.pop(index1)
    nums.insert(index1, nums.pop(index2 - 1))
    nums.insert(index2, index1_element)
    return nums


def multiply(nums, index1, index2):
    nums[index1] *= nums[index2]
    return nums


def decrease(nums):
    nums = [x - 1 for x in nums]
    return nums


main()
