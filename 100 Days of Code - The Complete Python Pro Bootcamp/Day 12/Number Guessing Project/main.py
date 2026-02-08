import random

def play_game():
    num_to_guess = random.randint(0,100)
    correct_guess = False

    print(f'Debug - answer = {num_to_guess}')

    lives = -1
    game_mode = input('Select difficulty: (easy or hard) ').lower()

    if game_mode == 'easy':
        lives = 10
    elif game_mode == 'hard':
        lives = 5

    while not correct_guess and lives > 0:
        user_guess = int(input('Guess a number: '))
        if user_guess > num_to_guess:
            lives -= 1
            print(f'Too high, try again. Attempts remaining: {lives}')
        elif user_guess < num_to_guess:
            lives -= 1
            print(f'Too low, try again. Attempts remaining: {lives}')
        else:
            print('Great job!')
            correct_guess = True

    if not lives > 0:
        print(f'Game over. No guesses left. The number was: {num_to_guess}')

    play_again = input('Do you want to play again: (y or n) ')
    if play_again == 'y':
        play_game()

play_game()