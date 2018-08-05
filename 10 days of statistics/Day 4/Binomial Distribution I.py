import math
import sys


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def binomial_distribution(boys, girls, n, m):
    b_prob = boys / (boys + girls)
    g_prob = girls / (boys + girls)
    result = nCr(n, m) * pow(b_prob, m) * pow(g_prob, n - m)
    return result


def main():
    line = sys.stdin.readline()
    boys, girls = list(map(float, line.split(' ')))

    result = binomial_distribution(boys, girls, 6, 3) + \
             binomial_distribution(boys, girls, 6, 4) + \
             binomial_distribution(boys, girls, 6, 5) + \
             binomial_distribution(boys, girls, 6, 6)

    # check if binomial_distribution is working right
    # validation should be equal to 1
    validation = binomial_distribution(boys, girls, 6, 0) + \
                 binomial_distribution(boys, girls, 6, 1) + \
                 binomial_distribution(boys, girls, 6, 2) + \
                 binomial_distribution(boys, girls, 6, 3) + \
                 binomial_distribution(boys, girls, 6, 4) + \
                 binomial_distribution(boys, girls, 6, 5) + \
                 binomial_distribution(boys, girls, 6, 6)

    print("{0:.3f}".format(result))


if __name__ == '__main__':
    main()
