#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import string
from AOC import AOC
from TerminalColors import *


testing = False
characters = string.ascii_lowercase + string.ascii_uppercase


def parse_input(code_input):
    result = code_input.read_lines()
    return result


def calc_priority(temp) -> int:
    # temp = ord(list(temp)[0])
    # if (temp > 95):
    #     return (temp - 96)
    # else
    #     return (temp - 38)

    # Get the index of character and add on becausae a=1 & A=27
    return characters.index(list(temp)[0]) + 1


def part1(data_input):
    priority_sum = 0
    for ruck_sack in data_input:
        # Split each ruck sack in to two equal compartments
        com1, com2 = ruck_sack[:len(ruck_sack) // 2], ruck_sack[(len(ruck_sack) // 2):]

        # Make a each comparment a set and then find the intersection
        # Per the challenge there should only ever be one overlapping element
        common_item = set(com1) & set(com2)

        # Calculate the priority value of the common element
        priority_sum += calc_priority(common_item)

    print(priority_sum)


def part2(data_input):
    priority_sum = 0

    # Create a loop that gets each group of three rucksacks
    for i in range(0, len(data_input), 3):

        # Convert the next three ruck sacks in to sets and find the commmon item
        common_item = set(data_input[i]) & set(data_input[i+1]) & set(data_input[i+2])

        # Calculate the priority value of the common element
        priority_sum += calc_priority(common_item)

    print(priority_sum)


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
