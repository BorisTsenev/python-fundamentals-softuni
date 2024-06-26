from math import floor


def center_point(x1, y1, x2, y2):
    first_sum = abs(x1) + abs(y1)
    second_sum = abs(x2) + abs(y2)

    if first_sum < second_sum:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

print(center_point(x1, y1, x2, y2))
