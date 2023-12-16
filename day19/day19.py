from collections import defaultdict

input = open("input.txt")

[replacements_input, medicine] = input.read().split("\n\n")
replacements = defaultdict(list)
for line in replacements_input.splitlines():
    [frm, to] = line.split(" => ")
    replacements[frm].append(to)


def replace(molecule, replacements):
    molecules = set()
    for frm, tos in replacements.items():
        length = len(frm)
        for i in range(len(molecule) - length + 1):
            if molecule[i : i + length] == frm:
                for to in tos:
                    molecules.add(molecule[:i] + to + molecule[i + length :])
    return molecules


count = len(replace(medicine, replacements))
print(f"Answer part 1: {count}")


def get_step_count(frm, to):
    rev_replacements = defaultdict(list)
    for key, values in replacements.items():
        for value in values:
            rev_replacements[value].append(key)

    ordered_keys = list(rev_replacements.keys())
    ordered_keys.sort(key=len, reverse=True)

    open = [(to, 0)]
    while open:
        [value, steps] = open.pop()
        if value == frm:
            return steps
        for key in rev_replacements.keys():
            replacement = {key: rev_replacements[key]}
            for next in replace(value, replacement):
                open.append((next, steps + 1))


step_count = get_step_count("e", medicine)
print(f"Answer part 2: {step_count}")
