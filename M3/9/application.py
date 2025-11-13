from card import *
from deck import *
from hand import *
from checker import *
class Application:
    def game(self):
        deck.fill_deck()
        deck.shuffle()
        hand = Hand()
        hand.cards()
        print(hand)
        hand.change_cards()
        print(hand)
        checker = Checker(hand)
        print(checker.result())
        again = input('Would you like to play again? y/n')
        if again == 'y':
            app.game()
        else:
            exit()
        
app = Application()
app.game()

