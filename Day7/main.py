#!/Users/rblount/.pyenv/versions/AdOfCode/bin/python


import sys
import os
from AOC import AOC
from TerminalColors import *

testing = False
maxDirSize = 100000
sizeRequired = 30000000
totalDiskSize = 70000000


class Directory:

    def __init__(self, dirName, parentDir) -> None:
        self.name = dirName
        self.subDirectories = list()
        self.files = dict()
        if parentDir != None:
            self.parentDir = parentDir
            self.parentDir.add_subdirectory(self)
        else:
            self.parentDir = None

    def add_file(self, filename, size) -> None:
        self.files[filename] = size

    def add_subdirectory(self, subDirectory) -> None:
        self.subDirectories.append(subDirectory)

    def folder_size(self) -> int:
        size = 0
        size += sum([x for x in self.files.values()])
        for dir in self.subDirectories:
            size += dir.folder_size()
        return size


def parse_input(code_input):
    result = code_input.read_lines()
    return result


def print_directory_struct(dir: Directory, level=0):
    print("  " * level, end="")
    print(f"- {BLUE}{dir.name.split('/')[-2]} (dir) - (size = {dir.folder_size()}{ENDCOLOR}")
    for subdirectory in dir.subDirectories:
        print_directory_struct(subdirectory, level + 1)
    for name, size in dir.files.items():
        print("  " * (level + 1), end="")
        print(f"- {RED}{name} (file, size = {size}){ENDCOLOR}")


def part1(commands):

    cmd_no = 1
    directories = dict()
    directories["/"] = Directory(" /", None)
    currentDir = directories["/"]
    currentPath = ["/"]
    total_cmds = len(commands)

    while cmd_no < total_cmds:
        subCommands = commands[cmd_no].split()
        if subCommands[0] == "$":
            if subCommands[1] == "ls":
                cmd_no += 1
                subCommands = commands[cmd_no].split()
                while subCommands[0] != "$":
                    if subCommands[0] == "dir":
                        dirName = subCommands[1]
                        newPathName = "".join(currentPath) + f"{dirName}/"
                        directories[newPathName] = Directory(newPathName, currentDir)
                    else:
                        size, fileName = int(subCommands[0]), subCommands[1]
                        currentDir.add_file(fileName, size)
                    cmd_no += 1
                    if cmd_no == total_cmds:
                        break
                    else:
                        subCommands = commands[cmd_no].split()
            elif subCommands[1] == "cd":
                if subCommands[2] == "..":
                    currentDir = currentDir.parentDir
                    currentPath.pop()
                else:
                    currentPath.append(f"{subCommands[2]}/")
                    currentPathName = "".join(currentPath)
                    currentDir = directories[currentPathName]
                cmd_no += 1
                subCommands = commands[cmd_no].split()

    total_size = 0
    for name, directory in directories.items():
        size = directory.folder_size()
        if size <= maxDirSize:
            print(f"Directory {name} : {size}")
            total_size += size
    print(total_size)
    # print_directory_struct(directories["/"])

    return directories


def part2(directories: list):
    usedSpace = directories["/"].folder_size()
    avaliableSpace = totalDiskSize - usedSpace
    minNeedToDelete = sizeRequired - avaliableSpace
    maxNeedToDelete = usedSpace
    dirToDelete = None
    for dir in directories.values():
        size = dir.folder_size()
        if (size > minNeedToDelete) and (maxNeedToDelete):
            dirToDelete = dir
    print(f"{dirToDelete.name} = {dirToDelete.folder_size()}")


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

    dirs = part1(data_input)
    part2(dirs)


if __name__ == "__main__":
    main()
