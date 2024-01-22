#!/bin/python3

import re

LEG_CELL_PHONE_CODE = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' ',
}

#
# Complete the 'is_valid' function below.
#
def is_valid(input: str) -> bool:
    """
    Input is valid if: 
    * Only starts with numbers 2-9 and 0.
    * Contains numbers from 2 to 9 and 0, plus '*'
    """
    regex = r"^[2-90]+[2-90*]*$"

    return True if re.match(regex, input) else False

#
# Complete the 'translate' function below.
#
def translate(key: str) -> str:
    translated_word = []
    prev_digit = None
    count = 0
    
    for digit in key:        
        # Check if it's a new digit or the same one from a previus iteration
        if prev_digit != digit or count == len(LEG_CELL_PHONE_CODE[prev_digit]):
            count = 0
            prev_digit = digit
        
        if digit == '*':
            continue
            
        # If it's the firt letter for the digit, append it. Otherwise, replace it.
        if count == 0:
            translated_word.append(LEG_CELL_PHONE_CODE[prev_digit][count])
        else:
            translated_word[-1] = LEG_CELL_PHONE_CODE[prev_digit][count]
        
        count += 1
        
    return ''.join(translated_word)
        

if __name__ == '__main__':

    input = input().strip().lstrip("*")

    if not is_valid(input):
        print(f"Invalid input: {input}.")
        exit(0)

    result = translate(input)

    print(result)
    