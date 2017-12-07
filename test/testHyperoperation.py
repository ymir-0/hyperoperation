#!/usr/bin/env python3
# PY test script file name must start with "test" to allow automatic recognition by PyCharm
# import
import unittest
# define test
class testHyperoperation(unittest.TestCase):
    # test addition
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
# run test
if __name__ == '__main__':
    unittest.main()