import sys
import os
import time
from AOC import AOC, addTuples
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
    visited = list()
    x = y = size // 2
    head = tail = (x, y)
    visited.append(tail)

    for move in moves:
        move_dir, steps = move
        for _ in range(steps):
            head = addTuples(head, move_dict[move_dir])
            tail_move = move_tail(head, tail)
            tail = addTuples(tail, tail_move)
            visited.append(tail)
    print(len(set(visited)))


def part2(moves):

    # Create a board to track the tail visits
    x = y = size // 2
    visited = list()

    # Create a list of knots 0-9 where 0 is HEAD and 9 is TAIL
    knots = [(x, y) for i in range(10)]
    visited.append(knots[9])

    for move_dir, steps in moves:
        for _ in range(steps):
            # First move the HEAD
            knots[0] = addTuples(knots[0], move_dict[move_dir])

            for i in range(1, 10):
                # Now move each knot using the new position of the previous knot
                tail_move = move_tail(knots[i-1], knots[i])
                knots[i] = addTuples(knots[i], tail_move)

            # Mark the position of the last knot as visited.
            visited.append(knots[9])

        # print_board(board, knots, start)
    print(len(set(visited)))


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
