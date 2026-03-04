"""Exercise 35: Gematria"""

def gematria_dict():
    return {num:chr(96+num) 
            for num in range(1,27)}

print(gematria_dict())
