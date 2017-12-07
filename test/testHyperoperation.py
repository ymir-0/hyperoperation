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
        for number0 in range(0,10):
            for number1 in range(number0, 10):
                # compare with addition
                expectedAddition=number0+number1
                actualRedifinedAddition=redifinedAddition(number0,number1)
                self.assertEqual(expectedAddition,actualRedifinedAddition,"redifined addition value : "+str(number0) + " / " + str(number1))
                # check commutativity
                commutatedRedifinedAddition=redifinedAddition(number1,number0)
                self.assertEqual(actualRedifinedAddition, commutatedRedifinedAddition, "redifined addition commutativity : "+str(number0) + " / " + str(number1))
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