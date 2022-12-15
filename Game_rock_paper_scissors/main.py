import random

def choose_options():
    options = ('stone','paper','scissors')
    user_option = input('Choose your option stone, paper, scissors: ')
    user_option = user_option.lower()

    if not user_option in options:
        print('Not a valid option')
        return None, None
    
    computer_option = random.choice(options)

    print('Player_Option =>', user_option)
    print('Contender_Option =>', computer_option)

    return user_option, computer_option

def check_rules (user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Tie')
    elif user_option == 'stone':
        if computer_option == 'scissors':
            print('stone beats scissors ')
            print('player win!')
            user_wins += 1
        elif computer_option == 'paper':
            print('paper beats stone')
            print('Contender win!')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'stone':
            print('paper beats stone')
            print('player win!')
            user_wins += 1
        elif computer_option == 'scissors':
            print('scissors beats paper')
            print('Contender win!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print('*'*10)
        print('ROUND ', rounds)
        print('*'*10)

        print('Contender wins', computer_wins)
        print('Player wins', user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins =check_rules(user_option,computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print('Contender its the winner')
            break
        if user_wins == 2:
            print('Player its the winner')
            break

run_game()


