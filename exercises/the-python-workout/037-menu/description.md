# Exercise 37: Menu

## Description

Write a new module called “menu” (in the file menu.py). The module should define a function, also called menu. The function takes any number of key–value pairs as arguments. Each value should be a callable, a fancy name for a function or class in Python. When the function is invoked, the user is asked to enter some input. If the user enters a string that matches one of the keyword arguments, the function associated with that keyword will be invoked, and its return value will be returned to menu’s caller. If the user enters a string that isn’t one of the keyword arguments, they’ll be given an error message and asked to try again.
The idea is that you’ll be able to define several functions and then indicate what user input will trigger each function.

## Learning

- think to **kwargs every time you hear "takes any number of key–value pairs as arguments"
