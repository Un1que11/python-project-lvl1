#!/usr/bin/env python3
from brain_games.games.even import generate_even_mode, RULES
from brain_games.game_engine import start_the_game


def main():
    start_the_game(RULES, generate_even_mode)


if __name__ == '__main__':
    main()
