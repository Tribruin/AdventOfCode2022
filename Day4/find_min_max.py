import sys
import os
from AOC import AOC
from TerminalColors import *

testing = False


def parse_input(code_input):
    result = code_input.split_line_re_int("[,-]")
    return result


def main():

    # Get the path name and strip to the last 1 or 2 folder paths
    codePath = os.path.dirname(sys.argv[0])
    absCodePath = os.path.abspath(codePath)
    codeDate = int(absCodePath.split("/")[-1][3:])
    codeYear = int(absCodePath.split("/")[-2])

    # global data
    code_input = AOC(codeDate, codeYear, test=testing)
    data_input = parse_input(code_input)

    full_list = [x for y in data_input for x in y]
    print(min(full_list), max(full_list))


if __name__ == "__main__":
    main()
