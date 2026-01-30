'''
Use enumerations instead of cluttering your code with constants or magic numbers.


In Python 🐍 you can create enumerations using the Enum class.


An enumeration is a set of symbolic names bound to unique, constant values.
'''

from enum import Enum, unique

@unique
class Direction(Enum):
  FORWARD = 1
  UP = 2
  DOWN = 3

def test_enums():
  print(repr(Direction.FORWARD)) 
  # <Direction.FORWARD: 1>
  print(DirectionInt.FORWARD == 1) 
  # False
