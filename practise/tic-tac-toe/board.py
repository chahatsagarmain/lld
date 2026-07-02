from abc import ABC, abstractmethod

try:
    from .strategy import IStrategy
except ImportError:
    from strategy import IStrategy

class IBoard(ABC):

    @abstractmethod
    def check_win(self, strategy: IStrategy) -> bool:
        pass

    @abstractmethod
    def check_valid_move(self, x: int, y: int) -> bool:
        pass

    @abstractmethod
    def make_move(self, x: int, y: int) -> bool:
        pass

    @abstractmethod
    def get_current_player(self) -> int:
        pass

    @abstractmethod
    def print_board(self):
        pass

    @abstractmethod
    def start_game(self, strategy: IStrategy):
        pass

class Board(IBoard):

    def __init__(self, n: int, char_first: str, char_second: str):
        self._n = n
        self._board = [[-1 for _ in range(self._n)] for _ in range(self._n)]
        self._char_first = char_first
        self._char_second = char_second
        self._moves = 0
        self._current_player = 0

    def check_valid_move(self, x: int, y: int) -> bool:
        if x >= self._n or y >= self._n or x < 0 or y < 0:
            return False
        return True
    
    def get_current_player(self) -> int:
        return self._current_player + 1

    def check_win(self, strategy: IStrategy) -> bool:
        return strategy.check_win(self._board, self._n)
    
    def print_board(self):
        for i in range(self._n):
            row = []
            for j in range(self._n):
                val = self._board[i][j]
                if val == -1:
                    row.append(" ")
                else:
                    row.append(str(val))
            print(" " + " | ".join(row) + " ")
            if i < self._n - 1:
                print("---" + "+---" * (self._n - 1))
        
    def make_move(self, x: int, y: int) -> bool:
        if not self.check_valid_move(x, y) or self._board[x][y] != -1:
            print("CAN'T MAKE THIS MOVE")
            print("PLEASE CHOOSE ANOTHER INDEX")
            return False
        curr_char = self._char_first if self._current_player == 0 else self._char_second
        self._board[x][y] = curr_char
        self._moves += 1
        self._current_player = (self._current_player + 1) % 2
        return True
    
    def start_game(self, strategy: IStrategy):
        print(f"\nPLAYER 1 HAS SELECTED: {self._char_first}")
        print(f"PLAYER 2 HAS SELECTED: {self._char_second}\n")
        self.print_board()
        
        while True:
            current = self.get_current_player()
            char = self._char_first if current == 1 else self._char_second
            print(f"\nNUMBER OF MOVES: {self._moves}")
            print(f"CURRENT PLAYER: Player {current} ({char})")
            
            # loop until valid move
            while True:
                try:
                    x = int(input(f"ENTER row (0 indexed, 0-{self._n-1}): "))
                    y = int(input(f"ENTER col (0 indexed, 0-{self._n-1}): "))
                    if self.make_move(x, y):
                        break
                except ValueError:
                    print("Invalid input. Please enter valid integers.")
            
            self.print_board()
            
            if self.check_win(strategy):
                winner = 1 if self._current_player == 1 else 2
                winner_char = self._char_first if winner == 1 else self._char_second
                print(f"\n🏆 PLAYER {winner} ({winner_char}) WINS! 🏆\n")
                break
                
            if self._moves == self._n * self._n:
                print("\n🤝 THE GAME IS A DRAW! 🤝\n")
                break

            
    
