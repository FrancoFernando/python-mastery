"""Exercise 10: Summing Anything"""

def my_sum(*args):

    if not args:
        return args
    # args is a tuple
    result = args[0]

    for arg in args[1:]:
        result += arg
    return result

print(my_sum(5, 10, 12, 15))
print(my_sum([5, 10], [12, 15]))
print(my_sum('abc','def'))
