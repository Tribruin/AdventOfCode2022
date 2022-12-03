#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from TerminalColors import *

testing = False

points = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 7, "Y": 2, "Z": 6}
}


def parse_input(code_input):
    result = code_input.split_lines(" ")
    return result


def part1(data_input):
    total_points = 0
    for x, y in data_input:
        total_points += points[x][y]
    print(total_points)


def part2(data_input):
    total_points = 0
    for x, y in data_input:
        scores = [x for x in points[x].values()]
        scores.sort()
        if y == "X":
            total_points += scores[0]
        elif y == "Y":
            total_points += scores[1]
        else:
            total_points += scores[2]
    print(total_points)


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {RED}{codeYear}{ENDCOLOR} - Day {RED}{codeDate}{ENDCOLOR}")

    # global data
    code_input = AOC(codeDate, codeYear, test=testing)
    data_input = parse_input(code_input)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
