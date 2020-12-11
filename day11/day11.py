# Puzzle link: https://adventofcode.com/2020/day/11

inputfile = open("D:\coding\Advent of Code 2020\day11\day11input.txt", "r")
lines = inputfile.readlines()
seatmap = []
for value in lines:
    seatmap.append(value.strip("\n"))


def day11(seatmap):
    changemap = []
    finalcount = 0
    for row in seatmap:
        newrow = ""
        firstrow = False
        lastrow = False
        rowindex = seatmap.index(row)
        if rowindex == 0:
            firstrow = True
        elif rowindex == len(seatmap) - 1:
            lastrow = True
        
        seatindex = 0
        for seat in row:
            if seatindex == 0:
                if firstrow == True:
                    adjacent = row[seatindex + 1] + seatmap[rowindex + 1][seatindex] + seatmap[rowindex + 1][seatindex + 1]
                elif lastrow == True:
                    adjacent = seatmap[rowindex - 1][seatindex] + seatmap[rowindex - 1][seatindex + 1] + row[seatindex + 1]
                else:
                    adjacent = seatmap[rowindex - 1][seatindex] + seatmap[rowindex - 1][seatindex + 1] + row[seatindex + 1] + seatmap[rowindex + 1][seatindex] + seatmap[rowindex + 1][seatindex + 1]
            elif seatindex == len(row) - 1:
                if firstrow == True:
                    adjacent = row[seatindex - 1] + seatmap[rowindex + 1][seatindex - 1] + seatmap[rowindex + 1][seatindex]
                elif lastrow == True:
                    adjacent = seatmap[rowindex - 1][seatindex] + seatmap[rowindex - 1][seatindex - 1] + row[seatindex - 1]
                else:
                    adjacent = seatmap[rowindex - 1][seatindex] + seatmap[rowindex - 1][seatindex - 1] + row[seatindex - 1] + seatmap[rowindex + 1][seatindex] + seatmap[rowindex + 1][seatindex - 1]
            elif firstrow == True:
                adjacent = row[seatindex - 1] + row[seatindex + 1] + seatmap[rowindex + 1][seatindex - 1] + seatmap[rowindex + 1][seatindex] + seatmap[rowindex + 1][seatindex + 1]
            elif lastrow == True:
                adjacent = seatmap[rowindex - 1][seatindex - 1] + seatmap[rowindex - 1][seatindex] + seatmap[rowindex - 1][seatindex + 1] + row[seatindex - 1] + row[seatindex + 1]
            else:
                adjacent = seatmap[rowindex - 1][seatindex - 1] + seatmap[rowindex - 1][seatindex] + seatmap[rowindex - 1][seatindex + 1] + row[seatindex - 1] + row[seatindex + 1] + seatmap[rowindex + 1][seatindex - 1] + seatmap[rowindex + 1][seatindex] + seatmap[rowindex + 1][seatindex + 1]

            if seat == "L":
                occupiedcount = 0
                for letter in adjacent:
                    if letter == "#":
                        occupiedcount += 1
                if occupiedcount == 0:
                    newrow += "#"
                else:
                    newrow += "L"
            elif seat == "#":
                ocount = 0
                for letter in adjacent:
                    if letter == "#":
                        ocount += 1
                if ocount >= 4:
                    newrow += "L"
                else:
                    newrow += "#"
            elif seat == ".":
                newrow += "."
            seatindex += 1
        changemap.append(newrow)
    if changemap == seatmap:
        for r in changemap:
            for s in r:
                if s == "#":
                    finalcount += 1
        return finalcount
    else:
        return day11(changemap)

print(day11(seatmap))