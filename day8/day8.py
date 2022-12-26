input = open("input.txt")

code_lengths = []
value_lengths = []
encoded_lengths = []
for line in input:
    line = line.strip()

    d = 2
    e = 4
    i = 1
    while i < len(line) - 1:
        if line[i:].startswith('\\"') or line[i:].startswith("\\\\"):
            d += 1
            e += 2
            i += 1
        elif line[i:].startswith("\\x"):
            d += 3
            e += 1
            i += 3
        i += 1

    code_length = len(line)
    code_lengths.append(code_length)
    value_lengths.append(code_length - d)
    encoded_lengths.append(code_length + e)

value_difference = sum(code_lengths) - sum(value_lengths)
encoded_difference = sum(encoded_lengths) - sum(code_lengths)
print(f"Answer part 1: {value_difference}")
print(f"Answer part 2: {encoded_difference}")
