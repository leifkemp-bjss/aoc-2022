file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]
print(fileLines)

elvesCondensed = []
currentVal = 0
for value in fileLines:
    if value != '':
        currentVal += int(value)
    else:
        elvesCondensed.append(currentVal)
        currentVal = 0

print(max(elvesCondensed))
print(sorted(elvesCondensed)[-3:])
print(sum(sorted(elvesCondensed)[-3:]))