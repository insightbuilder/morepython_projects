#!/bin/python

# script will take a list of numbers, which are feature counts of the past
# and provide the feature count that needs to be implementend in next
# project

# the script will calculate the mean, stdev of the given numbers
# and provide the range between which the next feature count must be
# and provide the current mean

from argparse import ArgumentParser
import numpy as np


if __name__ == "__main__":
    tgt_parser = ArgumentParser(
        prog="Feature Calculator",
        usage="""
    ./calc_feature_count.py 2 5 7 9 8 6
    Target 6 features to be implemented
    """,
    )

    tgt_parser.add_argument(
        "nums", help="Provide a past series of features implemented", nargs="*"
    )
    tgt_args = tgt_parser.parse_args()
    print(tgt_args)
    # make array of numbers
    np_array = []

    if len(tgt_args.nums) > 0:
        for idx, num in enumerate(tgt_args.nums):
            try:
                np_array.append(int(num))
            except Exception as e:
                print(f"Provide integer or whole numbers: {e}")

    # get the mean
    mean = np.mean(np_array)
    std = np.std(np_array)

    print(f"The mean of past implementation is {mean}")
    print(f"The future count must be between is {mean + std} and {mean - std}")
