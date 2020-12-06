# Puzzle Link: https://adventofcode.com/2020/day/3

import math

inputfile = open("D:\coding\Advent of Code 2020\day3\day3input.txt", "r")
lines = inputfile.readlines()
multiplier = 0
slopemap = []

for value in lines:
    slopemap.append(value.strip("\n"))

height = len(slopemap)

def day3(map, down, across):
    requiredwidth = 0
    multiplier = 0
    treecount = 0
    rightindex = 0
    downindex = 0
    extendedmap = []
    requiredwidth = across * height
    multiplier = math.ceil(requiredwidth / len(slopemap[0]))
    for line in map:
        extendedmap.append(line * multiplier)

    for line in extendedmap:
        if downindex != len(extendedmap) - 1:
            if extendedmap[downindex + down][rightindex + across] == "#":
                rightindex += across
                downindex += down
                treecount += 1
            else:
                rightindex += across
                downindex += down
    return treecount


print(day3(slopemap, 1, 1) * day3(slopemap, 1, 3) * day3(slopemap, 1, 5) * day3(slopemap, 1, 7) * day3(slopemap, 2, 1))