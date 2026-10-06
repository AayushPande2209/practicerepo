"""
Program: Word Frequency Analyzer
Author: Aayush Pande
Purpose: This program lets the user choose a text file from a menu and
         reports how many times each word appears in that file.
Starter Code: None
Date: October 5, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    """Counts the words in a text file."""

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        """Read the file and count each word. Return True if successful."""
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            translation_table = str.maketrans("", "", string.punctuation)
            with self.__filepath.open("r", encoding="utf-8-sig") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translation_table)
                    words = line.split()
                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1
            return True
        except FileNotFoundError:
            print(f"Error: The file '{self.__filepath.name}' was not found.")
            return False

    def print_report(self):
        """Print each word and its count in alphabetical order."""
        words = list(self.__frequencies.keys())
        words.sort()
        for word in words:
            print(f"{word:<20} :: {self.__frequencies[word]}")


def main():
    folder = Path(__file__).parent
    files = {
        "1": folder / "Tarzan Assessment.txt",
        "2": folder / "Monte Cristo Assessment.txt",
        "3": folder / "Princess Mars Assessment.txt",
        "4": folder / "Treasure Island Assessment.txt",
    }

    running = True
    while running:
        print()
        print("1. Tarzan")
        print("2. Monte Cristo")
        print("3. Princess Mars")
        print("4. Treasure Island")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            running = False
        elif choice in files:
            filepath = files[choice]
            print(f"Processing {filepath.name}...")
            analyzer = WordAnalyzer(filepath)
            if analyzer.process_file():
                analyzer.print_report()
            input("Press Enter to return to the menu.")
        else:
            print("Invalid choice. Please select from 1-5.")
            input("Press Enter to return to the menu.")


if __name__ == "__main__":
    main()
