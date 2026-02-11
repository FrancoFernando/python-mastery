# Exercise 15: Rainfall

## Description

 Write a function, get_rainfall, that tracks rainfall in a number of cities. Users of your program will enter the name of a city; if the city name is blank, the function prints a report before exiting. If the city name isn’t blank, the program should also ask the user how much rain has fallen in that city (typically measured in millimeters). After the user enters the quantity of rain, the program again asks them for a city name, rainfall amount, and so on, until the user presses Enter instead of typing the name of a city. When the user enters a blank city name, the program exits, but first, it reports how much total rainfall there was in each city.

 ## Learning

- the input method always return a string even in case of numbers, so you need to explicitly convert string to numbers
- when updating a dictionary you can't use something like dict[key] += number because you need to handle the first time the key is inserted. Alternatives are dict.get(key, defaultvalue) or default dict.
