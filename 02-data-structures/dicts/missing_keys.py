'''
 🐍 Python has 4 common ways to detect and handle missing keys in dictionaries: 

1. KeyError exception
2. in expression
3. get method
4. setdefault

Which is the best one ?

Let's suppose we need to assign a value to the missing key.

In expression is not efficient, requiring 2 access and 1 assignment.

KeyError exception is better, requiring only 1 access.

Both require duplicated code for the assignment.

This reduce readability. Better to avoid.

The get method also requires 1 access and 1 assignment, but it’s shorter than KeyError.

This make it the best solution when values are basic types like numbers or strings.

For complex values (i.e. lists), it is still effective, especially combined with the walrus operator.

The setdefault method is an alternative. 

If the key isn’t present, it assigns the default value provided to that key. 

In any case, it returns the value for that key.

It is shorter than using get, but it can be tricky for 2 reasons.

1. The default value is assigned and not copied into the dictionary when the key is missing. So it's necessary to construct a new default value for each key.

2. The name of the method is not self-explanatory for people not familiar with it.

'''
def simple_values():
    fruit = {
        'apple': 3,
        'lemon': 2,
    }

    key = 'orange'

    if key in fruit:
        fruit[key] += 1
    else:
        fruit[key] = 1
        
    try:
        fruit[key] += 1
    except KeyError:
        fruit[key] = 1
        
    # get method  
    count = fruit.get(key, 0)
    fruit[key] = count + 1
    
    # setdefault method  
    count = fruit.setdefault(key, 0)
    fruit[key] = count + 1

def complex_values():
    origin = {
        'apple': ['ch', 'it'],
        'lemon': ['spa', 'it'],
    }
    key = 'orange'
    where = 'it'

    # get method  
    if (fruit := origin.get(key)) is None:
        origin[key] = countries = []

    countries.append(where)
 
    # setdefault method  
    countries = origin.setdefault(key, [])
    countries.append(where)

