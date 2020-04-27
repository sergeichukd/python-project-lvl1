from brain_games import cli


questions_to_win = 3


def check_answer(guess, right_answer):
    return guess == right_answer


def run(module):
    name = cli.welcome_user(module.spec_info)
    for turn in range(questions_to_win):
        question, right_answer = module.make_question_answer()

        guess = cli.get_answer(question)

        if not check_answer(guess, right_answer):
            cli.show_wrong_answer_message(name, guess, right_answer)
            break
        cli.show_correct_answer_message()
    else:
        cli.show_you_win_message(name)
