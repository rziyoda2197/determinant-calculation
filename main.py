def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for c in range(len(matrix)):
            sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1)**c)*matrix[0][c]*determinant(sub_matrix)
        return det

# Misol uchun ma'lumotlar
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(determinant(matrix))
```

```python
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

# Misol uchun ma'lumotlar
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(determinant(matrix))
