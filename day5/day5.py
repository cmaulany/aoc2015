input = open("input.txt")
strings = [line for line in input]


def is_nice(string):
    has_three_vowels = sum(c in "aeiou" for c in string) >= 3
    has_pair = any(string[i - 1] == string[i] for i in range(len(string)) if i > 0)
    not_banned = all(not ban in string for ban in ["ab", "cd", "pq", "xy"])
    return has_three_vowels and has_pair and not_banned


def is_nice2(string):
    has_pairs = any(
        string[i - 1] == string[j - 1] and string[i] == string[j]
        for i in range(len(string))
        for j in range(len(string))
        if i > 0 and j > 0 and abs(i - j) > 1
    )
    has_with_interval = any(
        string[i - 2] == string[i] for i in range(len(string)) if i > 1
    )
    return has_with_interval and has_pairs


nice_string_count = sum(is_nice(line) for line in strings)
nice_string_count2 = sum(is_nice2(line) for line in strings)
print(f"Answer part 1: {nice_string_count}")
print(f"Answer part 2: {nice_string_count2}")
