import sys


def median(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        return arr[len(arr) // 2]


def main():
    sys.stdin.readline()  # skip first line
    line = sys.stdin.readline()
    arr = list(map(int, line.split(' ')))
    arr.sort()

    q1 = median(arr[:len(arr) // 2])  
    q2 = median(arr)
    q3 = 0
    
    arr_len_even = len(arr) % 2 == 0
    if arr_len_even:  # 0 1 2 3 4 5
        q3 = median(arr[len(arr) // 2:])  # 3 4 5
    else:  # 0 1 2 3 4 5 6
        q3 = median(arr[len(arr) // 2 + 1:])  # 4 5 6

    print(int(q1))
    print(int(q2))
    print(int(q3))


if __name__ == '__main__':
    main()
