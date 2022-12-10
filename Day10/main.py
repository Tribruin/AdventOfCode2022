import sys
import os
from AOC import AOC
from TerminalColors import *

testing = False
global cyclesToCheck
cyclesToCheck = [x for x in range(20, 221, 40)]
screen = {x: False for x in range(0, 240)}


def parse_input(code_input):
    result = code_input.read_lines()
    return result


def printLine(screen, cycle):
    for x in range(1, cycle + 1):
        if screen[x - 1]:
            print("█", end="")
        else:
            print(" ", end="")
        if x % 40 == 0:
            print()
    print()
    print()


def part1(commands):
    regX = 1
    cycle = 0
    sigStrengths = list()
    for cmd in commands:
        cycle += 1
        if cmd == "noop":
            if cycle in cyclesToCheck:
                sigStrengths.append(cycle * regX)
                print(cycle, regX, cycle * regX)
        else:
            val = int(cmd.split()[1])
            if cycle in cyclesToCheck:
                sigStrengths.append(cycle * regX)
                print(cycle, regX, cycle * regX)
            cycle += 1
            if cycle in cyclesToCheck:
                sigStrengths.append(cycle * regX)
                print(cycle, regX, cycle * regX)
            regX += val
        # print(cycle, regX, cmd)
    print(sum(sigStrengths))


def part2(commands):
    regX = 1
    cycle = 0
    sprit_pos = 1
    for cmd in commands:
        cycle += 1
        if cmd == "noop":
            if sprit_pos - 1 <= (cycle - 1) % 40 <= sprit_pos + 1:
                screen[cycle - 1] = True
        else:
            val = int(cmd.split()[1])
            if sprit_pos - 1 <= (cycle - 1) % 40 <= sprit_pos + 1:
                screen[cycle - 1] = True
            cycle += 1
            if sprit_pos - 1 <= (cycle - 1) % 40 <= sprit_pos + 1:
                screen[cycle - 1] = True
            regX += val
        sprit_pos = regX
    printLine(screen, cycle)


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
    part2(data_input)


if __name__ == "__main__":
    main()
