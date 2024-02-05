from abc import ABC

class LargeAmount_5_7_Coins(ABC):

    def __init__(self, amount):
        assert(amount > 23)
        self._amount = amount
        self._coins = list()
        self.change(amount)
    
    def change(self, amount):
        """
        >>> coins = LargeAmount_5_7_Coins(29)
        >>> print(coins._coins)
        [5, 5, 7, 7, 5]
        """
        if (amount == 24):
            return [5, 5, 7, 7]
        elif (amount == 25):
            return [5, 5, 5, 5, 5]
        elif (amount == 26):
            return [5, 7, 7, 7]
        elif (amount == 27):
            return [5, 5, 5, 5, 7]
        elif (amount == 28):
            return [7, 7, 7, 7]
        else:
            self._coins = self.change(amount - 5)
            self._coins.append(5)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    coins = LargeAmount_5_7_Coins(29)
    print(coins._coins)