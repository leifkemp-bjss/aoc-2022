# I dislike this solution even more but it's pretty funny
file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]

# Structure for each subarray: Lose, Draw, Win
veryBadList = [["Z", "X", "Y"], ["X", "Y", "Z"], ["Y", "Z", "X"]]

scoreStep1 = 0
scoreStep2 = 0

for line in fileLines:
    inputA,inputB = line.split()[0], line.split()[1]
    scoreStep1 += veryBadList[ord(inputA) - 65].index(inputB) * 3 + ord(inputB) - 87
    scoreStep2 += (3 * (ord(inputB) - 88)) + ord(veryBadList[ord(inputA) - 65][ord(inputB) - 88]) - 87

print(scoreStep1)
print(scoreStep2)