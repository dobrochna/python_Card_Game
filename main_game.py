import hand
import deck

colors = ['Pik', 'Trefl', 'Kier', 'Karo']  # cards colors
figures = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']  # cards figures
values = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
          '3': 3, '2': 2}  # values of cards figures


def hit_or_stand(player, deckk):  # player decide if he wants to hit or to stand
    while True:
        if player.value < 21:
            decision = input("Type 'h' for hit or 's' for stand: ")
            if decision.lower() == 'h':
                player.add_card(deckk.deal())  # if player hits add one card to his hand
                player.if_ace()  # check if player has an ace in hand
                print('Now you have in hand: \n' + player.print_hand(len(player.cards)))
                print('Do you want more cards?')
            elif decision.lower() == 's':
                print('OK you stand, its dealer turn!')
                break
            else:
                print('There is no option like %s, try again!' % decision)
        else:  # player cant hit if value of his cards exceede 21 or is 21
            print('Value of your cards is 21 or more, you cant hit anymore.')
            break


def play_dealer(dealer, deckk):  # after player stands play dealer
    while dealer.value < 17:
        dealer.add_card(deckk.deal())
        dealer.if_ace()


def calculate_winner(player, dealer):  # calculate who won
    if player.value > 21:
        print("Oooops you've lost!")
        return False
    elif dealer.value > 21:
        print("Yeeeey you've won!")
        return True
    else:
        if player.value >= dealer.value:
            print("Yeeeey you've won!")
            return True
        else:
            print("Oooops you've lost!")
            return False


def calculate_chips(if_won, chipss, bett):  # calculate how much chips have player after game
    if if_won:
        chipss += bett
        print('Congratulations! Now you have: %i chips!' % chipss)
        return chipss
    else:
        chipss -= bett
        print('Sorry that you lost the game, now you have: %i chips.' % chipss)
        return chipss


def more_game(chipss):  # ask player if he wants to play again
    if chipss > 0:
        while True:
            dec = input("Do you want to play again? Type 'y' or 'n': ")
            if dec.lower() == 'y':
                return True
            elif dec.lower() == 'n':
                return False
            else:
                print("Ooops type only 'y' or 'n'!")
    else:  # player cant play again if he dosent have chips
        print('You dont have more chips! Cant play again!')
        return False

if __name__ == "__main__":

    playing = True
    name = input('Welcome in Black Jack game! Please insert your name: ')

    while True:  # ask player for chips
        try:
            chips = int(input('How many chips do you want? '))
        except ValueError:
            print('Chips value must be an integer!')
        else:
            break

    while playing:

        while True:  # ask player for bet for this game
            try:
                print('You have %i chips.' % chips)
                bet = int(input('What is your bet for this game %s? ' % name))
            except ValueError:
                print('A bet must be an integer!')
            else:
                if bet > chips:
                    print('Sorry you dont have that much chips!')
                else:
                    print('OK, so lets play!')
                    break

        game_deck = deck.Deck()  # create deck for the game
        game_deck.shuffle_deck()  # shuffle deck

        player_hand = hand.Hand()  # create players hand
        player_hand.add_card(game_deck.deal())  # add cards for players hand
        player_hand.add_card(game_deck.deal())
        print('In hand you have: \n' + player_hand.print_hand(2))  # print player hand

        dealer_hand = hand.Hand()  # create dealer hand
        dealer_hand.add_card(game_deck.deal())  # add cards for dealer hand
        dealer_hand.add_card(game_deck.deal())
        print('First dealers card is: \n ' + dealer_hand.print_hand(1))  # print one dealers card

        hit_or_stand(player_hand, game_deck)  # player decide to hit or stand
        play_dealer(dealer_hand, game_deck)  # play dealer to hit more cards if value < 17

        print('In hand you have: \n' + player_hand.print_hand(len(player_hand.cards)))  # print player hand and value
        print('Value of your cards is: ' + str(player_hand.value) + '\n')
        print('Dealers cards are: \n ' + dealer_hand.print_hand(len(dealer_hand.cards)))  # print dealer hand and value
        print('Value of dealer cards is: ' + str(dealer_hand.value) + '\n')

        player_won = calculate_winner(player_hand, dealer_hand)  # calculate if player won
        chips = calculate_chips(player_won, chips, bet)  # calculate player chips
        playing = more_game(chips)  # ask if he wants to play more

    print('It was a pleasure to play with you! See you soon :)')  # if no, say bay
