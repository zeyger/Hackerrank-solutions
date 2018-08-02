import sys


def median(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        return arr[len(arr) // 2]


def main():
    sys.stdin.readline()  # skip first line
    line = sys.stdin.readline()
    arr_set = list(map(int, line.split(' ')))

    line = sys.stdin.readline()
    weights = list(map(int, line.split(' ')))

    arr = list()

    for i in range(len(arr_set)):
        for count in range(weights[i]):
            arr.append(arr_set[i])



    arr.sort()
    arr_len_even = len(arr) % 2 == 0

    q1 = median(arr[:len(arr) // 2])  # 0 1 2

    if arr_len_even:  # 0 1 2 3 4 5
        q3 = median(arr[len(arr) // 2:])  # 3 4 5
    else:  # 0 1 2 3 4 5 6
        q3 = median(arr[len(arr) // 2 + 1:])  # 3 4 5
    print("{0:.1f}".format(q3 - q1))


if __name__ == '__main__':
    main()
