import sys
import os
from time import sleep
from AOC import AOC
from TerminalColors import *

testing = False
cyclesToCheck = [x for x in range(20, 221, 40)]
screen = [False] * 240


def parse_input(code_input):
    result = code_input.read_lines()
    return result


def printScreenInter(screen, cycle, sprite_pos):
    print(f"{CLEAR}")
    chars = [" ", f"{BLUE}█{ENDCOLOR}", f"{GREEN}░{ENDCOLOR}", f"{RED}█{ENDCOLOR}", f"{YELLOW}█{ENDCOLOR}"]

    if sprite_pos == 1:
        sprite_range = [0, 1]
    elif sprite_pos == 40:
        sprite_range = [39, 40]
    else:
        sprite_range = list(range(sprite_pos-1, sprite_pos+2))

    for x in range(0, 40):
        if (x in sprite_range):
            if (x % 40 == (cycle - 1) % 40):
                print(chars[3], end="")
            else:
                print(chars[2], end="")
        else:
            print(chars[0], end="")
    print()

    for x in range(0, 241):
        line = 0

        if x == (cycle - 1):
            print(chars[4], end="")

        elif x <= cycle - 1:
            print(chars[screen[x]], end="")
        else:
            print(chars[0], end="")
        if ((x + 1) % 40) == 0:
            line += 1
            print()
    print()
    print(f"Cycle: {cycle} - Sprite Range: {min(sprite_range)}:{max(sprite_range)}")
    sleep(0.15)


def printScreen(screen, cycle):
    print(f"{CLEAR}{BLUE}")
    chars = [" ", "█"]
    for x in range(0, cycle-1, 40):
        # Cyscl through each 40 characters and create the line
        line = "".join([chars[y] for y in screen[x: x+40]])
        print(line)
    print()
    print()


def part1(commands):
    regX = 1                                # Starting value of Register X
    cycle = 1                               # Starting Cycle
    sigStrengths = 0                        # Track my sum
    for cmd in commands:
        match cmd.split():
            case["noop"]:
                if cycle in cyclesToCheck:
                    sigStrengths += cycle * regX
                cycle += 1
            case['addx', val]:
                for _ in range(2):
                    if cycle in cyclesToCheck:
                        sigStrengths += cycle * regX
                    cycle += 1
                regX += int(val)
    print(sigStrengths)


def part2(commands):
    regX = 1
    cycle = 1
    sprit_pos = 1
    for cmd in commands:
        match cmd.split():
            case ['noop']:
                if sprit_pos - 1 <= (cycle - 1) % 40 <= sprit_pos + 1:
                    screen[cycle-1] = True
                printScreenInter(screen, cycle, sprit_pos)
                cycle += 1
            case ['addx', val]:
                for _ in range(2):
                    if sprit_pos - 1 <= (cycle - 1) % 40 <= sprit_pos + 1:
                        screen[cycle-1] = True
                    printScreenInter(screen, cycle, sprit_pos)
                    cycle += 1
                regX += int(val)
        sprit_pos = regX
    printScreen(screen, cycle)


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
