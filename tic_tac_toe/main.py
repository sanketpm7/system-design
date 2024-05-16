from tic_tac_toe import TicTacToe

class Main:
    def main(self) -> None:
        game = TicTacToe()
        winner = game.start_game()
        print('winner is: ', winner)

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()