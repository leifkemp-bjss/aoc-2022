file = open("input.txt", "r")
line = file.readline()

def findMarker(length):
    index = 0
    endIndex = length
    foundSlice = False
    while index < len(line) - (length-1):
        slice = line[index:endIndex]
        if(len(slice) == len(set(slice))): # this is our marker
            foundSlice = True
            break
        index += 1
        endIndex += 1

    if foundSlice: return(endIndex)
    else: return -1

print(findMarker(4))
print(findMarker(14))