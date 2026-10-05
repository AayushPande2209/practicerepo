"""
Program Name: Match Coins Game: Player Class
Author: Aayush Pande
Purpose: Defines the Player class, including the player's name, wallet,
         and Coin object.
Starter Code: None
Date: October 4, 2026
"""

from coin import Coin


class Player:
    def __init__(self, name):
        """Initialize a player with a name, 20 coins, and a Coin object."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Toss the player's coin."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the current side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Remove one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the number of coins in the player's wallet."""
        return self.__wallet

    def get_name(self):
        """Return the player's name."""
        return self.__name