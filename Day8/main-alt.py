
#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
import numpy as np
from AOC import AOC
from TerminalColors import *

testing = False


def parse_input(code_input):
    array = list()

    for line in code_input.read_lines():
        temp = [int(a) for a in line]
        array.append(temp)

    result = np.array(array, dtype=int)
    return result


def part1(trees):

    y_len = len(trees)
    x_len = len(trees[0])

    visible_trees = 2 * x_len + 2 * (y_len - 2)
    for y in range(1, y_len-1):
        for x in range(1, x_len-1):
            tree_val = trees[y, x]
            row_from_left = trees[y, :x]
            row_to_right = trees[y, x+1:]
            column_from_top = trees[:y, x]
            column_to_bottom = trees[y+1:, x]

            if (tree_val > max(row_from_left)) or (tree_val > max(row_to_right)) or (tree_val > max(column_from_top)) or (tree_val > max(column_to_bottom)):
                visible_trees += 1
    print(visible_trees)


def part2(trees):

    y_len = len(trees)
    x_len = len(trees[0])

    best_view = 0
    for y in range(1, y_len-1):
        for x in range(1, x_len-1):
            tree_val = trees[y, x]
            row_from_left = trees[y, :x][::-1]
            row_to_right = trees[y, x+1:]
            column_from_top = trees[:y, x][::-1]
            column_to_bottom = trees[y+1:, x]

            tree_lines_to_check = [row_from_left, row_to_right, column_from_top, column_to_bottom]
            tree_value = 1
            for tree_line in tree_lines_to_check:
                i = 0
                while i < len(tree_line):
                    if tree_val <= tree_line[i]:
                        i += 1
                        break
                    i += 1

                tree_value *= i
            if tree_value > best_view:
                best_view = tree_value

    print(best_view)


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
