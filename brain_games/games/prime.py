from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def is_the_number_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_prime_mode():
    question = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_the_number_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
