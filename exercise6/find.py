#!/bin/python3

# implementing the find command in python

# find . -name "*.txt" -print
# find . -type d -print
# find . -name "*.rb" -exec rm {} \;

from argparse import ArgumentParser
from os import scandir
from subprocess import run
from glob import glob
from pathlib import Path

parser = ArgumentParser(
    prog="find",
    usage="""
 - find.py . -name "*.txt" -print

 - find.py . -type c -print
      File is of type c:
      d      directory
      f      regular file
      other file types can be implemented

 - find.py . -name "*.rb" -exec rm {} \\;
""",
)

# if the path is not specified then search currdir,
# if name is not provided then consider listing *.* recursively on given dir

parser.add_argument("path", default=".")
parser.add_argument("-name", help="File / Folder to be found", default="*.*")
parser.add_argument("-type", help="Type of the object being searched")
parser.add_argument("-print", help="Prints the file path", default=True)
parser.add_argument("-exec", help="Exec commands files/ folders found")

# below call to parse_args executes the parser
cliargs = parser.parse_args()

print(f"orig path: {cliargs.path}")
print(f"orig name: {cliargs.name}")
print(f"orig type: {cliargs.type}")
print(f"orig print: {cliargs.print}")

# define a function that takes a final_part of a path
# and the target matcher and returns bool


def find_name_in_path(path: str, obj_name: str, to_print: bool, obj_type: str = "f"):
    """Prints files and folders in the path that matches the obj_name
    and obj_type if to_print is true.
    Else returns the paths of the objects for further
    processing to exec_name_function
    obj_name can be:
        - *.ext
        - *.*
        - text*
        - *text
        - text
        ...
    """
    # took a detour to use glob and hit a road block
    # got distracted a lot by the beat songs
    # tried implementing the path_matcher then realized the file matching
    # become tedious. So moved back to using glob to begin with
    # assuming both directory and files can be listed
    file_paths = glob(f"{path}/{obj_name}", recursive=True)
    # stores the paths for returning
    print(f"{path}/{obj_name}")
    print(f"Raw path: {file_paths}")
    path_store = []
    for path in file_paths:
        # if to_print is true and final part matches obj_name
        if to_print and obj_type == "d":
            if Path(path).is_dir():
                print(path)
                continue
        elif to_print and not cliargs.exec:
            print(path)
        else:
            path_store.append(path)
    return path_store


if cliargs.path and cliargs.name and cliargs.print:
    find_name_in_path(path=cliargs.path, obj_name=cliargs.name, to_print=cliargs.print)

if cliargs.path and cliargs.name and cliargs.print and cliargs.exec:
    path_store = find_name_in_path(
        path=cliargs.path, obj_name=cliargs.name, to_print=cliargs.print
    )
    run_cmds = [cliargs.exec.replace("{}", val).split(" ") for val in path_store]
    # print(run_cmds)
    captures = []
    for cmd in run_cmds:
        outputs = run(cmd, check=True, capture_output=True)
        captures.append(outputs)
    print(captures)
