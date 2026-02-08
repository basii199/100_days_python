from art import logo

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

action_is_active = True
while action_is_active:
    bids = {}
    print(logo)

    other_bidders_present = True

    while other_bidders_present:

        bidder_name = str(input('What is your name? \n'))
        bid_price = int(input('How much is your max bid? ($) \n'))

        bids[bidder_name] = bid_price

        while True:
            other_bidders = str(input('Are there other bidders present? (yes or no) \n'))

            if other_bidders == 'no':
                other_bidders_present = False
                print('\n'*3)
                print('<<<<<<<<<< * | * Auction complete * | * >>>>>>>>>>')
                max_bid = {
                    'name': '',
                    'price': 0,
                }

                for key in bids:
                    if bids[key] > max_bid['price']:
                        max_bid['name'] = key
                        max_bid['price'] = bids[key]

                print(f'The winner of this auction is {max_bid['name']} with ${max_bid['price']}')
                print('\n'*3)
                break
            elif other_bidders == 'yes':
                print('\n'*100)
                break
            else:
                print(f'Invalid response - {other_bidders}. Type yes or no')


    while True:
        restart_auction = input('Do you want to go for another auction? (yes or no) \n').lower()

        if restart_auction == 'yes':
            break
        elif restart_auction == 'no':
            action_is_active = False
            break
        else:
            print(f'Invalid response - {restart_auction}. Type yes or no')




