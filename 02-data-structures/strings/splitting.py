'''
In Python 🐍 you can split a string starting at its end using rpartition or rsplit.


The advantage of rpartition is that it guarantee a fixed argument unpacking size.


The advantage of rsplit is that it allow to specify the maximum number of split.
'''

def test_rpartition():
  s = "1.2.3"
  a, dot, b = s.rpartition('.')
  # ('1.2', '.', '3')
  a, b = s.rsplit('.', 1)
  #['1.2', '3']
  a, b, c = s.rsplit('.', 2)
  # ['1', '2', '3']
