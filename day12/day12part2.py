# Puzzle link: https://adventofcode.com/2020/day/12

inputfile = open("D:\coding\Advent of Code 2020\day12\day12input.txt", "r")
lines = inputfile.readlines()
directions = []
for value in lines:
    directions.append(value.strip("\n"))

def day12(directions):
    x = 0
    y = 0
    wx = 10
    wy = 1
    for direction in directions:
        print(direction)
        if direction[0] == "N":
            wy += int(direction[1:])
        elif direction[0] == "S":
            wy -= int(direction[1:])
        elif direction[0] == "E":
            wx += int(direction[1:])
        elif direction[0] == "W":
            wx -= int(direction[1:])
        elif direction[0] == "F":
            x += wx * int(direction[1:])
            y += wy * int(direction[1:])
        
        xdiff = wx
        ydiff = wy
        if direction[0] == "R":
            if int(direction[1:]) % 360 == 90:
                wx = ydiff
                wy = -1 * xdiff
            elif int(direction[1:])% 360 == 180:
                wx = -1 * xdiff
                wy = -1 * ydiff
            elif int(direction[1:]) % 360 == 270:
                wx = -1 * ydiff
                wy = xdiff
            
        elif direction[0] == "L":
            if int(direction[1:]) % 360 == 90:
                wx = -1 * ydiff
                wy = xdiff
            elif int(direction[1:]) % 360 == 180:
                wx = -1 * xdiff
                wy = -1 * ydiff
            elif int(direction[1:]) % 360 == 270:
                wx = ydiff
                wy = -1 * xdiff
        print("waypoint: ", wx, wy)
        print("boat: ", x, y)
    return abs(x) + abs(y)


print(day12(directions))