import sys

from Code.distance import *


def get_position(record_row):
    return numpy.matrix(record_row)


class Knn:
    # 0: train set
    # 1: test set
    data_sets = []
    records = None
    neighbours_number = 5

    def __init__(self, data_sets, records, neighbours_number):
        self.neighbours_number = neighbours_number
        self.data_sets = data_sets
        self.records = records

    def test(self):
        for test_index in self.data_sets[1]:
            real_answer = self.records.keys[test_index]
            answers = self.find_answers(test_index)
            answer_dict = {}
            for answer in answers:
                if answer in answer_dict:
                    answer_dict[answer] = answer_dict[answer] + 1
                else:
                    answer_dict[answer] = 1

            best_answer = self.look_for_best_answer(answer_dict)
            print('find: ' + best_answer + ' real: ' + real_answer)



    def find_answers(self, test_index):
        question_row = self.records.rows[test_index]
        question_position = get_position(question_row)
        neighboards_list = self.data_sets[0].copy()
        answers_list = []
        for i in range(self.neighbours_number):
            nearest_neighboard_index = self.find_nearest_neighboard(question_position, neighboards_list)
            record_index = neighboards_list[nearest_neighboard_index]
            del neighboards_list[nearest_neighboard_index]
            answers_list.append(self.records.keys[record_index])
        return answers_list

    def find_nearest_neighboard(self, question_position, neighboards_list):
        nearest_neighboard = None
        nearest_distance = sys.float_info.max

        list_index = 0
        for neighboard_index in neighboards_list:
            neighboard = self.records.rows[neighboard_index]
            neighboard_position = get_position(neighboard)
            distance_current = distance_euclidean(question_position, neighboard_position)
            if distance_current < nearest_distance:
                nearest_distance = distance_current
                nearest_neighboard = list_index
            list_index = list_index + 1

        return nearest_neighboard

    def look_for_best_answer(self, answers_dict):
        best_answer = None
        best_count = 0
        for answer_key in answers_dict:
            answer_value = answers_dict[answer_key]
            if answer_value > best_count:
                best_answer = answer_key

        return best_answer
