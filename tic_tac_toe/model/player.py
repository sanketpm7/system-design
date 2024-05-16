from model.playing_piece import PlayingPiece

class Player:
    def __init__(self, name: int, playing_piece: PlayingPiece):
        self.name = name
        self.playing_piece = playing_piece

    def get_name(self) -> str:
        return self.name

    def get_playing_piece(self) -> PlayingPiece:
        return self.playing_piece

    def set_name(self, name) -> None:
        self.name = name
    
    def set_playing_piece(self, playing_piece) -> None:
        self.playing_piece = playing_piece