#!/bin/python3

# Need to find the properties of the files and folders
# need to refer to the https://docs.python.org/3/library/os.html#os.DirEntry
# use them further in the script to filter them.
# Following are the examples that help on the same

import os

listfiles = os.listdir(".")
for file in listfiles:
    print(type(file))  # will be string

# find if it is a folder
# find if it is a file

listfiles = os.scandir(".")
for file in listfiles:
    print(type(file))  # will DirEntry
    print(f"{file.name} is directory {file.is_dir()}")
    print(f"{file.name} is file {file.is_file()}")
    print(f"{file.name} path is {file.path}")
    statobj = os.stat(file.path)
    print(statobj)
