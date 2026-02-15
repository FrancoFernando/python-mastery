"""Exercise 19: Etc Passwd To Dict"""

def passwd_to_dict(filename):
    output = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('#'):
                username, _, id, *_ = line.split(':')
                output[username] = id
    return output


from pathlib import Path

script_dir = Path(__file__).parent
filepath = script_dir / 'passwd.txt'
print(passwd_to_dict(filepath))
