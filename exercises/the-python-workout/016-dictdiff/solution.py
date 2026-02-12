"""Exercise 16: Dictdiff"""

def dictdiff(first, second):
    output = {}
    keys = first.keys() | second.keys()
    
    for key in keys:
        value_first = first.get(key)
        value_second = second.get(key)
        if value_first != value_second:
            output[key] = [value_first, value_second]
    return output

def dictdiff_v2(first, second):
    keys = first.keys() | second.keys()

    return {
        key: [first.get(key), second.get(key)]
        for key in keys if first.get(key) != second.get(key)
    }

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1,d2))
print(dictdiff_v2(d1,d2))

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3,d4))
print(dictdiff_v2(d3,d4))


d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d5))
print(dictdiff_v2(d1, d5))