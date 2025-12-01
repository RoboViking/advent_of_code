import math
start = 50
end = start
zero_cross_count = 0
"""
def spin(direction, distance):
    global start, end
    
    if direction == "R":
        newPosition = end + distance
    elif direction == "L":
        newPosition = end - distance
    finalPosition = newPosition % 100
    end = finalPosition

    print(f"Spun {direction}{distance}: from {start} to {end}")
    
"""
def spin(direction, distance):
    global end, zero_cross_count

    step = 1 if direction == "R" else -1

    for _ in range(distance):
        end += step
        if end >= 100:
            end = 0
            zero_cross_count += 1
        elif end < 0:
            end = 99
            zero_cross_count += 1

    print(f"Spun {direction}{distance}: now at {end}, zero crosses so far: {zero_cross_count}")


def main():
    startPosition = int(50)
    currentPosition = startPosition
    password = int(0)
    with open("day_1/input.txt", "r") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])
            
            spin(direction, distance)

if __name__ == "__main__":
    main()