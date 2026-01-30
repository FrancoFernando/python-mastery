'''
The Python 🐍 any() built-in function implements a common programming pattern.


It takes an iterable as input returning True if any element of the iterable is true.


That's very handy in many cases, especially when combined with list comprehension.
'''

def test_any():

  nums = [1,3,5]
  # False
  print(any(n % 2 == 0 for n in nums))
  # True
  print(any(n % 2 != 0 for n in nums))

  text = "I love coding."
  # False
  print(any(char.isdigit() for char in text))
  # True
  print(any(char.isupper() for char in text))
