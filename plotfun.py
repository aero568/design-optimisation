import matplotlib.pyplot as plt
import numpy as np

def set_plot(f,xlim=[-5,5],ylim=[-4,8]):

    # design variables
    x1 = np.arange(-10, 10.1, 0.05)
    x2 = np.arange(-10, 10.1, 0.05)
    X1, X2 = np.meshgrid(x1, x2)
    
    # Defining contour levels
    levels = np.linspace(-40, 40, 40)

    # set contour plot
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.title("Two-dimensional function")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.contour(X1, X2, f(X1, X2), levels=levels)
