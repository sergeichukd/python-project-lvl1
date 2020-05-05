import random


SPEC_INFO = "Answer 'yes' if number even otherwise answer 'no'."
ROUNDS_NUMBER = 3


def generate_number():
    return random.randint(1, 100)


def is_even(number):
    return "yes" if (number % 2 == 0) else "no"


def make_question_answer():
    number = generate_number()
    right_answer = is_even(number)
    return number, right_answer
