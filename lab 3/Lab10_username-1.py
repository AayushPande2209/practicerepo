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
            with self.__filepath.open("r", encoding="utf-8") as file:
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
