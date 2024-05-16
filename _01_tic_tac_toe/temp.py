from model.player import Player
from model.play_piece_x import PlayPieceX


cur_player = Player('P01', PlayPieceX()) 
print('Player ' + cur_player.get_name() + ' enter row & col: ', end=' ')
inp = input().split(' ')



print(inp)