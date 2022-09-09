#!/usr/bin/env python3
from brain_games.games.even import essence_and_solution_of_even, RULES
from brain_games.game_engine import start_the_game


def main():
    start_the_game(RULES, essence_and_solution_of_even)


if __name__ == '__main__':
    main()
