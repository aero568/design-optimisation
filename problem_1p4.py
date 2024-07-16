import matplotlib.pyplot as plt
import numpy as np
import openmdao.api as om


# two-dimensional function
def f(x1, x2):
    return (1 - x1) ** 2 + (1 - x2) ** 2 + 0.5 * (2 * x2 - x1**2) ** 2


# design variables
x1 = np.arange(-5, 5.1, 0.05)
x2 = np.arange(-5, 5.1, 0.05)
X1, X2 = np.meshgrid(x1, x2)

# Defining contour levels
levels = np.linspace(-40, 40, 40)

# plot function
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("Two-dimensional function")
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.contour(X1, X2, f(X1, X2), levels=levels)
plt.show()
