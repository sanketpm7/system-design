from model.piece_type import PieceType
from model.play_piece import PlayPiece 

class Player:
    def __init__(self, name: str, play_piece: PlayPiece):
        self.__name = name
        self.__play_piece = play_piece
    
    def get_name(self): return self.__name
    def get_play_piece(self): return self.__play_piece