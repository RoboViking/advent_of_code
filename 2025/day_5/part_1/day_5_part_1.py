safeRanges = set()

def insertRanges(line):
    global safeRanges
    startOfRange = line.split("-")[0]
    endOfRange = line.split("-")[1]
    #print("Start:", startOfRange, "End:", endOfRange)

    safeRanges.update(range(int(startOfRange), int(endOfRange)+1))

def main():
    nums = []
    with open("day_5/input.txt", "r") as file:
        for line in file:
            if not line.strip():
                break
            line = line.strip()
            insertRanges(line)
        
        for line in file:
            line = line.strip()
            nums.append(line)
    
    freshAmount = 0
    for num in nums:
        if int(num) not in safeRanges:
            print("Invalid number found:", num)
        else:
            freshAmount += 1
    
    print("Amount of valid numbers:", freshAmount)
    

if __name__ == "__main__":
    main()