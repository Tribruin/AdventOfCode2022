
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
        self.size = 0
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

        # Check is we already computed the size and return it.
        # No need to do more work
        if self.size != 0:
            return self.size

        # Ok, let's compute the size
        size = 0
        size += sum([x for x in self.files.values()])
        for dir in self.subDirectories:
            size += dir.folder_size()

        # Set the self.size for future use
        self.size = size
        return size


def parse_input(code_input):
    result = code_input.read_lines()
    return result


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
            cmd = subCommands[1]
        else:
            cmd = subCommands[0]

        if cmd == "ls":
            pass
        elif cmd == "cd":
            if subCommands[2] == "..":
                currentDir = currentDir.parentDir
                currentPath.pop()
            else:
                currentPath.append(f"{subCommands[2]}/")
                currentPathName = "".join(currentPath)
                currentDir = directories[currentPathName]
        elif cmd == "dir":
            dirName = subCommands[1]
            newPathName = "".join(currentPath) + f"{dirName}/"
            directories[newPathName] = Directory(newPathName, currentDir)

        else:
            size, fileName = int(subCommands[0]), subCommands[1]
            currentDir.add_file(fileName, size)
        cmd_no += 1

    total_size = 0
    for name, directory in directories.items():
        size = directory.folder_size()
        if size <= maxDirSize:
            total_size += size
    print(total_size)

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
