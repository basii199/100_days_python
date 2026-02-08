import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card(n):
    return random.choices(cards, k=n)

def begin_game():
    print(logo)

    player_cards = get_card(2)
    dealer_cards = get_card(2)

    def display_player_cards():
        print(f'Your cards {player_cards}, current score = {sum(player_cards)}')

    def display_dealer_cards():
        print(f'Dealer cards: {dealer_cards}. Score: {sum(dealer_cards)}')

    def display_result():
        print(f'Player: {sum(player_cards)} - Dealer: {sum(dealer_cards)}')

    def adjust_for_soft_aces(current_cards):
        while 11 in current_cards and sum(current_cards) > 21:
            i = current_cards.index(11)
            current_cards[i] = 1
            print('*** Ace adjusted ***')

    def confirm_restart_game():
        restart_game = True
        while restart_game:
            answer = input('Do you want to play again. (\'y\' or \'n\') \n')
            if answer == 'y':
                begin_game()
                return
            elif answer == 'n':
                restart_game = False
            else:
                print('Invalid input.')

    display_player_cards()

    if sum(dealer_cards) == 21:
        print('*** Dealer BlackJack! Player Loses! ***')
        display_dealer_cards()
        return

    print(f'Dealer\'s first card: {dealer_cards[0]} \n\n')

    # Player logic
    players_turn = True
    while players_turn:
        player_choice = input('Type \'y\' to hit, \'n\' to stand:').lower()

        if player_choice == 'y':
            player_cards += get_card(1)

            if sum(player_cards) > 21:
                adjust_for_soft_aces(player_cards)

                if sum(player_cards) > 21:
                    print('*** Bust! Game Over. Player loses! ***')
                    display_player_cards()
                    confirm_restart_game()
                    return

            display_player_cards()

        elif player_choice == 'n':
            players_turn = False
        else:
            print('*** Invalid selection ***')

    # Dealer logic
    dealers_turn = True
    display_dealer_cards()

    while dealers_turn:

        if sum(dealer_cards) == 21:
            print('*** Dealer BlackJack! Player Loses! ***')
            display_dealer_cards()
            return

        elif sum(dealer_cards) <= 16:
            print('*** Dealer hits ***')
            dealer_cards += get_card(1)
            display_dealer_cards()

        elif sum(dealer_cards) > 21:
            adjust_for_soft_aces(dealer_cards)

            if sum(dealer_cards) > 21:
                print('*** Bust! Game Over. Player wins! ***')
                confirm_restart_game()
                return
        else:
            print('*** Dealer stands ***')
            dealers_turn = False

    if sum(player_cards) > sum(dealer_cards):
        display_result()
        print('*** Game Over. Player wins! ***')
    else:
        display_result()
        print('*** Game Over. Player losses! ***')
    confirm_restart_game()

begin_game()