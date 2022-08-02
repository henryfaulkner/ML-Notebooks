import pandas as pd
import numpy as np
from scipy import sparse

data = pd.read_csv('../iris.csv')
eye = [[0, 0, 1], [1, 0, 0], [1, 0, 0]]
print(f'NumPy array: {np.eye(4)}')
print(f'SciPy sparse CSR matrix: {sparse.csr_matrix(eye)}')
