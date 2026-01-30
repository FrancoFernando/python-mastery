'''
🐍 Python: zip 🐍


You can use zip to iterate in parallel over multiple iterators.


➤ wraps multiple iterators with a lazy generator


➤ the generator yields tuples containing the next value from each iterator


➤ the output is truncated to the shortest iterator

🐍 #Python: zip_longest 🐍

You should consider using zip_longest to iterate in parallel over multiple iterators of different lenght.

➤ included in itertools

➤ no truncation to the shortest iterable

➤ replaces missing values with the passed fillvalue (default = None)
'''

def list_iteration():

    # empty list
    my_list = []

    # list initialized always with same element
    n = 1000
    my_int_list = [0] * n
    my_bool_list = [False] * n
    
    for i, num in enumerate(my_list):
        print("index " + str(i) + " value " + str(num))

    stocks = ['GOOG','AAPL','MSFT']
    prices = [2700, 173, 310]

    for stock, price in zip(stocks, prices):
        print(f'{stock} value is {price}')
    
    stocks.append('XYZ')

    for stock, price in itertools.zip_longest(stocks, prices, fillvalue = 0):
        print(f'{stock} value is {price}')
