# Exercise 26: Prefix Notation Calculator

## Description

Write a function (calc) that expects a single argument—a string containing a simple math expression in prefix notation—with an operator and two numbers.
Your program will parse the input and produce the appropriate output. For our purposes, it’s enough to handle the six basic arithmetic
operations in Python: addition, subtraction, multiplication, division (/), modulus (%), and exponentiation (**). The normal Python math rules should work, such that
division always results in a floating-point number. We’ll assume, for our purposes, that
the argument will only contain one of our six operators and two valid numbers.

- hint: you should implement each of the operations as a separate function
- you shouldn’t use an if statement to decide which function should be run
- look at the operator module, whose functions implement many of Python’s operators

## Learning

- a dispatch table is a dictionary where values are functions that can be called as table[key](args)
- lambda notation: lambda x,y : x**y 
- maxsplit = 2 can be passed to split to say the max numbers of split to make (equal to the max valid index in the output list)
  