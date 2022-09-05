from random import randint


rule = 'Find the greatest common divisor of given numbers.'


def gcd_of_two_numbers(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    gcd = first_number + second_number
    return gcd


def gcd_logic():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    question = str(first_number) + ' ' + str(second_number)
    correct_answer = gcd_of_two_numbers(first_number, second_number)
    return str(correct_answer), question


def gcd_game():
    start_the_game(rule, gcd_logic)
