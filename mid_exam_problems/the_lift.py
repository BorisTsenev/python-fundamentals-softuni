def lift_filler(people_count, wagons: list):
    for i in range(len(wagons)):
        current_wagon = wagons[i]
        people_count -= 4 - current_wagon
        current_wagon += 4 - current_wagon
        if people_count < 0:
            current_wagon += people_count
            people_count = 0
        wagons[i] = current_wagon

    return wagons


def have_enough_space(people_count, wagons: list, people):
    if len(wagons) * 4 >= people_count:
        return "The lift has empty spots!"
    else:
        diff = people_count - len(wagons) * 4 + people
        return f"There isn't enough space! {diff} people in a queue!"


peoples = int(input())
list_of_wagons = list(map(int, input().split()))
peoples_in_wagons = sum(list_of_wagons)

list_of_wagons = lift_filler(peoples, list_of_wagons)
print(have_enough_space(peoples, list_of_wagons, peoples_in_wagons))
print(" ".join(list(map(str, list_of_wagons))))
