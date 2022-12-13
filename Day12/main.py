import sys
import os
import numpy as np
from AOC import AOC, addTuples
from TerminalColors import *

testing = True


class Graph():
    def __init__(self, mapInput) -> None:
        y_len = len(mapInput)
        x_len = len(mapInput[0])
        self.mapSize = (x_len, y_len)
        self.heightMap = dict()
        for y in range(y_len):
            for x in range(x_len):
                curPos = dict()
                if mapInput[y][x] == "S":
                    self.startPos = (x, y)
                    curPos['height'] = 'a'
                elif mapInput[y][x] == "E":
                    self.endPos = (x, y)
                    curPos['height'] = 'z'
                else:
                    curPos['height'] = mapInput[y][x]
                curPos['dist'] = float('inf')
                curPos['edges'] = list()
                self.heightMap[(x, y)] = curPos
        self.findEdges()
        self.heightMap[self.startPos]['dist'] = 0

    def findEdges(self):
        for y in range(self.mapSize[1]):
            for x in range(self.mapSize[0]):
                self.heightMap[(x, y)]['edges'] = list()
                for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    edge = addTuples(move, (x, y))
                    if (0 <= edge[0] < self.mapSize[0]) and (0 <= edge[1] <= self.mapSize[1] - 1):
                        if ord(self.heightMap[(x, y)]['height']) + 1 >= ord(self.heightMap[edge]['height']):
                            self.heightMap[(x, y)]['edges'].append(edge)
                # print(f"Point: {(x,y)} - Edges: {self.heightMap[(x,y)]['edges']}")

    def resetMap(self):
        for point in self.heightMap.keys():
            self.heightMap[point]['dist'] = float('inf')


def parse_input(code_input):
    result = Graph(code_input.read_lines())
    return result


def findNextPoint(points: list, graphMap: Graph) -> tuple:
    lowestVal = float('inf')
    lowestPoint = None
    for point in points:
        if graphMap.heightMap[point]['dist'] < lowestVal:
            lowestVal = graphMap.heightMap[point]['dist']
            lowestPoint = point
    return lowestPoint


def part1(graphMap):
    visited = list()
    unvisited = list(graphMap.heightMap.keys())
    currentPoint = graphMap.startPos
    visited.append(currentPoint)
    unvisited.pop(unvisited.index(currentPoint))

    while len(unvisited) > 0 and currentPoint != graphMap.endPos:
        pointsToCheck = graphMap.heightMap[currentPoint]['edges']
        pointVal = graphMap.heightMap[currentPoint]['dist']
        for point in pointsToCheck:
            newDist = pointVal + 1
            if newDist < graphMap.heightMap[point]['dist']:
                graphMap.heightMap[point]['dist'] = newDist
        currentPoint = findNextPoint(unvisited, graphMap)
        visited.append(currentPoint)
        unvisited.pop(unvisited.index(currentPoint))
    print(graphMap.heightMap[graphMap.endPos]['dist'])


def part2(graphMap):

    allPossStartingPoints = [x for x in graphMap.heightMap.keys() if graphMap.heightMap[x]['height'] == 'a']

    bestStartPos = None
    bestValue = float('inf')
    i = 1
    for startingPoint in allPossStartingPoints:
        graphMap.heightMap[startingPoint]['dist'] = 0
        currentPoint = startingPoint
        visited = list()
        unvisited = list(graphMap.heightMap.keys())
        visited.append(currentPoint)
        unvisited.pop(unvisited.index(currentPoint))

        while len(unvisited) > 0 and currentPoint != graphMap.endPos:
            pointsToCheck = graphMap.heightMap[currentPoint]['edges']
            pointVal = graphMap.heightMap[currentPoint]['dist']
            for point in pointsToCheck:
                newDist = pointVal + 1
                if newDist < graphMap.heightMap[point]['dist']:
                    graphMap.heightMap[point]['dist'] = newDist
            currentPoint = findNextPoint(unvisited, graphMap)
            if currentPoint == None:
                unvisited = list()
                break
            visited.append(currentPoint)
            unvisited.pop(unvisited.index(currentPoint))

        # if graphMap.heightMap[graphMap.endPos]['dist'] != float('inf'):
            # print(f"{i} - Starting Point: {startingPoint} - Dist: {graphMap.heightMap[graphMap.endPos]['dist']}")

        if graphMap.heightMap[graphMap.endPos]['dist'] < bestValue:
            bestValue = graphMap.heightMap[graphMap.endPos]['dist']
            bestStartPos = startingPoint
            print(f"{i} - Found new best value: {bestValue} at {bestStartPos}")
        i += 1

        graphMap.resetMap()

    print(bestValue)


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

    data_input = parse_input(code_input)
    part2(data_input)


if __name__ == "__main__":
    main()
