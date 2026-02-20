"""Exercise 23: Json"""
import json 
from pathlib import Path
from collections import defaultdict

def print_scores(directory_name):
    output = {}
    for file_name in Path(directory_name).iterdir():
        with open(file_name) as file:
            output[file.name] = defaultdict(list)
            for row in json.load(file):
                for subject, score in row.items():
                    output[file.name][subject].append(score)
    #print(output)
    for file_name, data in output.items():
        print(file_name)
        for subject, scores in data.items():
            print(f"{subject}: min {min(scores)} max {max(scores)} average {sum(scores)/len(scores)}")



test_directory = Path(__file__).parent / "scores"
print_scores(test_directory)

#file_name -> subject -> list of scores