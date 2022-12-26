import json

input = open("input.txt")
parsed = json.loads(input.read())


def sum_numbers(data):
    if isinstance(data, dict):
        return sum(map(sum_numbers, data.values()))
    if isinstance(data, list):
        return sum(map(sum_numbers, data))
    if isinstance(data, int):
        return data
    return 0


def sum_non_red_numbers(data):
    if isinstance(data, dict):
        if "red" in data.values():
            return 0
        else:
            return sum(map(sum_non_red_numbers, data.values()))
    if isinstance(data, list):
        return sum(map(sum_non_red_numbers, data))
    if isinstance(data, int):
        return data
    return 0


number_sum = sum_numbers(parsed)
non_red_number_sum = sum_non_red_numbers(parsed)
print(f"Answer part 1: {number_sum}")
print(f"Answer part 2: {non_red_number_sum}")
