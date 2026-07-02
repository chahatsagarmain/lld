from abc import ABC, abstractmethod

class IStrategy(ABC):

    @abstractmethod
    def check_win(self, board, n: int) -> bool:
        pass
             
class DefaultStrategy(IStrategy):

    def check_win(self, board, n: int) -> bool:
        # Check rows
        for i in range(n):
            first = board[i][0]
            if first != -1:
                found = True
                for j in range(1, n):
                    if board[i][j] != first:
                        found = False
                        break
                if found:
                    return True

        # Check columns
        for j in range(n):
            first = board[0][j]
            if first != -1:
                found = True
                for i in range(1, n):
                    if board[i][j] != first:
                        found = False
                        break
                if found:
                    return True

        # Check main diagonal
        first = board[0][0]
        if first != -1:
            found = True
            for i in range(1, n):
                if board[i][i] != first:
                    found = False
                    break
            if found:
                return True

        # Check anti-diagonal
        first = board[0][n - 1]
        if first != -1:
            found = True
            for i in range(1, n):
                if board[i][n - 1 - i] != first:
                    found = False
                    break
            if found:
                return True

        return False

             