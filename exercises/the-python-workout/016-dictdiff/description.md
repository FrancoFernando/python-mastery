# Exercise 16: Dictdiff

## Description

Write a function, dictdiff, that takes two dicts as arguments. The function returns a new dict that expresses the difference between the two dicts. If there are no differences between the dicts, dictdiff returns an empty dict. For each key–value pair that differs, the return value of dictdiff will have a key–value pair in which the value is a list containing the values from the two different dicts. If one of the dicts doesn’t contain that key, it should contain None.

## Learning 

- Using first.keys() | second.keys() is the best approach to find all the keys in 2 dictionaries
- The comparison first.get(key) != second.get(key) would work for lists and dicts because Python compares their contents, not identity.
- when you need to build a new dictionary consider dictionary comprehension
