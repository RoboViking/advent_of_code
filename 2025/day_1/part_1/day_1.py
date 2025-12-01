def main():
    startPosition = int(50)
    currentPosition = startPosition
    password = int(0)
    with open("day_1/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])
            
            if direction == "R":
                newPosition = currentPosition + distance
            else:
                newPosition = currentPosition - distance
                
            finalPosition = newPosition % 100
            currentPosition = finalPosition
            
            if currentPosition == 0:
                password +=1

    print(password)

if __name__ == "__main__":
    main()