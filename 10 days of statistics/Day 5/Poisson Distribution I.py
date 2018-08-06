import math


def poisson_distribution(mean, expected):
    result = pow(mean, expected) * pow(math.e, -mean) / math.factorial(expected)
    return result


def main():
    mean = float(input())
    expected = int(input())
    result = poisson_distribution(mean, expected)
    print("{0:.3f}".format(result))


if __name__ == '__main__':
    main()
