# Exercise 36: Sales Tax

## Description

Write a Python module, freedonia.py. It should provide a function, calculate_tax, that takes three arguments: the amount of the purchase, the province in which the purchase took place, and the hour (an integer, from 0–24) at which it happened. The calculate_tax function should return the final price, as a float. Sales tax on purchases in Freedonia depends on where the purchase was made, as well as the time of the purchase. Freedonia has four provinces, each of which charges its own percentage of tax:

- Chico: 50%
- Groucho: 70%
- Harpo: 50%
- Zeppo: 40%
The amount of tax applied depends on the hour at which the purchase takes place. The tax percentage is always multiplied by the hour at which the purchase was made.

Write this solution using two separate files. The calculate_tax function and the file freedonia.py, a Python module, which includes any supporting data and functions. . The program that calls calculate_tax should be in a file called use_freedonia.py, which then uses import to load the function.
