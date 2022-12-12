import sys
import os
import re
from copy import deepcopy
from AOC import AOC
from TerminalColors import *

testing = False


class Monkey:
    def __init__(self, name: str, startItems: list, oper: str, testCond: int, testTrue: int, testFalse: int) -> None:
        self.name = int(name)
        self.itemWorryLevels = [int(x) for x in startItems]
        self.operator = oper[0]
        self.opVal = oper[1]
        self.testCond = int(testCond)
        self.testTrue = int(testTrue)
        self.testFalse = int(testFalse)
        self.itemsChecked = 0

    def playWithItem(self, currentItemValue: int) -> int:
        """ Monkey plays with the item """

        if self.opVal == "old":
            opVal = currentItemValue
        else:
            opVal = int(self.opVal)

        if self.operator == "+":
            return currentItemValue + opVal
        elif self.operator == "*":
            return currentItemValue * opVal
        else:
            print("WARNING: BAD OPERATOR")
            return 0

    def playRoundPart1(self) -> list():
        ''' Return a list of tuples, which include the monkey to throw to
            and the new worry value of the item'''

        result = list()
        self.itemsChecked += len(self.itemWorryLevels)
        for item in self.itemWorryLevels:
            newItemValue = self.playWithItem(item) // 3                 # Play witj item then divide by 3
            testValue = newItemValue % self.testCond
            if testValue == 0:
                result.append((newItemValue, self.testTrue))
            else:
                result.append((newItemValue, self.testFalse))
        self.itemWorryLevels = []
        return result

    def playRoundPart2(self) -> list():
        ''' Return a list of tuples, which include the monkey to throw to
            and the new worry value of the item'''

        result = list()
        self.itemsChecked += len(self.itemWorryLevels)
        for item in self.itemWorryLevels:
            newItemValue = self.playWithItem(item)
            testValue = newItemValue % self.testCond
            if testValue == 0:
                result.append((newItemValue, self.testTrue))
            else:
                result.append((newItemValue, self.testFalse))
        self.itemWorryLevels = []
        return result


def parse_input(code_input):
    monkeyData = code_input.read_lines()
    result = list()
    i = 0
    while i < len(monkeyData):
        name = monkeyData[i][7]
        items = re.findall("\d+", monkeyData[i+1])
        operation = (monkeyData[i+2].split()[4], monkeyData[i+2].split()[5])
        testCond = int(monkeyData[i+3].split()[3])
        testTrue = int(monkeyData[i+4].split()[5])
        testFalse = int(monkeyData[i+5].split()[5])
        result.append(Monkey(name, items, operation, testCond, testTrue, testFalse))
        i += 7

    return result


def part1(monkies):

    for playRound in range(1, 21):
        for monkey in monkies:
            results = monkey.playRoundPart1()
            for itemVal, monkeyNum in results:
                monkies[monkeyNum].itemWorryLevels.append(itemVal)
            totalItemsProcessed = sorted([x.itemsChecked for x in monkies], reverse=True)
    print(totalItemsProcessed[0] * totalItemsProcessed[1])


def part2(monkies):

    # We need to find a divisor that can be used to reduce the resulting item value after each throw
    # In this case, we will create a new divisor that is the factor of all the individual divisors
    # After each throw we will calculate newWorryValue % refactorDiv
    refactorDiv = 1
    for monkey in monkies:
        refactorDiv *= monkey.testCond

    for playRound in range(1, 10001):

        for monkey in monkies:
            subresults = monkey.playRoundPart2()
            results = [(x % refactorDiv, y) for x, y in subresults]
            for result in results:
                monkies[result[1]].itemWorryLevels.append(result[0])

    worryLevels = [x.itemsChecked for x in monkies]
    worryLevels = sorted(worryLevels, reverse=True)[0:2]
    print(worryLevels[0] * worryLevels[1])


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

    # Reset the data_input
    data_input = parse_input(code_input)
    part2(data_input)


if __name__ == "__main__":
    main()
