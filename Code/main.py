import numpy

default_setting = {
    "k": "",
    "metric": "euclides",
    "train": "train",
    "decision_index": -1,
    "file": "..\\Resource\\bezdekIris.data"
}


def parse_csv(file):
    data = ''
    with open(file, 'r') as myfile:
        data = myfile.read()

    print(data)
    raw_records = data.split('\n')
    records = []
    for raw_record in raw_records:
        split_record = raw_record.split(',')
        if len(split_record) == 1:
            continue
        records.append(split_record)
        print(split_record)

    print('hello')


def main():
    print('test')
    records = parse_csv(default_setting["file"])


def distance_euclidean(a, b):
    dist = numpy.linalg.norm(a - b)
    return dist


main()
