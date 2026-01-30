'''
🐍 Python: enumerate 🐍

The enumerate function allow to iterate over a list and know the index of the current item.

➤  yields pairs of loop indexes and the values from the given list

➤  each yielded pair can be succinctly unpacked in a for statement 
'''

def list_iteration():

    my_list = [0,1,2,3,4,5]

    for i in range(0, len(my_list)):
        print(my_list[i])

    for i in range(0, len(my_list),2):
        print(my_list[i])

    for i, num in enumerate(my_list):
        print(f"index {i} value {num}")

    countries = ["Italy","Usa","India","China"]
    
    for i, city in enumerate(countries,1):
        print(f"#{i}: {city}")