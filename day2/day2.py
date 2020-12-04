# Puzzle: https://adventofcode.com/2020/day/2

inputfile = open("D:\coding\Advent of Code 2020\day2\day2input.txt", "r")
lines = inputfile.readlines()
endlines = []
ranges = []
split = []
startnum = 0
endnum = 0
endpart = ""
colonindex = 0
desiredletter = ""
numrange = []
password = ""


def day2(inputtext):
    goodpasswordcount = 0
    # Create a list with all of the lines from the .txt file
    for value in lines:
        endlines.append(value.strip("\n"))


    for combo in endlines:
        count = 0
        # Split each line by the dash to get the desired range of numbers
        split = combo.split("-")
        startnum = int(split[0])
        endpart = split[1].rstrip()
        endnum = int(endpart.split(" ")[0])

        # Get the desired letter by using indices
        for character in combo:
            if character == ":":
                colonindex = combo.index(character)
        desiredletter = combo[colonindex - 1]

        # Make a list with all numbers in the desired range   
        numrange = list(range(startnum, endnum + 1))
        password = combo.split(":")[1].lstrip()

        # Find the number of occurences of the desired letter in the password and check if its in the desired range
        for letter in password:
            if letter == desiredletter:
                count += 1
        if count in numrange:
            goodpasswordcount += 1
    return goodpasswordcount

print(day2(lines))