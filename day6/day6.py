# Puzzle Link: https://adventofcode.com/2020/day/6

from collections import Counter

inputfile = open("D:\coding\Advent of Code 2020\day6\day6input.txt", "r")
with inputfile as f:
    lines = f.read()
forms = lines.split("\n\n")

cleanedforms = []
for p in forms:
    cleanedforms.append(p.split("\n"))

def day6(formlist):
    lettercount = 0
    for group in formlist:
        chardict = {}
        for person in group:
            for letter in person:
                keys = chardict.keys()
                if letter in keys:
                    chardict[letter] += 1
                else:
                    chardict[letter] = 1
        for letter in chardict:
            lettercount += 1
    return lettercount

print(day6(cleanedforms))

