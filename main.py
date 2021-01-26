import numpy as np
import matplotlib.pyplot as plt
from utils import plot_with_residual

X = np.array([1,2,3])
Y = np.array([2,1,5])

plot_with_residual(X,Y,0,1)
plt.title("residual plot")
plt.show()