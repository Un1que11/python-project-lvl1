from random import randint


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_the_number_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def prime_logic():
    question = randint(0, 100)
    correct_answer = 'yes' if is_the_number_prime(question) is True else 'no'
    return correct_answer, question
