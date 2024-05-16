from typing import Optional
from model.play_piece import PlayPiece

class Board:
    def __init__(self, size):
        self.board: list[list[Optional[PlayPiece]]] = [ [None] * size for _ in range(size) ]
        self.size = size
    
    def cell_val(self, row, col) -> Optional[PlayPiece]:
        return self.board[row][col]

    def add_piece(self, row, col, play_piece: PlayPiece) -> bool:
        if self.board[row][col] is not None:
            return False
        
        self.board[row][col] = play_piece
        return True

    def free_cell_cnt(self):
        cnt = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    cnt += 1
        return cnt

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(self.board[i][j].piece_type.name, end=' | ')
                else:
                    print(' ', end=' | ')