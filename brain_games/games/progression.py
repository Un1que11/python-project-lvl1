from random import randint
from brain_games.game_engine.game_engine import start_the_game


rule = 'What number is missing in the progression?'


def progression_logic():
    item_position = randint(0, 9)
    first_number = randint(0, 20)
    regularity = randint(1, 15)
    arithmetic_progression = ''
    i = 0
    while i < 10:
        arithmetic_progression += str(first_number) + ' '
        first_number += regularity
        i += 1
    arithmetic_progression = arithmetic_progression.split()
    correct_answer = arithmetic_progression[item_position]
    arithmetic_progression[item_position] = '..'
    arithmetic_progression = ' '.join(arithmetic_progression)
    question = arithmetic_progression
    return str(correct_answer), question


def progression_game():
    start_the_game(rule, progression_logic)
