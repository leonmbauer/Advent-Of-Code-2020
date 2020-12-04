# Puzzle Link: https://adventofcode.com/2020/day/4

import re

inputfile = open("D:\coding\Advent of Code 2020\day4\day4input.txt", "r")
with inputfile as f:
    lines = f.read()
passports = lines.split("\n\n")
cleanedpassports = []
passporttest = []
for p in passports:
    cleanedpassports.append(p.replace("\n", " "))
passportsplit = []
for passport in cleanedpassports:
    passportsplit.append(passport.split(" "))
def day4(passportsplit):
    goodpassportcount = 0
    for p in passportsplit:
        byrbool = False
        iyrbool = False
        eyrbool = False
        hgtbool = False
        hclbool = False
        eclbool = False
        pidbool = False
        for value in p:
            if "byr" in value:
                if len(value) == 8:
                    if int(value[-4:]) >= 1920 and int(value[-4:]) <= 2002:
                        byrbool = True
            if "iyr" in value:
                if len(value) == 8:
                    if int(value[-4:]) >= 2010 and int(value[-4:]) <= 2020:
                        iyrbool = True
            if "eyr" in value:
                if int(value[-4:]) >= 2020 and int(value[-4:]) <= 2030:
                        eyrbool = True
            if "hgt" in value:
                if value[-2:] == "cm":
                    if int(value.split(":")[1].rstrip("cm")) >= 150 and int(value.split(":")[1].rstrip("cm")) <= 193:
                        hgtbool = True
                elif value[-2:] == "in":
                    if int(value.split(":")[1].rstrip("in")) >= 59 and int(value.split(":")[1].rstrip("in")) <= 76:
                        hgtbool = True
            if "hcl" in value:
                if len(value) == 11 and value[4] == "#":
                    hclbool = True
            if "ecl" in value:
                if value.split(":")[1] == "amb" or value.split(":")[1] == "blu" or value.split(":")[1] == "brn" or value.split(":")[1] == "gry" or value.split(":")[1] == "grn" or value.split(":")[1] == "hzl" or value.split(":")[1] == "oth":
                    eclbool = True
            if "pid" in value:
                if len(value.split(":")[1]) == 9:
                    pidbool = True
        if byrbool == True and iyrbool == True and eyrbool == True and hgtbool == True and hclbool == True and eclbool == True and pidbool == True:
            goodpassportcount += 1
    return goodpassportcount
print(day4(passportsplit))