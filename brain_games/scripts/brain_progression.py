#!/usr/bin/env python3
from brain_games.games.progression import generate_progression_mode, RULES
from brain_games.game_engine import start_the_game


def main():
    start_the_game(RULES, generate_progression_mode)


if __name__ == '__main__':
    main()
