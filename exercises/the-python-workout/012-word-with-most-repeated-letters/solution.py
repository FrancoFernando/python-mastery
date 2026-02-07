"""Exercise 12: Word With Most Repeated Letters"""
from collections import Counter

def most_repeating_word(words):
    if not words:
        return ""
    
    output = ""
    max_frequency = 0
    for word in words:
        max_letter_frequency = Counter(word).most_common(1)[0][1]
        if max_letter_frequency > max_frequency:
            output = word
            max_frequency = max_letter_frequency
    
    return output

def most_repeating_word_v2(words):
    if not words:
        return ""
    
    return max(words, key=lambda w : Counter(w).most_common(1)[0][1])

print(most_repeating_word(['this', 'is', 'an', 'elementary', 'test', 'example']))
print(most_repeating_word_v2(['this', 'is', 'an', 'elementary', 'test', 'example']))
