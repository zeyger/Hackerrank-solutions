import sys
import math


def nCr(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n - r)


def binomial_distribution(defect_prob, batch, defects_count):
    normal_prob = 1 - defect_prob
    normal_count = batch - defects_count
    result = nCr(batch, defects_count) * pow(defect_prob, defects_count) * pow(normal_prob, normal_count)
    return result


def main():
    line = sys.stdin.readline()
    defect_percent, batch = list(map(int, line.split(' ')))
    defect_prob = defect_percent/100

    no_more_than_two = 0
    at_least_two = 0
    for i in range(3):
        print(i)
        no_more_than_two += binomial_distribution(defect_prob, batch, i)

    for i in range(batch - 2 + 1):
        print(i+2)
        at_least_two += binomial_distribution(defect_prob, batch, i+2)


    print("{0:.3f}".format(no_more_than_two))
    print("{0:.3f}".format(at_least_two))

if __name__ == '__main__':
    main()
