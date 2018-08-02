import sys


def mean(arr):
    return sum(arr) / len(arr)


def std(mean, arr):
    for i in range(len(arr)):
        arr[i] = pow(arr[i] - mean, 2)
    return pow(sum(arr) / len(arr), 0.5)


def main():
    sys.stdin.readline()  # skip first line
    line = sys.stdin.readline()
    arr = list(map(int, line.split(' ')))
    standard_deviation = std(mean(arr), arr)
    print("{0:.1f}".format(standard_deviation))


if __name__ == '__main__':
    main()
