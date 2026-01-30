'''
Two ways to compare Python 🐍 lists without considering their order:

1. Using the builtin sorted method

2. Using Counter from collections

Do you know any alternative ?
'''

from collections import Counter

def compare_lists():
  A = [1,2,1,3]
  B = [2,1,3,4]
  C = [2,1,3,1]

  # sorted
  print(sorted(A) == sorted(B)) # False
  print(sorted(A) == sorted(C)) # True

  # counter
  print(Counter(A) == Counter(B)) # False
  print(Counter(A) == Counter(C)) # True
