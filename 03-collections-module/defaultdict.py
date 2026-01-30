'''
🐍 #Python defaultdict

You can use defaultdict to manage a dictionary with many potential keys.

✦ available in the collections built-in module

✦ store a default value when a key is missing

✦ initialized with a function returning the default value
'''

class Students:
    def __init__(self):
       self.data = defaultdict(set)

    def add(self, course, student):
       self.data[course].add(student)

def test_defaultdict():

    students = Students()
    students.add('French', 'Louie')
    students.add('French', 'Adi')
    print(students.data)

