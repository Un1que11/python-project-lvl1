from random import randint, choice


operators = '+', '-', '*'
rule = 'What is the result of the expression?'


def calc_logic():
    first_number = randint(0, 100)
    operator = choice(operators)
    second_number = randint(0, 100)
    question = str(first_number) + ' ' + operator + ' ' + str(second_number)
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return str(correct_answer), question
