from collections import defaultdict

input = open("input.txt")

[replacements_input, molecule] = input.read().split("\n\n")
replacements = defaultdict(lambda: [])
for line in replacements_input.splitlines():
    [frm, to] = line.split(" => ")
    replacements[frm].append(to)

combs = set()
for frm, tos in replacements.items():
    print("Fff", frm)
    l = len(frm)
    for i in range(len(molecule) - l + 1):
        print(molecule[i : i + l], frm)
        if molecule[i : i + l] == frm:
            for to in tos:
                print("-", to)
                combs.add(molecule[:i] + to + molecule[i + l :])

print(len(combs))
