file = open("input.txt", "r")
line = file.readline()

index = 0
endIndex = 4
while index < len(line) - 3:
    slice = line[index:endIndex]
    print(slice)
    if(len(slice) == len(set(slice))): # this is our marker
        break
    index += 1
    endIndex += 1

print(endIndex)