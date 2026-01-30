"""
🐍 Python: String Slicing 🐍

➤ Definition & syntax
➤ Slicing with step
➤ Reverse Slicing
➤ Partial Slicing

1. Definition & syntax

Slicing a string means getting a portion of it using its indexes.

The syntax is 🠖 string[start:end]
start 🠖 index from where the substring start
end 🠖 index where the substring end

The character at the end index is not included in the substring.

2. Slicing with step

You can specify a step for skipping characters in the string.

The syntax is 🠖 string[start:end:step]

The default step when no specified is

3. Reverse Slicing

Reverse slicing return a reversed substring.

This requires to switch the order of the start and end indices and a negative step.

4. Partial Slicing

Specifying the start and end indexes is optional.

When start is not provided, the substring has all the characters until the end index.

When end is not provided, the substring begins from the start index and go all the way to the end.
"""

def slicing():

    my_name = "I am Franco Fernando!"
    print(my_name[0:5]) # From the start till before the 4th index
    print(my_name[1:7])
    print(my_name[8:len(my_name)]) # From the 8th index till the end

    #with step
    print(my_name[0:7:2])  # A step of 2
    print(my_name[0:7:5])  # A step of 5

    #reverse
    print(my_name[13:2:-1]) # Take 1 step back each time
    print(my_name[17:0:-2]) # Take 2 steps back. The opposite of what happens in the slide above

    #partial
    print(my_name[:8]) # All  characters before index 8
    print(my_name[8:])  # All the characters starting from 'M'
    print(my_name[:])  # The whole string
    print(my_name[::-1])  # The whole string in reverse (step is -1)