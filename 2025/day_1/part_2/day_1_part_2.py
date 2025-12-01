import math
start = 50
dialSize = 100
dialPos = start
password = 0
rev = 0

def spin(direction, distance):
    global dialPos, password, dialSize

    if direction == "R":
        for _ in range(distance):
            dialPos += 1
            if dialPos >= dialSize:
                dialPos = 0
                password += 1

    elif direction == "L":
        for _ in range(distance):
            dialPos -= 1
            if dialPos < 0:
                dialPos = 99
            
            if dialPos == 0:
                password += 1
            
    print(f"Spun {direction}{distance}: now at {dialPos}, password: {password}")

def main():
    with open("day_1/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])
            
            spin(direction, distance)

if __name__ == "__main__":
    main()