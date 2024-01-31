from abc import ABC, abstractmethod
from random import shuffle
from time import sleep

class Topologic(ABC):

    def __init__(self, perm, r, c, d):
        self._size = len(perm) - 1
        self.constructor(perm, r, c, d)
    def constructor(self, perm, r, c, d):
        if r == 0 and c == 0:
            self._adjacents = False
        elif r == self._size and c == 0:
            self._adjacents = self.downleft_corner(perm, r, c, d)
        elif c == self._size and r == 0:
            self._adjacents = self.upperright_corner(perm, r, c, d)
        elif c == self._size and c == self._size:
            self._adjacents = self.downright_corner(perm, r, c, d)
        elif c == 0 and (r != 0 or r != self._size):
            self._adjacents = self.centralleft_side(perm, r, c, d)
        elif c == self._size and (r != 0 or r != self._size):
            self._adjacents = self.centralright_side(perm, r, c, d)
        elif r == 0 and (c != 0 or c != self._size):
            self._adjacents = self.centralupper_side(perm, r, c, d)
        elif r == self._size and (c != 0 or c != self._size):
            self._adjacents = self.centraldown_side(perm, r, c, d)
        else:
            self._adjacents = self.central(perm, r, c, d)
    @abstractmethod
    def downleft_corner(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def upperright_corner(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def downright_corner(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def centralleft_side(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def centralright_side(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def centralupper_side(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def centraldown_side(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def central(self, perm, r, c, d): #OK
        pass
    @abstractmethod
    def get_adjacents(self): #OK
        pass

class Diagonals(Topologic):
    def __init__(self, perm, r, c, d):
        super().__init__(perm, r, c, d)
    def downleft_corner(self, perm, r, c, d): #OK
        if d and perm[r-1][c+1]:
            return d == perm[r-1][c+1]
        return False
    def upperright_corner(self, perm, r, c, d): #OK
        return False
    def downright_corner(self, perm, r, c, d): #OK
        if d and perm[r-1][c-1]:
            return d == perm[r-1][c-1]
        return False
    def centralleft_side(self, perm, r, c, d): #OK
        return self.downleft_corner(perm, r, c, d)
    def centralright_side(self, perm, r, c, d): #OK
        return self.downright_corner(perm, r, c, d)
    def centralupper_side(self, perm, r, c, d): #OK
        return False
    def centraldown_side(self, perm, r, c, d): #OK
        return self.downleft_corner(perm, r, c, d) or self.downright_corner(perm, r, c, d)
    def central(self, perm, r, c, d): #OK
        return self.downleft_corner(perm, r, c, d) or self.downright_corner(perm, r, c, d)
    def get_adjacents(self): #OK
        return self._adjacents

class NotDiagonals(Topologic):
    def __init__(self, perm, r, c, d):
        super().__init__(perm, r, c, d)
    def downleft_corner(self, perm, r, c, d): #OK
        if d and perm[r-1][c]:
            return d != perm[r-1][c]
        return False
    def upperright_corner(self, perm, r, c, d): #OK
        if d and perm[r][c-1]:
            return d != perm[r][c-1]
        return False
    def downright_corner(self, perm, r, c, d): #OK
        if d and perm[r-1][c] and perm[r][c-1]:
            return d != perm[r-1][c] or d != perm[r][c-1]
        elif d and perm[r-1][c] and not perm[r][c-1]:
            return d != perm[r-1][c]
        elif d and not perm[r-1][c] and perm[r][c-1]:
            return d != perm[r][c-1]
        return False
    def centralleft_side(self, perm, r, c, d): #OK
        return self.downleft_corner(perm, r, c, d)
    def centralright_side(self, perm, r, c, d): #OK
        return self.downright_corner(perm, r, c, d)
    def centralupper_side(self, perm, r, c, d): #OK
        return self.upperright_corner(perm, r, c, d)
    def centraldown_side(self, perm, r, c, d): #OK
        return self.downleft_corner(perm, r, c, d)
    def central(self, perm, r, c, d): #OK
        return self.downright_corner(perm, r, c, d)
    def get_adjacents(self): #OK
        return self._adjacents

def is_not_possible(perm, r, c, d):
    diagonals = Diagonals(perm, r, c, d).get_adjacents()
    notDiagonals = NotDiagonals(perm, r, c, d).get_adjacents()
    return diagonals or notDiagonals

## La solución es una fusión de backtracking y brute force using random numbers
def diagonal_permutator(cell, d, maxd, diagonals=16):
    if cell == 25 and d == diagonals:
        return True
    elif cell == 25:
        if d > maxd:
            maxd = d
            print(maxd)
        return False
    else:
        row = int(cell / size)
        col = cell - row * 5
        # Randomly select one of the arrangements
        shuffle(types)
        for i in types:
            if is_not_possible(perm, row, col, i):
                continue
            else:
                perm[row][col] = i
                if i:
                    if diagonal_permutator(cell + 1, d + 1, maxd): return True
                else:
                    if diagonal_permutator(cell + 1, d, maxd): return True
        return False

if __name__ == "__main__":
    size = 5
    perm = [[None for i in range(size)] for i in range(size)]
    types = ["l", "r", None]
    permv = False
    maxd = 0
    while permv == False:
        if diagonal_permutator(0, 0, maxd): permv = True
    print(perm)
    
    