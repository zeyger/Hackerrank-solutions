import sys

import numpy as np


def mean(arr):
    return sum(arr) / len(arr)


def mode(arr):
    count = 0
    prev = None
    mode = 0
    mode_count = 0
    for elem in arr:
        if prev is not None:
            if elem == prev:
                count += 1
            else:
                if count > mode_count:
                    mode = prev
                    mode_count = count
                count = 1
                prev = elem
        else:
            prev = elem
            count += 1
    if count > mode_count:  # because elems doesn't change last time and don't trigger this check
        mode = prev
    return mode


def median(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        return arr[len(arr) // 2]


def main():
    sys.stdin.readline()  # skip first line
    line = sys.stdin.readline()
    arr = np.array(line.split(' ')).astype(int)
    arr.sort()
    men = "{0:.1f}".format(mean(arr)).replace('.0', '')
    med = "{0:.1f}".format(median(arr)).replace('.0', '')
    mod = mode(arr)
    print(men)
    print(med)
    print(mod)


if __name__ == '__main__':
    main()
