"""Exercise 20: Word Count"""

def wordcount(filename):
    char_count = 0
    words_count = 0
    lines_count = 0
    unique_words = set()
    with open(filename) as file:
        for line in file:
            char_count += len(line)
            lines_count += 1
            words = line.split()
            words_count += len(words)
            unique_words.update(words)

    stats = {
        'characters': char_count,
        'words': words_count,
        'lines': lines_count,
        'unique_words': len(unique_words)
    }
    
    for key, value in stats.items():
        print(f"{key.title()}: {value}")

    return stats

from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir.joinpath("wcfile.txt")
wordcount(file_path)