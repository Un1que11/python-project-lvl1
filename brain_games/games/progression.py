from random import randint


RULES = 'What number is missing in the progression?'
ITEM_LOWER_LIMIT = 0
ITEM_UPPER_LIMIT = 4
DIFFERENCE_LOWER_LIMIT = 1
DIFFERENCE_UPPER_LIMIT = 15
TERM_LOWER_LIMIT = 0
TERM_UPPER_LIMIT = 20
LENGTH_LOWER_LIMIT = 5
LENGTH_UPPER_LIMIT = 10


def creating_arithmetic_sequence(initial_term, common_difference,
                                 progression_length):
    arithmetic_progression = ''
    i = 0
    while i < progression_length:
        arithmetic_progression += str(initial_term) + ' '
        initial_term += common_difference
        i += 1
    return arithmetic_progression.split()


def creating_string_progression(progression, index_of_missing_character):
    progression[index_of_missing_character] = '..'
    progression = ' '.join(progression)
    return progression


def generate_progression_mode():
    item_position = randint(ITEM_LOWER_LIMIT, ITEM_UPPER_LIMIT)
    initial_term = randint(TERM_LOWER_LIMIT, TERM_UPPER_LIMIT)
    common_difference = randint(DIFFERENCE_LOWER_LIMIT, DIFFERENCE_UPPER_LIMIT)
    progression_length = randint(LENGTH_LOWER_LIMIT, LENGTH_UPPER_LIMIT)
    progression = creating_arithmetic_sequence(initial_term,
                                               common_difference,
                                               progression_length)
    correct_answer = progression[item_position]
    progression = creating_string_progression(progression, item_position)
    question = progression
    return str(correct_answer), question
