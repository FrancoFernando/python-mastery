"""Exercise 35: Gematria"""

import string

def gematria_dict():
    return {num+1:chr(ord('a')+num) 
            for num in range(26)}

def gematria_dict_v2():
    return {num:char 
            for char, num in enumerate(string.ascii_lowercase,1)}

print(gematria_dict())
print(gematria_dict_v2())