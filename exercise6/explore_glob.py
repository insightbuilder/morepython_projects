# file to explore the glob package
# To note down the functions and their signatures that can be useful
# glob is doing the work of the os.listdir already and storing it in memory
# https://docs.python.org/3/library/glob.html

# import pandas as pd
import glob

glob.glob("./[0-9].*")

glob.glob("*.gif")

glob.glob("?.gif")

glob.glob("**/*.txt", recursive=True)

glob.glob("./**/", recursive=True)

# string extracted from cli args can be directly sent to glob
# iglob doesn't store the file details in the memory

# https://builtin.com/software-engineering-perspectives/glob-in-python
# set filepath to search
path = "/Users/tara/ml_guides/" + "**/*.ipynb"

# string to search for
search_term = "kdeplot"

# empty list to hold files that contain matching string
files_to_check = []

# looping through all the filenames returned
# set recursive = True to look in sub-directories too
for filename in glob.iglob(path, recursive=True):
    # adding error handling just in case!
    try:
        with open(filename) as f:
            # read the file as a string
            contents = f.read()
            # if the search term is found append to the list of files
            if search_term in contents:
                files_to_check.append(filename)
    except Exception:
        pass
