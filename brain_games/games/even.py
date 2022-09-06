from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def is_the_number_even(number):
    if number % 2 == 0:
        return True
    return False


def generate_even_mode():
    question = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_the_number_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
