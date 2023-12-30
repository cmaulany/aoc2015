import re

input = open("input.txt")

instructions = []
for line in input.readlines():
    name, *rest = re.split(",? ", line.strip())
    if name == "jio" or name == "jie":
        register = rest[0]
        value = int(rest[1])
    elif name == "jmp":
        register = None
        value = int(rest[0])
    else:
        register = rest[0]
        value = None
    instructions.append((name, register, value))


def run(instructions, registers={"a": 0, "b": 0}):
    i = 0
    while i < len(instructions):
        name, register, value = instructions[i]
        if name == "hlf":
            registers[register] //= 2
        elif name == "tpl":
            registers[register] *= 3
        elif name == "inc":
            registers[register] += 1
        elif (
            name == "jmp"
            or (name == "jie" and registers[register] % 2 == 0)
            or (name == "jio" and registers[register] == 1)
        ):
            i += value - 1
        i += 1
    return registers


result_zero = run(instructions)
print(f"Answer part 1: {result_zero['b']}")

result_one = run(instructions, {"a": 1, "b": 0})
print(f"Answer part 2: {result_one['b']}")
