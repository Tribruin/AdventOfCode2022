#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from TerminalColors import *

testing = True


def parse_input(code_input):
    result = code_input.split_line_re_int("[,-]")
    return result


def part1(line):

    a1, a2, b1, b2 = line
    s1 = [x for x in range(a1, a2+1)]
    s2 = [x for x in range(b1, b2+1)]
    length = min([len(s1), len(s2)])
    if len(list(set(s1) & set(s2))) == length:
        counter = True
    print(counter)


def part2(data_input):
    counter = 0
    for a1, a2, b1, b2 in data_input:
        s1 = [x for x in range(a1, a2+1)]
        s2 = [x for x in range(b1, b2+1)]
        if len(list(set(s1) & set(s2))) > 0:
            counter += 1
    print(counter)


def draw_screen(data_input):

    if testing:
        last = 10
    else:
        last = 10
    for line in data_input:
        print(f"{CLEAR}", end="")
        line.sort()
        a, b, c, d = line
        print(f"{BLUE}", end="")
        for _ in range(0, a):
            print("*", end="")
        print(f"{RED}", end="")
        for _ in range(a, b):
            print("*", end="")
        print(f"{YELLOW}", end="")
        for _ in range(b, c):
            print("*", end="")
        print(f"{RED}", end="")
        for _ in range(c, d):
            print("*", end="")
        print(f"{BLUE}", end="")
        for _ in range(d, last):
            print("*", end="")
        print()


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

    # part1(data_input)
    # part2(data_input)
    draw_screen(data_input)


if __name__ == "__main__":
    main()
