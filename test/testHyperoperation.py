#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest
from hyperoperation.hyperoperation import subAddition,redifinedAddition
# define test
class testHyperoperation(unittest.TestCase):
    # test redifined surrogate
    def testRedifinedAddition(self):
        for repertedNumber in range(0,10):
            for repertingNumber in range(0, 10):
                expectedAddition=repertedNumber+repertingNumber
                actualAddition=redifinedAddition(repertedNumber,repertingNumber)
                self.assertEqual(expectedAddition,actualAddition,str(repertedNumber)+"+"+str(repertingNumber))
# run test
if __name__ == '__main__':
    unittest.main()