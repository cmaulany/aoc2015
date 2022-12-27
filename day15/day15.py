import re

input = open("input.txt")

ingredients = {}
for line in input:
    parts = re.split("[:,]? ", line.strip())
    ingredients[parts[0]] = (
        int(parts[2]),
        int(parts[4]),
        int(parts[6]),
        int(parts[8]),
        int(parts[10]),
    )


def get_distributions(length, n):
    if n == 1:
        return [[length]]
    return [
        [i, *distribution]
        for i in range(length + 1)
        for distribution in get_distributions(length - i, n - 1)
    ]


def bake_cookie(recipe, ingredients):
    score = 1
    for i in range(4):
        property_score = sum(
            ingredient[i] * n for n, ingredient in zip(recipe, ingredients.values())
        )
        score *= max(0, property_score)
    calories = sum(
        ingredient[4] * recipe[i] for i, ingredient in enumerate(ingredients.values())
    )
    return (score, calories)


recipes = get_distributions(100, len(ingredients))
cookies = [*map(lambda recipe: bake_cookie(recipe, ingredients), recipes)]
best_cookie = max(cookies, key=lambda cookie: cookie[0])
print(f"Answer part 1: {best_cookie[0]}")

calories500_cookies = [cookie for cookie in cookies if cookie[1] == 500]
best_calories500_cookie = max(map(lambda score: score[0], calories500_cookies))
print(f"Answer part 2: {best_calories500_cookie}")
