import prompt


def welcome_user(spec_info):
    print("Welcome to the Brain Games!")
    print("{}\n".format(spec_info))
    name = prompt.string("May I have your name? ")
    print("Hello, {}!\n".format(name))
    return name


def ask_question(question):
    print(question)
    answer = prompt.string("Your answer: ")
    return answer

