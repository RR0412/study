from field import Field
from player import Player
from bot import Bot
from checker import Checker
import random

class Game:
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players

    def game(self):
        size = int(input("Enter number of fields you want to play: "))
        field = Field(size)
        checker = Checker(field)

        if self.number_of_players == 1:
            player = Player('X', field)
            bot = Bot('O', field)
            options = [player, bot]
            first = random.choice(options)
            options.remove(first)
            second = options[0]
        elif self.number_of_players == 2:
            player_1 = Player('X', field)
            player_2 = Player('O', field)
            options = [player_1, player_2]
            first = random.choice(options)
            options.remove(first)
            second = options[0]
        else:
            print("Invalid number of players!")
            return

        while True:
            first.make_move()
            if checker.check(first):
                print(f'{first.symbol} won!')
                break
            print(field)
            if all(cell != '' for row in field.table for cell in row):
                print("It's a draw!")
                break

            second.make_move()
            if checker.check(second):
                print(f'{second.symbol} won!')
                break
            print(field)
            if all(cell != '' for row in field.table for cell in row):
                print("It's a draw!")
                break

        again = input('Would you like to play again? y/n: ')
        if again.lower() == 'y':
            self.game()
        else:
            print("Great play!")
            exit()