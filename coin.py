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
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup