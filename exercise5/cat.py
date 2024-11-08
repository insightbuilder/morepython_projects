#!/bin/python

# 3.1) No file is given as input, with / without
# flags

#     - Use input() function in python in while loop

# 3.2) Implement -n and -b flags

#     - Use the idx variable to increment numbers and print them for each line
#     - Check if line is empty or not depending on the flag

# 3.3) Multiple files are given as input

#     - Read each file with open() function
#     - Concatenate them as strings
#     - print them

from argparse import ArgumentParser

catparser = ArgumentParser(prog="cat", usage="%(prog)s [options] blank / filename ")

# catparser.add_argument(
#     " ", "--blank", help="Prints input from standard input", default=None
# )

catparser.add_argument(
    "-n",
    help="Prints the line number of all lines in the file or stdin",
    nargs="*",
    default=None,
)
catparser.add_argument(
    "-b", help="Prints line number for non empty lines", nargs="*", default=None
)

catparser.add_argument(
    "-vE",
    help="Prints the content and show end of lines with $",
    nargs="*",
    default=None,
)

catparser.add_argument(
    "-bvE",
    help="Prints the content with line number and show end of lines with $",
    nargs="*",
    default=None,
)

catparser.add_argument("args", nargs="*", help="Takes one or more files")

cli = catparser.parse_args()


def process_file_eol(filename):
    """Prints the file contents without line numbers & with eol with $"""
    with open(filename) as nonum:
        for line in nonum.readlines():
            print(line.replace("\n", "$"))


def process_file_nonum(filename):
    """Prints the file contents without line numbers"""
    with open(filename) as nonum:
        for line in nonum.readlines():
            if line != "\n":
                print(line, end="")


def process_file_num(filename):
    """Prints the file contents with line numbers
    for non empty lines"""
    with open(filename) as num:
        idx = 1
        for line in num.readlines():
            if line != "" and line != "\n":
                print(f"{idx} {line}", end="")
                idx += 1


def process_file_num_eol(filename):
    """Prints the file contents with line numbers
    for non empty lines"""
    with open(filename) as num:
        idx = 1
        for line in num.readlines():
            if line != "" and line != "\n":
                replaceline = line.replace("\n", "$")
                print(f"{idx} {replaceline}")
                idx += 1


def process_file_allline(filename):
    """Prints the file contents with line numbers for all lines"""
    with open(filename) as allline:
        for idx, line in enumerate(allline.readlines()):
            print(f"{idx} {line}", end="")


def process_file_allline_eol(filename):
    """Prints the file contents with line numbers & eol marker for all lines"""
    with open(filename) as allline:
        for idx, line in enumerate(allline.readlines()):
            replaceline = line.replace("\n", "$")
            print(f"{idx} {replaceline}")


def ask_input_nonum():
    """Echos the input back to the user"""
    while True:
        temp = input()
        print(temp)


def add_num(text: str, idx: int):
    if text != "\n":
        out = f"{idx} {text}"
        return out


def ask_input_num():
    """Echos the input back to user with numbers"""
    idx = 0
    while True:
        temp = input()
        if temp != "\n":
            print(f"{idx} {temp}")
            idx += 1


def ask_input_num_eol():
    """Echos the input back to user with numbers and eol markers"""
    idx = 0
    while True:
        temp = input()
        if temp != "\n":
            print(f"{idx} {temp}$")
            idx += 1
        else:
            print("$")


def ask_input_num_all():
    """Echos the input back to user with numbers for empty lines also"""
    idx = 0
    while True:
        temp = input()
        print(f"{idx} {temp}")
        idx += 1


def ask_input_eol():
    """Echos the input back to user with eol marked with $"""
    while True:
        temp = input()
        print(f"{temp}$")


print(cli.n)
print(cli.b)
print(cli.args)
print(cli.vE)
print(cli.bvE)


# if there is one file or many files concatenate their outputs
# create some files

if cli.n is None and cli.b is None and len(cli.args) > 0:
    for file in cli.args:
        process_file_nonum(file)

elif cli.b is not None:
    if len(cli.b) > 0:
        for file in cli.b:
            process_file_num(file)
    else:
        ask_input_num()

elif cli.n is not None:
    if len(cli.n) > 0:
        for file in cli.n:
            process_file_allline(file)
    else:
        ask_input_num_all()

elif cli.vE is not None:
    if len(cli.vE) > 0:
        for file in cli.vE:
            process_file_eol(file)
    else:
        ask_input_eol()

elif cli.bvE is not None:
    if len(cli.bvE) > 0:
        for file in cli.bvE:
            process_file_num_eol(file)
    else:
        ask_input_num_eol()
else:
    ask_input_nonum()
