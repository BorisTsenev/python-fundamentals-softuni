explosions = [x for x in input()]
deleted_indexes = []
for i in range(len(explosions)):
    if explosions[i] == ">":
        if explosions[i+2] != ">":
            deleted_indexes.append(i+1)
            for k in range(i + 2, i + 1 + int(explosions[i+1])):
                deleted_indexes.append(k)
        else:
            deleted_indexes.append(i+1)
deleted_indexes.sort(reverse=True)
for i in deleted_indexes:
    explosions.pop(i)

print("".join(explosions))