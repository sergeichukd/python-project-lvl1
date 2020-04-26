from random import randint
from brain_games.cli import ask_question


even_spec_info = "Answer 'yes' if number even otherwise answer 'no'."
questions_to_win = 3


def number_generator():
    return randint(1, 100)


def question_generator(number):
    return "Question: {}".format(number)


def is_even(number):
    return "yes" if (number % 2 == 0) else "no"


def check_answer(guess, truth):
    if guess == truth:
        message = "Correct!"
    else:
        message = "'{}' is wrong answer ;(. Correct answer is '{}'.".format(guess, truth)  # noqa: E501
    return message, guess == truth


def even_main(name):
    for turn in range(questions_to_win):
        number = number_generator()
        question = question_generator(number)
        truth = is_even(number)

        guess = ask_question(question)
        message, result = check_answer(guess, truth)
        print("{}".format(message))
        if not result:
            print("Let's try again, {}!".format(name))
            return

    print("Congratulations, {}!".format(name))
