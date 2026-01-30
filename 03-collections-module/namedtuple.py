'''
A Python 🐍 named tuple is like a tuple but with named fields.


It can be a great alternative to construct a class with immutable object types.


Named tuples are handy to:


✓ increase the code readability

✓ enforce a better structure for the data
'''

from collections import namedtuple

def test_namedtuple():
  Point = namedtuple('Point','x,y')
  A = Point(1,3)
  B = Point(2,4)
  dot_product = (A.x * B.x) + (A.y * B.y)
  print(dot_product) #14
