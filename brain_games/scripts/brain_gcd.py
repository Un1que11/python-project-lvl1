#!/usr/bin/env python3
from brain_games.games.gcd import save_question_and_correct_answer_of_gcd, \
    RULES
from brain_games.game_engine import start_the_game


def main():
    start_the_game(RULES, save_question_and_correct_answer_of_gcd)


if __name__ == '__main__':
    main()
