'''
Sometimes the Python 🐍 split() function is not enough to process the words in string.

For example, you need to use re.split() with a group to preserve whitespaces.
'''

import re

def test_preserve():

  line = '4   green  12.3 \n'
  items = re.split(r'(\s+)', line)

  print(items)  
  # ['4', '   ', 'green', '  ', '12.3', ' \n', '']
  print(repr(''.join(items)))
  # ' 4   green   12.3\n'
