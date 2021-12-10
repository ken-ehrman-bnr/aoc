# Advent of Code 2021
# Day 06
# Problem 01
initial_state = [3, 4, 3, 1, 2]
population = [0]*9

for day in initial_state:
    population[day] += 1

noobs = 0
for day in range(0, 80):
    print(population)

    next = [0]*9
    noobs = population[0]
    for age in range(0, 8):
        next[age] = population[age+1]
    next[6] += noobs
    next[8] = noobs
    population = next

print(sum(population))
