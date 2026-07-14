'''Program Name: Lab10 - Word Analyzer
Author: [Your Name Here]
Purpose: An OOP-based program that presents a menu of 4 predefined text
         files, lets the user choose one, reads it, counts the frequency
         of every word in the file, and prints an alphabetical report of
         word counts. Supports an optional stop-word list so common words
         can be excluded from the final count.
Starter Code: None used - written from scratch based on assignment
              instructions.
Date: 2026-07-13
'''


import string
from pathlib import Path


class WordAnalyzer:
    '''Reads a text file and computes word frequency counts.'''

    def __init__(self, filepath, stop_words=None):
        '''
        :param filepath: str or Path to the text file to analyze.
        :param stop_words: optional iterable of words to ignore when
                            counting (the "Challenge" feature).
        '''
        # Private Path object for the file we will process.
        self.__filepath = Path(filepath)

        # Private dictionary that will hold {word: count}.
        self.__frequencies = {}

        # Private set of words to skip during counting (may be empty).
        self.__stop_words = set(w.lower() for w in stop_words) if stop_words else set()

    def process_file(self):
        '''
        Reads self.__filepath line by line, strips punctuation, lowercases
        the text, splits it into words, and tallies word frequencies in
        self.__frequencies.

        :return: True if the file was processed successfully,
                 False if a FileNotFoundError occurred.
        '''
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError(f"{self.__filepath} does not exist.")

            # Translation table that maps every punctuation character to None,
            # effectively stripping punctuation from a string.
            translator = str.maketrans('', '', string.punctuation)

            with self.__filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translator)
                    words = line.split()

                    for word in words:
                        if word in self.__stop_words:
                            continue
                        self.__frequencies[word] = self.__frequencies.get(word, 0) + 1

            return True

        except FileNotFoundError as e:
            print(f"Error: Could not find the file - {e}")
            return False

    def print_report(self):
        '''Prints every word and its frequency, sorted alphabetically.'''
        sorted_words = sorted(self.__frequencies.keys())

        # Find the longest word so the counts line up in neat columns.
        width = max((len(w) for w in sorted_words), default=0)

        for word in sorted_words:
            print(f"{word:<{width}} :: {self.__frequencies[word]}")


def main():
    # Build the 4 file paths using pathlib, relative to this script's location.
    base_dir = Path(__file__).parent

    files = {
        "1": base_dir / "princess_mars.txt",
        "2": base_dir / "Tarzan.txt",
        "3": base_dir / "treasure_island.txt",
        "4": base_dir / "monte_cristo.txt",
    }

    # Friendly display names shown in the menu (no file extensions).
    display_names = {
        "1": "A Princess of Mars (Chapter 1)",
        "2": "Tarzan of the Apes (Chapter 1)",
        "3": "Treasure Island (Chapter 1)",
        "4": "The Count of Monte Cristo (Chapter 1)",
    }

    # Optional: words to ignore when counting (Challenge feature).
    # Leave as an empty list if you don't want to use the challenge.
    stop_words = ["the", "a", "an", "of", "and", "to", "in", "is", "it"]

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key in sorted(files.keys()):
            print(f"{key}. {display_names[key]}")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break

        if choice not in files:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu... ")
            continue

        filepath = files[choice]
        print(f"\nProcessing '{filepath.name}'...\n")

        analyzer = WordAnalyzer(filepath, stop_words=stop_words)
        success = analyzer.process_file()

        if success:
            analyzer.print_report()
        else:
            print("Skipping report due to file error.")

        input("\nPress Enter to return to the menu... ")


if __name__ == "__main__":
    main()