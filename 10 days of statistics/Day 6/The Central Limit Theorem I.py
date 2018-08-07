import math
import sys


def standard_normal_cdf(x):
    result = (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
    return result


def standardize_value(value, mean, std):
    return (value - mean) / std


def normal_cdf(x, mean, std):
    x = standardize_value(x, mean, std)
    return standard_normal_cdf(x)


def main():
    capability = float(sys.stdin.readline())
    count = int(sys.stdin.readline())
    atom_mean = float(sys.stdin.readline())
    atom_std = float(sys.stdin.readline())

    new_mean = count * atom_mean
    new_std = math.sqrt(count) * atom_std
    result = normal_cdf(capability, new_mean, new_std)
    print("{0:.4f}".format(result))


if __name__ == '__main__':
    main()
