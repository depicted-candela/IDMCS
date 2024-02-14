
from abc import ABC


class GuessANumber(ABC):
    """A class to guess a number between two boundaries

    Args:
        ABC (_type_): _description_
    """
    def __init__(self, end):
        """Initializes the class' instance, will be always the lowest boundary
        Args:
            end (int): biggest boundary
        """
        self._end = end
        self._start = 1
    def has_next(self):
        """Determines if there is another step between the boundaries to iterate. Is the base case or prior knowledge about the problem for recursive solutions
        Returns:
            bool: False if there arent more steps, otherwise True
        """
        return self._end - self._start > 1
    def next(self):
        """Calculates the new criterion number
        """
        next = self._start + (self._end - self._start) / 2
        if next - int(next) == 0:
            self._next =  next
        else:
            self._next = next - 0.5
    def higher(self):
        """To know where is the desired number, higher o less than the criterion number
        Returns:
            bool: True if the criterion number is already the desired number, performs like a base case of prior knowledge
        """
        higher = input(f"Is higher than {self._next}? (y/n): ").lower().strip() == 'y'
        if higher: self._start = self._next
        if not higher:
            if not self.has_next(): return True
            self._end = self._next
    def run(self):
        """Iterates until the desired number is reached (or the base case)
        """
        while (self.has_next()):
            self.next()
            print(f"The middle is {self._next}")
            if self.higher(): break
        print(f"The number is {self._next}")

if __name__ == "__main__":
    gn = GuessANumber(2097151)
    gn.run()
    print("YOU WIN!")