def hex_output():

    hex = input("Enter an hex number (without 0x): ")
    result = 0
    for index, digit in enumerate(reversed(hex)):
        result += int(digit) * (16 ** index)

    print(f"The corresponding integer is {result}")

hex_output()