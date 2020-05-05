import prompt


def welcome_user(spec_info):
    print("Welcome to the Brain Games!")
    print("{}".format(spec_info))
    print()
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    print()
    return name


def get_answer(question):
    print("Question: {}".format(question))
    answer = prompt.string("Your answer: ")
    return answer


def show_correct_answer_message():
    print("Correct")


def show_wrong_answer_message(name, guess, right_answer):
    print("'{}' is wrong answer ;(. Correct answer is '{}'.".format(guess, right_answer))  # noqa: E501
    print("Let's try again, {}!".format(name))


def show_you_win_message(name):
    print("Congratulations, {}!".format(name))
