import math


def maxDistance(arrays):
    smallest = arrays[0][0]
    biggest = arrays[0][-1]
    max_distance = 0

    for i in range(1, len(arrays)):
        arr = arrays[i]
        max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
        smallest = min(smallest, arr[0])
        biggest = max(biggest, arr[-1])


maxDistance([[0, 7], [1, 4]])
maxDistance([[1, 4], [0, 5]])
maxDistance([[1, 7], [0, 5]])
maxDistance([[1, 5], [3, 4]])
maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]])
