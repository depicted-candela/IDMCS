from abc import ABC, abstractmethod

class Topologic(ABC):

    def __init__(self, board, r, c, d):
        self._size = len(board) - 1
        self.constructor(board, r, c, d)
    def constructor(self, board, r, c, d):
        if r == 0 and c == 0:
            self._diagonals = self.upperleft_corner(board, r, c, d)
        elif r == self._size and c == 0:
            self._diagonals = self.downleft_corner(board, r, c, d)
        elif c == self._size and r == 0:
            self._diagonals = self.upperright_corner(board, r, c, d)
        elif c == self._size and c == self._size:
            self._diagonals = self.downright_corner(board, r, c, d)
        elif c == 0 and (r != 0 or r != size):
            self._diagonals = self.centralleft_side(board, r, c, d)
        elif c == size and (r != 0 or r != size):
            self._diagonals = self.centralright_side(board, r, c, d)
        elif r == 0 and (c != 0 or c != size):
            self._diagonals = self.centralupper_side(board, r, c, d)
        elif r == size and (c != 0 or c != size):
            self._diagonals = self.centraldown_side(board, r, c, d)
        else:
            self._diagonals = self.central(board, r, c, d)
    @abstractmethod
    def upperleft_corner(self, board, r, c, d): #OK
        pass
    @abstractmethod
    def downleft_corner(self, board, r, c, d): #OK
        pass
    @abstractmethod
    def upperright_corner(self, board, r, c, d): #OK
        pass
    @abstractmethod
    def downright_corner(self, board, r, c, d): #OK
        pass
    def centralleft_side(self, board, r, c, d): #OK
        return self.upperleft_corner(board, r, c, d) or self.downleft_corner(board, r, c, d)
    def centralright_side(self, board, r, c, d): #OK
        return self.upperright_corner(board, r, c, d) or self.downright_corner(board, r, c, d)
    def centralupper_side(self, board, r, c, d): #OK
        return self.upperleft_corner(board, r, c, d) or self.upperright_corner(board, r, c, d)
    def centraldown_side(self, board, r, c, d): #OK
        return self.downleft_corner(board, r, c, d) or self.downright_corner(board, r, c, d)
    def central(self, board, r, c, d): #OK
        return self.centralleft_side(self, board, r, c, d) or self.centralright_side(self, board, r, c, d)
    def get_diagonals(self): #OK
        self._diagonals

class Diagonals(Topologic):
    def __init__(self, board, r, c, d):
        super().__init__(board, r, c, d)
    def upperleft_corner(self, board, r, c, d): #OK
        if d == "l":
            return d == board[r+1][c+1]
        return False
    def downleft_corner(self, board, r, c, d): #OK
        if d == "r":
            return d == board[r-1][c+1]
        return False
    def upperright_corner(self, board, r, c, d): #OK
        if d == "r":
            return d == board[r+1][c-1]
        return False
    def downright_corner(self, board, r, c, d): #OK
        if d == "l":
            return d == board[r-1][c-1]
        return False


class NotDiagonals(Topologic):
    def __init__(self, board, r, c, d):
        super().__init__(board, r, c, d)
    def upperleft_corner(self, board, r, c, d): #OK
        return d == board[r+1][c] or d == board[r][c+1]
    def downleft_corner(self, board, r, c, d): #OK
        return d == board[r-1][c] or d == board[r][c+1]
    def upperright_corner(self, board, r, c, d): #OK
        return d == board[r][c-1] or d == board[r+1][c]
    def downright_corner(self, board, r, c, d): #OK
        return d == board[r-1][c] or d == board[r][c-1]


def is_not_possible(board, r, c, d):
    diagonals = Diagonals(board, r, c, d)
    notDiagonals = NotDiagonals(board, r, c, d)
    return diagonals or notDiagonals

def diagonal_permutator(c, perm, diagonals=16):
    if c == diagonals:
        return perm
    for i in range(size):
        for j in range(size):
            for k in ["r", "l", None]:
                if not is_not_possible(perm, i, j, k):
                    perm[i][j] = k
                    diagonal_permutator(c + 1, perm)
                else:
                    continue

if __name__ == "__main__":
    size = 5
    perm = [[None for i in range(size)] for i in range(size)]
    diagonal_permutator(0, perm)