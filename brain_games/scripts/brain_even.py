from brain_games.games.even_logic import even_main, even_spec_info
from brain_games.cli import welcome_user


def main():
    name = welcome_user(even_spec_info)
    even_main(name)


if __name__ == "__main__":
    main()
