#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from TerminalColors import *

testing = False


def parse_input(code_input):
    result = code_input.read_lines()[0]
    return result


def part1(data_input):
    length = len(data_input)
    for i in range(3, length+1):
        string = data_input[i-3:i+1]
        str_set = set([x for x in string])
        if len(str_set) == 4:
            print(i+1, string)
            return


def part2(data_input):
    length = len(data_input)
    for i in range(13, length+1):
        string = data_input[i-13:i+1]
        str_set = set([x for x in string])
        if len(str_set) == 14:
            print(i+1, string)
            return


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
