from random import randint


spec_info = "Answer 'yes' if number even otherwise answer 'no'."


def generate_number():
    return randint(1, 100)


def is_even(number):
    return "yes" if (number % 2 == 0) else "no"


def make_question_answer():
    number = generate_number()
    right_answer = is_even(number)
    return number, right_answer
