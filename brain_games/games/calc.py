from random import randint, choice


OPERATORS = '+', '-', '*'
RULES = 'What is the result of the expression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def essence_and_solution_of_calc():
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    operator = choice(OPERATORS)
    second_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = str(first_number) + ' ' + operator + ' ' + str(second_number)
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return str(correct_answer), question
