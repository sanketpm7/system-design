from model.play_piece import PlayPiece
from model.piece_type import PieceType

class PlayPieceX(PlayPiece):
    def __init__(self):
        super().__init__(PieceType.X)