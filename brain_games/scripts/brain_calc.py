import prompt
from random import randint, choice
from brain_games import name


def rules():
    print('What is the result of the expression?')


def game():
    i = 0
    while i < 3:
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
        answer = prompt.string('Your answer: ')
        if str(answer) == str(correct_answer):
            print('Correct!')
        else:
            print(f''''{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
    Let's try again {name}!''')
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    rules()
    game()
