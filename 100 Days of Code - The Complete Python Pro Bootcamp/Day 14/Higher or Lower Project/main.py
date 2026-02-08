import random

from game_data import data
from art import logo, vs


def game_start():
    current_score = 0
    compare_direction = 0

    a = random.choice(data)

    def get_info_string(info):
        return f"{info['name']}, a {info['description']}, from {info['country']}"

    def get_compare_direction():
        while True:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            if user_choice == 'A':
                return 1
            elif user_choice == 'B':
                return -1
            else:
                print('Invalid input')

    def get_guess_result(val1, val2, direction):
        return (direction == 1 and val1 > val2) or (direction == -1 and val1 < val2)

    # UI ORDER PRESERVED
    def display_game_stats(score):
        print('\n' * 20)
        print(logo)

        # Result directly under logo
        if compare_direction != 0:
            result = get_guess_result(
                a['follower_count'],
                b['follower_count'],
                compare_direction
            )
            if result:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                return score, False  # end game

        # Rest of UI
        print(f"Compare A: {get_info_string(a)}")
        print(vs)
        print(f"Against B: {get_info_string(b)}")

        return score, True  # continue game

    keep_playing = True

    while keep_playing:
        b = random.choice(data)
        while a['name'] == b['name']:
            b = random.choice(data)

        # First display (no result yet)
        current_score, keep_playing = display_game_stats(current_score)
        if not keep_playing:
            break

        compare_direction = get_compare_direction()

        # Second display (shows result under logo)
        current_score, keep_playing = display_game_stats(current_score)
        if not keep_playing:
            break

        a = b


# Replay loop
while True:
    game_start()
    new_game = input("Do you want to play again? ('y' to continue): ").lower()
    if new_game != 'y':
        break
