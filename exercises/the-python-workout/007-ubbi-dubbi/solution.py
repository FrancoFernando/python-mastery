"""Exercise 7: Ubbi Dubbi"""

def ubbi_dubbi():
    word = input("Enter a word:")
    print(f"Ubbi Dubbi translation is: {ubbi_dubbi_internal(word)}")

def ubbi_dubbi_internal(word):
    output = []
    for c in word:
        if c in "aeiou":
            output.append(f"ub{c}")
        else:
            output.append(c)
    return ''.join(output)

ubbi_dubbi()
