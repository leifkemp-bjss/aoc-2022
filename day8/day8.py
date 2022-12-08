file = open("input.txt", "r")
fileLines = [[int(x) for x in line.strip("$\n")] for line in file.readlines()]
#visibleTrees = fileLines.copy()
#print(fileLines)

# Search from the left and right first
for line in fileLines:
    maxHeightLeft, maxHeightRight = -1, -1
    for index in range(len(line)):
        if(line[index] % 10 > maxHeightLeft):
            maxHeightLeft = line[index] % 10
            if(line[index] // 10 < 1):
                line[index] += 10 # Mark a tree as visible by adding 10 to it, as they range from 0 to 9

        if(line[len(line) - (index+1)] % 10 > maxHeightRight):
            maxHeightRight = line[len(line) - (index+1)] % 10
            if(line[len(line) - (index+1)] // 10 < 1):
                line[len(line) - (index+1)] += 10 # Mark a tree as visible by adding 10 to it, as they range from 0 to 9

# Then top and bottom
for width in range(len(fileLines[0])):
    maxHeightTop, maxHeightBottom = -1, -1
    
    for height in range(len(fileLines)):
        if(fileLines[height][width] % 10 > maxHeightTop):
            maxHeightTop = fileLines[height][width] % 10
            if(fileLines[height][width] // 10 < 1):
                fileLines[height][width] += 10 # Mark a tree as visible by adding 10 to it, as they range from 0 to 9

        if(fileLines[len(fileLines) - height - 1][width] % 10 > maxHeightBottom):
            maxHeightBottom = fileLines[len(fileLines) - height - 1][width] % 10
            if(fileLines[len(fileLines) - height - 1][width] // 10 < 1):
                fileLines[len(fileLines) - height - 1][width] += 10 # Mark a tree as visible by adding 10 to it, as they range from 0 to 9

print(fileLines[0])
print(len([int(x) for line in fileLines for x in line if x // 10 > 0]))