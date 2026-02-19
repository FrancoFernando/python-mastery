# Exercise 21: Longest Word Per File

## Description

Write two functions. First, find_longest_word takes a filename as an argument and returns the longest word found in the file. The second function, find_all_longest_words, takes a directory name and returns a dict in which the keys are filenames and the values are the longest words from each file

## Learning

- multiple ways to iterate over a file. os module is the traditional way. os works with strings: the os.path.join(1,2) concatenate multiple paths, os.path.isfile(1) check if the path is a file, os.listdir(dirname) lists all files in a directory. pathlib is the new standard, it uses object oriented approach. constructor initialized with an absolute path, then you have methods to iterate ofver a file iterdir(), join paths script_path / 'files', or check if isfile.

- dictionary comprehension when generating or returninga dict 