import hashlib

input = open("input.txt")
code = input.readline()


def find_hash(code, padstart):
    i = 0
    while True:
        hash = hashlib.md5((code + str(i)).encode()).hexdigest()
        if all(c == "0" for c in hash[0:padstart]):
            break
        i += 1
    return i


hash5 = find_hash(code, 5)
print(f"Answer part 1: {hash5}")

hash6 = find_hash(code, 6)
print(f"Answer part 2: {hash6}")
