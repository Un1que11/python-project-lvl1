#!/usr/bin/env python3
from brain_games.games.gcd import generate_gcd_mode, RULES
from brain_games.game_engine import start_the_game


def main():
    start_the_game(RULES, generate_gcd_mode)


if __name__ == '__main__':
    main()
