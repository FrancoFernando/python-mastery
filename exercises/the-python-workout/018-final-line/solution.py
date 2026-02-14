"""Exercise 18: Final Line"""

def get_final_line(filename):
    last_line = ""
    with open (filename, 'r') as file:
        for line in file:
            last_line = line
    return last_line

from pathlib import Path

script_dir = Path(__file__).parent
filepath = script_dir / 'demofile.txt'
print(get_final_line(filepath))