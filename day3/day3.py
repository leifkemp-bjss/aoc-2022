file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]

commonChars = []

for line in fileLines:
    #"A" starts at ASCII 65, "a" starts at ASCII 97
    commonChars += set([ord(x) for x in line[:len(line) // 2] if x in line[len(line) // 2:]])

sortedChars = [x - 38 if 65 <= x < 91 else x - 96 for x in commonChars]

print(sortedChars)
print(sum(sortedChars))