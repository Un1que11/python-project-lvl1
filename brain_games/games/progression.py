from random import randint


RULES = 'What number is missing in the progression?'
ITEM_LOWER_LIMIT = 0
ITEM_UPPER_LIMIT = 4
DIFFERENCE_LOWER_LIMIT = 1
DIFFERENCE_UPPER_LIMIT = 15
TERM_LOWER_LIMIT = 0
TERM_UPPER_LIMIT = 20
PROGRESSION_LENGTH = 10


def create_arithmetic_sequence(initial_term, common_difference,
                               end_of_progression):
    return list(range(initial_term, end_of_progression, common_difference))


def create_string_progression(progression, index_of_missing_character):
    progression[index_of_missing_character] = '..'
    progression = ' '.join(map(str, progression))
    return progression


def save_question_and_correct_answer_of_progression():
    item_position = randint(ITEM_LOWER_LIMIT, ITEM_UPPER_LIMIT)
    initial_term = randint(TERM_LOWER_LIMIT, TERM_UPPER_LIMIT)
    common_difference = randint(DIFFERENCE_LOWER_LIMIT, DIFFERENCE_UPPER_LIMIT)
    end_of_progression = initial_term + common_difference * PROGRESSION_LENGTH
    progression = create_arithmetic_sequence(initial_term, common_difference, end_of_progression)
    correct_answer = progression[item_position]
    progression = create_string_progression(progression, item_position)
    question = progression
    return str(correct_answer), question
