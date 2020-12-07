# Puzzle link: https://adventofcode.com/2020/day/7

inputfile = open("D:\coding\Advent of Code 2020\day7\day7input.txt", "r")
lines = inputfile.readlines()
rules = []
totalbags = []
for value in lines:
    rules.append(value.strip("\n"))


def day7(rules, color):
    acceptsbag = []
    splitrule = ""
    for rule in rules:
        splitrule = rule.split("bags")[1:]
        for split in splitrule:
            if color in split:
                if rule.split("bags")[0].rstrip(" ") not in acceptsbag:
                    acceptsbag.append(rule.split("bags")[0].rstrip(" "))
    for bag in acceptsbag:
        totalbags.append(bag)
        day7(rules, bag)
    
day7(rules, "shiny gold")
print(len(set(totalbags)))