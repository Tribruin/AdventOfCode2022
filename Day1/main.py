#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from TerminalColors import *

testing = False


def parse_input(code_input: AOC):
    result = code_input.read_lines()
    return result


def part1(data_input):
    elves = list()
    current_elf = 0
    for line in data_input:
        if line == "":
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    print(max(elves))


def part2(data_input):
    elves = list()
    current_elf = 0
    for line in data_input:
        if line == "":
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    elves.sort(reverse=True)
    print(sum(elves[0:3]))


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])
    print(f"Running Advent of Code for Year: {RED}{codeYear}{ENDCOLOR} - Day {RED}{codeDate}{ENDCOLOR}")

    # global data
    code_data = AOC(codeDate, codeYear, test=testing)
    data_input = parse_input(code_data)

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
