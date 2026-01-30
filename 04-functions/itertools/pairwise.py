'''
Python 🐍 3.10 introduced a pairwise function in itertools.

• return consecutive overlapping pairs from an iterable

• the number of pairs is 1 fewer than the length of the iterable

I've found pairwise very handy in many common use cases.
'''


from itertools import pairwise

nums = [1, 2, 3, 4]
for x, y in pairwise(nums):
   print("{} + {} = {}".format(x, y, y-x))

# 2 - 1 = 1
# 3 - 2 = 1
# 4 - 3 = 1
