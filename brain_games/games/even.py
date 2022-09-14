from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def is_even(number):
    return number % 2 == 0


def get_question_and_correct_answer():
    question = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
