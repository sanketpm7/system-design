from model.play_piece import PlayPiece
from model.piece_type import PieceType

class PlayPieceY(PlayPiece):
    def __init__(self):
        super().__init__(PieceType.Y)