import prompt
from random import randint, choice


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
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
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')


def brain_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = (1, 2, 3)
    for i in counter:
        first_number = randint(0, 100)
        second_number = randint(0, 100)
        print(f'Question: {first_number} {second_number}')
        while first_number != 0 and second_number != 0:
            if first_number > second_number:
                first_number = first_number % second_number
            else:
                second_number = second_number % first_number
        correct_answer = first_number + second_number
        answer = answers()
        if str(correct_answer) == str(answer):
            print('Correct!')
        else:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')


def brain_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    counter = (1, 2, 3)
    for i in counter:
        item_position = randint(0, 9)
        first_number = randint(0, 20)
        regularity = randint(1, 15)
        arithmetic_progression = ''
        counter = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        for i in counter:
            arithmetic_progression += str(first_number) + ' '
            first_number += regularity
        arithmetic_progression = arithmetic_progression.split()
        correct_answer = arithmetic_progression[item_position]
        arithmetic_progression[item_position] = '..'
        arithmetic_progression = ' '.join(arithmetic_progression)
        print(f'Question: {arithmetic_progression}')
        answer = answers()
        if str(answer) == (correct_answer):
            print('Correct!')
        else:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')
