from math import prod
from functools import cache
from itertools import combinations

input = open("input.txt")
packages = tuple(map(int, input.readlines()))


@cache
def has_solution(packages, weights):
    if len(packages) == 0 and all(weight == 0 for weight in weights):
        return True

    if sum(weights) > sum(packages) or any(weight < 0 for weight in weights):
        return False

    package, *rest = packages
    for i in range(len(weights)):
        weight = weights[i]
        if has_solution(
            tuple(rest),
            weights[:i] + (weight - package,) + weights[i + 1 :],
        ):
            return True

    return False


def find_best_qe(packages, group_count):
    weight = sum(packages) // group_count

    solutions = []
    for i in range(len(packages)):
        for group in combinations(packages, i):
            rest = tuple(set(packages) - set(group))
            if sum(group) == weight and has_solution(
                rest,
                (weight,) * (group_count - 1),
            ):
                solutions.append(group)

        if solutions:
            break

    return min(map(prod, solutions))


qe_three_groups = find_best_qe(packages, 3)
print(f"Answer part 1: {qe_three_groups}")

qe_four_groups = find_best_qe(packages, 4)
print(f"Answer part 2: {qe_four_groups}")
