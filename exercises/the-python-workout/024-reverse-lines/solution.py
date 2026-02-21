"""Exercise 24: Reverse Lines"""

def reverse_lines(input_file_path, output_file_path):
    with open(input_file_path) as input_file, \
        open(output_file_path, 'w') as output_file:
        for line in input_file:
            stripped_line = line.rstrip() # needed to reverse only the content not the newline
            output_file.write(f"{stripped_line[::-1]}\n") # put back the newline after reversing

from pathlib import Path

script_path = Path(__file__).parent
input_path = script_path / "testfile.txt"
output_path = script_path / "reversed.txt"
reverse_lines(input_path, output_path)