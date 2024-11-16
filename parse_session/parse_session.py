#!/bin/python3

from datetime import datetime
from typing import List
from argparse import ArgumentParser


def get_session(session_file: str):
    sess_count = 0
    with open(session_file) as sess:
        linedata = sess.readlines()
        for line in linedata:
            if "session" in line:
                sess_count += 1
    return sess_count


def get_intervals(session_file: str):
    intervals = []
    with open(session_file) as sess:
        ldata = sess.readlines()
        for line in ldata:
            if "session" in line:
                line_spc = line.split(" ")
                itrvl = [line_spc[2].strip(), line_spc[4].strip()]
                intervals.append(itrvl)
    return intervals


def get_interval_diff(interval: List[str]):
    s = datetime.strptime(interval[0], "%H:%M")
    e = datetime.strptime(interval[1], "%H:%M")
    return (e - s).total_seconds() / 60


def get_total_time(session_file: str):
    intervals = get_intervals(session_file)
    time_used = 0
    for intr in intervals:
        # print(intr)
        # print(get_interval_diff(intr))
        time_used += get_interval_diff(intr)
    return time_used


if __name__ == "__main__":
    sesparser = ArgumentParser(
        prog="Session Parsers",
        usage="""
    parse_session session_data.txt
    """,
    )
    sesparser.add_argument("file", help="provide file name")

    sesargs = sesparser.parse_args()

    if sesargs.file:
        print(f"Time used: {get_total_time(sesargs.file)}")
    else:
        print("Check usage...")
