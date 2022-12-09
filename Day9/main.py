#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import time
import numpy as np
from AOC import AOC
from TerminalColors import *

testing = False
size = 500
move_dict = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def parse_input(code_input):
    result = [(x, int(y)) for x, y in code_input.split_lines(" ")]
    return result


def add_tuple(a, b) -> tuple:
    return (a[0] + b[0], a[1] + b[1])


def print_board(board: np.array, knot_pos: list, start_pos: tuple):
    x, y = board.shape
    print(f"{CLEAR}")
    for y_pos in range(y):
        for x_pos in range(x):
            if (x_pos, y_pos) in knot_pos:
                knot_no = str(knot_pos.index((x_pos, y_pos)))
                if knot_no == "0":
                    knot_no = f"{BRED}H"
                print(f"{BYELLOW}{knot_no}{ENDCOLOR}", end="")
            elif (x_pos, y_pos) == start_pos:
                print(f"{GREEN}s{ENDCOLOR}", end="")
            elif board[(x_pos, y_pos)]:
                print(f"{WHITE}#{ENDCOLOR}", end="")
            else:
                print(f"{CYAN}.{ENDCOLOR}", end="")
        print()
    print()
    time.sleep(0.25)


def move_tail(head_pos, tail_pos) -> tuple:
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    # check if the tail is within one position of the head and return a (0,0)
    if ((abs(head_x - tail_x)) <= 1) and (abs(head_y - tail_y) <= 1):
        return (0, 0)
    if head_y == tail_y:
        x_move = (head_x - tail_x) // abs(head_x - tail_x)
        return (x_move, 0)
    elif head_x == tail_x:
        y_move = (head_y - tail_y) // abs(head_y - tail_y)
        return (0, y_move)
    else:
        x_move = (head_x - tail_x) // abs(head_x - tail_x)
        y_move = (head_y - tail_y) // abs(head_y - tail_y)
        return(x_move, y_move)
    return (0, 0)


def part1(moves):
    board = np.zeros((size, size), dtype=bool)
    x = y = size // 2
    head = (x, y)
    tail = (x, y)
    board[tail] = True

    for move in moves:
        move_dir, steps = move
        for step in range(steps):
            head = add_tuple(head, move_dict[move_dir])
            tail_move = move_tail(head, tail)
            tail = add_tuple(tail, tail_move)
            board[tail] = True
    print(np.sum(board))


def part2(moves):
    board = np.zeros((size, size), dtype=bool)
    x = y = size // 2
    start = (x, y)
    knots = [(x, y) for i in range(10)]
    board[knots[0]] = True
    # print_board(board, knots, start)

    for move in moves:
        move_dir, steps = move
        for step in range(steps):
            knots[0] = add_tuple(knots[0], move_dict[move_dir])
            for i in range(1, 10):
                tail_move = move_tail(knots[i-1], knots[i])
                knots[i] = add_tuple(knots[i], tail_move)
            board[knots[9]] = True
        # print_board(board, knots, start)
    print(np.sum(board))


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
