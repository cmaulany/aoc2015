import re
from itertools import product

input = open("input.txt")
boss = list(map(int, (line.split(": ")[1] for line in input.readlines())))

shop_input = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""
shop = {}
for category in shop_input.split("\n\n"):
    cat_name = category.split(":")[0].lower()
    shop[cat_name] = []
    for line in category.split("\n")[1:]:
        [name, *stats] = re.split("  +", line)
        shop[cat_name].append((name, list(map(int, stats))))


def with_none(items):
    return [["None", [0, 0, 0]], *items]


def attack(source, target):
    [hit_points, damage, armor] = target
    return [
        hit_points - max(source[1] - armor, 1),
        damage,
        armor,
    ]


def fight(player, boss):
    while True:
        boss = attack(player, boss)
        if boss[0] <= 0:
            return True
        player = attack(boss, player)
        if player[0] <= 0:
            return False


def equip(items):
    return [100, *[sum(item[1][i] for item in items) for i in range(1, 3)]]


def cost(items):
    return sum(item[1][0] for item in items)


weapons = shop["weapons"]
armor = shop["armor"]
rings = shop["rings"]

loadouts = list(product(weapons, with_none(armor), with_none(rings), with_none(rings)))

valid_loadouts = [
    loadout
    for loadout in loadouts
    if all(sum(item[0] == other[0] for other in loadout) == 1 for item in loadout)
]

wins = [loadout for loadout in valid_loadouts if fight(equip(loadout), boss)]
losses = [loadout for loadout in valid_loadouts if loadout not in wins]

best = min(wins, key=lambda loadout: cost(loadout))
print(f"Answer part 1: {cost(best)}")

worst = max(losses, key=lambda loadout: cost(loadout))
print(f"Answer part 2: {cost(worst)}")
