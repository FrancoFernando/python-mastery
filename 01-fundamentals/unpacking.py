"""
🐍 Python: unpacking 🐍


You can increase code clarity by assigning multiple values in a single statement.


Can be applied for:


➤ accessing tuple values


➤ unpacking iterables in any nested levels


➤ avoiding explicitly indexing into sequences

🐍 Python: inplace  swap 🐍

You can use the unpacking syntax to swap indexes in 1 line.

➤ the right side of the assignment is evaluated first

➤ its values are put into a new temporary unnamed tuple

➤ that tuple value is unpacked to the left side of the assignment
"""

def unpacking():
  
   #tuple unpacking
   my_tuple = ('Red', 'Green')
   red, green = my_tuple 
   print(red, '&', green)

   school_classes = {
    'A': ('Bob', 10),
    'B': ('Ann', 18),
    'C': ('Tim', 20),
    }

   #iterables unpacking
   ((class1, (teacher1, students1)),
   (class2, (teacher2, students2)),
   (class3, (teacher3, students3))) = school_classes.items()

   print(f'Teacher {teacher1} has {class1} with {students1} students')
   print(f'Teacher {teacher2} has {class2} with {students2} students')
   print(f'Teacher {teacher3} has {class3} with {students3} students')

   #no index iteration
   stocks = [('GOOG', 2700),('AAPL', 173), ('MSFT', 310)]
   for rank, (name, price) in enumerate(stocks, 1):
    print(f'#{rank}: {name} value is ${price}')

   # Swap
   nums = [5, 2, 8, 3, 5, 4]
   for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        nums[i-1], nums[i] = nums[i], nums[i-1] 
  