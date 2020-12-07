# Puzzle link: https://adventofcode.com/2020/day/7

inputfile = open("D:\coding\Advent of Code 2020\day7\day7input.txt", "r")
lines = inputfile.readlines()
rules = []
bags = []
totalbags = []
totalbagct = []
finalanswer = 1
for value in lines:
    rules.append(value.strip("\n"))
for value in lines:
    if value.strip("\n").split("bags")[0].rstrip(" ") not in bags:
        bags.append(value.strip("\n").split("bags")[0].rstrip(" "))

def day7(rules, color):
    nextbags = []
    goodrules = []
    splitrule = ""
    for rule in rules:
        if rule.split("bags")[0].rstrip(" ") == color:
            goodrules.append(rule)
    for rule in goodrules:
        splitrule = rule.split("bags")[1:]
        for split in splitrule:
            for bag in bags:
                if bag in split:
                    nextbags.append(bag)
    print(color)
    print(nextbags)
    for bag in nextbags:
        totalbags.append(bag)
        day7(rules, bag)
day7(rules, "shiny gold")
print(totalbags)