"""
🐍 Python: filter function 🐍

➤ extracts elements from an iterable

➤ the synthax is filter(function, iterable)

➤ function is commonly passed as a lambda

➤ returns an iterator convertible to a list, tuple, set, ...

-------------------------------------------------------------

🐍 Python: map function 🐍

➤ apply a function to items of an iterable

➤ the synthax is map(function, iterable, ...)

➤ function is commonly passed as a lambda

➤ multiple iterables can be passed as inputs 

➤ returns a map object usable to create a list, set, ...
"""

def builtin():

   nums  = [0, 1, 2, 3, 4, 5]
   nums2 = [1, 2, 3, 4, 5, 6]
   #map
   double_list = map(lambda n: n * 2, nums)
   print(list(double_list))

   #Correspondent items of each iterable are summed up until the shorter iterable ends
   sum_list = map(lambda n1, n2: n1 + n2, nums, nums2)
   print(list(sum_list))

   #filter
   odd_nums = list(filter(lambda n: n % 2 != 0, nums))
   print(odd_nums)
  