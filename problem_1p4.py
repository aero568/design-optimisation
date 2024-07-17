import matplotlib.pyplot as plt
import numpy as np
import openmdao.api as om


def set_plot():

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
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.contour(X1, X2, f(X1, X2), levels=levels)


# FIRST PART
# two-dimensional function
def f(x1, x2):
    y = (1 - x1) ** 2 + (1 - x2) ** 2 + 0.5 * (2 * x2 - x1**2) ** 2
    return y


# plot function
# set_plot()
# plt.show()


# SECOND PART
# build the model
prob = om.Problem()
prob.model.add_subsystem(
    "function",
    om.ExecComp("obj = (1 - x1) ** 2 + (1 - x2) ** 2 + 0.5 * (2 * x2 - x1**2) ** 2"),
)

# setup the optimization
prob.driver = om.ScipyOptimizeDriver()
prob.driver.options["optimizer"] = "SLSQP"
prob.model.add_design_var("function.x1", lower=-10, upper=10)
prob.model.add_design_var("function.x2", lower=-10, upper=10)
prob.model.add_objective("function.obj")
prob.setup()

# set initial values
prob.set_val("function.x1", 1.0)
prob.set_val("function.x2", -1.0)

# run the optimization
prob.run_driver()

# minimum value
print(prob.get_val("function.obj"))

# location of the minimum
x1_opt = prob.get_val("function.x1")
x2_opt = prob.get_val("function.x2")
print(x1_opt)
print(x2_opt)

# plot location of the minimum over contour
set_plot()
plt.plot(x1_opt, x2_opt, "rd")
plt.show()
