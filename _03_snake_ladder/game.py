from board import Board
from cell import Cell
from dice import Dice
from player import Player
from collections import deque

class Game:
    def __init__(self, n_players):
        self.board = Board(10, 10, 10)
        self.dice = Dice(1)
        self.players = deque()
        self.winner = None

        self.add_players(n_players)
    
    def add_players(self, n_players):
        for i in range(n_players):
            self.players.append(Player('P' + str(i), 0))
    
    def next_player(self) -> Player:
        player = self.players.popleft()
        self.players.append(player)
        return player
    
    def jump_check(self, new_pos: int) -> int:
        if new_pos > self.board.size * self.board.size - 1:
            return new_pos
        
        cell: Cell = self.board.get_cell(new_pos)

        if cell.get_jump() != None and cell.get_jump().get_start() == new_pos:
            jump_type = 'Snake' 
            if cell.get_jump().get_start() < cell.get_jump().get_end():
                jump_type = 'Ladder'
            
            print('jump done by: ' + jump_type, end=' ')
            return cell.get_jump().get_end()
        
        return new_pos
    
    def start_game(self):
        while not self.winner:
            cur_player = self.next_player()
            print('Player: ' + cur_player.get_id() + ' cur_pos: '+ str(cur_player.get_cur_pos()), end='  ')

            dice_val = self.dice.roll_dice()

            new_pos = cur_player.get_cur_pos() + dice_val
            new_pos = self.jump_check(new_pos)

            cur_player.set_cur_pos(new_pos)


            print('  >>  Player: ' + cur_player.get_id() + ' new_pos: '+ str(new_pos))

            if new_pos > (self.board.size * self.board.size - 1):
                self.winner = cur_player
        
        print('WINNER: ', cur_player.get_id())