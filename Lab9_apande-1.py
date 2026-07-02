'''Program Name: Match Coins Game
Author: Aayush Pande
Purpose: Runs the Match Coins game using the Player and Coin classes.
Starter Code: None
Date: July 1, 2026'''

from player import Player


def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    choice = input("\nDo you want to toss the coins? (y/n): ")

    while choice.lower() == "y":

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match! Player 2 wins a coin.")

        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        # Optional Game Over feature
        if player1.get_wallet() == 0:
            print("\nGame Over!")
            print(f"{player1.get_name()} has no coins left.")
            break

        if player2.get_wallet() == 0:
            print("\nGame Over!")
            print(f"{player2.get_name()} has no coins left.")
            break

        choice = input("\nDo you want to toss the coins? (y/n): ")

    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins the game!")
    else:
        print("It's a draw!")


main()