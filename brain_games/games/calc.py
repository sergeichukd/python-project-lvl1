from random import randint, choice
from operator import mul, sub, add


spec_info = "What is the result of the expression?"


def generate_number():
    return randint(1, 100)


def generate_operator():
    operators = {'*': mul, '-': sub, '+': add}
    operator_key = choice(list(operators.keys()))
    return operator_key, operators[operator_key]


def calculate(arg0, arg1, operator):
    return operator(arg0, arg1)


def make_question_answer():
    arg0 = generate_number()
    arg1 = generate_number()
    operator_symbol, operator_fun = generate_operator()
    right_answer = calculate(arg0, arg1, operator_fun)
    return "{} {} {}".format(arg0, operator_symbol, arg1), str(right_answer)
