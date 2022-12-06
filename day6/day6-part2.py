file = open("input.txt", "r")
line = file.readline()

index = 0
endIndex = 14
foundSlice = False
while index < len(line) - 13:
    slice = line[index:endIndex]
    print(slice)
    if(len(slice) == len(set(slice))): # this is our marker
        foundSlice = True
        break
    index += 1
    endIndex += 1

if foundSlice: print(endIndex)