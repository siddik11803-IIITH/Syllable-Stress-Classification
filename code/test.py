import scipy.io as sp
import numpy as np
mat_1 = sp.loadmat('../GER_test.mat')
x = (mat_1['GER_test'])
x = np.array(x)
print(x.shape)