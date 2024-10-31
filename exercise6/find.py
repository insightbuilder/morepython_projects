#!/bin/python3

# implementing the find command in python

# find . -name "*.txt" -print
# find . -type d -print
# find . -name "*.rb" -exec rm {} \;

from argparse import ArgumentParser
from os import scandir
from subprocess import run
from glob import glob

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

parser.add_argument("path", nargs="*", default=".")
parser.add_argument("-name", help="File / Folder to be found", default="*.*")
parser.add_argument("-type", help="Type of the object being searched")
parser.add_argument("-print", help="Prints the file path", default=True)
parser.add_argument("-exec", help="Command to be executed on files/ folders found")

# below call to parse_args executes the parser
cliargs = parser.parse_args()

print(f"orig path: {cliargs.path}")
print(f"orig name: {cliargs.name}")
print(f"orig type: {cliargs.type}")
print(f"orig print: {cliargs.print}")

# define a function that takes a final_part of a path
# and the target matcher and returns bool


def path_matcher(obj_name: str, final_part: str):
    """Returns True if the final_part matches the obj_name.
    obj_name can can be:
        - *.ext
        - *.*
        - text*
        - *text
        - text
        ...
    """
    # check if obj_name is of *.ext / *.* pattern
    if "." in obj_name:
        front, back = obj_name.split(".")
        if front == "*" and back == "*":
            return "all"


def find_name_in_path(path: str, obj_name: str, obj_type: str, to_print: bool):
    """Prints files and folders in the path that matches the obj_name and obj_type if to_print is true.
    Else returns the paths of the objects for further processing to exec_name_function
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
    file_paths = glob(path)
    # stores the paths for returning
    path_store = []
    for obj in file_objs:
        # if to_print is true and final part matches obj_name
        final_part = obj.path.split("\\")[-1]
        if to_print and last_part:
            print(obj.path)
        else:
            path_store.append(path)
