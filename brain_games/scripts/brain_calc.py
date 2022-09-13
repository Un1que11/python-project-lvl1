#!/usr/bin/env python3
from brain_games.games.calc import save_question_and_correct_answer_of_calc, \
    RULES
from brain_games.game_engine import run_the_game


def main():
    run_the_game(RULES, save_question_and_correct_answer_of_calc)


if __name__ == '__main__':
    main()
