# Puzzle Link: https://adventofcode.com/2020/day/5

import math

inputfile = open("D:\coding\Advent of Code 2020\day5\day5input.txt", "r")
lines = inputfile.readlines()
ticketlist = []
for value in lines:
    ticketlist.append(value.strip("\n"))

ticketmaxlist = []
def day5(ticketlist):
    ticketmax = 0
    maxid = 0
    index = 0
    for ticket in ticketlist:
        top = 127
        bot = 0
        left = 0
        right = 7
        for letter in ticket:
            if letter == "F":
                top = bot + math.floor((top - bot) / 2)
            elif letter == "B":
                bot = top - math.floor((top - bot) / 2)
            elif letter == "L":
                right = left + math.floor((right - left) / 2)
            elif letter == "R":
                left = right - math.floor((right - left) / 2)
        ticketmax = (bot * 8) + left
        ticketmaxlist.append(ticketmax)
        if ticketmax > maxid:
            maxid = ticketmax
    ticketmaxlist.sort()
    for t in ticketmaxlist:
        if (ticketmaxlist[index + 1] - t) > 1:
            return "Seat ID: " + str(t + 1)
        index += 1
print(day5(ticketlist))