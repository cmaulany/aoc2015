from itertools import permutations

input = open("input.txt")

nodes = set()
edges = []
for line in input:
    parts = line.strip().split(" ")
    nodes.add(parts[0])
    nodes.add(parts[2])
    edges.append((parts[0], parts[2], int(parts[4])))

distances = [
    sum(
        next(
            edge[2]
            for edge in edges
            if route[i - 1] in edge[0:2] and route[i] in edge[0:2]
        )
        for i in range(1, len(route))
    )
    for route in permutations(nodes)
]

print(f"Answer part 1: {min(distances)}")
print(f"Answer part 2: {max(distances)}")
