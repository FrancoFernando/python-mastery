"""Exercise 26: Prefix Notation Calculator"""

dispatch_table = {"+": lambda x,y : x+y, 
                  "-": lambda x,y : x-y,
                  "*": lambda x,y : x*y,
                  "/": lambda x,y : x/y,
                  "%": lambda x,y : x%y,
                  "**": lambda x,y : x**y,}

def calc(prefix_expression):
    operator, left, right = prefix_expression.split(maxsplit=2)
    return dispatch_table[operator](int(left), int(right))

print(calc("** 2 3"))