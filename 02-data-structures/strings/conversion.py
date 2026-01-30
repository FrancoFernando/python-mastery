'''
Python 🐍 has built-in functions to get a string representation of an integer in different bases:

• bin() → binary
• oct() → octal
• hex() → hexadecimal

That's convenient, but I prefer to use fstrings for the same task.
'''

def test_str_to_num():

  num = 17
  # builtin
  binary = bin(num)[2:] #slice out prefix
  octal = oct(num)[2:]
  hexadecimal = hex(num)[2:]

  print(binary,octal, hexadecimal)
  # fstrings
  binary = f"{num:b}"
  octal = f"{num:o}"
  hexadecimal = f"{num:X}"

  print(binary,octal, hexadecimal)
