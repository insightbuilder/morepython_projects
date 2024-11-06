#!/bin/python

from argparse import ArgumentParser
from typing import List, TextIO
from sys import stdin


def basic_sort(input: List[str] | TextIO, r: bool):
    """Sorts the lines fed into the function
    and returns the list of lines. Arg 'r'
    determines if the lines have to sorted in reverse"""
    # using sorted with key referring to first char of line
    sorted_lines = sorted(input, key=lambda x: x[0], reverse=r)
    return sorted_lines


def do_ignore_b(input: List[str]):
    """Removes the first blank space in the line"""
    cleaned = [x.strip() for x in input]
    print(cleaned)


def read_file_lines(file_path: str):
    with open(file_path) as obj:
        data = obj.readlines()
        return data


if __name__ == "__main__":
    sortparser = ArgumentParser(
        prog="SORT",
        usage="""
    ./sort.py -r -b -d -f test.txt

    -f option has to be the last

    To sort stdin 

    ls -l | ./sort.py -r -b -d
    or 
    ./sort.py -r -b -d 
    """,
    )
    # the parser will have options which will have no args
    sortparser.add_argument("-b", help="ignore leading blanks", nargs="*")
    sortparser.add_argument("-d", help="dictionary sort", nargs="*")
    sortparser.add_argument("-r", help="reverse the sort", nargs="*")
    sortparser.add_argument("-f", help="Take input file", nargs="?")

    sortargs = sortparser.parse_args()
    print(sortargs)

    if sortargs.f is None:
        # take stdin and do default sort
        rev = False
        if sortargs.r is not None:
            # if reverse is enabled then reverse it
            rev = True
        sort_stdin = basic_sort(input=stdin, r=rev)
        for sents in sort_stdin:
            print(sents, end="")

    elif sortargs.f:
        print(len(sortargs.b))
        # take stdin and do default sort on the file
        file_lines = read_file_lines(sortargs.f)
        rev = False
        if sortargs.r is not None:
            # if reverse is enabled then reverse it
            rev = True
        sort_stdin = basic_sort(input=file_lines, r=rev)
        for sents in sort_stdin:
            print(sents, end="")
