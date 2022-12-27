from itertools import permutations
from collections import defaultdict

input = open("input.txt")

scores = defaultdict(lambda: {})
for line in input:
    parts = line.strip().split(" ")
    person_a = parts[0]
    person_b = parts[10][:-1]
    sign = 1 if parts[2] == "gain" else -1
    amount = int(parts[3])
    scores[person_a][person_b] = sign * amount


def get_max_score(scores):
    names = set(scores.keys())
    arrangements = [perm for perm in permutations(names) if perm[0] == list(names)[0]]
    scored = [
        sum(
            scores[arr[i]][arr[i - 1]] + scores[arr[i]][arr[(i + 1) % len(arr)]]
            for i in range(len(arr))
        )
        for arr in arrangements
    ]
    return max(scored)


max_score = get_max_score(scores)
print(f"Answer part 1: {max_score}")

for value in scores.values():
    value["You"] = 0
scores["You"] = {name: 0 for name in scores.keys()}

max_score_with_you = get_max_score(scores)
print(f"Answer part 2: {max_score_with_you}")
