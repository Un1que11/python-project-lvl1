import prompt


greeting = 'Welcome to the Brain Games!'
name = 'May I have your name? '
hello = 'Hello, {}!'
answer = 'Your answer: '
num_of_games = 3
task = 'Question: {}'
correct = 'Correct!'
game_over = ("'{}' is wrong answer ;( Correct answer was '{}'\n"
             "Let's try again, {}!")
congratulations = 'Congratulations, {}!'


def start_the_game(rule, what_kind_of_game):
    print(greeting)
    username = prompt.string(name)
    print(hello.format(username))
    print(rule)
    game_count = 0
    while game_count < num_of_games:
        correct_answer, question = what_kind_of_game()
        print(task.format(question))
        user_answer = prompt.string(answer)
        if user_answer == correct_answer:
            game_count += 1
            print(correct)
        else:
            print(game_over.format(user_answer, correct_answer, username))
            return
    print(congratulations.format(username))
