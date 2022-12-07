file = open("input.txt", "r")
fileLines = [line.strip("$\n") for line in file.readlines()]
#print(fileLines)

structure = ["/"]
path = []
validSmallDirectores = []
smallSizes = []
directoriesAndSizes = []

def findDir(structure, target):
    currentStruct = structure
    for step in target:
        for directory in currentStruct:
            if(isinstance(directory, list) and directory[0] == step):
                currentStruct = directory
                break

    return currentStruct

def getDirectorySize(structure):
    size = 0
    
    for dir in structure:
        if(isinstance(dir, list)):
            size += getDirectorySize(dir)
        elif(isinstance(dir, int)):
            size += dir
    if(size <= 100000):
        validSmallDirectores.append(structure[0])
        smallSizes.append(size)

    directoriesAndSizes.append([structure[0], size])

    return size

# Build the directory
for line in fileLines:
    command = line.split()
    
    directory = findDir(structure, path)
    if(command[0] == "dir"):
        directory.append([command[1]])
    elif(command[0] == "cd"):
        if(command[1] != ".." and command[1] != "/"): path.append(command[1])
        elif(command[1] == ".."): path = path[:-1]
        else: path = []
    elif(command[0].isdigit()):
        foundInt = False
        for i in range(len(directory)):
            if(isinstance(directory[i], int)):
                foundInt = True
                directory[i] += int(command[0])
                break
        if(not foundInt): directory.append(int(command[0]))

print(getDirectorySize(structure))
print(sum(smallSizes))

dirSize = getDirectorySize(structure)
size = 70000000
req = 30000000
sizeNeeded = req - (size - dirSize)
print(sizeNeeded)

minimumEligible = [None, -1]
for directory in directoriesAndSizes:
    if(directory[1] >= sizeNeeded):
        if(directory[1] < minimumEligible[1] or minimumEligible[1] == -1):
            minimumEligible = directory

print(minimumEligible)