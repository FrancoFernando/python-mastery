"""Exercise 30: Flatten A List"""

def flatten(input_list):
    return [item 
            for sublist in input_list 
            for item in sublist]

print(flatten([[1,2], [3,4]]))
