import re

input = open("input.txt")

sues = []
for line in input:
    items = re.split(":?,? ", line.strip())
    sue = {}
    for i in range(0, len(items), 2):
        sue[items[i]] = int(items[i + 1])
    sues.append(sue)

simple_conditions = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
simple_sue = next(
    sue for sue in sues if all(sue.get(k, v) == v for k, v in simple_conditions.items())
)
print(f"Answer part 1: {simple_sue['Sue']}")

advanced_conditions = {
    "children": lambda a: a == 3,
    "cats": lambda a: a > 7,
    "samoyeds": lambda a: a == 2,
    "pomeranians": lambda a: a < 3,
    "akitas": lambda a: a == 0,
    "vizslas": lambda a: a == 0,
    "goldfish": lambda a: a < 5,
    "trees": lambda a: a > 3,
    "cars": lambda a: a == 2,
    "perfumes": lambda a: a == 1,
}
advanced_sue = next(
    sue
    for sue in sues
    if all(k not in sue or v(sue.get(k)) for k, v in advanced_conditions.items())
)
print(f"Answer part 2: {advanced_sue['Sue']}")
