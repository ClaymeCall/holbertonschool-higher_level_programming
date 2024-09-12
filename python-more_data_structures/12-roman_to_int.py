#!/usr/bin/python3

def roman_to_int(roman_string):
    # Checking for incorrect input roman string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Reversing roman string to facilitate its processing
    rom = list(reversed(roman_string))

    conv = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    res = conv[rom[0]]  # Start with the first value in the reversed string

    # Loop through the reversed Roman string starting from the second element
    for i in range(1, len(rom)):
        # If current numeral is less than the previous one, subtract its value
        if conv[rom[i]] < conv[rom[i - 1]]:
            res -= conv[rom[i]]
        else:
            # Otherwise, just add its value
            res += conv[rom[i]]

    return res
