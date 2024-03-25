def calculations(operator, a, b):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a / b)


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculations(input_operator, first_num, second_num))
