from abc import ABC, abstractmethod
import random

class AbstractPlayer(ABC):
    def __init__(self, symbol, name):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def move(self, **kwargs):
        """Return an integer representing the column where the player intends to play a piece."""


class ConsolePlayer(AbstractPlayer):
    def move(self, **kwargs):
        """Get which column to play in from the user via text console"""
        move_not_valid=True
        while move_not_valid:
            choice=input('Enter which column to play in: ')
            if isinstance(choice,int):
                return choice
            else:
                print("Not a number, please try again")


# TODO: Create a CPUPlayer class which selects moves without user intervention
class CPUPlayer(AbstractPlayer):
    def move(self, **kwargs):
        move_choice=random.randint(0,6)
        return move_choice