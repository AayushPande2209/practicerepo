"""
Program Name: Match Coins Game: Coin Class
Author: Aayush Pande
Purpose: Defines the Coin class used in the Match Coins game.
Starter Code: None
Date: July 1, 2026
"""

import random

class Coin:
    def __init__(self):
        """Initialize the coin with a random side up."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self):
        """Randomly toss the coin."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side facing up."""
        return self.__sideup