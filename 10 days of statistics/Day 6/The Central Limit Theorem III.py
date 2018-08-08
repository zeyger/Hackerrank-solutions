import math
import sys


def margin_of_error(n, std, z_score):
    # https://www.thoughtco.com/margin-of-error-formula-3126275, thank you ferpitol
    return z_score * std / math.sqrt(n)


def main():
    sample_size = int(sys.stdin.readline())
    population_mean = float(sys.stdin.readline())
    population_std = float(sys.stdin.readline())
    distribution_percentage = float('0' + sys.stdin.readline())
    z_score = float(sys.stdin.readline())

    A = population_mean - margin_of_error(sample_size, population_std, z_score)
    B = population_mean + margin_of_error(sample_size, population_std, z_score)

    print("{0:.2f}".format(A))
    print("{0:.2f}".format(B))


if __name__ == '__main__':
    main()
