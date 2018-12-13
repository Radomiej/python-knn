import numpy


def distance_euclidean(a, b):
    dist = numpy.linalg.norm(a - b)
    return dist


def distance_manhattan(x, y):
    n = len(x)
    return distancesum(x, n) + distancesum(y, n)


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