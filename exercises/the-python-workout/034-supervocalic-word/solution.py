"""Exercise 34: Supervocalic Word"""
from collections import Counter

def get_sv(filename):

    vocals = {'a','e','i','o','u'}
       
    with open(filename) as file:
        return {word 
                for word in file
                if vocals < set(word)}
    
from pathlib import Path
script_path = Path(__file__).parent
file_path = script_path / "words.txt"
print(get_sv(file_path))



