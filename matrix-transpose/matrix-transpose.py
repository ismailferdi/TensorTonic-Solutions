import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n, m = np.array(A).shape
    A_T = np.zeros(shape=(m, n))
    for i in range(n):
        for j in range(m):
            A_T[j][i] = A[i][j]
    return A_T
