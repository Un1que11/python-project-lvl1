from random import randint


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_the_number_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def even_logic():
    question = randint(0, 100)
    if is_the_number_even(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
