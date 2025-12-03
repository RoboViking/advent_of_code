def findLargestNumber(numbers):
    largestNum = ""
    numberList = list(numbers)
    firstNum = numberList[0]
    firstNumPosition = 0

    for i in range((len(numberList)-1)):
        if numberList[i] > firstNum:
            firstNum = numberList[i]
            firstNumPosition = i
    
    j = firstNumPosition + 1
    secondNum = numberList[j]

    for k in range(j, len(numberList)):
        if numberList[k] > secondNum:
            secondNum = numberList[k]

    largestNum += firstNum + secondNum  
        
    print(largestNum)
    return int(largestNum)

def main():
    with open("day_3/input.txt", "r") as file:
        password = 0
        for line in file:
            line = line.strip()
            password += findLargestNumber(line)
        
        print("Password:", password)

if __name__ == "__main__":
    main()