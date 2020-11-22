"""
Common functions for AdventOfCode2019.
"""


def read_file(filepath):
    file_lines = []
    with open('input_01.txt') as input:
        for line in input.readlines():
            file_lines.append(int(line.strip()))
    input.close()
    return file_lines
