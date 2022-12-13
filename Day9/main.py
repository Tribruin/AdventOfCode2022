import sys
import os
import time
import numpy as np
from AOC import AOC, addTuple
from TerminalColors import *

testing = False
size = 500
move_dict = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def parse_input(code_input):
    result = [(x, int(y)) for x, y in code_input.split_lines(" ")]
    return result


def sign(x) -> int:
    # Returns the sign of the X (-1, 0, 1)
    if x == 0:
        return 0
    else:
        return (x // abs(x))


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
    # Return the move vector for the tail based on the head position

    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    # check if the tail is within one position of the head and return a (0,0)
    if ((abs(head_x - tail_x)) <= 1) and (abs(head_y - tail_y) <= 1):
        return (0, 0)

    # Else we are goign to return a vector that equals the signs of movement
    # Yes, it works. For example if the HEAD is (5,5) and TAIL is (3,3)
    # The move vector is (1,1) to move TAIL to (4,4)
    # Note this only works if the TAIL moves every time the HEAD moves.

    return (sign(head_x-tail_x), sign(head_y - tail_y))


def part1(moves):

    # Create a board to track the tail visits
    board = np.zeros((size, size), dtype=bool)
    x = y = size // 2
    head = tail = (x, y)
    board[tail] = True

    for move in moves:
        move_dir, steps = move
        for _ in range(steps):
            head = addTuple(head, move_dict[move_dir])
            tail_move = move_tail(head, tail)
            tail = addTuple(tail, tail_move)
            board[tail] = True
    print(np.sum(board))


def part2(moves):

    # Create a board to track the tail visits
    board = np.zeros((size, size), dtype=bool)
    x = y = size // 2

    # Create a list of knots 0-9 where 0 is HEAD and 9 is TAIL
    knots = [(x, y) for i in range(10)]
    board[knots[9]] = True
    # print_board(board, knots, start)

    for move_dir, steps in moves:
        # move_dir, steps = move
        for _ in range(steps):
            # First move the HEAD
            knots[0] = addTuple(knots[0], move_dict[move_dir])

            for i in range(1, 10):
                # Now move each knot using the new position of the previous knot
                tail_move = move_tail(knots[i-1], knots[i])
                knots[i] = addTuple(knots[i], tail_move)

            # Mark the position of the last knot as visited.
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

    part1(data_input)
    part2(data_input)


if __name__ == "__main__":
    main()
