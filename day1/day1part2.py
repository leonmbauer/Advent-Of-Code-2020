# Puzzle: https://adventofcode.com/2020/day/1

inputfile = open("D:\coding\Advent of Code 2020\day1\day1input.txt", "r")
numlist = []
lines = inputfile.readlines()
endlines = []
for value in lines:
    endlines.append(int(value.strip("\n")))

def day1(numbers):
    answer = 0
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if (i + j + k) == 2020:
                    answer = i * j * k
    return answer

print(day1(endlines))