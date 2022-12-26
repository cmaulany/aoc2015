input = open("input.txt")


def increment(password):
    chars = list(password)
    for i in reversed(range(len(chars))):
        c = ord(chars[i]) + 1
        if c <= ord("z"):
            chars[i] = chr(c)
            break
        chars[i] = "a"
    return "".join(chars)


def is_valid(password):
    if any(c in "iol" for c in password):
        return False

    pairs = 0
    i = 0
    while pairs < 2 and i < len(password) - 1:
        if password[i] == password[i + 1]:
            i += 2
            pairs += 1
        else:
            i += 1

    if pairs < 2:
        return False

    return any(
        ord(password[i + 1]) == ord(password[i]) + 1
        and ord(password[i + 2]) == ord(password[i]) + 2
        for i in range(len(password) - 2)
    )


password = input.readline().strip()
while not is_valid(password):
    password = increment(password)
print(f"Answer part 1: {password}")

password = increment(password)
while not is_valid(password):
    password = increment(password)
print(f"Answer part 2: {password}")
