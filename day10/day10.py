input = open("input.txt")


def look_and_say(value):
    nextvalue = []

    i, j = 0, 1
    while j <= len(value):
        if j == len(value) or value[i] != value[j]:
            nextvalue.append(str(j - i))
            nextvalue.append(value[i])
            i = j
        j += 1

    return "".join(nextvalue)


after40 = input.readline()
for i in range(40):
    after40 = look_and_say(after40)
print(f"Answer part 1: {len(after40)}")

after50 = after40
for i in range(10):
    after50 = look_and_say(after50)
print(f"Answer part 2: {len(after50)}")
