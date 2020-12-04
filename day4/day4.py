# Puzzle Link: https://adventofcode.com/2020/day/4

import re

inputfile = open("D:\coding\Advent of Code 2020\day4\day4input.txt", "r")
with inputfile as f:
    lines = f.read()
passports = lines.split("\n\n")
cleanedpassports = []
for p in passports:
    cleanedpassports.append(p.replace("\n", " "))
def day4(passportlist, optional):
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
            if re.findall(r"byr:", passport) != []:
                byrbool = True
        if "iyr" in passport:
            if re.findall(r"iyr:", passport)!= []:
                iyrbool = True
        if "eyr" in passport:
            if re.findall(r"eyr:", passport) != []:
                eyrbool = True
        if "hgt" in passport:
            if re.findall(r"hgt:", passport) != []:
                hgtbool = True
        if "hcl" in passport:
            if re.findall(r"hcl:", passport) != []:
                hclbool = True
        if "ecl" in passport:
            if re.findall(r"ecl:", passport) != []:
                eclbool = True
        if "pid" in passport:
            if re.findall(r"pid:", passport) != []:
                pidbool = True
        if byrbool == True and iyrbool == True and eyrbool == True and hgtbool == True and hclbool == True and eclbool == True and pidbool == True:
            goodpassportcount += 1
    return goodpassportcount
print(day4(cleanedpassports, True))