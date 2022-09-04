from random import randint
from brain_games.game_engine.game_engine import start_the_game


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_logic():
    question = randint(0, 100)
    i = 2
    while question % i != 0:
        i += 1
    if i == question:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def prime_game():
    start_the_game(rule, prime_logic)
