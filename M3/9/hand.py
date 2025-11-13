from card import Card,RANKS,SUITS
from deck import *
class Hand:
    def __init__(self):
        self.hand = []

    def cards(self):
        for i in range(5):
            self.hand.append(deck.give_card())

    def change_cards(self):
        to_change = input('please enter card numbers your would like to change')
        if to_change:
            array = []
            for i in to_change.replace(' ',''):
                array.append(int(i))
            if len(array)>0:
                for number in array:
                    self.hand[number-1] = deck.give_card()
        else:
            pass

    def __str__(self):
        string = '|1   |2   |3   |4   |5\n'
        for card in self.hand:
            string += f'{str(card):5}'
        return string








