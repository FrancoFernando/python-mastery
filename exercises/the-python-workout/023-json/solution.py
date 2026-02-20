"""Exercise 23: Json"""
import json 
from pathlib import Path

def print_scores(directory_name):
    for file_name in Path(directory_name).iterdir():
        with open(file_name) as file:
            print(json.load(file))

test_directory = Path(__file__).parent / "scores"
print_scores(test_directory)