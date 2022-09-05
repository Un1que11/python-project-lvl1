import prompt


num_of_games = 3


def start_the_game(rule, what_kind_of_game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(username))
    print(rule)
    game_count = 0
    while game_count < num_of_games:
        correct_answer, question = what_kind_of_game()
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
