from collections import defaultdict

input = open("input.txt")
number = int(input.readline())

infinite = defaultdict(lambda: 0)
fifty = defaultdict(lambda: 0)
for i in range(1, number // 10):
    for j in range(0, number // 10, i):
        if j == 0:
            continue
        infinite[j] += i * 10
        if j // i <= 50:
            fifty[j] += i * 11

smallestInfinite = next(i for i, n in infinite.items() if n >= number)
smallestFifty = next(i for i, n in fifty.items() if n >= number)
print(f"Result part 1: {smallestInfinite}")
print(f"Result part 2: {smallestFifty}")