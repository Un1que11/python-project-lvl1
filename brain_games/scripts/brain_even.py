import prompt
from random import randint
from brain_games import name


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game():
    i = 0
    while i < 3:
        number = randint(0, 100)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer.lower() == correct_answer.lower():
            print('Correct!')
            i += 1
        else:
            print(f'''"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".
Let's try again, {name}!''')
            return
    print(f'Congratulations {name}!')


if __name__ == '__main__':
    rules()
    game()
