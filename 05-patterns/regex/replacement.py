import re

def replace_string():
    my_string = "  This is  a test   "
    print(my_string)
    #remove all whitespaces
    my_string = re.sub(r'\s', '', my_string)
    print(my_string)