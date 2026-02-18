"""Exercise 21: Longest Word Per File"""

def find_longest_word(filename):
    longest_word = ""
    with open(filename) as file:
        for line in file:
            longest_word = max(longest_word, max(line.split(), key=len), key=len)
        return longest_word

