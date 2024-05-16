from model.playing_piece import PlayingPiece
from model.piece_type import PieceType

class PlayingPieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)
    
# class PlayingPieceX(PlayingPiece):
#     def __init__(self):
#         self.piece_type = PieceType.X