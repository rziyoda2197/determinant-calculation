import pytest
import numpy as np

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def test_calculate_determinant():
    matrix = np.array([[1, 2], [3, 4]])
    assert round(calculate_determinant(matrix), 2) == -2.0

def test_calculate_determinant_zero():
    matrix = np.array([[1, 2], [1, 2]])
    assert calculate_determinant(matrix) == 0.0

def test_calculate_determinant_identity():
    matrix = np.array([[1, 0], [0, 1]])
    assert calculate_determinant(matrix) == 1.0

def test_calculate_determinant_invalid_input():
    with pytest.raises(ValueError):
        calculate_determinant(np.array([1, 2, 3]))

def test_calculate_determinant_non_square_matrix():
    with pytest.raises(np.linalg.LinAlgError):
        calculate_determinant(np.array([[1, 2, 3], [4, 5, 6]]))
