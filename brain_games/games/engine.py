from brain_games import cli


def check_answer(guess, right_answer):
    return guess == right_answer


def run(module):
    name = cli.welcome_user(module.SPEC_INFO)
    for turn in range(module.ROUNDS_NUMBER):
        question, right_answer = module.make_question_answer()

        guess = cli.get_answer(question)

        if not check_answer(guess, right_answer):
            cli.show_wrong_answer_message(name, guess, right_answer)
            break
        cli.show_correct_answer_message()
    else:
        cli.show_you_win_message(name)
