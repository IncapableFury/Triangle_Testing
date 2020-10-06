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
    """
    define multiple sets of tests as functions with names that begin
    """

    def test_input_validation(self):
        """
        test inputs validation
        """
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput',
                         'input values be >= 0 and <= 200')
        self.assertEqual(classify_triangle(-1, 2, 2), 'InvalidInput',
                         'input values be >= 0 and <= 200')
        self.assertEqual(classify_triangle(3, 4, 999), 'InvalidInput',
                         'input values be >= 0 and <= 200')
        self.assertEqual(classify_triangle(3, 4, 6.1), 'InvalidInput',
                         'input values be integer.')
        self.assertEqual(classify_triangle(3.0, 4.0, 5.0), 'InvalidInput',
                         'input values be integer.')

    def test_not_triangle(self):
        """
        test if program can catch non-triangle inputs
        """
        self.assertEqual(classify_triangle(3, 4, 7), "NotATriangle",
                         'The sum of arbitrary two sides should be greater than the third side.')

    def test_right_triangle(self):
        """
        test if program can identify right triangles
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene+Right',
                         '3,4,5 is a Right and Scalene triangle')
        self.assertEqual(classify_triangle(4, 5, 3), 'Scalene+Right',
                         '3,4,5 is a Right and Scalene triangle')
        self.assertEqual(classify_triangle(13, 12, 5), 'Scalene+Right',
                         '5,12,13 is a Right and Scalene triangle')

    def test_isosceles_triangle(self):
        """
        test if program can identify isosceles triangles
        """
        self.assertEqual(classify_triangle(6, 6, 9), 'Isoceles',
                         '6,6,9 is a Isosceles triangle')
        self.assertEqual(classify_triangle(20, 30, 20), 'Isoceles',
                         '20,20,30 is a Isosceles triangle')

    def test_scalene_triangle(self):
        """
        test if program can identify scalene triangles
        """
        self.assertEqual(classify_triangle(5, 6, 9), 'Scalene',
                         '5,6,9 is a Scalene triangle')

    def test_equilateral_triangles(self):
        """
        test if program can identify equilateral triangles
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral',
                         '1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(200, 200, 200), 'Equilateral',
                         '200,200,200 should be equilateral')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
