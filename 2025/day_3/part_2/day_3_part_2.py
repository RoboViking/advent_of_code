def findLargestNumber(numbers):
    numberList = list(numbers) #the input string of numbers
    resultList = []
    resultListString = "" 
    amountOfNumbers = 12 #lenth of the result number
    
    currentNum = "" #the current largest number we are looking at
    currentNumPosition = 0 #the position of the current largest number
    
    i = 0 
    while i < amountOfNumbers:
        for j in range(len(numberList)):
            if(j <= (len(numberList) - amountOfNumbers + len(resultList)) and j >= currentNumPosition):
                if numberList[j] > currentNum:
                    currentNum = numberList[j]
                    currentNumPosition = j    
        
        currentNum = numberList[currentNumPosition]
        resultList.insert(i, currentNum)
        
        currentNumPosition += 1 
        i += 1

    for num in resultList:
        resultListString += num
    
    print(resultListString)
    return int(resultListString)

def main():
    with open("day_3/test_input.txt", "r") as file:
        password = 0
        for line in file:
            line = line.strip()
            password += findLargestNumber(line)
        
        print("Password:", password)

if __name__ == "__main__":
    main()