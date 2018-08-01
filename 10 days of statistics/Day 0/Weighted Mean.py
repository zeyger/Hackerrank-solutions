import sys


def weighted_mean(arr, weights):
    assert len(arr) == len(weights)

    sum_weights = sum(weights)
    sum_elems = 0
    for i in range(len(arr)):
        sum_elems += arr[i] * weights[i]
    return sum_elems / sum_weights


def main():
    sys.stdin.readline()  # skip first line
    line = sys.stdin.readline()
    arr = list(map(int, line.split(' ')))

    line = sys.stdin.readline()
    weights = list(map(int, line.split(' ')))

    print("{0:.1f}".format(weighted_mean(arr, weights)))


if __name__ == '__main__':
    main()
