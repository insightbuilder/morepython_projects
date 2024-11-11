from glob import glob
from pathlib import Path
import re


def process_file_nonum(filename: str):
    """Prints the file contents without line numbers"""
    no_newline = []
    with open(filename) as nonum:
        for line in nonum.readlines():
            if line != "\n":
                no_newline.append(line)
        return no_newline


def process_file_num(filename: str):
    """Prints the file contents with line numbers
    for non empty lines"""
    line_with_num = []
    with open(filename) as num:
        idx = 1
        for line in num.readlines():
            if line != "" and line != "\n":
                # print(f"{idx} {line}", end="")
                line_with_num.append(f"{idx} {line}")
                idx += 1
        return line_with_num


def process_file_eol(filename: str):
    """Prints the file contents without
    line numbers & with eol with $"""
    eol_no_lnum = []
    with open(filename) as nonum:
        for line in nonum.readlines():
            eol_no_lnum.append(line.replace("\n", "$"))
        return eol_no_lnum


def process_file_num_eol(filename: str):
    """Prints the file contents with line numbers
    for non empty lines"""
    nemp_eol_lnum = []
    with open(filename) as num:
        idx = 1
        for line in num.readlines():
            if line != "" and line != "\n":
                replaceline = line.replace("\n", "$")
                nemp_eol_lnum.append(f"{idx} {replaceline}")
                idx += 1
        return nemp_eol_lnum


def process_file_allline(filename: str):
    """Prints the file contents with line numbers for all lines"""
    all_line = []
    with open(filename) as allline:
        for idx, line in enumerate(allline.readlines()):
            all_line.append(f"{idx} {line}")
        return all_line


def process_file_allline_eol(filename):
    """Prints the file contents with line numbers & eol marker for all lines"""
    all_line_eol = []
    with open(filename) as allline:
        for idx, line in enumerate(allline.readlines()):
            replaceline = line.replace("\n", "$")
            all_line_eol.append(f"{idx} {replaceline}")
        return all_line_eol


def add_num(text: str, idx: int):
    if text != "\n":
        out = f"{idx} {text}"
        return out


def add_num_eol(text: str, idx: int):
    if text != "\n":
        print(f"{idx} {text}$")
        return idx + 1
    else:
        print("$")
        return idx


# Start find.py functions


def find_name_in_path(
    path: str, obj_name: str, to_print: bool, cliarg: bool, obj_type: str = "f"
):
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
        elif to_print and not cliarg:
            print(path)
        else:
            path_store.append(path)
    return path_store


def file_pattern_matcher(file_pattern: str, search_pattern: str):
    """Locates the files based on given pattern and reads the lines.
    Finds the lines that matches the search pattern"""
    print(f"Recieved file pattern: {file_pattern} and search pattern: {search_pattern}")
    files = glob(file_pattern)  # this will capture even if single file is given as list
    # print(f"Matched files: {files}")
    #     file_line = """[I 2024-10-21 17:19:37.083 ServerApp] Starting buffering for bc93e630-c608-441
    # d-bbb4-c6d3c5e73bf5:6a94bc89-9f9d-4d4a-8376-895a0ce6add1"""
    print(files)
    reobj = re.compile(search_pattern)
    #     matcher = reobj.search(file_line)
    #     print(f"Matched patterns: {matcher}")
    # start working on opening and reading files
    matched_objs = []
    for file in files:
        with open(file) as data:
            filelines = data.readlines()
            for line in filelines:
                # print(f"Before match: {line}")
                ptrn_search = reobj.search(line)
                # print(ptrn_search)
                if ptrn_search:
                    # print the line
                    # print(f"After match line: {line}")
                    print(f"Matched obj: {ptrn_search}")
                    matched_objs.append(ptrn_search.group())
            # print(matched_objs)
    return matched_objs


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
    take_sections = []
    for idx, line in enumerate(stdin):
        line = line.strip()
        # split the lines with delim
        line_splits = line.split(delim)
        # get the split_len
        split_len = len(line_splits)
        sec1 -= 1
        sec2 -= 1
        select_section = line_splits[sec1:sec2]
        take_sections.append(select_section)
    return " ".join(take_sections)


# todo test exception capture
# todo test file read parse capture
def parse_file(file_name: str, delim: str, sections: str):
    # get the sections
    sec1m, sec2m = sections.split("-")
    try:
        sec1m = int(sec1m)
        sec2m = int(sec2m)

        # read the file lines
        take_section = []
        with open(file_name) as cutd:
            yourlines = cutd.readlines()
            # process the lines one by one
            for line in yourlines:
                # split the lines with delim
                line_splits = line.split(delim)
                # print(line_splits)
                # get the split_len
                split_len = len(line_splits)
                # sec2 is greater than line_splits len,
                if sec2m > split_len:
                    # bring the sec2 to split_len
                    # this will be a challenge when lines have different sections
                    sec1 = sec1m - 1
                    sec2 = split_len
                else:
                    sec1 = sec1m - 1
                    sec2 = sec2m - 1
                # print(sec1, sec2)
                select_section = line_splits[sec1:sec2]
                # print(select_section)
                take_section.append(select_section)
            return take_section

    except Exception as e:
        return "There is issue in args"
