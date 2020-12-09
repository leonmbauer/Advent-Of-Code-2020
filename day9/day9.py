# Puzzle link: https://adventofcode.com/2020/day/7

inputfile = open("D:\coding\Advent of Code 2020\day9\day9input.txt", "r")
lines = inputfile.readlines()
rules = []
added = []
for value in lines:
    rules.append(int(value.strip("\n")))

def day9(numlist):
    for num in numlist:
        index = numlist.index(num)
        if numlist.index(num) >= 25:
            preamble = []
            added = []
            for i in range(index - 25, index):
                preamble.append(numlist[i])
            for x in preamble:
                for y in preamble:
                    if (x + y) not in added:
                        added.append(x + y)
            if num not in added:
                return num
    index += 1


badnum = day9(rules)


def part2helper(numlist, badnum):
    for num in numlist:
        index = numlist.index(num)
        i = index
        numbers = []
        numbers.append(num)
        while sum(numbers) < badnum:
            numbers.append(numlist[i+1])
            i += 1
        if sum(numbers) == badnum:
            return min(numbers) + max(numbers)
        
print(part2helper(rules, badnum))