import random
import operator


SPEC_INFO = "What is the result of the expression?"
ROUNDS_NUMBER = 3
OPERATIONS = {'*': operator.mul, '-': operator.sub, '+': operator.add}


def generate_number():
    return random.randint(1, 100)


def generate_operator():
    operator_key = random.choice(list(OPERATIONS.keys()))
    return operator_key, OPERATIONS[operator_key]


def calculate(arg0, arg1, arg_operator):
    return arg_operator(arg0, arg1)


def make_question_answer():
    arg0 = generate_number()
    arg1 = generate_number()
    operator_symbol, operator_fun = generate_operator()
    right_answer = calculate(arg0, arg1, operator_fun)
    return "{} {} {}".format(arg0, operator_symbol, arg1), str(right_answer)
