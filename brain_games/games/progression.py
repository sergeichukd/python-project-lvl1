from random import randint


SPEC_INFO = "What number is missing in the progression?"
ROUNDS_NUMBER = 3


def make_a():
    return randint(0, 100)


def make_d():
    return randint(0, 20)


def make_gap_number():
    return randint(0, 9)


def make_question_answer():
    """Make Arithmetic Progression with length = PROGRESSION_LENGTH
    The progression has view: [a, a + d, a + 2d, ... , a + nd, ...]"""

    progression = ""
    gap_number = make_gap_number()
    a = make_a()
    d = make_d()
    right_answer = None
    for i in range(10):
        if i == gap_number:
            progression += ' ' + '..'
            right_answer = str(a + i * d)
            continue
        progression = progression + ' ' + str(a + i * d)
    return progression, right_answer
