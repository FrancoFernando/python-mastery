"""Exercise 12: Word With Most Repeated Letters"""
from collections import Counter

def most_repeating_word(words):
    output = ""
    high_frequency = 0
    for word in words:
        most_repeated_value = Counter(word).most_common(1)[0][1]
        if most_repeated_value > high_frequency:
            output = word
            high_frequency = most_repeated_value
    
    return output

print(most_repeating_word(['this', 'is', 'an', 'elementary', 'test', 'example']))

