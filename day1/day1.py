input = open("input.txt", "r")
line = input.readline()

final_floor = sum(1 if c == "(" else -1 for c in line)
print(f"Answer part 1: {final_floor}")

floor = 1
for i, c in enumerate(line):
    floor += 1 if c == "(" else -1
    if floor == -1:
        position = i
        break

print(f"Answer part 2: {position}")
