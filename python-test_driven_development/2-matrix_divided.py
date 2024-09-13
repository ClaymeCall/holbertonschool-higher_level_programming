#!/usr/bin/python3
"""
This module contains the matrix_divided function.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix with each 
    element rounded to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The number by which to divide the matrix elements.

    Returns:
        list of lists of floats: A new matrix with each element divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats or 
                   if div is not a number, or if matrix rows are not of equal size.
        ZeroDivisionError: If div is zero.
    """
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create a new matrix with divided elements rounded to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
