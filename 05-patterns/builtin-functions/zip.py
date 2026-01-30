'''
The Python 🐍 zip function can be used to iterate over multiple iterators in parallel.


But be careful when supplying iterators of different length ⚠️


Zip truncates its output silently to the shortest iterator.


Use the zip_longest function from itertools to avoid truncation.
'''

import itertools

fruits = ['apple','lemon','orange','pear']
prices = [5, 2, 7]

for fruit,price in zip(fruits, prices):
  print(f"{fruit} price is {price}$")
# apple price is 5$
# lemon price is 2$
# orange price is 7$
  
for fruit,price in itertools.zip_longest(fruits, prices):
  print(f"{fruit} price is {price}$")
  
# apple price is 5$
# lemon price is 2$
# orange price is 7$
# pear price is None$
