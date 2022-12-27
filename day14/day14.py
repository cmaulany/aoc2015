from collections import defaultdict

input = open("input.txt")

reindeer = []
for line in input:
    parts = line.strip().split(" ")
    speed = int(parts[3])
    duration = int(parts[6])
    rest = int(parts[13])
    reindeer.append((parts[0], speed, duration, rest))

distances = defaultdict(lambda: 0)
scores = defaultdict(lambda: 0)
for t in range(2503):
    for name, speed, duration, rest in reindeer:
        cycle_duration = duration + rest
        if t % cycle_duration < duration:
            distances[name] += speed
    max_distance = max(distances.values())
    leaders = [name for name in distances.keys() if distances[name] == max_distance]
    for leader in leaders:
        scores[leader] += 1

max_distance = max(distances.values())
max_score = max(scores.values())

print(f"Answer part 1: {max_distance}")
print(f"Answer part 2: {max_score}")
