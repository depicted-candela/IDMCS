## To understand if the permutation has no Queens in 
## attack zones
def can_be_extended_to_solution(perm):
    # To use all the possible numbers up to the size of the
    # board in it rows and cols
    i = len(perm) - 1
    # Iterate along all the possible numbers up to the size
    # of the borad in it rows and cols to know if its to
    # aggregate the new Queen to the board
    for j in range(i):
        # See for the diagonal attack zones
        if i - j == abs(perm[i] - perm[j]):
            return False
        # See for the horizontal and vertical attack zones
        if i == perm[i] or j == perm[j]:
            return False
    return True

## Extend the Queens over the board, stating with one up the desired
## number 'n'
def extend(perm, n):
    """
    >>> perm = extend(perm = [], n = 20)
    >>> print(perm)
    [1, 3, 0, 2, 7, 9, 13, 19, 16, 18, 15, 17, 5, 10, 8, 6, 4, 12, 14, 11]
    """
    # If the desired number of Queens is reached, then stop
    if len(perm) == n:
        return perm
    
    # Permutates all the possible numbers up to the number of Queens
    # that also is the number of columns or rows
    for k in range(n):
        # A rule to add just new columns or rows to the board setting
        if k not in perm:
            # Add the new column or row to the board permutation
            perm.append(k)
            # Detects if it's a correct solution
            if can_be_extended_to_solution(perm):
                # Recursion to look into a single loop until discover if
                # the solution works
                extend(perm, n)
            # If the solution does not work, empty the list and start with
            # a new recursion
            perm.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod()