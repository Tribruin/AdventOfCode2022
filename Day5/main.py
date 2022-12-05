#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import re
from collections import deque
from AOC import AOC


from TerminalColors import *

testing = False


def parse_input(code_input):
    lines = code_input.read_lines_no_strip()
    stacks = [""]
    if testing:
        stacks_pos = [-1, 1, 5, 9]
    else:
        stacks_pos = [-1, 1, 5, 9, 13, 17, 21, 25, 29, 33]

    # Create the stacks
    for i in range(1, len(stacks_pos)):
        stacks.append(deque())

    # Get the boxes from the stack
    i = 0
    while lines[i][1] != "1":
        for k in range(1, len(stacks_pos)):
            box = lines[i][stacks_pos[k]]

            if box != " ":
                stacks[k].append(box)
        i += 1

    i += 2
    moves = list()
    while i < len(lines):
        move = re.findall(r"\d+", lines[i])
        move = list(map(int, move))
        moves.append(move)
        i += 1

    return stacks, moves


def part1(stacks, moves):
    new_stacks = stacks.copy()
    for move in moves:
        no_boxes, fro, to = move
        for _ in range(no_boxes):
            box = new_stacks[fro].popleft()
            new_stacks[to].appendleft(box)

    for stack in range(1, len(new_stacks)):
        print(f"{new_stacks[stack][0]}", end="")
    print()


def part2(stacks, moves):
    new_stacks = stacks.copy()
    for move in moves:
        no_boxes, fro, to = move
        move_stack = list()
        for _ in range(no_boxes):
            box = new_stacks[fro].popleft()
            move_stack.append(box)

        for box in move_stack[::-1]:
            new_stacks[to].appendleft(box)

    for stack in range(1, len(new_stacks)):
        print(f"{new_stacks[stack][0]}", end="")
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
    stacks, moves = parse_input(code_input)
    part1(stacks, moves)

    stacks, moves = parse_input(code_input)
    part2(stacks, moves)


if __name__ == "__main__":
    main()
