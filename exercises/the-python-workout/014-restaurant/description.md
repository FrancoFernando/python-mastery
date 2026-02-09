# Exercise 14: Restaurant

## Description

Create a new constant dict, called MENU, representing the possible items you can order at a restaurant. The keys will be strings, and the values will be prices (which we’ll make integers for the sake of simplicity). You should then write a function, restaurant, that asks the user to enter an order:

- If the user enters the name of a dish on the menu, the program prints the price and the running total. It then asks the user again for their order.
- If the user enters the name of a dish not on the menu, the program scolds the user (mildly). It then asks the user again for their order.
- If the user enters an empty string, the program stops prompting and prints the total amount.

## Learning

- walrus operator can replace while True
- syntax for dictionary is {key:value,key:value,..}
