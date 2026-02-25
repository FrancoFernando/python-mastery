"""Exercise 28: Join Numbers"""

def join_numbers(range):
    return ','.join([str(x) for x in range])

print(join_numbers(range(15)))