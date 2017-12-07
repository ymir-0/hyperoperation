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
                # compare with addition
                expectedAddition=repertedNumber+repertingNumber
                actualRedifinedAddition=redifinedAddition(repertedNumber,repertingNumber)
                self.assertEqual(expectedAddition,actualRedifinedAddition,"redifined addition value : "+str(repertedNumber) + " / " + str(repertingNumber))
                # check commutativity
                commutatedRedifinedAddition=redifinedAddition(repertingNumber,repertedNumber)
                self.assertEqual(actualRedifinedAddition, commutatedRedifinedAddition, "redifined addition commutativity : "+str(repertedNumber) + " / " + str(repertingNumber))
    # test smooth
    def testJump(self):
        for number in range(1, 10):
            # check jump
            smoothValue=subAddition(number,number-1)
            roughValue=subAddition(number,number-1,Jump.rough)
            self.assertEqual(smoothValue, roughValue+1, "Jump rough/smooth : "+str(smoothValue) + "+" + str(roughValue))
            # check commutativity
            commutatedRoughValue=subAddition(number,number-1,Jump.rough)
            self.assertEqual(roughValue, commutatedRoughValue, "Jump commutativity : " + str(roughValue) + " / " + str(commutatedRoughValue))
# run test
if __name__ == '__main__':
    unittest.main()