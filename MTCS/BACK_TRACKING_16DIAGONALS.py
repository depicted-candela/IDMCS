from abc import ABC, abstractmethod
from time import time
from copy import deepcopy

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
        if d == "r":
            return d == perm[r-1][c+1]
        return False
    def upperleft_corner(self, perm, r, c, d):
        return False
    def upperright_corner(self, perm, r, c, d): #OK
        return False
    def downright_corner(self, perm, r, c, d): #OK
        if d == "l":
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
    def upperright_corner(self, perm, r, c, d): #OK
        if perm[r][c-1]:
            return d != perm[r][c-1]
    def downleft_corner(self, perm, r, c, d): #OK
        if perm[r-1][c]:
            return d != perm[r-1][c]
    def downright_corner(self, perm, r, c, d): #OK
        return self.downleft_corner(perm, r, c, d) or self.upperright_corner(perm, r, c, d)
    def centralleft_side(self, perm, r, c, d): #OK
        return self.downleft_corner(perm, r, c, d)
    def centralright_side(self, perm, r, c, d): #OK
        return self.downright_corner(perm, r, c, d)
    def centralupper_side(self, perm, r, c, d): #OK
        return self.upperright_corner(perm, r, c, d)
    def centraldown_side(self, perm, r, c, d): #OK
        return self.downright_corner(perm, r, c, d)
    def central(self, perm, r, c, d): #OK
        return self.downright_corner(perm, r, c, d)
    def get_adjacents(self): #OK
        return self._adjacents

class FillnxnBoardWithDiagonals:
    """
    Fills a board of size n * n with not topologically touched diagonals
    >>> size = 5
    >>> diagonals = 16
    >>> perm = [[None] * 5 for i in range(size)]
    >>> permutator = FillnxnBoardWithDiagonals(size, diagonals)
    >>> permutator.diagonal_permutator(perm)
    >>> len(permutator._perms) == 2
    True
    >>> for i in permutator._perms:
    ...     print(i)
    [['r', 'r', 'r', None, 'l'], [None, None, 'r', None, 'l'], ['l', 'l', None, 'l', 'l'], ['l', None, 'r', None, None], ['l', None, 'r', 'r', 'r']]
    [['r', None, 'l', 'l', 'l'], ['r', None, 'l', None, None], ['r', 'r', None, 'r', 'r'], [None, None, 'l', None, 'r'], ['l', 'l', 'l', None, 'r']]

    """
    def __init__(self, size, diagonals):
        self._size  = size
        self._d     = diagonals
        self._perms = list()

    def is_not_possible(self, perm, r, c, d):
        diagonals = Diagonals(perm, r, c, d).get_adjacents()
        notDiagonals = NotDiagonals(perm, r, c, d).get_adjacents()
        return diagonals or notDiagonals

    ## La solución es back tracking: cada camino requiere un comienzo
    ## The solution is Back Tracking: each path needs a starting
    def diagonal_permutator(self, perm, cell=0, d=0):
        # If the possible diagonals in the permutations are less than
        # the number of desired diagonals, or say, if the remaining
        # cells (adding one to complete the size in physical terms -
        # starting from 1 - and in Python - starting from 0 -) in the
        # board plus the filled diagonals are less than the desired
        # diagonals, then the permutation can't be filled with such
        # number of diagonals
        if (self._size**2 - cell + 1) + d < self._d:
            # return to the previous step and permutate with the next symbol
            # (r, l, None)
            return
        
        # When the last cell is reached
        if cell == self._size**2:
            # And the number of diagonals is the desired
            if d == self._d:
                # Print such filled board with the desired
                # number of diagonals
                self._perms.append(deepcopy(perm))
                # print(perm)
            # Flag to finish the permutation, because that despite could be
            # one available cell and one remaining diagonal to use, the
            # constraints could disable the usability of such cell
            return
        
        ## Creates the rows and columns with cells less than
        ## the last one avoiding the problem of PYthon that starts
        ## with 0 and not 1
        row = cell // self._size
        col = cell % self._size

        # Uses the constraints from the classes Diagonals
        # and NotDiagonals with the first branch of symbols: r
        if not self.is_not_possible(perm, row, col, "r"):
            # First symbol: r
            perm[row][col] = "r"
            # If the permutation does not returns, continue with such
            # sub ramification
            self.diagonal_permutator(perm, cell + 1, d + 1)
            # If the permutation return to this step, put None
            # as symbol to make the condition fit the the constrainer
            # class; to use again self.is_not_possible enabling it simplicity
            # or avoiding writing more code to it
            perm[row][col] = None
        # Uses the constraints from the classes Diagonals
        # and NotDiagonals with the second branch of symbols: l
        if not self.is_not_possible(perm, row, col, "l"):
            # Second symbol: l
            perm[row][col] = "l"
            # If the permutation does not returns, continue with such
            # sub ramification
            self.diagonal_permutator(perm, cell + 1, d + 1)
            # If the permutation return to this step, put None
            # as symbol because there is no more options
            perm[row][col] = None
        # If both r and l symbols does not work for the current
        # ramification, None was used and the permutation continues
        self.diagonal_permutator(perm, cell + 1, d)


if __name__ == "__main__":
    import doctest
    doctest.testmod()