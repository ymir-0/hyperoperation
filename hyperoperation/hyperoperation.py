#!/usr/bin/env python3
__version__ = '0.0.0'
'''
TODO :
 - define reverse operation
 - define for decimal numbers
 - define for negative numbers
'''
def subAddition(number0,number1,*extraNumbers):
    # initiation
    result=None
    # do defined operation
    if number0==number1:
        result=2+number0
    elif abs(number0-number1)>1:
        result = max(number0, number1) + 1
    else:
        result=max(number0,number1)
    # continue with extra parameters
    if len(extraNumbers)>0:
        for extraNumber in extraNumbers:
            result = subAddition(result, extraNumber)
    # finalisation
    return result
def redifinedAddition(repertedNumber,repertingNumber):
    # initiation
    result=None
    # the sub addition is strangely defined for adding 1
    if repertedNumber == 1 or repertingNumber == 1:
        number = repertingNumber
        if repertingNumber == 1 :
            number=repertedNumber
        result = subAddition(number,number+1)
    # otherwise, addition can be described with sub addition
    else:
        result = repertedNumber
        for repetition in range(1, repertingNumber):
            result = subAddition(result,repertedNumber)
    # finalisation
    return result
