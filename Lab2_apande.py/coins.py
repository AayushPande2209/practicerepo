"""
Program Name: Match Coins Game: Coin Class
Author: Aayush Pande
Purpose: Defines the Coin class used to represent and toss a single coin.
Starter Code: None
Date: October 4, 2026
"""

import random


class Coin:
    def __init__(self):
        """Initialize the coin with a random side facing up."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self):
        """Toss the coin and randomly set it to Heads or Tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side of the coin."""
        return self.__sideup