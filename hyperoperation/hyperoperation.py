#!/usr/bin/env python3
__version__ = '0.0.0'
from enum import Enum, unique
@unique
class Jump(Enum):
    smooth = True
    rough = False
'''
TODO :
 - define reverse operation
 - define for decimal numbers
 - define for negative numbers
'''
def subAddition(number0,number1,jump=Jump.smooth):
    # initiation
    result=None
    # do defined operation
    if number0==number1:
        result=2+number0
    elif jump.value or (not jump.value and abs(number0-number1)>1):
        result = max(number0, number1) + 1
    else:
        result=max(number0,number1)
    # finalisation
    return result
def redifinedAddition(repertedNumber,repertingNumber,jump=Jump.smooth):
    # initiation
    result=None
    # the sub addition is not defined for adding 1
    if repertedNumber == 1 or repertingNumber == 1:
        result = repertedNumber+repertingNumber
    # otherwise, addition can be descripted with sub addition
    else:
        result = repertedNumber
        for repetition in range(1, repertingNumber):
            result = subAddition(result, repertedNumber,jump)
    # finalisation
    return result
