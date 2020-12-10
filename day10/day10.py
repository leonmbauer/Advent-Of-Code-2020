# Puzzle link: https://adventofcode.com/2020/day/10

inputfile = open("D:\coding\Advent of Code 2020\day10\day10input.txt", "r")
lines = inputfile.readlines()
voltages = []

for value in lines:
    voltages.append(int(value.strip("\n")))
voltages.sort()
voltages.append(max(voltages) + 3)
finalvoltages = [0] + voltages

def day10(voltages):
    onediff = 0
    threediff = 0
    for voltage in voltages:
        index = voltages.index(voltage)
        if index < len(voltages) - 1:
            if voltages[index + 1] - voltage == 1:
                onediff += 1
            elif voltages[index + 1] - voltage == 3:
                threediff += 1
    return onediff * threediff
print(day10(finalvoltages))