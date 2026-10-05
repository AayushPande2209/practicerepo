"""
Program Name: Match Coins Game
Author: Aayush Pande
Purpose: Runs an interactive coin-matching game using Player objects.
         Players toss their coins and gain or lose coins based on the results.
Starter Code: None
Date: October 4, 2026
"""

from player import Player


def main():
    # Create the two players.
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play_again = "y"

    while play_again.lower() == "y":
        print("\nTossing...")

        # Toss both players' coins.
        player1.toss_coin()
        player2.toss_coin()

        # Get the results.
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        # Display the results.
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        # Determine the winner.
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match! Player 2 wins a coin.")

        # Display current wallets.
        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        # Ask if the user wants to continue.
        play_again = input("\nDo you want to toss the coins? (y/n): ")

    # Display final results.
    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()