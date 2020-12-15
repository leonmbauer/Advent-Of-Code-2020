# Puzzle link: https://adventofcode.com/2020/day/14

inputfile = open("D:\coding\Advent of Code 2020\day14\day14input.txt", "r")
lines = inputfile.readlines()
endlines = []
for value in lines:
    endlines.append(value.strip("\n"))

memdict = {}
keys = memdict.keys()

def day14(commands):
    binary = ""
    finalanswer = 0
    for command in commands:
        if command.split("=")[0].rstrip() == "mask":
            mask = command.split("=")[1].lstrip()
        elif command.split("[")[0] == "mem":
            address = int(command.split("[")[1].split("]")[0])
            memdict[address] = command.split("=")[1].lstrip()
            binary = str(bin(int(command.split("=")[1].lstrip()))[2:])
            while len(binary) < 36:
                binary = "0" + binary
            index = 0
            finalbin = ""
            for i in mask:
                if i == "1":
                    finalbin += "1"
                elif i == "X":
                    finalbin += binary[index]
                elif i == "0":
                    finalbin += "0"
                index += 1
            memdict[address] = finalbin
    for x in memdict:
        finalanswer += int(memdict[x], 2)
    return finalanswer
print(day14(endlines))