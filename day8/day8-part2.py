file = open("input.txt", "r")
fileLines = [[int(x) for x in line.strip("$\n")] for line in file.readlines()]
scoring = [[0 for x in line] for line in fileLines]

def scoreTree(width, height):
    centre = fileLines[height][width]
    scoreLeft, scoreRight, scoreTop, scoreBottom = 0, 0, 0, 0

    left, right, top, bottom = width - 1, width + 1, height - 1, height + 1
    while left >= 0:
        scoreLeft += 1
        if(fileLines[height][left] >= centre):
            break
        left -= 1

    while right < len(fileLines[height]):
        scoreRight += 1
        if(fileLines[height][right] >= centre):
            break
        right += 1

    while top >= 0:
        scoreTop += 1
        if(fileLines[top][width] >= centre):
            break
        top -= 1

    while bottom < len(fileLines):
        scoreBottom += 1
        if(fileLines[bottom][width] >= centre):
            break
        bottom += 1

    scoring[height][width] = scoreLeft*scoreRight*scoreTop*scoreBottom
    return scoring[height][width]

for height in range(len(fileLines)):
    for width in range(len(fileLines[height])):
        scoreTree(width, height)

print(scoreTree(2, 1))

print(max([x for line in scoring for x in line]))