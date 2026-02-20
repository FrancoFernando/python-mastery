"""Exercise 23: Json"""
import json 
from pathlib import Path
from collections import defaultdict

def print_scores(directory_name):
    directory = Path(directory_name)
    if not directory.exists():
        return
    
    json_files = Path(directory_name).glob('*.json')
    if not json_files:
        return
    
    output = {}
    for file_path in sorted(json_files):
        with open(file_path) as file:
            output[file_path.name] = defaultdict(list)
            for row in json.load(file):
                for subject, score in row.items():
                    output[file_path.name][subject].append(score)

    print_statistics(output)

def print_statistics(stats):
    for file_path, data in stats.items():
        print(file_path)
        for subject, scores in data.items():
            print(f"{subject}: min {min(scores)}, max {max(scores)}," \
                   f"average {sum(scores)/len(scores)}")

test_directory = Path(__file__).parent / "scores"
print_scores(test_directory)

#file_name -> subject -> list of scores