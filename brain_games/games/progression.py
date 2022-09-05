from random import randint


rule = 'What number is missing in the progression?'


def arithmetic_sequence(number, common_difference):
    arithmetic_progression = ''
    i = 0
    while i < 10:
        arithmetic_progression += str(number) + ' '
        number += common_difference
        i += 1
    return arithmetic_progression


def getting_string_progression(progression, missing_character):
    progression[missing_character] = '..'
    progression = ' '.join(progression)
    return progression


def progression_logic():
    item_position = randint(0, 9)
    first_number = randint(0, 20)
    common_difference = randint(1, 15)
    progression = arithmetic_sequence(first_number, common_difference)
    progression = progression.split()
    correct_answer = progression[item_position]
    progression = getting_string_progression(progression, item_position)
    question = progression
    return str(correct_answer), question
