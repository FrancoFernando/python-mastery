'''
I personally find Python 🐍 reverse stride slicing very confusing.


An alternative that I often use is the reversed function combined slicing.


Maybe it's a bit less efficient, but much more readable.
'''

def test_reversed():
  foo = '0123456'
  
  backward = foo[-2:0:-1]
  
  backward = ''.join(reversed(foo[1:-1]))
  print(reversed_mid)
