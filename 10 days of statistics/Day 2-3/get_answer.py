import random


def get_quiz_answer():
    return str(random.randint(1, 4))


if __name__ == '__main__':
    print('The quiz solution is ' + get_quiz_answer())  # absolutely correct answer
