import sys


def mean(arr):
    return sum(arr) / len(arr)


def std(mean, arr):
    arr = arr.copy()
    for i in range(len(arr)):
        arr[i] = pow(arr[i] - mean, 2)
    return pow(sum(arr) / len(arr), 0.5)


def pearson_corr_coef(x, y):
    assert len(x) == len(y)
    count = len(x)
    x_mean = mean(x)
    y_mean = mean(y)

    x_std = std(x_mean, x)
    y_std = std(y_mean, y)

    covariance = 0
    for i in range(count):
        covariance += (x[i] - x_mean) * (y[i] - y_mean)
    covariance = covariance / count
    pearson = covariance / (x_std * y_std)
    return pearson


def main():
    sys.stdin.readline()
    line = sys.stdin.readline().strip()
    x = list(map(float, line.split(' ')))
    line = sys.stdin.readline().strip()
    y = list(map(float, line.split(' ')))

    pearson = pearson_corr_coef(x, y)
    print("{0:.3f}".format(pearson))


if __name__ == '__main__':
    main()
