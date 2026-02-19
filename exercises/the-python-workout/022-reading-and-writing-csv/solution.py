"""Exercise 22: Reading And Writing Csv"""
import csv

def passwd_to_csv(input_filename, output_filename):
    with open(input_filename) as input_file, open(output_filename,'w') as output_file:
        input = csv.reader(input_file, delimiter=':')
        output = csv.writer(output_file, delimiter='\t')
        for row in input:
            print(row)
            if row and not row[0].startswith('#'):
                username, _, id, *_ = row
                output.writerow([username,id])

from pathlib import Path

script_path = Path(__file__).parent
input = script_path / 'passwd.txt'
output = script_path / 'passwd_out.txt'
passwd_to_csv(input,output)


