#!/usr/bin/env python3
__version__ = '0.0.0'
'''
TODO : test if
 - input is iterable : https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
 - then check at least 2 values
'''
def subAddition(numbers):
    # initiation
    result=None
    # do defined operation
    if numbers[0]==numbers[1]:
        result=2+numbers[0]
    elif abs(numbers[0]-numbers[1])>1:
        result = max(numbers[0], numbers[1]) + 1
    else:
        result=max(numbers[0],numbers[1])
    # continue with extra parameters
    if len(numbers)>2:
        result = subAddition(tuple([result] + list(numbers[2:])))
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
        result = subAddition((number,number+1))
    # otherwise, addition can be described with sub addition
    else:
        result = repertedNumber
        for repetition in range(1, repertingNumber):
            result = subAddition((result,repertedNumber))
    # finalisation
    return result
