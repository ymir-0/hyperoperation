#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest
from hyperoperation.hyperoperation import subAddition,redifinedAddition,solveSubAddition
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
                # test solving
                self.testSubAdditionSolving(number0, subAdditionResult)
                self.testSubAdditionSolving(number1, subAdditionResult)
        # not verified properties
        self.assertNotEqual(subAddition((subAddition((0, 0)),1)),subAddition((0, subAddition((0, 1)))), "not left alternative : (xx)y == x(xy) ; x=0 ; y=1")
        self.assertNotEqual(subAddition((1,subAddition((0, 0)))),subAddition((subAddition((1, 0)),0)), "not right alternative : y(xx) == (yx)x ; x=0 ; y=1")
        self.assertNotEqual(subAddition((0, subAddition((0, subAddition((0, 1)))))),subAddition((subAddition((0, subAddition((0, 0)))),1)), "left bol : x(y(xz)) == (x(yx))z ; x=0=y=0 ; z=1")
        self.assertNotEqual(subAddition((subAddition((subAddition((1, 0)),0)),0)),subAddition((subAddition((1, subAddition((0, 0)))),0)), "right bol : ((zx)y)x == z((xy)x) ; x=0=y=0 ; z=1")
        pass
    # test sub addition solving
    def testSubAdditionSolving(self,knownValue,result):
        solutions = solveSubAddition(knownValue, result)
        self.checkSolveSubAdditionResults(solutions,knownValue, result)
    def checkSolveSubAdditionResults(self,solutions,knownValue, result):
        # if solution is a set, check is element
        if type(solutions)==set and result in solutions:
            for solution in solutions:
                self.checkSolveSubAdditionResults(solution, knownValue, result)
        # else check result
        else:
            # assume solution is a number
            limitSolution = solutions
            # if solution is a range, check inferior value is valid
            if type(solutions)==range:
                limitSolution = solutions[-1]
                self.assertEqual(subAddition((knownValue, limitSolution - 1)), result,"solving issue : a(x-1) == b : (a,b)=" + str((knownValue, result)))
            # if solution is number, check inferior value is invalid
            else:
                self.assertNotEqual(subAddition((knownValue, limitSolution - 1)), result,"solving issue : a(x-1) != b : (a,b)=" + str((knownValue, result)))
            # check limit and superior values are valid
            self.assertEqual(subAddition((knownValue, limitSolution)), result,"solving issue : ax = b : " + str((knownValue, result)))
            self.assertNotEqual(subAddition((knownValue, limitSolution + 1)), result,"solving issue : a(x+1) != b : (a,b)=" + str((knownValue, result)))
# run test
if __name__ == '__main__':
    unittest.main()