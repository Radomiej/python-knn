import math


def distance_euclidean(a, b):
    distance = 0.0
    for columnNumber in range(len(a)):
        diff = float(a[columnNumber]) - float(b[columnNumber])
        distance = distance + diff * diff

    distance = math.sqrt(distance)
    return distance


def distance_manhattan(a, b):
    n = len(a)
    return distancesum(a, n) + distancesum(b, n)


def distancesum(arr, n):
    # sorting the array.
    arr.sort()

    # for each point, finding
    # the distance.
    res = 0
    sum = 0
    for i in range(n):
        res += (arr[i] * i - sum)
        sum += arr[i]

    return res


class EuclideanDistanceCalculator:
    def calculate_distance(self, a, b):
        return distance_euclidean(a, b)


class ManhattanDistanceCalculator:
    def calculate_distance(self, a, b):
        return distance_manhattan(a, b)
