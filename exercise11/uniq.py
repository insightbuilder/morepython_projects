#!/bin/python

from argparse import ArgumentParser
from sys import stdin
from typing import List, TextIO, Dict, Union


def read_file(file_path: str) -> List[str]:
    with open(file_path) as inobj:
        data = inobj.readlines()

    return data


def get_unique(
    in_line: Union[List[str], TextIO], ret_count: bool
) -> Union[List[str], Dict[str, int]]:
    """Prints only the unique lines"""
    uniq_lines = []
    # rather than making a set, counting will be better
    count_dict = dict()
    # go through each of the line,
    # check if line is repeated else where in the list
    # check if line is present in the chek_set
    # if above is true then don't include in the uniq_lines
    for dp in in_line:
        dp = dp.strip()
        if dp not in count_dict:
            count_dict[dp] = 1
        else:
            count_dict[dp] += 1
    print(count_dict)
    for key, val in count_dict.items():
        if val == 1:
            uniq_lines.append(key)

    if ret_count:
        return count_dict

    return uniq_lines


if __name__ == "__main__":
    uniqparser = ArgumentParser(
        prog="UNIQ",
        usage="""
    uniq [option] filename 
    uniq [option] stdin

    uniq -u : prints only unique lines omits duplicates completely
    uniq -c : prints only unique lines and counts if repeated
    uniq -d : prints only duplicate lines once
    uniq -D : prints only duplicate lines
    """,
    )
    uniqparser.add_argument("-u", help="Return unique lines only", action="store_true")
    uniqparser.add_argument("-c", help="Return lines with counts", action="store_true")
    uniqparser.add_argument("file", help="Takes file or stdin", nargs="?")

    uniqargs = uniqparser.parse_args()
    print(uniqargs)

    if uniqargs.u and uniqargs.file:
        file_lines = read_file(uniqargs.file)
        unique_lines = get_unique(in_line=file_lines, ret_count=False)
        for line in unique_lines:
            print(line, end="\n")

    elif uniqargs.c and uniqargs.file:
        file_lines = read_file(uniqargs.file)
        line_dict = get_unique(in_line=file_lines, ret_count=True)
        for key, cnt in line_dict.items():
            print(f"{cnt} {key}", end="\n")

    elif uniqargs.u and not uniqargs.file:
        unique_lines = get_unique(in_line=stdin, ret_count=False)
        for line in unique_lines:
            print(line, end="\n")

    elif uniqargs.c and not uniqargs.file:
        line_dict = get_unique(in_line=stdin, ret_count=True)
        for key, cnt in line_dict.items():
            print(f"{cnt} {key}", end="\n")
