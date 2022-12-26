input = open("input.txt")
line = input.readline()

position = (0, 0)
houses = {position: 1}
for c in line:
    x, y = position
    if c == ">":
        position = (x + 1, y)
    if c == "v":
        position = (x, y + 1)
    if c == "<":
        position = (x - 1, y)
    if c == "^":
        position = (x, y - 1)
    houses[position] = houses.get(position, 0) + 1

print(f"Answer part 1: {len(houses)}")

positions = [(0, 0), (0, 0)]
index = 0
houses = {position: 1 for position in positions}
for c in line:
    x, y = positions[index]
    if c == ">":
        position = (x + 1, y)
    if c == "v":
        position = (x, y + 1)
    if c == "<":
        position = (x - 1, y)
    if c == "^":
        position = (x, y - 1)

    positions[index] = position

    houses[position] = houses.get(position, 0) + 1
    index = (index + 1) % len(positions)

print(f"Answer part 2: {len(houses)}")
