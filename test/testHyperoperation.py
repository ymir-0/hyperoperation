#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest
from hyperoperation.hyperoperation import subAddition,redifinedAddition,Jump
# define test
'''
TODO :
 - test bump
 - test symetry
 - test associativity
'''
class testHyperoperation(unittest.TestCase):
    # test redifined surrogate
    def testRedifinedAddition(self):
        for repertedNumber in range(0,10):
            for repertingNumber in range(0, 10):
                expectedAddition=repertedNumber+repertingNumber
                actualAddition=redifinedAddition(repertedNumber,repertingNumber)
                self.assertEqual(expectedAddition,actualAddition,str(repertedNumber)+"+"+str(repertingNumber))
    # test smooth
    def testJump(self):
        for number in range(1, 10):
            smoothValue=subAddition(number,number-1)
            roughValue=subAddition(number,number-1,Jump.rough)
            associatedRoughValue=subAddition(number,number-1,Jump.rough)
            self.assertEqual(smoothValue, roughValue+1, "Jump rough/smooth : "+str(smoothValue) + "+" + str(roughValue))
            self.assertEqual(roughValue, associatedRoughValue, "Jump associated : " + str(roughValue) + "+" + str(associatedRoughValue))
# run test
if __name__ == '__main__':
    unittest.main()