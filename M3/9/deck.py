from card import Card,RANKS,SUITS
import random
class Deck():
    def __init__(self):
        self.deck = []

    def fill_deck(self):
        for rank  in RANKS:
           for suit in SUITS:               
            card = Card(rank,suit)
            self.deck.append(card)

    def give_card(self):
        card = self.deck.pop(0)
        return card

    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def __str__(self):
        string = ''        
        for card in self.deck:
             string += f'{card}'
             string+='\n'
        return string

deck = Deck()    
