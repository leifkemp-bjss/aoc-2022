file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]

def overlaps(section):
    print(section)
    ass1, ass2 = section[0], section[1]
    range1, range2 = ass1[1] - ass1[0], ass2[1] - ass2[0]
    median1, median2 = (ass1[1] + ass1[0]) / 2, (ass2[1] + ass2[0]) / 2

    if(range1 > range2): # Range 1 is larger, check that assignment 2 doesn't exceed boundaries
        if(ass1[0] <= median2 - (range2 / 2) and median2 + (range2 / 2) <= ass1[1]):
            return True
    else:
        if(ass2[0] <= median1 - (range1 / 2) and median1 + (range1 / 2) <= ass2[1]):
            return True

    return False


overlappingSections = 0
for line in fileLines:
    sections = line.split(",")
    
    sectionsSplitUp = [[int(x) for x in section.split("-")] for section in sections]
    
    if(overlaps(sectionsSplitUp)):
        print(str(sections) + " is overlapping")
        overlappingSections += 1

print(overlappingSections)