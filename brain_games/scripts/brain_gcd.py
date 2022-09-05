#!/usr/bin/env python3
from brain_games.games.gcd import gcd_logic, rule
from brain_games.games.game_engine import start_the_game


def main():
    start_the_game(rule, gcd_logic)


if __name__ == '__main__':
    main()
