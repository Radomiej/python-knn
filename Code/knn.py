import sys


class Knn:
    # 0: train set
    # 1: test set
    data_sets = []
    records = None
    neighbours_number = 5
    distance_calculator = None

    def __init__(self, data_sets, records, neighbours_number, distance_calculator):
        self.distance_calculator = distance_calculator
        self.neighbours_number = neighbours_number
        self.data_sets = data_sets
        self.records = records

    def test(self):
        valid_test = 0
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
            if best_answer == real_answer:
                valid_test = valid_test + 1
            # print('| ' + best_answer + ' | ' + real_answer + " |")
            # print('find: ' + best_answer + ' real: ' + real_answer)
        accuracy = float(valid_test) / len(self.data_sets[1]) * 100
        wrong = len(self.data_sets[1]) - valid_test
        print('-------------------------------------------------------------')
        print(
            '| Training set: ' + str(len(self.data_sets[0])) + ' | Testing set: ' + str(len(self.data_sets[1])) + " |")
        print('| OK: ' + str(valid_test) + ' | Fail: ' + str(wrong) + ' | accuracy: ' + str(accuracy) + ' % |')
        return accuracy

    def find_answers(self, test_index):
        question_row = self.records.rows[test_index]
        question_position = self.get_position(question_row)
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
            neighboard_position = self.get_position(neighboard)
            # distance_current = distance_euclidean(question_position, neighboard_position)
            distance_current = self.distance_calculator.calculate_distance(question_position, neighboard_position)
            if distance_current < nearest_distance:
                nearest_distance = distance_current
                nearest_neighboard = list_index
            list_index = list_index + 1

        return nearest_neighboard

    @staticmethod
    def look_for_best_answer(answers_dict):
        best_answer = None
        best_count = 0
        for answer_key in answers_dict:
            answer_value = answers_dict[answer_key]
            if answer_value > best_count:
                best_answer = answer_key
                best_count = answer_value

        return best_answer

    @staticmethod
    def get_position(record_row):
        return record_row.copy()
