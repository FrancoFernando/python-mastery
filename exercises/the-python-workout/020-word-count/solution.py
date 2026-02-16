"""Exercise 20: Word Count"""

def wordcount(filename):
    characters = 0
    number_of_words = 0
    lines = 0
    unique_words = set()
    with open(filename) as file:
        for line in file:
            characters += len(line)
            words = line.split()
            number_of_words += len(words)
            lines += 1
            unique_words.update(words)
    
    print(f"Characters: {characters} \n" 
          f"Words: {number_of_words} \n"
          f"Lines: {lines} \n"
          f"Unique words: {len(unique_words)} \n")

    

from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir.joinpath("wcfile.txt")
wordcount(file_path)