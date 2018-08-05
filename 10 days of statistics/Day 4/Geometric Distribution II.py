import sys


def geometric_distribution(fail_prob, fail_index):
    assert 1 >= fail_prob >= 0
    assert fail_index > 0
    succ_prob = 1 - fail_prob
    succ_prob_mult = pow(succ_prob, fail_index - 1)
    result = succ_prob_mult * fail_prob
    return result


def main():
    line = sys.stdin.readline()
    num, den = list(map(int, line.split(' ')))
    fail_index = int(input())
    result = 0
    for i in range(fail_index):
        result += geometric_distribution(num / den, i+1)

    print("{0:.3f}".format(result))


if __name__ == '__main__':
    main()
