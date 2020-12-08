# Puzzle link: https://adventofcode.com/2020/day/8

inputfile = open("D:\coding\Advent of Code 2020\day8\day8input.txt", "r")
lines = inputfile.readlines()
instructionsplit = []
instructions = []
for value in lines:
    instructions.append(value.strip("\n"))
    instructionsplit.append(value.strip("\n").split(" "))
instructdict = {}
keys = instructdict.keys()
for i in range(0,len(instructions)):
    instructdict[i] = 0

def day8(instructions, index, accumulator):
    i = index
    a = accumulator
    instructdict[i] += 1
    if instructdict[i] > 1:
        return  "a: ", a
    else:
        if instructions[i][0] == "acc":
            a += int(instructions[i][1])
        elif instructions[i][0] == "jmp":
            i += (int(instructions[i][1]) - 1)
    i += 1
    return day8(instructions, i, a)
print(day8(instructionsplit, 0, 0))