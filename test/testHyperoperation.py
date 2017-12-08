#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest
from hyperoperation.hyperoperation import subAddition,redifinedAddition
# define test
class testHyperoperation(unittest.TestCase):
    # test redifined addition (& commutativity)
    def testSubAddition(self):
        for number0 in range(0,10):
            for number1 in range(number0, 10):
                # redifined addition value
                result0=number0+number1
                result1=redifinedAddition(number0,number1)
                self.assertEqual(result0,result1,"redifined addition value : "+str((number0,number1)))
                # redifined addition commutativity
                result2=redifinedAddition(number1,number0)
                self.assertEqual(result1, result2, "redifined addition commutativity : "+str((number0,number1)))
                # sub addition commutativity
                result0=subAddition(number0=number0,number1=number1)
                result1=subAddition(number0=number1,number1=number0)
                self.assertEqual(result0, result1, "sub addition commutativity : "+str((number0,number1)))
                # sub addition flexibility
                result0 = subAddition(number0=subAddition(number0=number0, number1=number1), number1=number0)
                result1 = subAddition(number0=number0, number1=subAddition(number0=number1, number1=number0))
                self.assertEqual(result0, result1, "sub addition flexibility : "+str((number0,number1)))
                ''' CONTINUE WITH Moufang loop
                for number2 in range(number1, 10):
                    pass
                '''
    # end of class
    pass
# run test
if __name__ == '__main__':
    unittest.main()