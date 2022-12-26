input = open("input.txt")
boxes = [map(int, line.split("x")) for line in input]

papers = []
ribbons = []
for l, w, h in boxes:
    squares = [2 * l * w, 2 * w * h, 2 * h * l]
    slack = min(squares) // 2
    paper = sum(squares) + slack
    papers.append(paper)

    perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
    min_perimeter = min(perimeters)
    bow = l * w * h
    ribbon = min_perimeter + bow
    ribbons.append(ribbon)

print(sum(papers))
print(sum(ribbons))
