file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]

def buildStack():
    stack = []
    for line in fileLines:
        command = line.split()
        #print(command)
        if(command[0] == "addx"):
            stack.append("")
            stack.append(int(command[1]))
        else:
            stack.append("")

    return stack

def p1(lines):
    X = 1
    stack = buildStack()
    xValues = []

    for index in range(max(lines)):
        if(index + 1 in lines):
            xValues.append(X)

        if(len(stack) > 0):
            stackHead = stack[0]
            if(isinstance(stackHead, int)):
                X += stackHead
                #print(f"X is now {X}")
            stack = stack[1:]

    return [x*y for x, y in zip(lines, xValues)]

def p2():
    X = 0
    pixelPos = 0
    stack = buildStack()
    pixels = ""
    pixelLines = []
    for i in stack:
        if(X <= pixelPos < X+3):
            pixels += "#"
        else:
            pixels += "."

        stackHead = stack[0]
        if(isinstance(stackHead, int)):
            X += stackHead
            
        stack = stack[1:]
        pixelPos += 1
        if(pixelPos % 40 == 0 and pixelPos != 0):
            pixelLines.append([pixels[0:]])
            pixels = ""
            pixelPos = 0

    for line in pixelLines:
        print(line)
#print(f"{solve([20, 60, 100, 140, 180, 220])}")
print(sum(p1([20, 60, 100, 140, 180, 220])))
print(p2())
