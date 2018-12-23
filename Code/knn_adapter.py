import random

from Code.distance import *
from Code.records import *
from Code.knn import *


class KnnAdapter:
    config = {
        "k": 5,
        "metric": "euclides",
        "train": "train",
        "percentage_split": 0.25,
        "decision_index": -1,
        "file": "..\\Resource\\bezdekIris.data"
    }

    def __init__(self, config):
        self.config = config

    def run(self):
        records = self.parse_csv(self.config["file"])
        self.parse_records(records)
        data_sets = self.setup_train_sets(records)
        distance_calculator = self.get_distance_calculator(self.config["metric"])

        print('K : ' + str(self.config['k']))
        print('--------------------')

        accuracy_total = 0.0
        iteration = 0
        while len(data_sets) >= 2:
            # Counter
            iteration = iteration + 1
            print('--------------------')
            print('Iteration : ' + str(iteration))

            # K-nn Process
            knn = Knn(data_sets, records, self.config["k"], distance_calculator)
            accuracy = knn.test()
            accuracy_total += accuracy
            # Delete data set
            del data_sets[0:2]
        print('--------------------')
        accuracy_total = accuracy_total / iteration
        print('FINAL ACCURACY : ' + str(accuracy_total) + " %")

    @staticmethod
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

    def parse_records(self, records):
        decision_index = self.config['decision_index']
        if decision_index == -1:
            decision_index = records.column_numbers - 1

        for record in records.raw_rows:
            records.keys.append(record[decision_index])
            formatted_record = []
            value_index = -1
            for value in record:
                value_index += 1
                if value_index == decision_index:
                    continue
                number_value = float(value)
                formatted_record.append(number_value)

            records.rows.append(formatted_record)

        records.rows_length = len(records.keys)
        pass

    @staticmethod
    def split_list(a_list, split_index):
        return a_list[:split_index], a_list[split_index:]

    def setup_train_sets(self, records):
        record_keys = []
        for x in range(records.rows_length):
            record_keys.append(x)

        train_sets = []
        if self.config['train'] == 'train':
            train_sets.append(record_keys)
            train_sets.append(record_keys)
        elif self.config['train'] == 'split':
            random.shuffle(record_keys)
            split_index = int(records.rows_length * self.config['percentage_split'])
            split_keys = self.split_list(record_keys, split_index)
            train_sets.append(split_keys[1])
            train_sets.append(split_keys[0])
        elif self.config['train'] == 'cross':
            iteration = self.config['cross_iteration']
            train_sets = self.cut_list(record_keys, iteration)

        # print('train set: ' + str(len(train_sets[0])))
        # print('test set: ' + str(len(train_sets[1])))
        return train_sets

    @staticmethod
    def get_distance_calculator(param):
        if param == 'euclides':
            return EuclideanDistanceCalculator()
        return ManhattanDistanceCalculator()

    @staticmethod
    def cut_list(record_keys, iteration):
        cut_size = int(len(record_keys) / iteration)
        print('Cross test set size: ' + str(cut_size))

        results = []
        for i in range(iteration):
            clone_keys = record_keys.copy()
            start_index = i * cut_size
            end_index = start_index + cut_size - 1
            cut_part = clone_keys[start_index:end_index]
            del clone_keys[start_index:end_index]
            results.append(clone_keys)
            results.append(cut_part)

        return results
