from random import randint


RULES = 'Find the greatest common divisor of given numbers.'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def calculate_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    gcd = first_number + second_number
    return gcd


def get_question_and_correct_answer():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = str(first_number) + ' ' + str(second_number)
    correct_answer = calculate_gcd(first_number, second_number)
    return str(correct_answer), question
