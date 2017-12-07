#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest
from hyperoperation.hyperoperation import subAddition
# define test
class testHyperoperation(unittest.TestCase):
    # test addition surrogate
    def testAdditionSurrogate(self):
        for repertedNumber in range(1,10):
            for repertingNumber in range(1, 10):
                expectedAddition=repertedNumber+repertingNumber
                actualAddition=subAddition(repertedNumber,0)
                for repetition in range(1,repertingNumber):
                    actualAddition=subAddition(actualAddition,repertedNumber)
                self.assertEqual(expectedAddition,actualAddition,str(repertedNumber)+"+"+str(repertingNumber))
# run test
if __name__ == '__main__':
    unittest.main()