# Exercise 31: Pig Latin Translation Of A File

## Description

Write a function plfile that takes a filename as an argument. It returns a string with the file’s contents, but with each word translated into Pig Latin, as per our plword function in chapter 3 on strings. The returned translation can ignore newlines and isn’t required to handle capitalization and punctuation in any specific way.

## Learning

- A generator expression looks almost like a list comprehension, but it uses round parentheses rather than square brackets. (x for x in ...) vs [x for x in ...]
- when you havea lotof data (i.e. reading from a file) it is better to use generator that return an iterator object because save memory, only calculating the minimum necessary for each iteration.
- With a generator, it yields one pig_latin(word) result at a time; join() consumes each value immediately; Only one word is in memory at any moment O(1) memory
- With a list comprehension, all translated words are computed first, the entire list is stored in memory, then join() processes the list
- using a generator expression inside a function call (like join) you can omit the generator parenthesis ()