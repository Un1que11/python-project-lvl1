import prompt
from random import randint, choice


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello {name}!')
    return name


def answers():
    answer = prompt.string('Your answer: ')
    return answer


def cycle():
    counter = (1, 2, 3)
    for i in counter:
        return


def even_logic():
    number = randint(0, 100)
    print('Question: ' + str(number))
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def calc_logic():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operation = ('+', '-', '*')
    random_operation = choice(operation)
    print(f'Question: {first_number} {random_operation} {second_number}')
    if random_operation == '+':
        correct_answer = first_number + second_number
    elif random_operation == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    return correct_answer


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = (1, 2, 3)
    for i in counter:
        correct_answer = even_logic()
        answer = answers()
        if str(answer.lower()) == str(correct_answer.lower()):
            print('Correct!')
        else:
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {name}!''')
            return
    print(f'Congratulations {name}!')


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    counter = (1, 2, 3)
    for i in counter:
        correct_answer = calc_logic()
        answer = answers()
        if str(answer) == str(correct_answer):
            print('Correct!')
        else:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again {name}!''')
            return
    print(f'Congratulations, {name}!')
