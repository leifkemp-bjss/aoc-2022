values = ["A", "B", "C"]
scores = [1, 2, 3]

file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]
print(fileLines)

score = 0

for line in fileLines:
    inputA, outcome = line.split()[0], line.split()[1]
    if outcome == "X": # Loss
        score += scores[(values.index(inputA) - 1) % 3]
    elif outcome == "Y": # Draw
        score += 3
        score += scores[values.index(inputA)]
    elif outcome == "Z": # Win
        score += 6
        score += scores[(values.index(inputA) - 2) % 3]

print(score)