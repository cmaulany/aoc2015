input = open("input.txt")

instructions = []
for line in input:
    parts = line.split(" ")
    if parts[0] == "turn":
        action = f"turn {parts[1]}"
        start = map(int, parts[2].split(","))
        end = map(int, parts[4].split(","))
    if parts[0] == "toggle":
        action = "toggle"
        start = map(int, parts[1].split(","))
        end = map(int, parts[3].split(","))
    instructions.append(
        {
            "action": action,
            "start": tuple(start),
            "end": tuple(end),
        }
    )


def count_binary_lights(instructions):
    lights = [[False] * 1000 for _ in range(1000)]

    for instruction in instructions:
        sx, sy = instruction["start"]
        ex, ey = instruction["end"]
        action = instruction["action"]
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if action == "toggle":
                    next_light = not lights[y][x]
                if action == "turn on":
                    next_light = True
                if action == "turn off":
                    next_light = False
                lights[y][x] = next_light

    return sum(light for row in lights for light in row)


def count_analog_lights(instructions):
    lights = [[0] * 1000 for _ in range(1000)]

    for instruction in instructions:
        sx, sy = instruction["start"]
        ex, ey = instruction["end"]
        action = instruction["action"]
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if action == "toggle":
                    delta = 2
                if action == "turn on":
                    delta = 1
                if action == "turn off":
                    delta = -1
                lights[y][x] = max(0, lights[y][x] + delta)

    return sum(light for row in lights for light in row)


binary_light_count = count_binary_lights(instructions)
print(f"Answer part 1: {binary_light_count}")

analog_light_count = count_analog_lights(instructions)
print(f"Answer part 2: {analog_light_count}")
