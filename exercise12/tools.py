from glob import glob
from pathlib import Path


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
