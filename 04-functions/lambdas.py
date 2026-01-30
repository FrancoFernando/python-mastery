"""
🐍 Python: lambdas 🐍

➤ lambdas are anonymous functions returning data

➤ syntax is lambda parameters : expression

➤ parameters shall be comma separated

➤ expression generate the return data

➤ can be used as function arguments

➤ can be assigned to variables

#Python
"""

def lambdas():

   plus_two = lambda num : num + 2  # Assigning the lambda to a variable
   even_odd = lambda num: "Odd" if num % 2 != 0 else "Even"
   print(plus_two(5))  # Calling the lambda and giving it a parameter
   print(even_odd(7))  # Calling the lambda and giving it a parameter

   def calculate(operation, x, y):
    return operation(x, y)

   print(calculate(lambda x,y : x*y, 10, 20))

   nums = [0, 1, 2, 3, 4, 5]
   double_list = map(lambda n: n * 2, nums)
   print(double_list)
   print(list(double_list))

   odd_nums = list(filter(lambda n: n % 2 != 0, nums))
   print(odd_nums)