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
def day4(passportlist):
    goodpassportcount = 0
    for passport in passportlist:
        byrbool = False
        iyrbool = False
        eyrbool = False
        hgtbool = False
        hclbool = False
        eclbool = False
        pidbool = False
        if "byr" in passport:
            if re.findall(r"byr:(19[2-9][0-9]|200[0-2])", passport) != []:
                byrbool = True
        if "iyr" in passport:
            if re.findall(r"iyr:20(1[0-9]|20)", passport) != []:
                iyrbool = True
        if "eyr" in passport:
            if re.findall(r"eyr:20(2[0-9]|30)", passport) != []:
                eyrbool = True
        if "hgt" in passport:
            if re.findall(r"hgt:1([5-8][0-9]|9[0-3])cm", passport) != [] or re.findall(r"hgt:(59|6[0-9]|7[0-6])in", passport) != []:
                hgtbool = True
        if "hcl" in passport:
            if re.findall(r"hcl:#[0-9|a-f][0-9|a-f][0-9|a-f][0-9|a-f][0-9|a-f][0-9|a-f]", passport) != []:
                hclbool = True
        if "ecl" in passport:
            if re.findall(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) != []:
                eclbool = True
        if "pid" in passport:
            if re.findall(r"pid:[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", passport) != []:
                pidbool = True
        if byrbool == True and iyrbool == True and eyrbool == True and hgtbool == True and hclbool == True and eclbool == True and pidbool == True:
            passporttest.append(passport)
            goodpassportcount += 1
    return goodpassportcount
print(day4(cleanedpassports))