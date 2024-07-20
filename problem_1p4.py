import matplotlib.pyplot as plt
import openmdao.api as om

from functions import f1p4 as f
from plotfun import set_plot

# build the model
prob = om.Problem()
prob.model.add_subsystem(
    "function",
    om.ExecComp("obj = (1 - x1) ** 2 + (1 - x2) ** 2 + 0.5 * (2 * x2 - x1**2) ** 2"),
    promotes=["x1", "x2","obj"],
)
prob.model.add_subsystem(
    "constraint1",
    om.ExecComp("g1 = x1**2+x2**2"),
    promotes=["x1", "x2", "g1"],
)
prob.model.add_subsystem(
    "constraint2",
    om.ExecComp("g2 = x1-3*x2+0.5"),
    promotes=["x1", "x2", "g2"],
)

# setup the optimization
prob.driver = om.ScipyOptimizeDriver()
prob.driver.options["optimizer"] = "SLSQP"
prob.model.add_design_var("x1", lower=0)
prob.model.add_design_var("x2", lower=0)
prob.model.add_constraint("g1", upper=1.0)
prob.model.add_constraint("g2", lower=0.0)
prob.model.add_objective("obj")
prob.setup()

# set initial values
prob.set_val("x1", 0.0)
prob.set_val("x2", 0.0)

# run the optimization
prob.run_driver()

# minimum value
print(prob.get_val("function.obj"))

# location of the minimum
x1_opt = prob.get_val("x1")
x2_opt = prob.get_val("x2")
print(x1_opt)
print(x2_opt)


# plot location of the minimum over contour
set_plot(f)
plt.plot(x1_opt, x2_opt, "bo")
# plt.imshow(g1<=1)
plt.show()
