# Exercise 27: Password Generator

## Description

Create a factory for password-generation function. The function create_password_ generator takes a string and return a function, which itself takes an integer argument. Calling this function will return a password of the specified length, using the string from which it was created.

alpha_password = create_password_generator('abcdef')
print(alpha_password(5)) # efeaa
