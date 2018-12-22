import argparse
import random

from Code.knn_adapter import KnnAdapter
from Code.records import *
from Code.knn import *


command_setting = {
    "k": 5,
    "metric": "euclides",
    "train": "train",
    "percentage_split": 0.25,
    "decision_index": -1,
    "file": "..\\Resource\\bezdekIris.data"
}


def parse_arguments():
    # print('parse arguments')
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int)
    parser.add_argument("--metric")
    parser.add_argument("--train")
    parser.add_argument("--percentage_split", type=float)
    parser.add_argument("--cross_iteration", type=int)
    parser.add_argument("--decision_index", type=int)
    parser.add_argument("--file")
    args = parser.parse_args()
    command_setting['k'] = int(args.k)
    command_setting['metric'] = args.metric
    command_setting['train'] = args.train
    command_setting['decision_index'] = int(args.decision_index)
    command_setting['file'] = args.file
    if args.percentage_split is not None:
        command_setting['percentage_split'] = args.percentage_split
    if args.cross_iteration is not None:
        command_setting['cross_iteration'] = args.cross_iteration


def main():
    parse_arguments()
    knn_adapter = KnnAdapter(command_setting)
    knn_adapter.run()


def is_number(n):
    try:
        float(n)  # Type-casting the string to `float`.
        # If string is not a valid `float`,
        # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True


main()
