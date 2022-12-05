file = open("input.txt", "r")

fileLines = [line.strip("\n") for line in file.readlines()]

emptyLine = fileLines.index("")
stackLines = fileLines[:emptyLine]
commands = fileLines[emptyLine+1:]
stacks = []

lastNum = eval(stackLines[len(stackLines)-1][-3:-1])
for i in range(lastNum):
    stacks.append([])


# Create the stacks
for i in range(1, len(stackLines)):
    currentLine = stackLines[len(stackLines)-1-i]
    # Start from the bottom of stackLines and build our way up, lets us build our list and then pop the top boxes
    if("[" in currentLine): # Line is made out of boxes, add them
        # Each character is split up by [] and whitespace, about 4 characters each
        for j in range((len(currentLine) // 4) + 1):
            boxContents = currentLine[j*4+1]
            if boxContents != " ": stacks[j].append(boxContents)

# Then apply the commands
for command in commands:
    splitCom = command.split()
    moveQuantity = eval(splitCom[1])
    fromStack = eval(splitCom[3])-1
    toStack = eval(splitCom[5])-1

    cratesToMove = []
    for i in range(moveQuantity):
        if(len(stacks[fromStack]) > 0):
            cratesToMove.append(stacks[fromStack].pop())
    cratesToMove.reverse() # Flip list to retain original order
    stacks[toStack].extend(cratesToMove)

# Now retrieve topmost items and join them
result = [stack[-1] for stack in stacks if len(stack) > 0]
print(''.join(result))