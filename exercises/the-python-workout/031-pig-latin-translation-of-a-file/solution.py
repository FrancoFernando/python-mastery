"""Exercise 31: Pig Latin Translation Of A File"""

def pig_latin(word):
    
    if word[0] in "aeiou":
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

def plfile(filename):
    with open(filename) as file:
        return ' '.join(pig_latin(word)
                         for line in file
                         for word in line.split())
    
from pathlib import Path

script_path = Path(__file__).parent
file_path = script_path / "demofile.txt"
print(plfile(file_path))