# Exercise 13: Printing Tuple Records

## Description

Assume we’re in charge of an upcoming G7 summit. We have information about each of the participating countries as a list of tuples. Write a Python function, format_sort_records, that takes the COUNTRIES list of tuples, and returns a formatted string that has each country appearing on its own line, with three nicely aligned columns. The countries should be presented in alphabetical order by country name.

## Learning

- don't create a list only to iterate over it with a for loop, but create it directly in the loop
- the syntax {name:14} assign to field in a fstring a size of 14
- use operator.itemgetter over a lambda if you only need to retrieve an element
- us "\n".join to concatenate a list of string over multiple line
- think about list comprehension when generating a new list
