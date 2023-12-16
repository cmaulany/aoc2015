import math

input = open("input.txt")

moves = {
    "magic_missiles": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229,
}

boss = tuple(map(int, (line.split(": ")[1] for line in input.readlines())))
player = (50, 500, 0, 0)
effects = ()


def get_allowed_moves(game):
    player, _, effects = game
    mana = player[1]
    allowed_moves = [
        k
        for k, v in moves.items()
        if mana >= v and all(name != k for name, _ in effects)
    ]
    return allowed_moves


def do_effects(game):
    player, boss, effects = game
    next_effects = []
    shield = any(name == "shield" for name, _ in effects)
    player = (player[0], player[1], 7 if shield else 0, player[3])
    for name, n in effects:
        if name == "poison":
            boss = (boss[0] - 3, boss[1])
        elif name == "recharge":
            player = (player[0], player[1] + 101, player[2], player[3])

        if n > 1:
            next_effects.append((name, n - 1))
    return (player, boss, tuple(next_effects))


def do_attack(game):
    player, boss, effects = game
    damage = max(1, boss[1] - player[2])
    player = (player[0] - damage, player[1], player[2], player[3])
    return (player, boss, effects)


def do_move(game, move):
    player, boss, effects = game
    cost = moves[move]
    player = player = (
        player[0],
        player[1] - cost,
        player[2],
        player[3] + cost,
    )
    next_effects = list(effects)
    if move == "magic_missiles":
        boss = (boss[0] - 4, boss[1])
    if move == "drain":
        player = (player[0] + 2, player[1], player[2], player[3])
        boss = (boss[0] - 2, boss[1])
    if move == "shield":
        next_effects.append(("shield", 6))
    if move == "poison":
        next_effects.append(("poison", 6))
    if move == "recharge":
        next_effects.append(("recharge", 5))
    return (player, boss, tuple(next_effects))


def do_turn(game, move, hard):
    if hard:
        player, boss, effects = game
        game = (player[0] - 1, player[1], player[2], player[3]), boss, effects
        if game[0][0] <= 0:
            return game
    game = do_move(game, move)
    game = do_effects(game)
    if game[1][0] <= 0:
        return game
    game = do_attack(game)
    game = do_effects(game)
    return game


def find_min_mana(game, hard):
    best = math.inf

    def fight(game):
        nonlocal best

        if game[0][3] > best:
            return []
        next = [do_turn(game, move, hard) for move in get_allowed_moves(game)]
        alive = [game for game in next if game[0][0] > 0]
        in_progress = [game for game in alive if game[1][0] > 0]
        win_scores = [game[0][3] for game in alive if game[1][0] <= 0]
        result = win_scores + [
            score for scores in map(fight, in_progress) for score in scores
        ]
        if result:
            best = min(best, *result)
        return result

    return min(fight(game))


game = player, boss, effects
min_mana = find_min_mana(game, False)
print(f"Answer part 1: {min_mana}")

min_mana_hard = find_min_mana(game, True)
print(f"Answer part 2: {min_mana_hard}")
