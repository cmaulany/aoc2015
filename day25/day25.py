import re

input = open("input.txt").read()
row, col = map(int, re.findall(r"(\d+)", input))

steps = 1
for i in range(1, row):
    steps += i

for i in range(1, col):
    steps += row + i

start = 20151125
mult = 252533
div = 33554393

n = start
for _ in range(steps - 1):
    n *= mult
    n %= div

print(f"Answer: {n}")
