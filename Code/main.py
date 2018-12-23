import argparse

from Code.knn_adapter import KnnAdapter

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
    parser.add_argument("--k", type=int, default=5, help='Number of nearest neighbors. Default: 5')
    parser.add_argument("--metric", type=str, default='euclid',
                        help='Metrics distance compute strategy: euclid(default) or manhattan')
    parser.add_argument("--train", type=str, default='train',
                        help='Testing category: train(default), split, cross')
    parser.add_argument("--percentage_split", type=float, default=0.25, help='Percentage split: (0,1) where 1 == 100%')
    parser.add_argument("--cross_iteration", type=int, default=5,
                        help='Cross iteration count also indicate how many part of set will be use like training and test data')
    parser.add_argument("--decision_index", type=int, required=True, help='Index of column with decisions')
    parser.add_argument("--file", type=str, required=True, help='File with data', )
    args = parser.parse_args()
    command_setting['k'] = int(args.k)
    command_setting['metric'] = args.metric
    command_setting['train'] = args.train
    command_setting['percentage_split'] = args.percentage_split
    command_setting['cross_iteration'] = args.cross_iteration
    command_setting['decision_index'] = int(args.decision_index)
    command_setting['file'] = args.file


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
