"""Exercise 19: Etc Passwd To Dict"""

def passwd_to_dict(filename):
    output = {}
    with open(filename) as file:
        for line in file:
            if not line.startswith(('#','\n')):
                fields = line.split(':')
                output[fields[0]] = fields[2]
    return output


from pathlib import Path

script_dir = Path(__file__).parent
filepath = script_dir / 'passwd.txt'
print(passwd_to_dict(filepath))
