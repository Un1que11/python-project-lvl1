from random import randint
from brain_games.game_engine.game_engine import start_the_game


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_logic():
    question = randint(0, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def even_game():
    start_the_game(rule, even_logic)
