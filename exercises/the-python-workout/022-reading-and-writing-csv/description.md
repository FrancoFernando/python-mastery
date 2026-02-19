# Exercise 22: Reading And Writing Csv

## Description

Create a function, passwd_to_csv, that takes two filenames as arguments: the first is a passwd-style file to read from, and the second is the name of a file in which to write the output. The new file’s contents are the username (index 0) and the user ID (index 2). Note that a record may contain a comment, in which case it will not have anything at index 2; you should take that into consideration when writing the file. The output file should use TAB characters to separate the elements.

## Learning

- python has a specific module for csv files, you need to create a reader/writer object and they take open files as arguments, you can write and read per rows (iterables). delimiter need to be defined in reader/writer
- it's possible concatenate multiple bounded context with comma (i.e. to open two files)
- to create a file use option 'w' in open
