# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@
"""


def classifyTriangle(a: int, b: int, c: int) -> str:
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then concatenate result with 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    def checkIfRight(a, b, c, e=0.001):
        return abs(1 - (a * a + b * b) / (c * c)) < e

    # require that the input values be >= 0 and <= 200 and have type integer

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # now we know that we have a valid triangle

    (a, b, c,) = sorted([a, b, c])  # a<b<c
    if not a + b > c:
        return "NotATriangle"

    isRight = checkIfRight(a, b, c)
    if a == b == c:
        triangleType = "Equilateral"
    elif a == b or b == c or a == c:
        triangleType = "Isoceles"
    else:
        triangleType = "Scalene"
    return triangleType + "+Right" if isRight else triangleType


