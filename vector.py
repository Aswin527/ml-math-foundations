import numpy as np

def magnitude(v: np.ndarray) -> float:
    """Calculate the magnitude of a vector."""
    # sum_of_squares = np.sum(v ** 2)
    # return np.sqrt(sum_of_squares)
    sum_of_squares = 0.0
    for i in v:
        sum_of_squares += i ** 2
    return sum_of_squares ** 0.5


def dot_product(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) != len(b):
        raise ValueError("Vectors must be of the same length")
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Calculate the cosine similarity between two vectors."""
    dot_prod = dot_product(a, b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)
    if mag_a == 0 or mag_b == 0:
        raise ValueError("Magnitude of a vector cannot be zero")
    return dot_prod / (mag_a * mag_b)
