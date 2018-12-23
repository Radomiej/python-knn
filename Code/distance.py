import math


def distance_euclidean(a, b):
    distance = 0.0
    for columnNumber in range(len(a)):
        diff = float(a[columnNumber]) - float(b[columnNumber])
        distance = distance + diff * diff

    distance = math.sqrt(distance)
    return distance


def distance_manhattan(a, b):
    distance = 0.0
    for columnNumber in range(len(a)):
        diff = float(a[columnNumber]) - float(b[columnNumber])
        distance = distance + abs(diff)

    distance = math.sqrt(distance)
    return distance


class EuclideanDistanceCalculator:
    @staticmethod
    def calculate_distance(a, b):
        return distance_euclidean(a, b)


class ManhattanDistanceCalculator:
    @staticmethod
    def calculate_distance(a, b):
        return distance_manhattan(a, b)
