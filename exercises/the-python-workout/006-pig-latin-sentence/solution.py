"""Exercise 6: Pig Latin Sentence"""

def pl_sentence():
    sentence = input("Enter a sentence:")
    print(pl_sentence_internal(sentence))

def pl_sentence_internal(sentence):
    pl_words = []
    for word in sentence.split():    
        if word[0] in "aeiou":
            pl_words.append(f"{word}way")
        else:
            pl_words.append(f"{word[1:]}{word[0]}ay")

    return " ".join(pl_words)

pl_sentence()
