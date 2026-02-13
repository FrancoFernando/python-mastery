"""Exercise 17: How Many Different Numbers"""

def how_many_different_numbers(nums):
    return len(set(nums))

numbers = [1, 2, 3, 1, 2, 3, 4, 1]
print(how_many_different_numbers(numbers))