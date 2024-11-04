#!/bin/python

from argparse import ArgumentParser
from sys import stdin


def parse_stdin(delim: str, sections: str):
    # get the sections
    sec1, sec2 = sections.split("-")
    try:
        sec1 = int(sec1)
        sec2 = int(sec2)
    except Exception as e:
        print(e)
    # read the file lines
    print(f"Section 1: {sec1} and Section 2: {sec2}")
    # process the lines one by one
    for idx, line in enumerate(stdin):
        line = line.strip()
        # print(line)
        # split the lines with delim
        line_splits = line.split(delim)
        # print(line_splits)
        # get the split_len
        split_len = len(line_splits)
        sec1 -= 1
        sec2 -= 1
        select_section = line_splits[sec1:sec2]
        print(select_section)
        # print(" ".join(select_section))


# implement the -d, -f and then finally file input
def parse_file(file_name: str, delim: str, sections: str):
    # get the sections
    sec1, sec2 = sections.split("-")
    try:
        sec1 = int(sec1)
        sec2 = int(sec2)
    except Exception as e:
        print(e)
    # read the file lines
    print(f"Section 1: {sec1} and Section 2: {sec2}")
    with open(file_name) as cutd:
        yourlines = cutd.readlines()
        # process the lines one by one
        for line in yourlines[:5]:
            # split the lines with delim
            line_splits = line.split(delim)
            # print(line_splits)
            # get the split_len
            split_len = len(line_splits)
            # sec2 is greater than line_splits len,
            if sec2 > split_len:
                # bring the sec2 to split_len
                # this will be a challenge when lines have different sections
                sec1 -= 1
                sec2 = split_len
            else:
                # print(f"Lines split in {split_len} parts")
                # move the sec1 and 2 by 1
                sec1 -= 1
                sec2 -= 1
            select_section = line_splits[sec1:sec2]
            print(select_section)
            # print(" ".join(select_section))


if __name__ == "__main__":
    cutparser = ArgumentParser(
        prog="CUT",
        usage="""
- cut -d ' ' -f 3-5 ~/jupy.log
- ls −l | cut −d ' ' −f 5−7
- Removes sections from each line of the file
    """,
    )
    # -d arg
    cutparser.add_argument("-d", help="Delimiter to split the lines")
    # -f arg
    cutparser.add_argument("-f", help="Sections of lines to take")
    # final file input
    cutparser.add_argument(
        "file", help="File which will be read and processed", nargs="?"
    )

    cutargs = cutparser.parse_args()

    print(cutargs)
    if not cutargs.d or not cutargs.f:
        print("Option missing, look at ./cut.py -h for usage details")
    elif not cutargs.file and stdin:
        # if no file but data in stdin
        parse_stdin(delim=cutargs.d, sections=cutargs.f)
    else:
        parse_file(file_name=cutargs.file, delim=cutargs.d, sections=cutargs.f)
