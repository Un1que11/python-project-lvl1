#!/usr/bin/env python3
import prompt
from random import randint


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello {name}!')


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game():
    counter = (1, 2, 3)
    for i in counter:
        number = randint(0, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer.lower() == correct_answer.lower():
            print('Correct!')
        else:
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {name}!''')
            return
    print(f'Congratulations {name}!')


if __name__ == '__main__':
    rules()
    game()
