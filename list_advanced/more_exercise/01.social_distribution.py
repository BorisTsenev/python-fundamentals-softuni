population = list(map(int, input().split(", ")))
min_population = int(input())

for current_population in population:
    if current_population < min_population:
        diff = min_population - current_population
        max_index = population.index(max(population))
        population[max_index] -= diff
        population[population.index(current_population)] = min_population
if max(population) <= min_population:
    print("No equal distribution possible")
else:
    print(population)
