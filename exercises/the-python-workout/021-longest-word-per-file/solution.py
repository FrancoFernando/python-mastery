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
    return {file.name:find_longest_word(file) for file in dir_path.iterdir() if file.is_file()}
    """ output = {}
    for file in dir_path.iterdir():
        output[file.name] = find_longest_word(file) 
    return output"""

def find_all_longest_words_v2(dirname):
    return {file:find_longest_word(os.path.join(dirname, file)) 
            for file in os.listdir(dirname) 
            if os.path.isfile(os.path.join(dirname, file))}

script_path = Path(__file__).parent
# to test find_longest_word alone
# filepath = script_path / 'files' / '43-0.txt'
print(find_all_longest_words(script_path / 'files'))
print(find_longest_word(script_path / 'files'))