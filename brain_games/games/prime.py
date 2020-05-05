from math import sqrt, ceil
import random


SPEC_INFO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ROUNDS_NUMBER = 3


def generate_number():
    return random.randint(0, 1000)


def is_2_or_3(number):
    return number == 2 or number == 3


def is_divisible_by(number, divider):
    return number % divider == 0


def optimize_prime_search(fun):
    def inner(number):
        if is_2_or_3(number):
            number_is_prime = True
        elif is_divisible_by(number, 2) or is_divisible_by(number, 3):
            number_is_prime = False
        else:
            number_is_prime = fun(number)

        return number_is_prime
    return inner


@optimize_prime_search
def is_prime(number):
    if number < 2:
        return False
    # Because the least common divider of N is <= sqrt(N)
    ceil_least_divider = ceil(sqrt(number))
    for divider in range(2, ceil_least_divider + 1):
        if is_divisible_by(number, divider):
            return False
    return True


def make_question_answer():
    number = generate_number()
    right_answer = is_prime(number)
    return str(number), 'yes' if right_answer else 'no'
