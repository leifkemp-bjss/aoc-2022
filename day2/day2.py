# Don't like this solution
values = ["A", "B", "C", "X", "Y", "Z"]
drawingValues = ["X", "Y", "Z"]
winningValues = ["Y", "Z", "X"]
score = [1, 2, 3]

file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]
#print(fileLines)

scoring = 0
for line in fileLines:
    inputA,inputB = line.split()[0], line.split()[1]
    inputAindex = values.index(inputA)
    inputBindex = values.index(inputB) % 3

    losingIndex = (inputAindex + 1) % 3
    winningIndex = (inputAindex + 2) % 3

    if drawingValues[inputAindex] == inputB:
        scoring += 3
    elif winningValues[inputAindex] == inputB:
        scoring += 6
    

    scoring += score[inputBindex]

print(scoring)
    