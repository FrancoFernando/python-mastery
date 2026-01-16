def my_sum(*nums):
    # nums is a tuple
    result = 0

    for num in nums:
        result += num
    return result

print(my_sum(5, 10, 12, 15))