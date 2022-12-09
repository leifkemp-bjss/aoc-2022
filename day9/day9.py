import itertools

file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]

def checkTail(previousTailCoords, knotChain, chainIndex=0):
    head = knotChain[chainIndex]
    tail = knotChain[chainIndex+1]
    # Tail is out of range, time to figure out where to move it
    if(abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1):
        if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
            pass
        elif head[0] - tail[0] == 0: # No horizontal change, it's moved vertically
            tail[1] = tail[1] + (1 if head[1] - tail[1] > 0 else -1)
        elif head[1] - tail[1] == 0:
            tail[0] = tail[0] + (1 if head[0] - tail[0] > 0 else -1)
        else: # Diagonal move
            tail[0], tail[1] = tail[0] + (1 if head[1] - tail[1] > 0 else -1), tail[1] + (1 if head[0] - tail[0] > 0 else -1)
    
    if(chainIndex == len(knotChain) - 2): # At 2nd to last element, add the tail end to positions
        previousTailCoords.append((tail[0], tail[1]))
    else:
        checkTail(previousTailCoords, knotChain, chainIndex+1)

def performMoves(length=2):
    previousTailCoords = []
    knotChain = [[0, 0] for i in range(length)]

    for line in fileLines:
        command = line.split()
        for i in range(int(command[1])):
            knotChain[0][0] += 1 if command[0] == "R" else -1 if command[0] == "L" else 0
            knotChain[0][1] += 1 if command[0] == "U" else -1 if command[0] == "D" else 0

            checkTail(previousTailCoords, knotChain)

    previousTailCoords.sort()
    print(len(list(previousTailCoords for previousTailCoords,_ in itertools.groupby(previousTailCoords))))

performMoves()

performMoves(10)