"""Exercise 35: Gematria"""

from pathlib import Path
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

def gematria_for_v2(word):
    d = gematria_dict()
    return sum(d[c] for c in word)

def gematria_equal_words(word):
    score = gematria_for(word.lower())
    return [w.strip() 
            for w in open(Path(__file__).parent / 'words.txt')
            if gematria_for(w.strip().lower()) == score]

print(gematria_dict())
print(gematria_dict_v2())
print(gematria_for('cat'))
print(gematria_for_v2('cat'))
print(gematria_equal_words('cat'))