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
def subAddition(jump=Jump.smooth,*extraNumbers,number0,number1):
    # initiation
    result=None
    # do defined operation
    if number0==number1:
        result=2+number0
    elif jump.value or (not jump.value and abs(number0-number1)>1):
        result = max(number0, number1) + 1
    else:
        result=max(number0,number1)
    # continue with extra parameters
    if len(extraNumbers)>0:
        if len(extraNumbers) == 1:
            result=subAddition(jump,number0=result,number1=extraNumbers[0])
        else:
            result=subAddition(jump,extraNumbers[1:],number0=result,number1=extraNumbers[0])
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
            result = subAddition(jump=jump,number0=result,number1=repertedNumber)
    # finalisation
    return result
