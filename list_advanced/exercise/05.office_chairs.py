def office_chairs(room_count):
    output = ""
    total_chairs_count = 0;
    for current_room in range(1, room_count + 1):
        room_list = input().split()
        chairs_count = len(room_list[0])
        people_count = int(room_list[1])
        chairs_left = chairs_count - people_count
        if chairs_left < 0:
            output += f"{abs(chairs_left)} more chairs needed in room {current_room}\n"
        total_chairs_count += chairs_left

    if output == "":
        output = f"Game On, {total_chairs_count} free chairs left"

    return output


rooms_count = int(input())
print(office_chairs(rooms_count))
