"""Exercise 35: Gematria"""

import string

def gematria_dict():
    return {chr(ord('a')+num):num+1
            for num in range(26)}

def gematria_dict_v2():
    return {char:num
            for char, num in enumerate(string.ascii_lowercase,1)}

def gematria_for(word):
    d = gematria_dict()
    result = 0
    for c in word:
        result += d[c]
    return result

print(gematria_dict())
print(gematria_dict_v2())
print(gematria_for('cat'))