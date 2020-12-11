# Puzzle link: https://adventofcode.com/2020/day/11

inputfile = open("D:\coding\Advent of Code 2020\day11\day11input.txt", "r")
lines = inputfile.readlines()
seatmap = []
for value in lines:
    seatmap.append(value.strip("\n"))


def day11(seatmap):
    changemap = []
    finalcount = 0
    rowindex = 0
    for row in seatmap:
        newrow = ""
        firstrow = False
        lastrow = False
        if rowindex == 0:
            firstrow = True
        elif rowindex == len(seatmap) - 1:
            lastrow = True
        
        seatindex = 0
        for seat in row:
            lct = 0
            rct = 0
            uct = 0
            dct = 0
            tlct = 0
            trct = 0
            blct = 0
            brct = 0
            up = []
            down = []
            left = []
            right = []
            topleft = []
            topright = []
            botleft = []
            botright = []    
            for r in range(0, seatindex):
                left.append(row[r])
            for i in reversed(left):
                if i == "L":
                    lct = 0
                    break
                elif i == "#":
                    lct = 1
                    break
            for r in range(seatindex + 1,len(row)):
                right.append(row[r])
            for i in right:
                if i == "L":
                    rct = 0
                    break
                elif i == "#":
                    rct = 1
                    break
            for r in range(0, rowindex):
                up.append(seatmap[r][seatindex])
            for i in reversed(up):
                if i == "L":
                    uct = 0
                    break
                elif i == "#":
                    uct = 1
                    break
            for r in range(rowindex + 1, len(seatmap)):
                down.append(seatmap[r][seatindex])
            for i in down:
                if i == "L":
                    dct = 0
                    break
                elif i == "#":
                    dct = 1
                    break

            y = 1
            x = 1
            a = 1
            b = 1
            while seatindex - y >= 0 and rowindex - y >= 0:
                topleft.append(seatmap[rowindex - y][seatindex - y])
                y += 1
            for i in topleft:
                if i == "L":
                    tlct = 0
                    break
                elif i == "#":
                    tlct = 1
                    break
            while seatindex + x <= len(row) - 1 and rowindex - x >= 0:
                topright.append(seatmap[rowindex - x][seatindex + x])
                x += 1
            for i in topright:
                if i == "L":
                    trct = 0
                    break
                elif i == "#":
                    trct = 1
                    break
            while seatindex - a >= 0 and rowindex + a <= len(seatmap) - 1:
                botleft.append(seatmap[rowindex + a][seatindex - a])
                a += 1
            for i in botleft:
                if i == "L":
                    blct = 0
                    break
                elif i == "#":
                    blct = 1
                    break
            while seatindex + b <= len(row) - 1 and rowindex + b <= len(seatmap) - 1:
                botright.append(seatmap[rowindex + b][seatindex + b])
                b += 1
            for i in botright:
                if i == "L":
                    brct = 0
                    break
                elif i == "#":
                    brct = 1
                    break

            around = uct + dct + lct + rct + tlct + trct + blct + brct

            if seat == "L":
                if around == 0:
                    newrow += "#"
                else:
                    newrow += "L"
            elif seat == "#":
                if around >= 5:
                    newrow += "L"
                else:
                    newrow += "#"
            elif seat == ".":
                newrow += "."
            seatindex += 1
        rowindex += 1
            
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