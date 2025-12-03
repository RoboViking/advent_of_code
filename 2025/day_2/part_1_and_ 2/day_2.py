import re

password = 0

def patternFind(start, end):
    global password
    currentNum = str(start)
    while start <= end:
        if currentNum[0] != "0":
            #if re.search(r"^(.+)\1$", currentNum): #part 1
            if re.search(r"^(.+)\1+$", currentNum): #part 2
                password += int(currentNum)
                print(currentNum)

        start += 1
        currentNum = str(start)   

def main():
    with open("day_2/input.txt", "r") as file:
        input = file.readline()
        ranges = input.split(",")
        for r in ranges:
            start, end = r.split("-")
            patternFind(int(start), int(end))
    print("Password: "+ str(password))

if __name__ == "__main__":
    main()