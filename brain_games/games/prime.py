from random import randint


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_the_number_prime(number):
    checking_for_simplicity = 2
    while number % checking_for_simplicity != 0:
        checking_for_simplicity += 1
        return True
    return False


def prime_logic():
    question = randint(0, 100)
    if is_the_number_prime(question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
