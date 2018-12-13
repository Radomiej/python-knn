import numpy
from Code.records import *
from Code.distance import *

default_setting = {
    "k": "",
    "metric": "euclides",
    "train": "train",
    "decision_index": -1,
    "file": "..\\Resource\\bezdekIris.data"
}


def parse_csv(file):
    records_result = Records()
    with open(file, 'r') as my_file:
        data = my_file.read()

    print(data)
    raw_records = data.split('\n')
    for raw_record in raw_records:
        split_record = raw_record.split(',')
        if len(split_record) == 1:
            continue

        if len(split_record) > records_result.row_length:
            records_result.row_length = len(split_record)

        records_result.raw_rows.append(split_record)
        print(split_record)

    return records_result


def parse_records(records):
    ommited = default_setting['decision_index']
    if ommited == -1:
        ommited = records.row_length - 1

    for record in records.raw_rows:
        records.keys.append(record[ommited])
        formatted_record = []
        value_index = 0
        for value in record:
            if value_index == ommited:
                continue
            number_value = float(value)
            formatted_record.append(number_value)
            value_index += 1

        records.rows.append(formatted_record)

    pass


def main():
    print('test')
    records = parse_csv(default_setting["file"])
    parse_records(records)
    print('records count: ' + str(len(records.raw_rows)) + ' row length: ' + str(records.row_length))


def is_number(n):
    try:
        float(n)  # Type-casting the string to `float`.
        # If string is not a valid `float`,
        # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True


main()
