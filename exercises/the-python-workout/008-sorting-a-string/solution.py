"""Exercise 8: Sorting A String"""

def strsort(input):
    return ''.join(sorted(input))

output = strsort(input('Enter a string:'))
print(output)
