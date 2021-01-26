import numpy as np
import matplotlib.pyplot as plt
from utils import plot_with_residual

X = np.array([1,5,6])
Y = np.array([4,9,13])

plot_with_residual(plt,X,Y,2,1.5)
plt.title("data set vs linear line + residual")
plt.show()