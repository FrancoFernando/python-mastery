"""Exercise 21: Longest Word Per File"""

from pathlib import Path
import os

def find_longest_word(filename):
    longest_word = ""
    with open(filename) as file:
        for line in file:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word

def find_all_longest_words(dirname):
    dir_path = Path(dirname)
    return {file.name:find_longest_word(file) for file in dir_path.iterdir()}
    """ output = {}
    for file in dir_path.iterdir():
        output[file.name] = find_longest_word(file) 
    return output"""

script_path = Path(__file__).parent
filepath = script_path / 'files' / '43-0.txt'
print(find_all_longest_words(script_path / 'files'))
#print(find_longest_word(filepath))