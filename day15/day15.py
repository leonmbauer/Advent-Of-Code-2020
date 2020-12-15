# Puzzle link: https://adventofcode.com/2020/day/15

numdict = {}
keys = numdict.keys()

def day15(startnums, turns):
    spoken = startnums
    turn = 1
    x = len(spoken)
    for i in spoken:
        numdict[i] = [1, turn, turn]
        turn += 1
    
    while x < turns:
        lastnum = spoken[-1]
        
        if numdict[lastnum][0] == 1:
            if 0 in keys:
                numdict[0] = [numdict[0][0] + 1, numdict[0][2], turn]
                spoken.append(0)
            else:
                numdict[0] = [1, turn, turn]
        elif numdict[lastnum][0] > 1:
            newnum = numdict[lastnum][2] - numdict[lastnum][1]
            spoken.append(newnum)
            if newnum not in keys:
                numdict[newnum] = [1, turn, turn]
            else:
                numdict[newnum] = [numdict[newnum][0] + 1, numdict[newnum][2], turn]
        turn += 1
        x += 1
    return spoken[-1]
print(day15([0,8,15,2,12,1,4], 2020))

# For part 2 run the following line. I suggest running it in Google Colab with GPU acceleration or it will take very long to run
# print(day15([0,8,15,2,12,1,4], 30000000))