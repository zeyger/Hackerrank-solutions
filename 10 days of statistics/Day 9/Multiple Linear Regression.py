import sys

from sklearn import linear_model  # I AM A SCIENTIST MUAHAHAHAHAHAHAHAHAAHAHAHAHA


def mult_regression(x, y):
    """
    BOW BEFORE MY BEAUTIFULLY DESIGNED  AND
    *obviously not copypasted from hackerrank example*
    MASTERFULLY IMPLEMENTED REGRESSION ALGORITHM!
    """
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    a = lm.intercept_
    b = lm.coef_
    return [a, b]


def main():  # BEHOLD! THIS IS USAGE OF MY *some mumbling about how good my algo is* REGRESSION ALGORITHM!
    buffer = sys.stdin.readlines()
    m, n = list(map(int, buffer[0].split(' ')))

    x = [[0 for i in range(m)] for i in range(n)]
    y = [0 for i in range(n)]

    for i in range(n):
        values = list(map(float, buffer[i + 1].split(' ')))
        y[i] = values[-1]
        x[i] = values[:-1]

    a, b = mult_regression(x, y)  # I AM A GOD

    q = int(buffer[n + 1])
    for i in range(q):  # AND A SCIENTIST, OF COURSE
        result = a
        f = list(map(float, buffer[n + 1 + i + 1].split(' ')))  # I AM BOTH
        for j in range(len(f)):
            result += f[j] * b[j]
        print("{0:.2f}".format(result))  # I AM A GOD OF SCIENCE


if __name__ == '__main__':  # NO MORTAL PROCESS SHOULD BE ALLOWED TO CALL MY FUNCTION
    main()



# finally, 10 days of statistics are done.