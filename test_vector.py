import numpy as np
from vector import magnitude, dot_product, cosine_similarity

v1 = np.array([3, 4])
v2 = np.array([1, 2])

print("Magnitude of v1:", magnitude(v1))
print("Magnitude of v2:", magnitude(v2))
print("Dot product of v1 and v2:", dot_product(v1, v2))
print("Cosine similarity between v1 and v2:", cosine_similarity(v1, v2 ))