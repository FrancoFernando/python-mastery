# Exercise 29: Add Numbers

## Description

Our function (sum_numbers) will take a string as an argument. For example, 10 abc 20 de44 30 55fg 40
Given that input, our function should return 100. That’s because the function will ignore any word that contains nondigits, turn the others into numbers, and then sum them.

## Learning

- str.isdigit check if the string has only digits
- split the input string to process each word
- int(str) convert str to integer, without the isdigit check raise an exception
