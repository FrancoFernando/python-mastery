"""Exercise 35: Gematria"""

def gematria_dict():
    return {num+1:chr(ord('a')+num) 
            for num in range(26)}

print(gematria_dict())
