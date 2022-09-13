import prompt


NUM_OF_ROUNDS = 3


def run_the_game(rules, question_and_correct_answer_of_game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(username))
    print(rules)
    game_count = 0
    while game_count < NUM_OF_ROUNDS:
        correct_answer, question = question_and_correct_answer_of_game()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            game_count += 1
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'\n"
                  "Let's try again, {}!".format(user_answer,
                                                correct_answer,
                                                username))
            return
    print('Congratulations, {}!'.format(username))
