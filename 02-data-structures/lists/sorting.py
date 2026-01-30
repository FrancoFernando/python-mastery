
'''
The simplest Python 🐍 solution to sort according multiple criteria is using the tuple type.

Tuples are comparable, have a natural ordering and all of the methods required by sort().

The limitation is that the direction of sorting for all criteria must be the same.
'''

def sort_multiple_criteria():
  students = [['Tim', 37.21], ['Bob', 37.21], ['Ada', 35]]
  students.sort(key = lambda x: (x[1],x[0]))
  print(students)
  # [['Ada', 35], ['Bob', 37.21], ['Tim', 37.21]]
