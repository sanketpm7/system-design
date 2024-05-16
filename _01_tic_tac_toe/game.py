from collections import deque
from typing import Optional

from model.player import Player
from model.board import Board

from model.play_piece import PlayPiece
from model.play_piece_x import PlayPieceX
from model.play_piece_y import PlayPieceY

class Game:
    def __init__(self):
        self.board = Board(3)
        self.players = deque()

        self.players.append(Player('P1', PlayPieceX()))
        self.players.append(Player('P2', PlayPieceY()))
    
    def player_turn(self) -> Player:
        player = self.players.popleft()
        self.players.append(player)
        return player

    def out_of_range(self, row, col):
        print('Invalid input, please enter valid row & col')
        return row < 0 or col < 0 or col >= self.board.size or col >= self.board.size

    def start_game(self):
        winner = None
        while winner is None:
            if self.board.free_cell_cnt() == 0:
                break

            cur_player = self.player_turn()

            print('Player ' + cur_player.get_name() + ' enter row & col: ', end=' ')
            inp = input().split(' ')
            row = int(inp[0])
            col = int(inp[1])

            if self.out_of_range(self, row, col):
                self.players.appendleft(cur_player)
                continue

            cur_piece_type = cur_player.get_play_piece()
            if not self.board.add_piece(row, col, cur_piece_type):
                self.players.appendleft(cur_player)
                print('Piece already exists in cell, please give different input')
                continue
            
            if self.check_winner(row, col, cur_piece_type):
                winner = cur_player
        return winner 

    '''
    1. check row
    2. check col
    3. check pos_diag
    4. check neg_diag
    '''
    def check_winner(self, row, col, play_piece: PlayPiece):
        row_match, col_match = True, True 
        pos_diag, neg_diag = True, True 

        for i in range(self.board.size):
            if self.board.board[row][i] is None or self.board.board[row][i] != play_piece:
                row_match = False  

        for i in range(self.board.size):
            if self.board.board[i][col] is None or self.board.board[i][col]!= play_piece:
                col_match = False  
            
        for i in range(self.board.size):
            if self.board.board[i][i] is None or self.board.board[i][i]!= play_piece:
                neg_diag = False  

        for i in range(self.board.size):
            if self.board.board[i][self.board.size - 1 - i] is None or self.board.board[i][self.board.size - 1 - i]!= play_piece:
                pos_diag = False  
        
        return row_match or col_match or pos_diag or neg_diag