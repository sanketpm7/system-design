from collections import deque

from model.board import Board
from model.player import Player
from model.playing_piece_x import PlayingPieceX
from model.playing_piece_o import PlayingPieceO
from model.piece_type import PieceType

class TicTacToe:
    def __init__(self) -> None:
        self.board = Board(3)

        p1 = Player('P1', PlayingPieceX())
        p2 = Player('P2', PlayingPieceO())

        self.players = deque()
        self.players.append(p1)
        self.players.append(p2)

    def start_game(self) -> str:
        no_winner = True

        while no_winner:
            cur_player: Player = self.players.popleft()

            self.board.print_board()

            free_spaces = self.board.get_free_cells()
            if len(free_spaces) == 0:
                break

            print(f'<< Player: {cur_player.get_name()}, >> : ', end='')
            inp = input('enter row and col: ')
            inp = inp.split(' ')
            row = int(inp[0])
            col = int(inp[1])

            is_piece_added = self.board.add_piece(row, col, cur_player.get_playing_piece())

            if not is_piece_added:
                print('Incorrect position chosen, try again')
                self.players.appendleft(cur_player)
                continue
            
            self.players.append(cur_player)

            winner = self.check_winner(row, col, cur_player.get_playing_piece().piece_type)

            if winner:
                return cur_player.get_name()

        return 'tie'

    def check_winner(self, row: int, col: int, cur_piece_type: PieceType) -> bool:
        row_match, col_match = True, True
        pos_diag, neg_diag = True, True
        board_size = self.board.get_size()

        # check row
        for i in range(board_size):
            if self.board.get_cell_val(row, i) == None or self.board.get_cell_val(row, i).piece_type != cur_piece_type:
                row_match = False 

        # check col
        for i in range(board_size):
            if self.board.get_cell_val(i, col) == None or self.board.get_cell_val(i, col).piece_type != cur_piece_type:
                col_match = False 

        # check pos_diag
        for i in range(board_size):
            if self.board.get_cell_val(i, i) == None or self.board.get_cell_val(i, i).piece_type != cur_piece_type:
                pos_diag = False 

        # check neg_diag
        for i in range(board_size):
            if ( 
                self.board.get_cell_val(i, board_size - 1 - i) == None or
                self.board.get_cell_val(i, board_size - 1 - i).piece_type != cur_piece_type
            ):
                neg_diag = False 
        
        return row_match or col_match or pos_diag or neg_diag