from itertools import combinations

input = open("input.txt")
cups = [int(line) for line in input]
combs = [
    comb for i in range(len(cups)) for comb in combinations(cups, i) if sum(comb) == 150
]
print(f"Answer part 1: {len(combs)}")

minimum_container_count = min(len(comb) for comb in combs)
minimum_container_combs = [
    comb for comb in combs if len(comb) == minimum_container_count
]
print(f"Answer part 2: {len(minimum_container_combs)}")
