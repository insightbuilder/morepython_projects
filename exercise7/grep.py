#!/bin/python

# implementing grep using glob and re modules

# target to complete the below features
# read the files that are selected by the glob
# find the lines that matches the given pattern

from argparse import ArgumentParser
from glob import glob
import re


def file_pattern_matcher(file_pattern: str, search_pattern: str):
    """Locates the files based on given pattern and reads the lines.
    Finds the lines that matches the search pattern"""
    print(f"Recieved file pattern: {file_pattern} and search pattern: {search_pattern}")
    files = glob(file_pattern)  # this will capture even if single file is given as list
    # print(f"Matched files: {files}")
    #     file_line = """[I 2024-10-21 17:19:37.083 ServerApp] Starting buffering for bc93e630-c608-441
    # d-bbb4-c6d3c5e73bf5:6a94bc89-9f9d-4d4a-8376-895a0ce6add1"""
    reobj = re.compile(search_pattern)
    #     matcher = reobj.search(file_line)
    #     print(f"Matched patterns: {matcher}")
    # start working on opening and reading files
    for file in files:
        with open(file) as data:
            filelines = data.readlines()
            for line in filelines:
                print(f"Before match: {line}")
                ptrn_search = reobj.search(line)
                print(ptrn_search)
                if ptrn_search:
                    # print the line
                    print(f"After match line: {line}")
                    print(f"Matched obj: {ptrn_search}")


if __name__ == "__main__":
    grepparse = ArgumentParser(
        prog="GREP implementation",
        usage="""
grep -n -- 'f.*\\.c$' *g\\*.h /dev/null
    """,
    )
    grepparse.add_argument("fileptrn", help="Provide the filename or pattern")
    grepparse.add_argument("searchptrn", help="Provide the pattern to match")
    cliargs = grepparse.parse_args()
    print(cliargs)
    file_pattern_matcher(cliargs.fileptrn, cliargs.searchptrn)
