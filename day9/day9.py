import itertools

file = open("sample.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]

headCoords = [0, 0]
tailCoords = [0, 0]
previousTailCoords = [[0, 0]]

def checkTail(oldHeadPosition):
    print(oldHeadPosition, oldHeadPosition)
    if(abs(headCoords[0] - tailCoords[0]) > 1 or abs(headCoords[1] - tailCoords[1]) > 1):
        tailCoords[0], tailCoords[1] = oldHeadPosition[0], oldHeadPosition[1]
    if(tailCoords not in previousTailCoords):
        previousTailCoords.append([oldHeadPosition[0], oldHeadPosition[1]])

for line in fileLines:
    command = line.split()
    print(command)
    for i in range(int(command[1])):
        oldHeadCoords = [headCoords[0], headCoords[1]] # write like this to avoid array trickery
        headCoords[0] += 1 if command[0] == "R" else -1 if command[0] == "L" else 0
        headCoords[1] += 1 if command[0] == "U" else -1 if command[0] == "D" else 0

        checkTail(oldHeadCoords)

print(list(previousTailCoords for previousTailCoords,_ in itertools.groupby(previousTailCoords)))
print(len(list(previousTailCoords for previousTailCoords,_ in itertools.groupby(previousTailCoords))))