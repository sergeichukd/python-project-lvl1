from math import sqrt, ceil
import random


SPEC_INFO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ROUNDS_NUMBER = 3


def generate_number():
    return random.randint(0, 1000)


def optimize_prime_search(fun):
    def inner(number):
        if number == 2 or number == 3:
            return True
        elif not (number % 2 and number % 3 and number):
            return False
        else:
            return fun(number)
    return inner


@optimize_prime_search
def is_prime(number):
    if number < 2:
        return False

    ceil_least_divider = ceil(sqrt(number))
    for divider in range(2, ceil_least_divider + 1):
        if number % divider == 0:
            return False
    return True


def make_question_answer():
    number = generate_number()
    right_answer = is_prime(number)
    return str(number), 'yes' if right_answer else 'no'
