# Exercise 23: Json

## Description

Write a function, print_scores, that takes a directory name as an argument and prints a summary of the student scores it finds. Each directory contains multiple files and each file contains the JSON equivalent of a list of dicts, with each dict containing scores for several different school subjects. Your function should print the highest, lowest, and average test scores for each subject in each class.

## Learning

- glob instead of iterdir allows to filter for patterns (pathlib)
- use defaultdict
- json.load loads from file, json.loads loads a string
- use items() to unpack and iterate over key, value in a dict
- - there is a statistics package to calculate i.e. avg
