levels_count = int(input())
the_maze = list()
for current_level in range(levels_count):
    level = [k for k in input()]
    the_maze.append(level)

y = 0
for i in range(len(the_maze)):
    if "k" in the_maze[i]:
        y = i
        break

x = the_maze[y].index("k")
total_moves = 0

while True:
    moved = 0
    if the_maze[y][x - 1] == " ":
        the_maze[y][x - 1] = "k"
        the_maze[y][x] = "#"
        x -= 1
        moved += 1

    if the_maze[y][x + 1] == " ":
        the_maze[y][x + 1] = "k"
        the_maze[y][x] = "#"
        x += 1
        moved +=1

    if the_maze[y - 1][x] == " ":
        the_maze[y - 1][x] = "k"
        the_maze[y][x] = "#"
        y -= 1
        moved += 1

    if the_maze[y + 1][x] == " ":
        the_maze[y + 1][x] = "k"
        the_maze[y][x] = "#"
        y += 1
        moved += 1

    total_moves += moved
    if x == len(the_maze[y]) - 1 or x == 0 \
       or y == levels_count - 1 or y == 0:
        print(f"Kate got out in {total_moves + 1} moves")
        break

    if moved == 0:
        print("Kate cannot get out")
        break
