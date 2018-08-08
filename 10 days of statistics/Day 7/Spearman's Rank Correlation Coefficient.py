import math
import sys


def mean(arr):
    return sum(arr) / len(arr)


def std(mean, arr):
    arr = arr.copy()
    for i in range(len(arr)):
        arr[i] = pow(arr[i] - mean, 2)
    return pow(sum(arr) / len(arr), 0.5)


def rank_array(x):
    sorted_x = sorted(x)
    result = [[0 for i in range(len(x))] for j in range(2)]
    for i in range(len(x)):
        result[0][i] = x[i]
        result[1][i] = sorted_x.index(x[i]) + 1
    return result


def main():
    sys.stdin.readline()
    line = sys.stdin.readline().strip()
    x = list(map(float, line.split(' ')))
    line = sys.stdin.readline().strip()
    y = list(map(float, line.split(' ')))

    r_x = rank_array(x)
    r_y = rank_array(y)

    count = len(x)
    sum_sqr_d = 0

    for i in range(count):
        sum_sqr_d += (r_x[1][i] - r_y[1][i])**2

    spearman = 1 - (6 * sum_sqr_d / (count*(count**2 - 1)))


    print("{0:.3f}".format(spearman))


if __name__ == '__main__':
    main()
