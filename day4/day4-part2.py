file = open("input.txt", "r")
fileLines = [line.strip("\n") for line in file.readlines()]

def overlaps(section):
    print(section)
    ass1, ass2 = section[0], section[1]

    # Join the assignments into a single list, if they don't overlap there should be no duplicate values
    sectionConcat = [x for x in range(ass1[0], ass1[1] + 1)] + [y for y in range(ass2[0], ass2[1] + 1)]
    if(len(sectionConcat) == len(set(sectionConcat))):
        return False

    return True


overlappingSections = 0
for line in fileLines:
    sections = line.split(",")
    sectionsSplitUp = [[int(x) for x in section.split("-")] for section in sections]
    if(overlaps(sectionsSplitUp)): overlappingSections += 1

print(overlappingSections)