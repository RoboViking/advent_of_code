safeRanges = []

def insertRanges(line):
    global safeRanges
    startOfRange = line.split("-")[0]
    endOfRange = line.split("-")[1]

    if len(safeRanges) == 0:
        safeRanges.append((int(startOfRange), int(endOfRange)))  
    else:
        newStart = int(startOfRange)
        newEnd = int(endOfRange)
        merged = False

        for i in range(len(safeRanges)):
            rangeStart, rangeEnd = safeRanges[i]
            if newEnd >= rangeStart and newEnd <= rangeEnd:
                safeRanges[i] = (newStart, rangeEnd)
                merged = True
                break
            elif newStart <= rangeEnd and newStart >= rangeStart:
                safeRanges[i] = (rangeStart, newEnd)
                merged = True
            
        if not merged:
            safeRanges.append((newStart, newEnd))
    

def main():

    with open("day_5/test_input.txt", "r") as file:
        for line in file:
            if not line.strip():
                break
            line = line.strip()
            insertRanges(line)
    
    for rangeStart, rangeEnd in safeRanges:
        print("Range:", rangeStart, "-", rangeEnd)
    print("Fresh ids:", len(safeRanges))

if __name__ == "__main__":
    main()