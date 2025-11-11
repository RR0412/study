import sys
import os

sys.path.append(os.path.dirname(__file__))

from game import Game

if __name__ == "__main__":
    player_number = int(input("Enter number of players (1 / 2): "))
    game = Game(player_number)
    game.game()