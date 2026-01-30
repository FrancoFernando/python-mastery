'''
A Python 🐍 OrderedDict is a dictionary remembering the insertion order of the keys.

Since Python 3.7 this behaviour is the default also for standard dictionaries.

But there still reasons to use OrderedDict.

1. performances: for high rates of insertions and popitem calls OrderedDict may be a better fit 

2. Intent signaling: using OrderedDict makes clear that the order of keys in the dictionary is important.

3. Controlling the order: the methods move_to_end() and popitem() can be used to reorder the keys

4. Equality test: OrderedDict is better to test dictionaries equality considering the order of the items

5 backward compatibility with versions of Python older than 3.6
'''

from collections import OrderedDict 

def test_orderddict():
  dict = OrderedDict() 
  dict['a'] = 1
  dict['b'] = 2
  dict['c'] = 3
  dict['d'] = 4

  for key, value in dict.items(): 
      print(key, value) 
  # a 1 b 2 c 3 d 4  
  dict['c'] = 5
  for key, value in dict.items(): 
      print(key, value)
  # a 1 b 2 c 5 d 4 
