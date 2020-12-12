# Puzzle link: https://adventofcode.com/2020/day/12

inputfile = open("D:\coding\Advent of Code 2020\day12\day12input.txt", "r")
lines = inputfile.readlines()
directions = []
for value in lines:
    directions.append(value.strip("\n"))

def day12(directions):
    angle = 0
    x = 0
    y = 0
    for direction in directions:
        if direction[0] == "N":
            y += int(direction[1:])
        elif direction[0] == "S":
            y -= int(direction[1:])
        elif direction[0] == "E":
            x += int(direction[1:])
        elif direction[0] == "W":
            x -= int(direction[1:])
        elif direction[0] == "L":
            angle += int(direction[1:])
        elif direction[0] == "R":
            angle -= int(direction[1:])
        elif direction[0] == "F":
            a = angle
            if a >= 360:
                a = a % 360
            if a < 0:
                a = abs(a)
                if a >= 360:
                    a = a % 360
                    a = 360 - a
                else:
                    a = 360 - a
            if a == 0 or a == 360:
                x += int(direction[1:])
            elif a == 90:
                y += int(direction[1:])
            elif a == 180:
                x -= int(direction[1:])
            elif a == 270:
                y -= int(direction[1:])
        print(x,y)
        print(angle)
    return abs(x) + abs(y)


print(day12(directions))