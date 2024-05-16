from model.playing_piece import PlayingPiece
from typing import Optional

class Board:
    def __init__(self, size: int):
        self.size = size
        self.board = [ [None] * size for _ in range(size)]
    
    def get_cell_val(self, row, col) -> Optional[PlayingPiece]:
        return self.board[row][col]

    def get_size(self) -> int:
        return self.size
    
    def add_piece(self, row: int, col: int, playing_piece: PlayingPiece) -> bool:
        if self.board[row][col] != None:
            return False

        self.board[row][col] = playing_piece
        return True
    
    def get_free_cells(self) -> list[list[int, int]]:
        free_cells = []

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    free_cells.append([i, j])
        return free_cells
    
    def print_board(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != None:
                    print(str(self.board[i][j].piece_type.name) + ' ', end='')
                else:
                    print('  ', end='')
                print('|  ', end='')
            print()
        print()