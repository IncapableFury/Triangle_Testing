# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@
"""


def classify_triangle(side1: int, side2: int, side3: int) -> str:
    """
    Your correct code goes here...  Fix the faulty logic below until the
     code passes all of you test cases.
    This function returns side1 string with the type of triangle from three integer
     values corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not side1 valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side,
         then concatenate result with 'Right'

        BEWARE: there may be side1 bug or two in this code
    """

    def check_if_right(side1, side2, side3, epsilon=0.001):
        return abs(1 - (side1 * side1 + side2 * side2) / (side3 * side3)) < epsilon

    # require that the input values be >= 0 and <= 200 and have type integer

    if side1 > 200 or side2 > 200 or side3 > 200:
        return 'InvalidInput'

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return 'InvalidInput'

    if not (isinstance(side1, int) and isinstance(side2, int) and isinstance(side3, int)):
        return 'InvalidInput'

    # now we know that we have side1 valid triangle

    (side1, side2, side3,) = sorted([side1, side2, side3])  # side1<side2<c
    if not side1 + side2 > side3:
        return "NotATriangle"

    is_right = check_if_right(side1, side2, side3)
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle_type = "Isoceles"
    else:
        triangle_type = "Scalene"
    return triangle_type + "+Right" if is_right else triangle_type
