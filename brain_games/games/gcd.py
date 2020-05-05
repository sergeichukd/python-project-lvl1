import random


SPEC_INFO = "Find the greatest common divisor of given numbers."
ROUNDS_NUMBER = 3


def gcd(a, b):
    return gcd(b, a % b) if b else a


def generate_number():
    return random.randint(1, 100)


def make_question_answer():
    pair = [generate_number(), generate_number()]
    pair.sort(reverse=True)
    return "{} {}".format(*pair), str(gcd(*pair))
