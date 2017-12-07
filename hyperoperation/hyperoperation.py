#!/usr/bin/env python3
__version__ = '0.0.0'
def subAddition(a,b):
    result=None
    if a==b:
        result=2+a
    else:
        result = max(a, b) + 1
    '''elif abs(a-b)>1:
        result = max(a, b) + 1
    else:
        result=max(a,b)'''
    return result