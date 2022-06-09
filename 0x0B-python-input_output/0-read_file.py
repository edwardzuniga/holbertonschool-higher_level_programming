#!/usr/bin/python3


"""Read file"""


def read_file(filename=""):
    """function that reads a text file (UTF8)"""
    with open('filename', 'r', encoding="utf-8") as f:
        """Reading and writing files"""
        for line in f:
            print(line, end='')
    f.close()
