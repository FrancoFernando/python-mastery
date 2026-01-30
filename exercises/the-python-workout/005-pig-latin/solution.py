"""Exercise 5: Pig Latin"""

def pig_latin():
    word = input("Enter an english word:")
    translation = pig_latin_internal(word)
    print(f"Pig latin translation:{translation}")

def pig_latin_internal(english_word):

    if len(english_word) == 0:
        return ''
    
    if english_word[0] in "aeiou":
        return f"{english_word}way"
    else:
        return f"{english_word[1:]}{english_word[0]}ay"
    
pig_latin()