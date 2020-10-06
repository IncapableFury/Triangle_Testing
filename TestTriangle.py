# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInputValidation(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', 'input values be >= 0 and <= 200')
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput', 'input values be >= 0 and <= 200')
        self.assertEqual(classifyTriangle(3, 4, 999), 'InvalidInput', 'input values be >= 0 and <= 200')
        self.assertEqual(classifyTriangle(3, 4, 6.1), 'InvalidInput', 'input values be integer.')
        self.assertEqual(classifyTriangle(3.0, 4.0, 5.0), 'InvalidInput', 'input values be integer.')


    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 7), "NotATriangle",
                         'The sum of arbitrary two sides should be greater than the third side.')

    def testRightTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Scalene+Right', '3,4,5 is a Right and Scalene triangle')
        self.assertEqual(classifyTriangle(4, 5, 3), 'Scalene+Right', '3,4,5 is a Right and Scalene triangle')
        self.assertEqual(classifyTriangle(13, 12, 5), 'Scalene+Right', '5,12,13 is a Right and Scalene triangle')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(6, 6, 9), 'Isoceles', '6,6,9 is a Isosceles triangle')
        self.assertEqual(classifyTriangle(20, 30, 20), 'Isoceles', '20,20,30 is a Isosceles triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5, 6, 9), 'Scalene', '5,6,9 is a Scalene triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200,200,200 should be equilateral')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
