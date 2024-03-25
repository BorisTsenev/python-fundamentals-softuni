import math


def factorial_divisor(a, b):
    a_fact = math.factorial(a)
    b_fact = math.factorial(b)
    divised = a_fact / b_fact
    return f"{divised:.2f}"


first_num = int(input())
second_num = int(input())

print(factorial_divisor(first_num, second_num))
