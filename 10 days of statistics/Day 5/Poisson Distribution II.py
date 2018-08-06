import sys

def sqr_poisson_mean(mean):
    return mean + pow(mean, 2)

def main():
    line = sys.stdin.readline()
    mean_x, mean_y = list(map(float, line.split(' ')))
    result_x = 160 + 40 * sqr_poisson_mean(mean_x)
    result_y = 128 + 40 * sqr_poisson_mean(mean_y)
    print("{0:.3f}".format(result_x))
    print("{0:.3f}".format(result_y))


if __name__ == '__main__':
    main()
