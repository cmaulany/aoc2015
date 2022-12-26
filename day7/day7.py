input = open("input.txt")


def parse(value):
    return int(value) if value.isnumeric() else value


instructions = []
for line in input:
    parts = line.strip().split(" ")
    if parts[0] == "NOT":
        instruction = {
            "type": "NOT",
            "inputs": (parse(parts[1]),),
            "output": parse(parts[3]),
        }
    if parts[1] == "->":
        instruction = {
            "type": "->",
            "inputs": (parse(parts[0]),),
            "output": parse(parts[2]),
        }
    if parts[1] in ["AND", "OR", "LSHIFT", "RSHIFT"]:
        instruction = {
            "type": parts[1],
            "inputs": (parse(parts[0]), parse(parts[2])),
            "output": parse(parts[4]),
        }
    instructions.append(instruction)


def solve(instructions, wire, register={}):
    while "a" not in register:
        instruction = next(
            instruction
            for instruction in instructions
            if instruction["output"] not in register
            and all(
                isinstance(input, int) or input in register
                for input in instruction["inputs"]
            )
        )

        inputs = [
            input if isinstance(input, int) else register[input]
            for input in instruction["inputs"]
        ]
        if instruction["type"] == "NOT":
            output = ~inputs[0]
        if instruction["type"] == "->":
            output = inputs[0]
        if instruction["type"] == "AND":
            output = inputs[0] & inputs[1]
        if instruction["type"] == "OR":
            output = inputs[0] | inputs[1]
        if instruction["type"] == "LSHIFT":
            output = inputs[0] << inputs[1]
        if instruction["type"] == "RSHIFT":
            output = inputs[0] >> inputs[1]
        register[instruction["output"]] = output

    return register[wire]


wire_a = solve(instructions, "a")
looped_wire_a = solve(instructions, "a", {"b": wire_a})
print(f"Answer part 1: {wire_a}")
print(f"Answer part 2: {looped_wire_a}")
