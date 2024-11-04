#!/bin/python

from argparse import ArgumentParser
from sys import stdin
from typing import TextIO
import re


def process_line(line: str, expr: str, tgt: str):
    """str_output = re.sub(regex_search_term, regex_replacement, str_input)"""
    updt_line = re.sub(expr, tgt, line)
    return updt_line


def parse_stdin(expr: str, datain: TextIO, output: bool):
    """Takes the expression and replaces in the given stream"""
    regex = expr.split("\\")[1]
    target = expr.split("\\")[2]
    # print(regex)
    # print(target)
    for idx, line in enumerate(datain):
        # each line will be processed and then printed
        updt = process_line(line=line, expr=regex, tgt=target)
        if int(output) == idx:
            print(updt, end="")


def parse_file(file_name: str, expr: str, output: bool):
    """Takes the expression and replaces in the given stream"""
    regex = expr.split("\\")[1]
    target = expr.split("\\")[2]
    # print(regex)
    # print(target)
    with open(file_name) as fn:
        datain = fn.readlines()
        for idx, line in enumerate(datain):
            # each line will be processed and then printed
            updt = process_line(line=line, expr=regex, tgt=target)
            if int(output) == idx:
                print(updt, end="")


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="SED",
        usage="""
- sed -e 's\\uberdev\\kamal\\g' ~/jupy.log
- ls −l | sed −e 's\\uberdev\\kamal\\g' 
- expression has to be in double or single quoutes
- Replaces the expression with the target
    """,
    )
    # -d arg
    parser.add_argument("-e", help="option to capture the expression")
    # -f arg
    parser.add_argument("-n", help="Suppresses the output", nargs="?")
    # final file input
    parser.add_argument("file", help="File which will be read and processed", nargs="?")

    yourargs = parser.parse_args()

    print(yourargs)
    if not yourargs.e and not yourargs.file:
        print("Option missing, look at ./sed.py -h for usage details")
    elif not yourargs.file and stdin and yourargs.e:
        # if no file but data in stdin
        parse_stdin(expr=yourargs.e, datain=stdin, output=yourargs.n)
    else:
        parse_file(file_name=yourargs.file, expr=yourargs.e, output=yourargs.n)
