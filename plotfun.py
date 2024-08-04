import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects


def set_plot(f, g1, g2, xlim=[-5, 5], ylim=[-4, 4]):

    # set up survey vectors
    nx = 500
    x1 = np.linspace(-10, 10, nx)
    x2 = np.linspace(-10, 10, nx)

    # set up survey matrices
    X1, X2 = np.meshgrid(x1, x2)

    # compute functions
    Z = {}
    G1 = {}
    G2 = {}
    f.compute(self=f, inputs={"x1": X1, "x2": X2}, outputs=Z)
    g1.compute(self=g1, inputs={"x1": X1, "x2": X2}, outputs=G1)
    g2.compute(self=g2, inputs={"x1": X1, "x2": X2}, outputs=G2)

    # contour plot
    _, ax = plt.subplots()
    cfo = ax.contour(
        X1, X2, Z["y"], levels=np.linspace(-40, 40, 40), cmap="Greys"
    )  # objective function
    cg1 = ax.contour(X1, X2, G1["g1"], [1], colors="red")  # constraint 1
    cg2 = ax.contour(X1, X2, G2["g2"], [0], colors="red")  # constraint 2

    # format contour
    cfo.set(linewidth=0.5)
    cg1.set(linewidth=0.75)
    cg2.set(
        linewidth=0.75,
        # path_effects=[patheffects.withTickedStroke(angle=-45, spacing=5, length=1)],
    )

    # format plot area
    plt.xlabel("x1",fontname='Times',fontsize=10)
    plt.ylabel("x2",fontname='Times',fontsize=10)
    plt.title("Two-dimensional function",fontname='Times',fontsize=14)
    plt.xticks(np.linspace(xlim[0],xlim[1],11),fontname='Times',fontsize=8)
    plt.yticks(np.linspace(ylim[0],ylim[1],9),fontname='Times',fontsize=8)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.clabel(cfo, fmt="%2.1f", use_clabeltext=True, fontsize=6)
    #plt.fill_between(x1, 0.3333 * (x1 + 0.5),
    #                 where=(x1 >= 0), 
    #                 color="r", 
    #                 alpha=0.3)
    plt.imshow(((X1**2 + X2**2 <= 1) & ((X1 - 3 * X2 + 0.5) >= 0) & (X1 >= 0) & (X2 >= 0)).astype(int),
       extent=(X1.min(), X1.max(), X2.min(), X2.max()),
       origin="lower",
       cmap="Reds",
       alpha=0.15,
       aspect="auto",
    )
