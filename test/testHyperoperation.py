#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest
from hyperoperation.hyperoperation import subAddition,redifinedAddition,solveSubAddition
from sys import maxsize
loopLimit=100
# define test
class testHyperoperation(unittest.TestCase):
    # test redifined addition (& commutativity)
    def testSubAddition(self):
        # verified properties
        for number0 in range(0,loopLimit):
            for number1 in range(number0, loopLimit):
                # redifined addition value : x + y
                result0=number0+number1
                result1=redifinedAddition((number0,number1))
                self.assertEqual(result0,result1,"redifined addition value : "+str((number0,number1)))
                # sub addition commutativity : xy = yx
                result0=subAddition((number0,number1))
                result1=subAddition((number1,number0))
                self.assertEqual(result0, result1, "sub addition commutativity : "+str((number0,number1)))
                subAdditionResult=result0
                # sub addition flexibility : (xy)x = x(yx)
                result0 = subAddition((subAddition((number0, number1)), number0))
                result1 = subAddition((number0, subAddition((number1, number0))))
                result2 = subAddition((number0, number1, number0))
                self.assertTrue(result0==result1==result2, "sub addition flexibility : (xy)x = x(yx) = xyx : "+str((number0,number1)))
                # test solving
                solution=solveSubAddition(number0,subAdditionResult)
                self.assertEqual(subAddition((number0, solution)), subAdditionResult, "solving issue : a µ x = b : "+str((number0,subAdditionResult)))
                self.assertNotEqual(subAddition((number0, solution-1)), subAdditionResult, "solving issue : a µ x-1 != b : "+str((number0,subAdditionResult)))
                self.assertNotEqual(subAddition((number0, solution+1)), subAdditionResult, "solving issue : a µ x+1 != b : "+str((number0,subAdditionResult)))
                solution = solveSubAddition(number1,subAdditionResult)
                self.assertEqual(subAddition((number1, solution)), subAdditionResult, "solving issue : a µ x = b : "+str((number1,subAdditionResult)))
                self.assertNotEqual(subAddition((number1, solution-1)), subAdditionResult, "solving issue : a µ x-1 != b : "+str((number1,subAdditionResult)))
                self.assertNotEqual(subAddition((number1, solution+1)), subAdditionResult, "solving issue : a µ x+1 != b : "+str((number1,subAdditionResult)))
        # not verified properties
        self.assertNotEqual(subAddition((subAddition((0, 0)),1)),subAddition((0, subAddition((0, 1)))), "not left alternative : (xx)y = x(xy) ; x=0 ; y=1")
        self.assertNotEqual(subAddition((1,subAddition((0, 0)))),subAddition((subAddition((1, 0)),0)), "not right alternative : y(xx) = (yx)x ; x=0 ; y=1")
        '''self.assertNotEqual(subAddition((1, subAddition((0, subAddition((1, 0)))))),subAddition((subAddition((subAddition((1, 0)),1)),0)), "not moufang #0 : z(x(zy)) = ((zx)z)y ; x=0=y=0 ; z=1")
        self.assertNotEqual(subAddition((0, subAddition((1, subAddition((0, 1)))))),subAddition((subAddition((subAddition((0, 1)),0)),1)), "not moufang #1 : x(z(yz)) = ((xz)y)z ; x=0=y=0 ; z=1")
        self.assertFalse(subAddition((subAddition((1, 0)),subAddition((0, 1))))==subAddition((subAddition((1, subAddition((0, 0)))),1))==subAddition((1,subAddition((subAddition((0, 0)),1)))), "not moufang #2 : (zx)(yz) = (z(xy))z = z((xy)z) ; x=0=y=0 ; z=1")'''
        self.assertNotEqual(subAddition((0, subAddition((0, subAddition((0, 1)))))),subAddition((subAddition((0, subAddition((0, 0)))),1)), "left bol : x(y(xz)) = (x(yx))z ; x=0=y=0 ; z=1")
        self.assertNotEqual(subAddition((subAddition((subAddition((1, 0)),0)),0)),subAddition((subAddition((1, subAddition((0, 0)))),0)), "right bol : ((zx)y)x = z((xy)x) ; x=0=y=0 ; z=1")
        pass
    # end of class
    pass
# run test
if __name__ == '__main__':
    unittest.main()