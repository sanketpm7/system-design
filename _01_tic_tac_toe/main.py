from model.player import Player
from typing import Optional
from game import Game

class Main:
    def __init__(self):
        game = Game()
        winner: Optional[Player] = game.start_game()

        if winner:
            print("WINNER: ", winner.get_name())
        else:
            print("TIE")

if __name__ == '__main__':
    main = Main()