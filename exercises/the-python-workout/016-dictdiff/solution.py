"""Exercise 16: Dictdiff"""

def dictdiff(first, second):
    output = {}
    keys = first.keys() | second.keys()
    
    for key in keys:
        value_first = first.get(key)
        value_second = second.get(key)
        if (value_first != value_second):
            output[key] = [value_first, value_second]
    return output

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1,d2))


