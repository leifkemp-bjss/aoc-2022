from itertools import groupby

file = open("input.txt", "r")
filelines = [line.strip("\n") for line in file.readlines()]

chunks = (list(g) for k,g in groupby(filelines, key=lambda x: x != '') if k)
chunksInt = [sum([int(i) for i in chunk]) for chunk in chunks]

print(max(chunksInt))
print(sorted(chunksInt)[-3:])