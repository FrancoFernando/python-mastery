# Exercise 24: Reverse Lines

## Description

The function takes two arguments: the names of the input file (to be read from) and the output file (which will be created).
For example, if a file looks like
abc def
ghi jkl
the output file will be
fed cba
lkj ihg
Notice that the newline remains at the end of the string, while the rest of the charac- ters are all reversed.

## learning

- list sliceing can be used to reverse a line [::-1]
- rstrip avoid reversing the newline as well
