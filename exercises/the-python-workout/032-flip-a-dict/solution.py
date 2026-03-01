"""Exercise 32: Flip A Dict"""

def flipped_dict(input_dict):
    return {value:key
            for key, value in input_dict.items()}

a_dict = {'a':1,'b':2,'c':3}
print(flipped_dict(a_dict))
