import math
import sys


def standard_normal_cdf(x):
    result = (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
    return result

def standardize_value(value, mean, std):
    return (value - mean)/std


def main():
    line = sys.stdin.readline()
    mean, std = list(map(float, line.split(' ')))
    below_than = float(sys.stdin.readline())
    line = sys.stdin.readline()
    betwen_lower, betwen_upper = list(map(float, line.split(' ')))

    less_than_value = standard_normal_cdf(standardize_value(below_than, mean, std))
    betwen_values = standard_normal_cdf(standardize_value(betwen_upper, mean, std)) - \
                    standard_normal_cdf(standardize_value(betwen_lower, mean, std))

    print("{0:.3f}".format(less_than_value))
    print("{0:.3f}".format(betwen_values))


if __name__ == '__main__':
    main()
