"""Exercise 29: Add Numbers"""

def sum_numbers(input):
    return sum([int(x) for x in input.split() if str.isdigit(x)])

print(sum_numbers("10 abc 20 de44 30 55fg 40"))
