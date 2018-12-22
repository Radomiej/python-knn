import argparse
import random
from Code.records import *
from Code.knn import *


default_setting = {
    "k": 5,
    "metric": "euclides",
    "train": "train",
    "percentage_split": 0.25,
    "decision_index": -1,
    "file": "..\\Resource\\bezdekIris.data"
}


def parse_arguments():
    print('parse arguments')
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int)
    parser.add_argument("--metric")
    parser.add_argument("--train")
    parser.add_argument("--percentage_split", type=float)
    parser.add_argument("--decision_index", type=int)
    parser.add_argument("--file")
    args = parser.parse_args()
    default_setting['k'] = int(args.k)
    default_setting['metric'] = args.metric
    default_setting['train'] = args.train
    default_setting['decision_index'] = int(args.decision_index)
    default_setting['file'] = args.file
    default_setting['percentage_split'] = args.percentage_split


def parse_csv(file):
    records_result = Records()
    with open(file, 'r') as my_file:
        data = my_file.read()

    # print(data)
    raw_records = data.split('\n')
    for raw_record in raw_records:
        split_record = raw_record.split(',')
        if len(split_record) == 1:
            continue

        if len(split_record) > records_result.column_numbers:
            records_result.column_numbers = len(split_record)

        records_result.raw_rows.append(split_record)
        # print(split_record)

    return records_result


def parse_records(records):
    decision_index = default_setting['decision_index']
    if decision_index == -1:
        decision_index = records.column_numbers - 1

    for record in records.raw_rows:
        records.keys.append(record[decision_index])
        formatted_record = []
        value_index = 0
        for value in record:
            if value_index == decision_index:
                continue
            number_value = float(value)
            formatted_record.append(number_value)
            value_index += 1

        records.rows.append(formatted_record)

    records.rows_length = len(records.keys)
    pass


def split_list(a_list, split_index):
    return a_list[:split_index], a_list[split_index:]


def setup_train_sets(records):
    record_keys = []
    for x in range(records.rows_length):
        record_keys.append(x)

    train_sets = []
    if default_setting['train'] == 'train':
        train_sets.append(record_keys)
        train_sets.append(record_keys)
    elif default_setting['train'] == 'split':
        random.shuffle(record_keys)
        split_index = int(records.rows_length * default_setting['percentage_split'])
        split_keys = split_list(record_keys, split_index)
        train_sets.append(split_keys[0])
        train_sets.append(split_keys[1])

    print('train set: ' + str(len(train_sets[0])))
    print('test set: ' + str(len(train_sets[1])))
    return train_sets





def main():
    parse_arguments()
    records = parse_csv(default_setting["file"])
    parse_records(records)
    data_sets = setup_train_sets(records)
    knn = Knn(data_sets, records, default_setting["k"])
    knn.test()
    print('records count: ' + str(len(records.raw_rows)) + ' row length: ' + str(records.column_numbers))


def is_number(n):
    try:
        float(n)  # Type-casting the string to `float`.
        # If string is not a valid `float`,
        # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True


main()
