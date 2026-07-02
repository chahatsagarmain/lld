try:
    from .board import Board
except ImportError:
    from board import Board

class BoardBuilder():

    def __init__(self):
        self._n = 0
        self.char_a = ""
        self.char_b = ""

    def set_board_size(self, n):
        self._n = n
        return self
    
    def set_player_char(self, player_num: int, player_char: str):
        if player_num not in {1, 2} or player_char not in {"X", "O"}:
            print("INVALID INPUT")
            return self
        if player_num == 1:
            self.char_a = player_char
        else:
            self.char_b = player_char
        return self
    
    def build_board(self):
        return Board(self._n, self.char_a, self.char_b)

# Compatibility alias for BoardBuiler
BoardBuiler = BoardBuilder