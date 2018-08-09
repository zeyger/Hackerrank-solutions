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

    buffer = sys.stdin.readlines()
    x = [0 for i in range(len(buffer))]
    y = [0 for i in range(len(buffer))]

    for i in range(len(buffer)):
        x[i], y[i] = list(map(float, buffer[i].split(' ')))

    x_mean = mean(x)
    y_mean = mean(y)
    x_std = std(x_mean, x)
    y_std = std(y_mean, y)

    pearson = pearson_corr_coef(x, y)

    b = pearson * y_std / x_std
    a = y_mean - b * x_mean

    result = a + b * 80

    print("{0:.3f}".format(result))


if __name__ == '__main__':
    main()
