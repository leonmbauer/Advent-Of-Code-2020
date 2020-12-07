# Puzzle link: https://adventofcode.com/2020/day/7

inputfile = open("D:\coding\Advent of Code 2020\day7\day7input.txt", "r")
lines = inputfile.readlines()
rules = []
bags = []
totalbags = []
totalbagct = []
finalanswer = 1
multiplier = 1
for value in lines:
    rules.append(value.strip("\n"))
for value in lines:
    if value.strip("\n").split("bags")[0].rstrip(" ") not in bags:
        bags.append(value.strip("\n").split("bags")[0].rstrip(" "))
ints = []
ruledict = {}
keys = ruledict.keys()
def day7(rules, color):
    nextbags = []
    counts = []
    countindex = 0
    tuples = []
    goodrules = []
    splitrules = []
    for rule in rules:
        if rule.split("bags")[0].rstrip(" ") == color:
            goodrules.append(rule)
    for rule in goodrules:
        splitrule = rule.split("bags")[1:]
        for split in splitrule:
            splitrules.append(split)
            for char in split:
                try:
                    counts.append(int(char))
                except ValueError:
                    continue
            for bag in bags:
                if bag in split:
                    nextbags.append(bag)
                    tuples.append((bag, counts[countindex]))
                    countindex += 1
    if color not in keys:
        ruledict[color] = tuples
    for bag in nextbags:
        totalbags.append(bag)
        day7(rules, bag)
testrules = ["shiny gold bags contain 2 dark red bags.", "dark red bags contain 2 dark orange bags.", "dark orange bags contain 2 dark yellow bags.", "dark yellow bags contain 2 dark green bags.", "dark green bags contain 2 dark blue bags.", "dark blue bags contain 2 dark violet bags.", "dark violet bags contain no other bags."]
day7(rules, "shiny gold")

# for rule in ruledict:
#     for bag in ruledict[rule]:
#         multiplier *= bag[1]

print(ruledict)

