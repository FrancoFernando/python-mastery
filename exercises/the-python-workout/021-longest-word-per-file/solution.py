"""Exercise 21: Longest Word Per File"""

def find_longest_word(filename):
    longest_word = ""
    with open(filename) as file:
        for line in file:
            words = line.split()
            if words:
                longest_word = max(longest_word, max(words, key=len), key=len)
        return longest_word

from pathlib import Path

script_path = Path(__file__).parent
filepath = script_path / 'files' / '43-0.txt'
print(find_longest_word(filepath))