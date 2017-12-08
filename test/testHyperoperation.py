#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest, sys
from hyperoperation.hyperoperation import subAddition,redifinedAddition
loopLimit=100
# define test
class testHyperoperation(unittest.TestCase):
    # test redifined addition (& commutativity)
    def testSubAddition(self):
        for number0 in range(0,loopLimit):
            # power associativity : x(x(xx)) = (x(xx))x = (xx)(xx)
            result0 = subAddition(number0,subAddition(number0,subAddition(number0, number0)))
            result1 = subAddition(subAddition(number0,subAddition(number0, number0)), number0)
            result2 = subAddition(subAddition(number0, number0),subAddition(number0, number0))
            result3 = subAddition(number0, number0,number0, number0)
            self.assertTrue(result0 == result1 == result2 == result3, "power associativity : " + str(number0))
            for number1 in range(number0, loopLimit):
                # redifined addition value
                result0=number0+number1
                result1=redifinedAddition(number0,number1)
                self.assertEqual(result0,result1,"redifined addition value : "+str((number0,number1)))
                # redifined addition commutativity
                result2=redifinedAddition(number1,number0)
                self.assertEqual(result1, result2, "redifined addition commutativity : "+str((number0,number1)))
                # sub addition commutativity
                result0=subAddition(number0,number1)
                result1=subAddition(number1,number0)
                self.assertEqual(result0, result1, "sub addition commutativity : "+str((number0,number1)))
                # sub addition flexibility
                result0 = subAddition(subAddition(number0, number1), number0)
                result1 = subAddition(number0, subAddition(number1, number0))
                result2 = subAddition(number0, number1, number0)
                self.assertTrue(result0==result1==result2, "sub addition flexibility : "+str((number0,number1)))
    # end of class
    pass
# run test
if __name__ == '__main__':
    unittest.main()