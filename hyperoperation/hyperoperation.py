#!/usr/bin/env python3
__version__ = '0.0.0'
from sys import maxsize
# TODO : test if
''' - input is iterable : https://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable
 - then check at least 2 values'''
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
def redifinedAddition(numbers):
    # initiation
    result=None
    # the sub addition is strangely defined for adding 1
    if numbers[0] == 1 or numbers[1] == 1:
        number = numbers[1]
        if numbers[1] == 1 :
            number=numbers[0]
        result = subAddition((number,number+1))
    # otherwise, addition can be described with sub addition
    else:
        result = numbers[0]
        for repetition in range(1, numbers[1]):
            result = subAddition((result,numbers[0]))
    # continue with extra parameters
    if len(numbers)>2:
        result = redifinedAddition(tuple([result] + list(numbers[2:])))
    # finalisation
    return result
# TODO : test if result > knownValue + 1
def solveSubAddition(knownValue,result):
    # initiation
    solution=None
    # check consistency
    if result < knownValue:
        pass
    # solving
    elif result==2+knownValue:
        solution=knownValue
    elif result==knownValue+1:
        solution=result
    elif result == knownValue:
        solution = knownValue-1
    elif result>knownValue+1:
        solution=result-1
    # finalisation
    return solution
