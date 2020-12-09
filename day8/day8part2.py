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



def day8(instructions):
    i = 0
    while i < len(instructions):
        if instructions[i].split(" ")[0] == "nop":
        i += 1
    instructdict[i] += 1

print(day8(instructions))