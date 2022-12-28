from itertools import product

input = open("input.txt")
lights = [[c == "#" for c in line.strip()] for line in input]


def neighbors(lights, position):
    positions = [
        map(sum, zip(position, delta))
        for delta in product([1, 0, -1], [1, 0, -1])
        if delta != (0, 0)
    ]
    width = len(lights[0])
    height = len(lights)
    return [
        (x, y) for x, y in positions if x >= 0 and x < width and y >= 0 and y < height
    ]


def tick(lights):
    next_lights = []
    for y, row in enumerate(lights):
        next_lights.append([])
        for x, on in enumerate(row):
            on_neighbors = sum(
                lights[neighbor[1]][neighbor[0]]
                for neighbor in neighbors(lights, (x, y))
            )
            next_lights[y].append((on and on_neighbors in [2, 3]) or on_neighbors == 3)

    return next_lights


def sum_after_ticks(lights, n, stuck=False):
    for _ in range(n):
        if stuck:
            for x, y in product([0, 99], [0, 99]):
                lights[y][x] = True
        lights = tick(lights)
    if stuck:
        for x, y in product([0, 99], [0, 99]):
            lights[y][x] = True

    return sum(on for row in lights for on in row)


normal_result = sum_after_ticks(lights, 100)
print(f"Answer part 1: {normal_result}")

stuck_result = sum_after_ticks(lights, 100, stuck=True)
print(f"Answer part 2: {stuck_result}")
