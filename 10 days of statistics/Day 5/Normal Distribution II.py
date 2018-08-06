import math
import sys


def standard_normal_cdf(x):
    result = (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
    return result


def standardize_value(value, mean, std):
    return (value - mean) / std


def main():
    line = sys.stdin.readline()
    mean, std = list(map(float, line.split(' ')))
    grade_A = float(sys.stdin.readline())
    grade_C = float(sys.stdin.readline())

    above_A = 1 - standard_normal_cdf(standardize_value(grade_A, mean, std))
    above_C = 1 - standard_normal_cdf(standardize_value(grade_C, mean, std))
    below_C = standard_normal_cdf(standardize_value(grade_C, mean, std))

    print("{0:.2f}".format(above_A * 100))
    print("{0:.2f}".format(above_C * 100))
    print("{0:.2f}".format(below_C * 100))


if __name__ == '__main__':
    main()
